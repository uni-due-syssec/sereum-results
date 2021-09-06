# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAbDC35433405972052FEB43cA900496fF0646E0c 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    auctionByTokenId
    # storage address 5
    unknown1c0c78bc
    # storage address 6
    unknownbf443c55
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 12
    tokenContractAddress # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    stor16 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 111414077815863400510004064629973595961579173665589224203503662149373724986688
    stor111414077815863400510004064629973595961579173665589224203503662149373724986688
    # storage address 111414077815863400510004064629973595961579173665589224203503662149373724986689
    stor111414077815863400510004064629973595961579173665589224203503662149373724986689
    # storage address 111414077815863400510004064629973595961579173665589224203503662149373724986690
    stor111414077815863400510004064629973595961579173665589224203503662149373724986690
# hash = 0x04d2dec6
# getter = None
# const = None
# payable = False
def getWalletAddress(): # not payable
  if addr(stor1.length) != caller:
      require caller == owner
  return addr(stor2.length)


# hash = 0x0ade4797
# getter = None
# const = None
# payable = False
def unknown0ade4797(uint256 _param1): # not payable
  require _param1 < unknownbf443c55.length
  require addr(stor3.length) == addr(unknownbf443c55[_param1].field_0)
  require _param1 < unknownbf443c55.length
  if uint64(unknownbf443c55[_param1].field_832) <= 0:
      revert with 0, 'must be on auction'
  if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
      if block.timestamp - uint64(unknownbf443c55[_param1].field_832) < uint64(unknownbf443c55[_param1].field_768):
          if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
              if block.timestamp - uint64(unknownbf443c55[_param1].field_768) >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 
                         uint64(unknownbf443c55[_param1].field_768) - block.timestamp + uint64(unknownbf443c55[_param1].field_832)
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         uint64(unknownbf443c55[_param1].field_768) - block.timestamp + uint64(unknownbf443c55[_param1].field_832)
          else:
              if 0 >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 
                         uint64(unknownbf443c55[_param1].field_768) - block.timestamp + uint64(unknownbf443c55[_param1].field_832)
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         uint64(unknownbf443c55[_param1].field_768) - block.timestamp + uint64(unknownbf443c55[_param1].field_832)
      else:
          if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
              if block.timestamp - uint64(unknownbf443c55[_param1].field_768) >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 0
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         0
          else:
              if 0 >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 0
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         0
  else:
      if 0 < uint64(unknownbf443c55[_param1].field_768):
          if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
              if block.timestamp - uint64(unknownbf443c55[_param1].field_768) >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 
                         uint64(unknownbf443c55[_param1].field_768)
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         uint64(unknownbf443c55[_param1].field_768)
          else:
              if 0 >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 
                         uint64(unknownbf443c55[_param1].field_768)
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         uint64(unknownbf443c55[_param1].field_768)
      else:
          if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
              if block.timestamp - uint64(unknownbf443c55[_param1].field_768) >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 0
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         0
          else:
              if 0 >= uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) - (uint128(unknownbf443c55[_param1].field_512) * stor8 / 10000), 0
              if uint64(unknownbf443c55[_param1].field_768):
                  return uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000), 
                         0
  ('iszero', ('type', 64, ('field', 768, ('stor', ('array', ('mul', 4, ('param', '_param1')), ('name', 'unknownbf443c55', 6))))))
  revert


# hash = 0x1c0c78bc
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]], ['cd', 36]]]
# const = None
# payable = False
def unknown1c0c78bc(addr _param1, uint256 _param2): # not payable
  require _param2 < uint256(unknown1c0c78bc[addr(_param1)].field_0)
  return uint256(unknown1c0c78bc[addr(_param1)][_param2].field_0)


# hash = 0x1e0f692e
# getter = None
# const = None
# payable = False
def unknown1e0f692e(addr _param1): # not payable
  require caller == owner
  require ext_code.size(_param1)
  call _param1.implementsERC721() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'candidate must implement ERC721'
  tokenContractAddress = _param1


# hash = 0x1e5c4d73
# getter = None
# const = None
# payable = False
def unknown1e5c4d73(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5, uint256 _param6): # not payable
  require caller == addr(stor1.length)
  stor13 = _param1
  stor14 = _param2
  stor15 = _param3
  stor16 = _param4
  stor17 = _param5
  stor18 = _param6


# hash = 0x1fb01896
# getter = None
# const = None
# payable = False
def unknown1fb01896(addr _param1, uint256 _param2, uint128 _param3, uint128 _param4, uint64 _param5, uint64 _param6): # not payable
  require caller == owner
  unknownbf443c55.length++
  addr(unknownbf443c55[unknownbf443c55.length].field_0) = _param1
  uint256(unknownbf443c55[unknownbf443c55.length].field_256) = _param2
  uint128(unknownbf443c55[unknownbf443c55.length].field_512) = _param3
  uint128(unknownbf443c55[unknownbf443c55.length].field_640) = _param4
  uint64(unknownbf443c55[unknownbf443c55.length].field_768) = _param5
  uint64(unknownbf443c55[unknownbf443c55.length].field_832) = _param6
  auctionByTokenId[_param2] = unknownbf443c55.length + 1
  uint256(unknown1c0c78bc[addr(_param1)].field_0)++
  uint256(unknown1c0c78bc[addr(_param1)][uint256(unknown1c0c78bc[addr(_param1)].field_0)].field_0) = unknownbf443c55.length + 1


