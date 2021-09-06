# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x029D74331F911d5DCc7F5aBc9Ce85B09F408f437 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 0
    paused # mask: a s
    # storage address 1
    nonFungibleContractAddress # mask: a s
    # storage address 2
    ownerCut # mask: a s
    # storage address 3
    unknownd4e119cf # mask: a s
    # storage address 4
    auction
    # storage address 5
    isSiringClockAuction # mask: a s
# hash = 0x0a912873
# getter = None
# const = None
# payable = False
def unknown0a912873(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, addr m_param5, bool m_param6): # not payable
  require m_param2 == uint128(m_param2)
  require m_param3 == uint128(m_param3)
  require m_param4 == uint64(m_param4)
  require caller == mnonFungibleContractAddress
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param5), this.address, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require uint64(m_param4) >= 60
  require uint128(m_param3) >= munknownd4e119cf
  require uint128(m_param2) >= 0
  mauctionm[m_param1m]m.field_0 = m_param5
  mauctionm[m_param1m]m.field_256 = uint128(m_param2)
  mauctionm[m_param1m]m.field_384 = uint128(m_param3)
  mauctionm[m_param1m]m.field_512 = uint64(m_param4)
  mauctionm[m_param1m]m.field_576 = uint64(block.timestamp)
  mauctionm[m_param1m]m.field_640 = uint128(m_param6)
  log 0x47c084ad: _param1, _param2 << 128, _param3 << 128, _param4 << 192, addr(_param5), _param6


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mowner
  require mpaused
  mpaused = 0
  return 1