# hash = 0x22f3e2d4
# getter = None
# const = None
# payable = False
def isActive(): # not payable
  return not bool(stor0)


# hash = 0x27ebe40a
# getter = None
# const = None
# payable = False
def createAuction(uint256 _tokenId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration, address _seller): # not payable
  require not stor0
  if _startingPrice >= 0xffffffffffffffffffffffffffffffff:
      revert with 0, 'can't be stored in 128 bits'
  if _endingPrice >= 0xffffffffffffffffffffffffffffffff:
      revert with 0, 'can't be stored in 128 bits'
  if _duration > 18446744073709551615:
      revert with 0, 'can't be stored in 64 bits'
  if _startingPrice < stor13:
      revert with 0, 'start price too low'
  if _startingPrice > stor14:
      revert with 0, 'start price too hight'
  if _endingPrice < stor15:
      revert with 0, 'end price too low'
  if _endingPrice > stor16:
      revert with 0, 'end price too low'
  if _duration < stor17:
      revert with 0, 'duration too short'
  if _duration > stor18:
      revert with 0, 'duration too long'
  if stor19:
      if _startingPrice < _endingPrice:
          revert with 0, 'only reverse auctions allowed'
  require ext_code.size(tokenContractAddress)
  call tokenContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_seller), this.address, _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknownbf443c55.length++
  addr(unknownbf443c55[unknownbf443c55.length].field_0) = _seller
  storF652[stor6.length] = _tokenId
  uint128(storF652[stor6.length].field_0) = uint128(_startingPrice)
  uint128(storF652[stor6.length].field_128) = uint128(_endingPrice)
  uint64(storF652[stor6.length].field_0) = uint64(_duration)
  uint64(storF652[stor6.length].field_64) = uint64(block.timestamp)
  auctionByTokenId[_tokenId] = unknownbf443c55.length
  uint256(unknown1c0c78bc[addr(_seller)].field_0)++
  uint256(unknown1c0c78bc[addr(_seller)][uint256(unknown1c0c78bc[addr(_seller)].field_0)].field_0) = unknownbf443c55.length
  log 0x17d39c64: 1, unknownbf443c55.length, uint256(unknown1c0c78bc[addr(_seller)].field_0) + 1, Array(len=4, data='add1')
  log AuctionCreated(
        uint256 tokenId=_tokenId,
        uint256 startingPrice=_startingPrice << 128,
        uint256 endingPrice=_endingPrice << 128,
        uint256 duration=uint64(_duration))


# hash = 0x339ccade
# getter = None
# const = None
# payable = False
def unknown339ccade(uint256 _param1): # not payable
  return _param1 - (_param1 * stor8 / 10000), 
         _param1 * stor9 / 10000,
         _param1 - (_param1 * stor8 / 10000) - (_param1 * stor9 / 10000)


# hash = 0x3620f819
# getter = None
# const = None
# payable = False
def unknown3620f819(addr _param1, uint256 _param2, uint256 _param3): # not payable
  require caller == owner
  require _param3 + _param2 < 10000
  stor8 = _param2
  stor9 = _param3
  stor10 = _param1
  stor11 = _param1


# hash = 0x3bc4c7ac
# getter = None
# const = None
# payable = False
def unknown3bc4c7ac(bool _param1): # not payable
  require caller == addr(stor1.length)
  stor19 = uint8(_param1)


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == owner
  require stor0
  stor0 = 0
  log Unpause()


# hash = 0x454a2ab3
# getter = None
# const = None
# payable = True
def bid(uint256 _tokenId) payable: 
  require not stor0
  require _tokenId < unknownbf443c55.length
  if uint64(unknownbf443c55[_tokenId].field_832) <= 0:
      revert with 0, 'must be on auction'
  if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
      if block.timestamp - uint64(unknownbf443c55[_tokenId].field_768) >= uint64(unknownbf443c55[_tokenId].field_768):
          if call.value < uint128(unknownbf443c55[_tokenId].field_640):
              revert with 0, 'bit amount too small'
          require _tokenId < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _tokenId:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _tokenId < unknownbf443c55.length
              addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_tokenId].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _tokenId < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                      call addr(unknownbf443c55[_tokenId].field_0) with:
                         value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                        uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                        address newOwner=caller,
                        uint256 uID=0)
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_tokenId].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          if uint128(unknownbf443c55[_tokenId].field_640) > 0:
              call addr(unknownbf443c55[_tokenId].field_0) with:
                 value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                address newOwner=caller,
                uint256 uID=0)
      else:
          require uint64(unknownbf443c55[_tokenId].field_768)
          if call.value < uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) - (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)):
              revert with 0, 'bit amount too small'
          require _tokenId < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _tokenId:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _tokenId < unknownbf443c55.length
              addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_tokenId].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _tokenId < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  if uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                      call addr(unknownbf443c55[_tokenId].field_0) with:
                         value uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                        uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)),
                        address newOwner=caller,
                        uint256 uID=0)
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_tokenId].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          if uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
              call addr(unknownbf443c55[_tokenId].field_0) with:
                 value uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_640)) - (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_640)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_832) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)),
                address newOwner=caller,
                uint256 uID=0)
  else:
      if 0 >= uint64(unknownbf443c55[_tokenId].field_768):
          if call.value < uint128(unknownbf443c55[_tokenId].field_640):
              revert with 0, 'bit amount too small'
          require _tokenId < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _tokenId:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _tokenId < unknownbf443c55.length
              addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_tokenId].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _tokenId < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                      call addr(unknownbf443c55[_tokenId].field_0) with:
                         value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                        uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                        address newOwner=caller,
                        uint256 uID=0)
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_tokenId].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_640) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          if uint128(unknownbf443c55[_tokenId].field_640) > 0:
              call addr(unknownbf443c55[_tokenId].field_0) with:
                 value uint128(unknownbf443c55[_tokenId].field_640) - (uint128(unknownbf443c55[_tokenId].field_640) * stor7 / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                uint256 price=uint128(unknownbf443c55[_tokenId].field_512),
                address newOwner=caller,
                uint256 uID=0)
      else:
          require uint64(unknownbf443c55[_tokenId].field_768)
          if call.value < uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)):
              revert with 0, 'bit amount too small'
          require _tokenId < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _tokenId:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _tokenId < unknownbf443c55.length
              addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_tokenId].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _tokenId < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  if uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                      call addr(unknownbf443c55[_tokenId].field_0) with:
                         value uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                        uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)),
                        address newOwner=caller,
                        uint256 uID=0)
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_tokenId].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              if uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
                  call addr(unknownbf443c55[_tokenId].field_0) with:
                     value uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                    uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)),
                    address newOwner=caller,
                    uint256 uID=0)
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_tokenId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          if uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) > 0:
              call addr(unknownbf443c55[_tokenId].field_0) with:
                 value uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)) - ((uint128(unknownbf443c55[_tokenId].field_512) * stor7) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768) * stor7) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256),
                uint256 price=uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)),
                address newOwner=caller,
                uint256 uID=0)
  require ext_code.size(tokenContractAddress)
  call tokenContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, uint256(unknownbf443c55[_tokenId].field_256)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(stor3.length))
  call addr(stor3.length).0x75314172 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x55a373d6
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def tokenContract(): # not payable
  return tokenContractAddress


# hash = 0x5b38730f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown5b38730f(): # not payable
  require caller == owner
  return unknownbf443c55.length


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(stor0)


# hash = 0x63bd1d4a
# getter = None
# const = None
# payable = False
def payout(): # not payable
  if addr(stor1.length) != caller:
      require caller == owner
  call addr(stor2.length) with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  require caller == owner
  require _newAdmin
  log OwnershipTransferred(
        address previousOwner=addr(stor1.length),
        address newOwner=_newAdmin)
  addr(stor1.length) = _newAdmin


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x757de573
# getter = None
# const = None
# payable = False
def setOwnerCut(uint256 _cut): # not payable
  require caller == owner
  if _cut > 10000:
      revert with 0, 'cut too large'
  if _cut < 0:
      revert with 0, 'cut too small'
  stor7 = _cut


# hash = 0x77413267
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def getAuctionByTokenId(uint256 _tokenId): # not payable
  require auctionByTokenId[_tokenId] < unknownbf443c55.length
  return addr(unknownbf443c55[stor4[_tokenId]].field_0), 
         uint256(unknownbf443c55[stor4[_tokenId]].field_256),
         uint128(unknownbf443c55[stor4[_tokenId]].field_512),
         uint128(unknownbf443c55[stor4[_tokenId]].field_512),
         uint64(unknownbf443c55[stor4[_tokenId]].field_768),
         uint64(unknownbf443c55[stor4[_tokenId]].field_768)


# hash = 0x78bd7935
# getter = ['struct', ['loc', 6]]
# const = None
# payable = False
def getAuction(uint256 _tokenId): # not payable
  require _tokenId < unknownbf443c55.length
  return addr(unknownbf443c55[_tokenId].field_0), 
         uint256(unknownbf443c55[_tokenId].field_256),
         uint128(unknownbf443c55[_tokenId].field_512),
         uint128(unknownbf443c55[_tokenId].field_512),
         uint64(unknownbf443c55[_tokenId].field_768),
         uint64(unknownbf443c55[_tokenId].field_768)