# hash = 0x598647f8
# getter = None
# const = None
# payable = False
def bid(uint256 m_amount, uint256 m_auctionId): # not payable
  require caller == mnonFungibleContractAddress
  require mauctionm[m_amountm]m.field_576 > 0
  if block.timestamp <= mauctionm[m_amountm]m.field_576:
      if 0 >= mauctionm[m_amountm]m.field_512:
          require m_auctionId >= mauctionm[m_amountm]m.field_384
          mauctionm[m_amountm]m.field_0 = 0
          mauctionm[m_amountm]m.field_256 = 0
          mauctionm[m_amountm]m.field_512 = 0
          if mauctionm[m_amountm]m.field_384 > 0:
              if bool(mauctionm[m_amountm]m.field_640) != 1:
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mauctionm[m_amountm]m.field_0, mauctionm[m_amountm]m.field_384 - (mauctionm[m_amountm]m.field_384 * mownerCut / 100)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mnonFungibleContractAddress, mauctionm[m_amountm]m.field_384 * mownerCut / 100
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          log 0x2446614a: _amount, auction[_amount].field_256, caller, 0
      else:
          require mauctionm[m_amountm]m.field_512
          require m_auctionId >= mauctionm[m_amountm]m.field_256 + (0 /′ mauctionm[m_amountm]m.field_512)
          mauctionm[m_amountm]m.field_0 = 0
          mauctionm[m_amountm]m.field_256 = 0
          mauctionm[m_amountm]m.field_512 = 0
          if mauctionm[m_amountm]m.field_256 + (0 /′ mauctionm[m_amountm]m.field_512) > 0:
              if bool(mauctionm[m_amountm]m.field_640) != 1:
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mauctionm[m_amountm]m.field_0, mauctionm[m_amountm]m.field_256 + (0 /′ mauctionm[m_amountm]m.field_512) - ((mauctionm[m_amountm]m.field_256 * mownerCut) + (0 /′ mauctionm[m_amountm]m.field_512 * mownerCut) / 100)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mnonFungibleContractAddress, (mauctionm[m_amountm]m.field_256 * mownerCut) + (0 /′ mauctionm[m_amountm]m.field_512 * mownerCut) / 100
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          log 0x2446614a: _amount, auction[_amount].field_256 + (0 /′ auction[_amount].field_512), caller, 0
  else:
      if block.timestamp - mauctionm[m_amountm]m.field_576 >= mauctionm[m_amountm]m.field_512:
          require m_auctionId >= mauctionm[m_amountm]m.field_384
          mauctionm[m_amountm]m.field_0 = 0
          mauctionm[m_amountm]m.field_256 = 0
          mauctionm[m_amountm]m.field_512 = 0
          if mauctionm[m_amountm]m.field_384 > 0:
              if bool(mauctionm[m_amountm]m.field_640) != 1:
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mauctionm[m_amountm]m.field_0, mauctionm[m_amountm]m.field_384 - (mauctionm[m_amountm]m.field_384 * mownerCut / 100)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mnonFungibleContractAddress, mauctionm[m_amountm]m.field_384 * mownerCut / 100
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          log 0x2446614a: _amount, auction[_amount].field_256, caller, 0
      else:
          require mauctionm[m_amountm]m.field_512
          require m_auctionId >= mauctionm[m_amountm]m.field_256 + ((block.timestamp * mauctionm[m_amountm]m.field_384) - (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_384) - (block.timestamp * mauctionm[m_amountm]m.field_256) + (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_256) /′ mauctionm[m_amountm]m.field_512)
          mauctionm[m_amountm]m.field_0 = 0
          mauctionm[m_amountm]m.field_256 = 0
          mauctionm[m_amountm]m.field_512 = 0
          if mauctionm[m_amountm]m.field_256 + ((block.timestamp * mauctionm[m_amountm]m.field_384) - (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_384) - (block.timestamp * mauctionm[m_amountm]m.field_256) + (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_256) /′ mauctionm[m_amountm]m.field_512) > 0:
              if bool(mauctionm[m_amountm]m.field_640) != 1:
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mauctionm[m_amountm]m.field_0, mauctionm[m_amountm]m.field_256 + ((block.timestamp * mauctionm[m_amountm]m.field_384) - (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_384) - (block.timestamp * mauctionm[m_amountm]m.field_256) + (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_256) /′ mauctionm[m_amountm]m.field_512) - ((mauctionm[m_amountm]m.field_256 * mownerCut) + ((block.timestamp * mauctionm[m_amountm]m.field_384) - (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_384) - (block.timestamp * mauctionm[m_amountm]m.field_256) + (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_256) /′ mauctionm[m_amountm]m.field_512 * mownerCut) / 100)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferTokenFrom(address from, address to, uint256 tokenId) with:
                       gas gas_remaining wei
                      args caller, mnonFungibleContractAddress, (mauctionm[m_amountm]m.field_256 * mownerCut) + ((block.timestamp * mauctionm[m_amountm]m.field_384) - (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_384) - (block.timestamp * mauctionm[m_amountm]m.field_256) + (mauctionm[m_amountm]m.field_576 * mauctionm[m_amountm]m.field_256) /′ mauctionm[m_amountm]m.field_512 * mownerCut) / 100
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          log 0x2446614a: _amount, auction[_amount].field_256 + ((block.timestamp * auction[_amount].field_384) - (auction[_amount].field_576 * auction[_amount].field_384) - (block.timestamp * auction[_amount].field_256) + (auction[_amount].field_576 * auction[_amount].field_256) /′ auction[_amount].field_512), caller, 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_amountm]m.field_0, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x76190f8f
# getter = ['bool', ['storage', 8, 0, 5]]
# const = None
# payable = False
def isSiringClockAuction(): # not payable
  return bool(misSiringClockAuction)


# hash = 0x78bd7935
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def getAuction(uint256 m_tokenId): # not payable
  require mauctionm[m_tokenIdm]m.field_576 > 0
  return mauctionm[m_tokenIdm]m.field_0, 
         mauctionm[m_tokenIdm]m.field_256,
         mauctionm[m_tokenIdm]m.field_256,
         mauctionm[m_tokenIdm]m.field_512,
         mauctionm[m_tokenIdm]m.field_576,
         bool(mauctionm[m_tokenIdm]m.field_640)


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
  require caller == mowner
  require not mpaused
  mpaused = 1
  return 1


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 m_tokenId): # not payable
  require mpaused
  require caller == mowner
  require mauctionm[m_tokenIdm]m.field_576 > 0
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x9b78714c: _tokenId, bool(auction[_tokenId].field_640)


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
  require mauctionm[m_tokenIdm]m.field_576 > 0
  require mauctionm[m_tokenIdm]m.field_0 == caller
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x9b78714c: _tokenId, bool(auction[_tokenId].field_640)


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 m_tokenId): # not payable
  require mauctionm[m_tokenIdm]m.field_576 > 0
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
  ('iszero', ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'auction', 4)))))
  revert


# hash = 0xd4e119cf
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknownd4e119cf(): # not payable
  return munknownd4e119cf


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return mnonFungibleContractAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