# hash = 0x7ce98eff
# getter = ['struct', ['loc', 5]]
# const = None
# payable = False
def unknown7ce98eff(addr _param1, uint256 _param2): # not payable
  require _param2 < uint256(unknown1c0c78bc[addr(_param1)].field_0)
  require uint256(unknown1c0c78bc[addr(_param1)][_param2].field_0) < unknownbf443c55.length
  return addr(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_0), 
         uint256(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_256),
         uint128(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_512),
         uint128(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_512),
         uint64(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_768),
         uint64(unknownbf443c55[uint256(stor5[addr(_param1)][_param2].field_0)].field_768)


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require caller == owner
  [93mselfdestruct([91mowner[93m)


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == owner
  require not stor0
  stor0 = 1
  log Pause()


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 _tokenId): # not payable
  require stor0
  require caller == owner
  require _tokenId < unknownbf443c55.length
  if uint64(unknownbf443c55[_tokenId].field_832) <= 0:
      revert with 0, 'must be on auction'
  require _tokenId < unknownbf443c55.length
  auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
  require unknownbf443c55.length - 1 < unknownbf443c55.length
  require unknownbf443c55.length - 1 < unknownbf443c55.length
  if unknownbf443c55.length - 1 == _tokenId:
      addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
      uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
  else:
      require _tokenId < unknownbf443c55.length
      addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
      uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
      uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
      uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
      uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
      uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
      uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
      Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
      uint128(unknownbf443c55[_tokenId].field_896) = 0
      require unknownbf443c55.length - 1 < unknownbf443c55.length
      addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
      uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
      require _tokenId < unknownbf443c55.length
      auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
  [94midx = 0
  while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
      mem[32] = 5
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
      mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
      if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
          [94midx = [94midx + 1
          continue 
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
      [94midx = 0
      while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
          mem[32] = 5
          require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
          if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
              [94midx = [94midx + 1
              continue 
          require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
          require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
          if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
              [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
              while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                  uint256(stor[[94midx]) = 0
                  [94midx = [94midx + 1
                  continue 
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
              while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                  addr(stor[[94midx]) = 0
                  uint256(stor1[[94midx]) = 0
                  uint256(stor2[[94midx]) = 0
                  uint128(stor3[[94midx]) = 0
                  [94midx = [94midx + 4
                  continue 
          require ext_code.size(tokenContractAddress)
          call tokenContractAddress.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
          stop
      unknownbf443c55.length--
      if unknownbf443c55.length > unknownbf443c55.length - 1:
          [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
          while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
              addr(stor[[94midx]) = 0
              uint256(stor1[[94midx]) = 0
              uint256(stor2[[94midx]) = 0
              uint128(stor3[[94midx]) = 0
              [94midx = [94midx + 4
              continue 
      require ext_code.size(tokenContractAddress)
      call tokenContractAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
      stop
  [94midx = 0
  while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
      mem[32] = 5
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
      if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
          [94midx = [94midx + 1
          continue 
      require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
      require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
      if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
          [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
          while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
              uint256(stor[[94midx]) = 0
              [94midx = [94midx + 1
              continue 
      unknownbf443c55.length--
      if unknownbf443c55.length > unknownbf443c55.length - 1:
          [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
          while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
              addr(stor[[94midx]) = 0
              uint256(stor1[[94midx]) = 0
              uint256(stor2[[94midx]) = 0
              uint128(stor3[[94midx]) = 0
              [94midx = [94midx + 4
              continue 
      require ext_code.size(tokenContractAddress)
      call tokenContractAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
      stop
  unknownbf443c55.length--
  if unknownbf443c55.length > unknownbf443c55.length - 1:
      [94midx = 4 * unknownbf443c55.length - 1
      while 4 * unknownbf443c55.length > [94midx:
          addr(unknownbf443c55[[94midx].field_0) = 0
          uint256(unknownbf443c55[[94midx].field_256) = 0
          uint256(unknownbf443c55[[94midx].field_512) = 0
          uint128(unknownbf443c55[[94midx].field_768) = 0
          [94midx = [94midx + 4
          continue 
  require ext_code.size(tokenContractAddress)
  call tokenContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x93507143
# getter = None
# const = None
# payable = False
def unknown93507143(addr _param1): # not payable
  require ext_code.size(addr(stor3.length))
  call addr(stor3.length).balanceOf(address owner) with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      return (ext_call.return_data[0] > 0)
  return (uint256(unknown1c0c78bc[addr(_param1)].field_0) > 0)


# hash = 0x96b5a755
# getter = None
# const = None
# payable = False
def cancelAuction(uint256 _tokenId): # not payable
  require _tokenId < unknownbf443c55.length
  if uint64(unknownbf443c55[_tokenId].field_832) <= 0:
      revert with 0, 'must be on auction'
  if addr(unknownbf443c55[_tokenId].field_0) != caller:
      revert with 0, 'sender must be seller'
  require _tokenId < unknownbf443c55.length
  auctionByTokenId[uint256(stor6[_tokenId].field_256)] = 0
  require unknownbf443c55.length - 1 < unknownbf443c55.length
  require unknownbf443c55.length - 1 < unknownbf443c55.length
  if unknownbf443c55.length - 1 == _tokenId:
      addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
      uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
  else:
      require _tokenId < unknownbf443c55.length
      addr(unknownbf443c55[_tokenId].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
      uint256(unknownbf443c55[_tokenId].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
      uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
      uint128(unknownbf443c55[_tokenId].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
      uint128(unknownbf443c55[_tokenId].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
      uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
      uint64(unknownbf443c55[_tokenId].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
      Mask(192, 0, unknownbf443c55[_tokenId].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
      uint128(unknownbf443c55[_tokenId].field_896) = 0
      require unknownbf443c55.length - 1 < unknownbf443c55.length
      addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
      uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
      uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
      require _tokenId < unknownbf443c55.length
      auctionByTokenId[uint256(stor6[_tokenId].field_256)] = _tokenId
  [94midx = 0
  while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
      mem[32] = 5
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
      mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
      if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
          [94midx = [94midx + 1
          continue 
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _tokenId
      [94midx = 0
      while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
          mem[32] = 5
          require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
          if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
              [94midx = [94midx + 1
              continue 
          require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
          require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
          uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
          if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
              [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
              while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
                  uint256(stor[[94midx]) = 0
                  [94midx = [94midx + 1
                  continue 
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
              while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                  addr(stor[[94midx]) = 0
                  uint256(stor1[[94midx]) = 0
                  uint256(stor2[[94midx]) = 0
                  uint128(stor3[[94midx]) = 0
                  [94midx = [94midx + 4
                  continue 
          require ext_code.size(tokenContractAddress)
          call tokenContractAddress.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
          stop
      unknownbf443c55.length--
      if unknownbf443c55.length > unknownbf443c55.length - 1:
          [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
          while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
              addr(stor[[94midx]) = 0
              uint256(stor1[[94midx]) = 0
              uint256(stor2[[94midx]) = 0
              uint128(stor3[[94midx]) = 0
              [94midx = [94midx + 4
              continue 
      require ext_code.size(tokenContractAddress)
      call tokenContractAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
      stop
  [94midx = 0
  while [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0):
      mem[32] = 5
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      mem[0] = sha3(addr(unknownbf443c55[_tokenId].field_0), 5)
      if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) != _tokenId:
          [94midx = [94midx + 1
          continue 
      require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      require [94midx < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0)
      require uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)][uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)].field_0) = 0
      uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0)--
      if uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) - 1:
          [94midx = uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) - 1
          while sha3(sha3(addr(unknownbf443c55[_tokenId].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_tokenId].field_0)].field_0) > [94midx:
              uint256(stor[[94midx]) = 0
              [94midx = [94midx + 1
              continue 
      unknownbf443c55.length--
      if unknownbf443c55.length > unknownbf443c55.length - 1:
          [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
          while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
              addr(stor[[94midx]) = 0
              uint256(stor1[[94midx]) = 0
              uint256(stor2[[94midx]) = 0
              uint128(stor3[[94midx]) = 0
              [94midx = [94midx + 4
              continue 
      require ext_code.size(tokenContractAddress)
      call tokenContractAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))
      stop
  unknownbf443c55.length--
  if unknownbf443c55.length > unknownbf443c55.length - 1:
      [94midx = 4 * unknownbf443c55.length - 1
      while 4 * unknownbf443c55.length > [94midx:
          addr(unknownbf443c55[[94midx].field_0) = 0
          uint256(unknownbf443c55[[94midx].field_256) = 0
          uint256(unknownbf443c55[[94midx].field_512) = 0
          uint128(unknownbf443c55[[94midx].field_768) = 0
          [94midx = [94midx + 4
          continue 
  require ext_code.size(tokenContractAddress)
  call tokenContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(unknownbf443c55[_tokenId].field_0), uint256(unknownbf443c55[_tokenId].field_256)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=uint256(unknownbf443c55[_tokenId].field_256))


# hash = 0x974c28b2
# getter = None
# const = None
# payable = False
def unknown974c28b2(uint256 _param1): # not payable
  require _param1 < unknownbf443c55.length
  if uint64(unknownbf443c55[_param1].field_832) <= 0:
      return (uint64(unknownbf443c55[_param1].field_832) > 0)
  require _param1 < unknownbf443c55.length
  if block.timestamp <= uint64(unknownbf443c55[_param1].field_832):
      return (block.timestamp > uint64(unknownbf443c55[_param1].field_832))
  require _param1 < unknownbf443c55.length
  return block.timestamp - uint64(unknownbf443c55[_param1].field_832) >= uint64(unknownbf443c55[_param1].field_768)


# hash = 0xac1a386a
# getter = None
# const = None
# payable = False
def setWalletAddress(address _wallet): # not payable
  require caller == owner
  require _wallet
  addr(stor2.length) = _wallet


# hash = 0xad223434
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknownad223434(uint256 _param1): # not payable
  return auctionByTokenId[_param1]


# hash = 0xb5074f58
# getter = None
# const = None
# payable = False
def unknownb5074f58(addr _param1): # not payable
  if not uint256(unknown1c0c78bc[addr(_param1)].field_0):
      mem[(32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 128] = 32
      mem[(32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 160] = uint256(unknown1c0c78bc[addr(_param1)].field_0)
      mem[(32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 192 len floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))] = mem[128 len floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))]
      return memory
        from (32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 128
         [93mlen (96 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 64
  mem[128] = uint256(unknown1c0c78bc[addr(_param1)].field_0)
  [94midx = 128
  [94ms = 0
  while (32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 96 > [94midx:
      mem[[94midx + 32] = uint256(unknown1c0c78bc[addr(_param1)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 192 len floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))] = mem[128 len floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))]
  return Array(len=uint256(unknown1c0c78bc[addr(_param1)].field_0), data=mem[128 len floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))], mem[(32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) + floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0)) + 192 len (32 * uint256(unknown1c0c78bc[addr(_param1)].field_0)) - floor32(uint256(unknown1c0c78bc[addr(_param1)].field_0))]), 


# hash = 0xbf443c55
# getter = ['struct', ['loc', 6]]
# const = None
# payable = False
def unknownbf443c55(uint256 _param1): # not payable
  require caller == owner
  require _param1 < unknownbf443c55.length
  return addr(unknownbf443c55[_param1].field_0), 
         uint256(unknownbf443c55[_param1].field_256),
         uint128(unknownbf443c55[_param1].field_512),
         uint128(unknownbf443c55[_param1].field_512),
         uint64(unknownbf443c55[_param1].field_768),
         uint64(unknownbf443c55[_param1].field_768)


# hash = 0xc44e6640
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknownc44e6640(): # not payable
  return unknownbf443c55.length


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 _tokenId): # not payable
  require _tokenId < unknownbf443c55.length
  if uint64(unknownbf443c55[_tokenId].field_832) <= 0:
      revert with 0, 'must be on auction'
  if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
      if block.timestamp - uint64(unknownbf443c55[_tokenId].field_832) < uint64(unknownbf443c55[_tokenId].field_768):
          if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
              if block.timestamp - uint64(unknownbf443c55[_tokenId].field_768) >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 
                         uint64(unknownbf443c55[_tokenId].field_768) - block.timestamp + uint64(unknownbf443c55[_tokenId].field_832)
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) - (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         uint64(unknownbf443c55[_tokenId].field_768) - block.timestamp + uint64(unknownbf443c55[_tokenId].field_832)
          else:
              if 0 >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 
                         uint64(unknownbf443c55[_tokenId].field_768) - block.timestamp + uint64(unknownbf443c55[_tokenId].field_832)
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         uint64(unknownbf443c55[_tokenId].field_768) - block.timestamp + uint64(unknownbf443c55[_tokenId].field_832)
      else:
          if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
              if block.timestamp - uint64(unknownbf443c55[_tokenId].field_768) >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 0
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) - (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         0
          else:
              if 0 >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 0
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)), 0
  else:
      if 0 < uint64(unknownbf443c55[_tokenId].field_768):
          if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
              if block.timestamp - uint64(unknownbf443c55[_tokenId].field_768) >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), uint64(unknownbf443c55[_tokenId].field_768)
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) - (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         uint64(unknownbf443c55[_tokenId].field_768)
          else:
              if 0 >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), uint64(unknownbf443c55[_tokenId].field_768)
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         uint64(unknownbf443c55[_tokenId].field_768)
      else:
          if block.timestamp > uint64(unknownbf443c55[_tokenId].field_832):
              if block.timestamp - uint64(unknownbf443c55[_tokenId].field_768) >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 0
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + ((block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) - (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) - (block.timestamp * uint128(unknownbf443c55[_tokenId].field_512)) + (uint64(unknownbf443c55[_tokenId].field_768) * uint128(unknownbf443c55[_tokenId].field_512)) /′ uint64(unknownbf443c55[_tokenId].field_768)), 
                         0
          else:
              if 0 >= uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512), 0
              if uint64(unknownbf443c55[_tokenId].field_768):
                  return uint128(unknownbf443c55[_tokenId].field_512) + (0 /′ uint64(unknownbf443c55[_tokenId].field_768)), 0
  ('iszero', ('type', 64, ('field', 768, ('stor', ('array', ('mul', 4, ('param', '_tokenId')), ('name', 'unknownbf443c55', 6))))))
  revert


# hash = 0xd7648949
# getter = None
# const = ['return', 1]
# payable = False
const unknownd7648949 = 1


# hash = 0xe3b0f95e
# getter = None
# const = None
# payable = True
def unknowne3b0f95e(uint256 _param1, uint256 _param2) payable: 
  require not stor0
  require _param1 < unknownbf443c55.length
  require ext_code.size(stor11)
  call stor11.0x5cc15c95 with:
       gas gas_remaining wei
      args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[12 len 20]
  require ext_call.return_data[12 len 20] != caller
  require _param1 < unknownbf443c55.length
  require addr(stor3.length) == addr(unknownbf443c55[_param1].field_0)
  if uint64(unknownbf443c55[_param1].field_832) <= 0:
      revert with 0, 'must be on auction'
  if block.timestamp > uint64(unknownbf443c55[_param1].field_832):
      if block.timestamp - uint64(unknownbf443c55[_param1].field_768) >= uint64(unknownbf443c55[_param1].field_768):
          if call.value < uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000):
              revert with 0, 'bit amount too small'
          require _param1 < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_param1].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _param1:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _param1 < unknownbf443c55.length
              addr(unknownbf443c55[_param1].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_param1].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_param1].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_param1].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _param1 < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_param1].field_256)] = _param1
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _param1
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                        uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                        address newOwner=caller,
                        uint256 uID=_param2)
                  call addr(ext_call.return_data[0]) with:
                     value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                       gas 2300 * is_zero(value) wei
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_param1].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                address newOwner=caller,
                uint256 uID=_param2)
          call addr(ext_call.return_data[0]) with:
             value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
               gas 2300 * is_zero(value) wei
      else:
          require uint64(unknownbf443c55[_param1].field_768)
          if call.value < uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_512)) - (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_768) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000):
              revert with 0, 'bit amount too small'
          require _param1 < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_param1].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _param1:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _param1 < unknownbf443c55.length
              addr(unknownbf443c55[_param1].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_param1].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_param1].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_param1].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _param1 < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_param1].field_256)] = _param1
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _param1
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                        uint256 price=uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                        address newOwner=caller,
                        uint256 uID=_param2)
                  call addr(ext_call.return_data[0]) with:
                     value (uint128(unknownbf443c55[_param1].field_512) * stor9) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                       gas 2300 * is_zero(value) wei
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_param1].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value (uint128(unknownbf443c55[_param1].field_512) * stor9) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value (uint128(unknownbf443c55[_param1].field_512) * stor9) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                uint256 price=uint128(unknownbf443c55[_param1].field_512) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                address newOwner=caller,
                uint256 uID=_param2)
          call addr(ext_call.return_data[0]) with:
             value (uint128(unknownbf443c55[_param1].field_512) * stor9) + ((block.timestamp * uint128(unknownbf443c55[_param1].field_640)) - (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_640)) - (block.timestamp * uint128(unknownbf443c55[_param1].field_512)) + (uint64(unknownbf443c55[_param1].field_832) * uint128(unknownbf443c55[_param1].field_512)) /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
               gas 2300 * is_zero(value) wei
  else:
      if 0 >= uint64(unknownbf443c55[_param1].field_768):
          if call.value < uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000):
              revert with 0, 'bit amount too small'
          require _param1 < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_param1].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _param1:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _param1 < unknownbf443c55.length
              addr(unknownbf443c55[_param1].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_param1].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_param1].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_param1].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _param1 < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_param1].field_256)] = _param1
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _param1
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                        uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                        address newOwner=caller,
                        uint256 uID=_param2)
                  call addr(ext_call.return_data[0]) with:
                     value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                       gas 2300 * is_zero(value) wei
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_param1].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                uint256 price=uint128(unknownbf443c55[_param1].field_640) - (uint128(unknownbf443c55[_param1].field_640) * stor8 / 10000),
                address newOwner=caller,
                uint256 uID=_param2)
          call addr(ext_call.return_data[0]) with:
             value uint128(unknownbf443c55[_param1].field_640) * stor9 / 10000 wei
               gas 2300 * is_zero(value) wei
      else:
          require uint64(unknownbf443c55[_param1].field_768)
          if call.value < uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000):
              revert with 0, 'bit amount too small'
          require _param1 < unknownbf443c55.length
          auctionByTokenId[uint256(stor6[_param1].field_256)] = 0
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          require unknownbf443c55.length - 1 < unknownbf443c55.length
          if unknownbf443c55.length - 1 == _param1:
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
          else:
              require _param1 < unknownbf443c55.length
              addr(unknownbf443c55[_param1].field_0) = addr(unknownbf443c55[unknownbf443c55.length - 1].field_0)
              uint256(unknownbf443c55[_param1].field_256) = uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_512) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_512)
              uint128(unknownbf443c55[_param1].field_640) = uint128(unknownbf443c55[unknownbf443c55.length - 1].field_640)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              uint64(unknownbf443c55[_param1].field_768) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_768)
              Mask(192, 0, unknownbf443c55[_param1].field_832) = uint64(unknownbf443c55[unknownbf443c55.length - 1].field_832)
              uint128(unknownbf443c55[_param1].field_896) = 0
              require unknownbf443c55.length - 1 < unknownbf443c55.length
              addr(unknownbf443c55[unknownbf443c55.length - 1].field_0) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_256) = 0
              uint256(unknownbf443c55[unknownbf443c55.length - 1].field_512) = 0
              uint128(unknownbf443c55[unknownbf443c55.length - 1].field_768) = 0
              require _param1 < unknownbf443c55.length
              auctionByTokenId[uint256(stor6[_param1].field_256)] = _param1
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[unknownbf443c55.length - 1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) != unknownbf443c55.length - 1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[stor6.length - 1].field_0)][[94midx].field_0) = _param1
              [94midx = 0
              while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
                  mem[32] = 5
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                      [94midx = [94midx + 1
                      continue 
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
                  require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
                  uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
                  if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                      [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                      while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                          uint256(stor[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                  unknownbf443c55.length--
                  if unknownbf443c55.length > unknownbf443c55.length - 1:
                      [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                      while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                          addr(stor[[94midx]) = 0
                          uint256(stor1[[94midx]) = 0
                          uint256(stor2[[94midx]) = 0
                          uint128(stor3[[94midx]) = 0
                          [94midx = [94midx + 4
                          continue 
                  log AuctionSuccessful(
                        uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                        uint256 price=uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                        address newOwner=caller,
                        uint256 uID=_param2)
                  call addr(ext_call.return_data[0]) with:
                     value (uint128(unknownbf443c55[_param1].field_512) * stor9) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                       gas 2300 * is_zero(value) wei
                  require ext_code.size(tokenContractAddress)
                  call tokenContractAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, uint256(unknownbf443c55[_param1].field_256)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor3.length))
                  call addr(stor3.length).0x75314172 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  stop
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value (uint128(unknownbf443c55[_param1].field_512) * stor9) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          [94midx = 0
          while [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0):
              mem[32] = 5
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              mem[0] = sha3(addr(unknownbf443c55[_param1].field_0), 5)
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) != _param1:
                  [94midx = [94midx + 1
                  continue 
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              require [94midx < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][[94midx].field_0) = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0)
              require uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1 < uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)][uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)].field_0) = 0
              uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0)--
              if uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) - 1:
                  [94midx = uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) + sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) - 1
                  while sha3(sha3(addr(unknownbf443c55[_param1].field_0), 5)) + uint256(unknown1c0c78bc[addr(stor6[_param1].field_0)].field_0) > [94midx:
                      uint256(stor[[94midx]) = 0
                      [94midx = [94midx + 1
                      continue 
              unknownbf443c55.length--
              if unknownbf443c55.length > unknownbf443c55.length - 1:
                  [94midx = sha3(6) + (4 * unknownbf443c55.length - 1)
                  while sha3(6) + (4 * unknownbf443c55.length) > [94midx:
                      addr(stor[[94midx]) = 0
                      uint256(stor1[[94midx]) = 0
                      uint256(stor2[[94midx]) = 0
                      uint128(stor3[[94midx]) = 0
                      [94midx = [94midx + 4
                      continue 
              log AuctionSuccessful(
                    uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                    uint256 price=uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                    address newOwner=caller,
                    uint256 uID=_param2)
              call addr(ext_call.return_data[0]) with:
                 value (uint128(unknownbf443c55[_param1].field_512) * stor9) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
                   gas 2300 * is_zero(value) wei
              require ext_code.size(tokenContractAddress)
              call tokenContractAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, uint256(unknownbf443c55[_param1].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor3.length))
              call addr(stor3.length).0x75314172 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stop
          unknownbf443c55.length--
          if unknownbf443c55.length > unknownbf443c55.length - 1:
              [94midx = 4 * unknownbf443c55.length - 1
              while 4 * unknownbf443c55.length > [94midx:
                  addr(unknownbf443c55[[94midx].field_0) = 0
                  uint256(unknownbf443c55[[94midx].field_256) = 0
                  uint256(unknownbf443c55[[94midx].field_512) = 0
                  uint128(unknownbf443c55[[94midx].field_768) = 0
                  [94midx = [94midx + 4
                  continue 
          log AuctionSuccessful(
                uint256 tokenId=uint256(unknownbf443c55[_param1].field_256),
                uint256 price=uint128(unknownbf443c55[_param1].field_512) + (0 /′ uint64(unknownbf443c55[_param1].field_768)) - ((uint128(unknownbf443c55[_param1].field_512) * stor8) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor8) / 10000),
                address newOwner=caller,
                uint256 uID=_param2)
          call addr(ext_call.return_data[0]) with:
             value (uint128(unknownbf443c55[_param1].field_512) * stor9) + (0 /′ uint64(unknownbf443c55[_param1].field_768) * stor9) / 10000 wei
               gas 2300 * is_zero(value) wei
  require ext_code.size(tokenContractAddress)
  call tokenContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, uint256(unknownbf443c55[_param1].field_256)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(stor3.length))
  call addr(stor3.length).0x75314172 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  if not _newOwner:
      revert with 0, 'new owner must be valid'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf5074f41
# getter = None
# const = None
# payable = False
def destroyAndSend(address _recipient): # not payable
  require caller == owner
  [93mselfdestruct([91m_recipient[93m)


# hash = 0xf5366a6f
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]]
# const = None
# payable = False
def unknownf5366a6f(addr _param1): # not payable
  return uint256(unknown1c0c78bc[addr(_param1)].field_0)


# hash = 0xf851a440
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def admin(): # not payable
  return addr(stor1.length)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


