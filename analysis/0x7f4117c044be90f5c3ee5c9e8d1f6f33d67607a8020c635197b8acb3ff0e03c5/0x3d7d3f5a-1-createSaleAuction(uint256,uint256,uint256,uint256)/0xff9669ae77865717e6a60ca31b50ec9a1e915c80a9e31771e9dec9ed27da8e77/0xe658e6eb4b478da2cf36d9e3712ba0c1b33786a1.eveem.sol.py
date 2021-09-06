# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xe658E6Eb4B478da2Cf36d9e3712ba0c1b33786A1 
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
    treasurerAddress # mask: a s
    # storage address 5
    unknown50e261d3
    # storage address 6
    unknownb59f1f62 # mask: a s
    # storage address 7
    unknownc51aba2bAddress # mask: a s
    # storage address 8
    unknownf20cd5fb # mask: a s
    # storage address 9
    isSaleClockAuction # mask: a s
    # storage address 10
    unknownf0a4ff80 # mask: a s
    # storage address 11
    unknowna33014c2
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    unknown464b802bAddress # mask: a s
    # storage address 14
    stor14
# hash = 0x0b7edea3
# getter = None
# const = None
# payable = False
def unknown0b7edea3(addr m_param1, uint256 m_param2): # not payable
  if mnonFungibleContractAddress != caller:
      require caller == munknown464b802bAddress
  [94ms = 0
  [94mt = 0
  [94midx = 0
  mwhile [94midx < mstor14m[addr(m_param1)m]m:
      mem[0] = sha3(addr(m_param1), 14)
      if mstor14m[addr(m_param1)m]m[[94midxm] != m_param2:
          [94ms = [94ms
          [94mt = mstor14m[addr(m_param1)m]m[[94midxm]
          [94midx = [94midx + 1
          mcontinue 
      mem[0] = mstor14m[addr(m_param1)m]m[[94midxm]
      mem[32] = 3
      if uint64(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_576) <= 0:
          [94ms = sha3(mstor14m[addr(m_param1)m]m[[94midxm], 3)
          [94mt = mstor14m[addr(m_param1)m]m[[94midxm]
          [94midx = [94midx + 1
          mcontinue 
      if block.timestamp <= uint64(uint64(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_512) + uint64(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_576)):
          [94ms = sha3(mstor14m[addr(m_param1)m]m[[94midxm], 3)
          [94mt = mstor14m[addr(m_param1)m]m[[94midxm]
          [94midx = [94midx + 1
          mcontinue 
      if addr(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_0) == m_param1:
          addr(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_0) = 0
          mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_256 = 0
          uint128(mauctionm[mstor14m[addr(m_param1)m]m[[94midxm]m]m.field_512) = 0
          require ext_code.size(mnonFungibleContractAddress)
          call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, addr(m_param1), mstor14m[addr(m_param1)m]m[[94midxm]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log AuctionCancelled(uint256 tokenId=stor14[addr(_param1)][idx])
      require mstor14m[addr(m_param1)m] - 1 < mstor14m[addr(m_param1)m]
      require [94midx < mstor14m[addr(m_param1)m]
      mstor14m[addr(m_param1)m]m[[94midxm] = mstor14m[addr(m_param1)m]m[mstor14m[addr(m_param1)m]m]
      mstor14m[addr(m_param1)m]--
      if mstor14m[addr(m_param1)m] > mstor14m[addr(m_param1)m] - 1:
          [94midx = mstor14m[addr(m_param1)m] + sha3(sha3(addr(m_param1), 14)) - 1
          mwhile sha3(sha3(addr(m_param1), 14)) + mstor14m[addr(m_param1)m] > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      stop


# hash = 0x27ebe40a
# getter = None
# const = None
# payable = False
def createAuction(uint256 m_tokenId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration, address m_seller): # not payable
  require m_startingPrice == uint128(m_startingPrice)
  require m_endingPrice == uint128(m_endingPrice)
  require m_duration == uint64(m_duration)
  if mnonFungibleContractAddress != caller:
      require caller == munknown464b802bAddress
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_seller), this.address, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require uint64(m_duration) >= 60
  addr(mauctionm[m_tokenIdm]m.field_0) = m_seller
  uint128(mauctionm[m_tokenIdm]m.field_256) = uint128(m_startingPrice)
  uint128(mauctionm[m_tokenIdm]m.field_384) = uint128(m_endingPrice)
  uint64(mauctionm[m_tokenIdm]m.field_512) = uint64(m_duration)
  uint64(mauctionm[m_tokenIdm]m.field_576) = uint64(block.timestamp)
  log AuctionCreated(
        uint256 tokenId=_tokenId,
        uint256 startingPrice=_startingPrice << 128,
        uint256 endingPrice=_endingPrice << 128,
        uint256 duration=uint64(_duration))
  mstor14m[addr(m_seller)m]++
  mstor14m[addr(m_seller)m]m[mstor14m[addr(m_seller)m]m] = m_tokenId


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mowner
  require mstor0
  mstor0 = 0
  log Unpause()


# hash = 0x454a2ab3
# getter = None
# const = None
# payable = True
def bid(uint256 m_tokenId) payable: 
  require uint64(mauctionm[m_tokenIdm]m.field_576) > 0
  if block.timestamp <= uint64(mauctionm[m_tokenIdm]m.field_576):
      if 0 >= uint64(mauctionm[m_tokenIdm]m.field_512):
          require call.value >= uint128(mauctionm[m_tokenIdm]m.field_384)
          addr(mauctionm[m_tokenIdm]m.field_0) = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          uint128(mauctionm[m_tokenIdm]m.field_512) = 0
          if uint128(mauctionm[m_tokenIdm]m.field_384) <= 0:
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_384) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call addr(mauctionm[m_tokenIdm]m.field_0) with:
                 value uint128(mauctionm[m_tokenIdm]m.field_384) - (uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_384) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(auction[_tokenId].field_256),
                address bidder=caller)
          require ext_code.size(mnonFungibleContractAddress)
          call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor12)
          call mstor12.getPlanet(uint256 planetId) with:
               gas gas_remaining wei
              args m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 448
          if not munknownc51aba2bAddress:
              munknownb59f1f62 += uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000
          else:
              require ext_code.size(munknownc51aba2bAddress)
              call munknownc51aba2bAddress.' Yj4' with:
                   gas gas_remaining wei
                  args ext_call.return_data[64], ext_call.return_data[96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[12 len 20]:
                  munknownb59f1f62 += uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000
              else:
                  if uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000:
                      require munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 / uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 == munknownf20cd5fb
                      munknown50e261d3m[ext_call.return_data[12 len 20]m] += munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 / 10000
                  if uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000:
                      require (10000 * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) - (munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) / uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 == -munknownf20cd5fb + 10000
                      munknownb59f1f62 += (10000 * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) - (munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) / 10000
          require ext_code.size(mstor12)
          call mstor12.0xaac0b776 with:
               gas gas_remaining wei
              args addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94midx = 0
          mwhile [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m:
              mem[0] = sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] != m_tokenId:
                  [94midx = [94midx + 1
                  mcontinue 
              require mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1 < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              require [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]--
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1:
                  [94midx = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] + sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) - 1
                  mwhile sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) + mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > [94midxm:
                      mstor[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
                  require munknownf0a4ff80 % 10 < 10
                  munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_384)
                  munknownf0a4ff80++
              stop
          if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
              require munknownf0a4ff80 % 10 < 10
              munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_384)
              munknownf0a4ff80++
      else:
          require uint64(mauctionm[m_tokenIdm]m.field_512)
          require call.value >= uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512))
          addr(mauctionm[m_tokenIdm]m.field_0) = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          uint128(mauctionm[m_tokenIdm]m.field_512) = 0
          if uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512)) <= 0:
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_256) - (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512)) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call addr(mauctionm[m_tokenIdm]m.field_0) with:
                 value uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512)) - ((uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_256) - (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512)) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(auction[_tokenId].field_256) + (0 /′ uint64(auction[_tokenId].field_512)),
                address bidder=caller)
          require ext_code.size(mnonFungibleContractAddress)
          call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor12)
          call mstor12.getPlanet(uint256 planetId) with:
               gas gas_remaining wei
              args m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 448
          if not munknownc51aba2bAddress:
              munknownb59f1f62 += (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000
          else:
              require ext_code.size(munknownc51aba2bAddress)
              call munknownc51aba2bAddress.' Yj4' with:
                   gas gas_remaining wei
                  args ext_call.return_data[64], ext_call.return_data[96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[12 len 20]:
                  munknownb59f1f62 += (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000
              else:
                  if (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000:
                      require munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 / (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 == munknownf20cd5fb
                      munknown50e261d3m[ext_call.return_data[12 len 20]m] += munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 / 10000
                  if (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000:
                      require (10000 * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) - (munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) / (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 == -munknownf20cd5fb + 10000
                      munknownb59f1f62 += (10000 * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) - (munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) / 10000
          require ext_code.size(mstor12)
          call mstor12.0xaac0b776 with:
               gas gas_remaining wei
              args addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94midx = 0
          mwhile [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m:
              mem[0] = sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] != m_tokenId:
                  [94midx = [94midx + 1
                  mcontinue 
              require mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1 < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              require [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]--
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1:
                  [94midx = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] + sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) - 1
                  mwhile sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) + mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > [94midxm:
                      mstor[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
                  require munknownf0a4ff80 % 10 < 10
                  munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512))
                  munknownf0a4ff80++
              stop
          if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
              require munknownf0a4ff80 % 10 < 10
              munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512))
              munknownf0a4ff80++
  else:
      if block.timestamp - uint64(mauctionm[m_tokenIdm]m.field_576) >= uint64(mauctionm[m_tokenIdm]m.field_512):
          require call.value >= uint128(mauctionm[m_tokenIdm]m.field_384)
          addr(mauctionm[m_tokenIdm]m.field_0) = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          uint128(mauctionm[m_tokenIdm]m.field_512) = 0
          if uint128(mauctionm[m_tokenIdm]m.field_384) <= 0:
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_384) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call addr(mauctionm[m_tokenIdm]m.field_0) with:
                 value uint128(mauctionm[m_tokenIdm]m.field_384) - (uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_384) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(auction[_tokenId].field_256),
                address bidder=caller)
          require ext_code.size(mnonFungibleContractAddress)
          call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor12)
          call mstor12.getPlanet(uint256 planetId) with:
               gas gas_remaining wei
              args m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 448
          if not munknownc51aba2bAddress:
              munknownb59f1f62 += uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000
          else:
              require ext_code.size(munknownc51aba2bAddress)
              call munknownc51aba2bAddress.' Yj4' with:
                   gas gas_remaining wei
                  args ext_call.return_data[64], ext_call.return_data[96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[12 len 20]:
                  munknownb59f1f62 += uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000
              else:
                  if uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000:
                      require munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 / uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 == munknownf20cd5fb
                      munknown50e261d3m[ext_call.return_data[12 len 20]m] += munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 / 10000
                  if uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000:
                      require (10000 * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) - (munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) / uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000 == -munknownf20cd5fb + 10000
                      munknownb59f1f62 += (10000 * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) - (munknownf20cd5fb * uint128(mauctionm[m_tokenIdm]m.field_384) * mownerCut / 10000) / 10000
          require ext_code.size(mstor12)
          call mstor12.0xaac0b776 with:
               gas gas_remaining wei
              args addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94midx = 0
          mwhile [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m:
              mem[0] = sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] != m_tokenId:
                  [94midx = [94midx + 1
                  mcontinue 
              require mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1 < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              require [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]--
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1:
                  [94midx = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] + sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) - 1
                  mwhile sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) + mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > [94midxm:
                      mstor[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
                  require munknownf0a4ff80 % 10 < 10
                  munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_384)
                  munknownf0a4ff80++
              stop
          if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
              require munknownf0a4ff80 % 10 < 10
              munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_384)
              munknownf0a4ff80++
      else:
          require uint64(mauctionm[m_tokenIdm]m.field_512)
          require call.value >= uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512))
          addr(mauctionm[m_tokenIdm]m.field_0) = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          uint128(mauctionm[m_tokenIdm]m.field_512) = 0
          if uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512)) <= 0:
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_256) - ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512)) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call addr(mauctionm[m_tokenIdm]m.field_0) with:
                 value uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512)) - ((uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - uint128(mauctionm[m_tokenIdm]m.field_256) - ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512)) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(auction[_tokenId].field_256) + ((block.timestamp * uint128(auction[_tokenId].field_384)) - (uint64(auction[_tokenId].field_576) * uint128(auction[_tokenId].field_384)) - (block.timestamp * uint128(auction[_tokenId].field_256)) + (uint64(auction[_tokenId].field_576) * uint128(auction[_tokenId].field_256)) /′ uint64(auction[_tokenId].field_512)),
                address bidder=caller)
          require ext_code.size(mnonFungibleContractAddress)
          call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor12)
          call mstor12.getPlanet(uint256 planetId) with:
               gas gas_remaining wei
              args m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 448
          if not munknownc51aba2bAddress:
              munknownb59f1f62 += (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000
          else:
              require ext_code.size(munknownc51aba2bAddress)
              call munknownc51aba2bAddress.' Yj4' with:
                   gas gas_remaining wei
                  args ext_call.return_data[64], ext_call.return_data[96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[12 len 20]:
                  munknownb59f1f62 += (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000
              else:
                  if (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000:
                      require munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 / (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 == munknownf20cd5fb
                      munknown50e261d3m[ext_call.return_data[12 len 20]m] += munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 / 10000
                  if (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000:
                      require (10000 * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) - (munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) / (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000 == -munknownf20cd5fb + 10000
                      munknownb59f1f62 += (10000 * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) - (munknownf20cd5fb * (uint128(mauctionm[m_tokenIdm]m.field_256) * mownerCut) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512) * mownerCut) / 10000) / 10000
          require ext_code.size(mstor12)
          call mstor12.0xaac0b776 with:
               gas gas_remaining wei
              args addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94midx = 0
          mwhile [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m:
              mem[0] = sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] != m_tokenId:
                  [94midx = [94midx + 1
                  mcontinue 
              require mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1 < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              require [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m]
              mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]--
              if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1:
                  [94midx = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] + sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) - 1
                  mwhile sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) + mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > [94midxm:
                      mstor[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
                  require munknownf0a4ff80 % 10 < 10
                  munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512))
                  munknownf0a4ff80++
              stop
          if munknown464b802bAddress == addr(mauctionm[m_tokenIdm]m.field_0):
              require munknownf0a4ff80 % 10 < 10
              munknowna33014c2m[ext_call.return_data[0]m]m[mstor10 % 10m]m.field_0 = uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512))
              munknownf0a4ff80++


# hash = 0x464b802b
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknown464b802b(): # not payable
  return munknown464b802bAddress


# hash = 0x496a298e
# getter = None
# const = None
# payable = False
def unknown496a298e(addr m_param1): # not payable
  require caller == mowner
  require m_param1
  munknownc51aba2bAddress = m_param1


# hash = 0x4d436c6a
# getter = None
# const = None
# payable = False
def unknown4d436c6a(addr m_param1): # not payable
  if m_param1 != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Only company owner can make withdrawing'
  if not m_param1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Company address should be defined'
  require munknown50e261d3m[addr(m_param1)m] > 0
  munknown50e261d3m[addr(m_param1)m] = 0
  call m_param1 with:
     value munknown50e261d3m[addr(m_param1)m] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x50131abc
# getter = None
# const = None
# payable = False
def unknown50131abc(): # not payable
  if mtreasurerAddress != caller:
      revert with 0, 'Only treasurer'
  require munknownb59f1f62 > 0
  munknownb59f1f62 = 0
  call mtreasurerAddress with:
     value munknownb59f1f62 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x50e261d3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknown50e261d3(addr m_param1): # not payable
  return munknown50e261d3m[m_param1m]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mstor0)


# hash = 0x611e68d4
# getter = None
# const = None
# payable = False
def unknown611e68d4(addr m_param1): # not payable
  require caller == mowner
  if m_param1:
      mtreasurerAddress = m_param1


# hash = 0x78bd7935
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def getAuction(uint256 m_tokenId): # not payable
  require uint64(mauctionm[m_tokenIdm]m.field_576) > 0
  return addr(mauctionm[m_tokenIdm]m.field_0), 
         uint128(mauctionm[m_tokenIdm]m.field_256),
         uint128(mauctionm[m_tokenIdm]m.field_256),
         uint64(mauctionm[m_tokenIdm]m.field_512),
         uint64(mauctionm[m_tokenIdm]m.field_576)


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
  require not mstor0
  mstor0 = 1
  log Pause()


# hash = 0x85b86188
# getter = ['bool', ['storage', 8, 0, 9]]
# const = None
# payable = False
def isSaleClockAuction(): # not payable
  return bool(misSaleClockAuction)


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 m_tokenId): # not payable
  require mstor0
  require caller == mowner
  require uint64(mauctionm[m_tokenIdm]m.field_576) > 0
  addr(mauctionm[m_tokenIdm]m.field_0) = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  uint128(mauctionm[m_tokenIdm]m.field_512) = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args this.address, addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
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
  require uint64(mauctionm[m_tokenIdm]m.field_576) > 0
  require addr(mauctionm[m_tokenIdm]m.field_0) == caller
  addr(mauctionm[m_tokenIdm]m.field_0) = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  uint128(mauctionm[m_tokenIdm]m.field_512) = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args this.address, addr(mauctionm[m_tokenIdm]m.field_0), m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=_tokenId)
  [94midx = 0
  mwhile [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m:
      mem[0] = sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)
      if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] != m_tokenId:
          [94midx = [94midx + 1
          mcontinue 
      require mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1 < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
      require [94midx < mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]
      mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[[94midxm] = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m[mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]m]
      mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m]--
      if mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] - 1:
          [94midx = mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] + sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) - 1
          mwhile sha3(sha3(addr(mauctionm[m_tokenIdm]m.field_0), 14)) + mstor14m[addr(mstor3m[m_tokenIdm]m.field_0)m] > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      stop


# hash = 0x9adbf583
# getter = None
# const = None
# payable = False
def unknown9adbf583(addr m_param1, uint256 m_param2): # not payable
  if mnonFungibleContractAddress != caller:
      require caller == munknown464b802bAddress
  [94ms = 0
  [94ms = 0
  [94ms = 0
  mwhile 0 < mstor14m[addr(m_param1)m]m:
      if [94ms > m_param2:
          stop
      require 0 < mstor14m[addr(m_param1)m]
      mem[0] = mstor14m[addr(m_param1)m]
      mem[32] = 3
      if uint64(mauctionm[mstor14m[addr(m_param1)m]m]m.field_576) > 0:
          if block.timestamp > uint64(uint64(mauctionm[mstor14m[addr(m_param1)m]m]m.field_512) + uint64(mauctionm[mstor14m[addr(m_param1)m]m]m.field_576)):
              if addr(mauctionm[mstor14m[addr(m_param1)m]m]m.field_0) == m_param1:
                  mem[32] = 3
                  addr(mauctionm[mstor14m[addr(m_param1)m]m]m.field_0) = 0
                  mauctionm[mstor14m[addr(m_param1)m]m]m.field_256 = 0
                  uint128(mauctionm[mstor14m[addr(m_param1)m]m]m.field_512) = 0
                  mem[100] = this.address
                  mem[132] = m_param1
                  mem[164] = mstor14m[addr(m_param1)m]
                  require ext_code.size(mnonFungibleContractAddress)
                  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args this.address, addr(m_param1), mstor14m[addr(m_param1)m]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[96] = mstor14m[addr(m_param1)m]
                  log AuctionCancelled(uint256 tokenId=stor14[addr(_param1)])
              require mstor14m[addr(m_param1)m] - 1 < mstor14m[addr(m_param1)m]
              require 0 < mstor14m[addr(m_param1)m]
              mem[0] = sha3(addr(m_param1), 14)
              mstor14m[addr(m_param1)m] = mstor14m[addr(m_param1)m]m[mstor14m[addr(m_param1)m]m]
              mstor14m[addr(m_param1)m]--
              if mstor14m[addr(m_param1)m] > mstor14m[addr(m_param1)m] - 1:
                  mem[0] = sha3(addr(m_param1), 14)
                  [94midx = mstor14m[addr(m_param1)m] + sha3(sha3(addr(m_param1), 14)) - 1
                  mwhile sha3(sha3(addr(m_param1), 14)) + mstor14m[addr(m_param1)m] > [94midxm:
                      mstor[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
      [94ms = sha3(mstor14m[addr(m_param1)m], 3)
      [94ms = mstor14m[addr(m_param1)m]
      [94ms = [94ms + 1
      mcontinue 


# hash = 0xa33014c2
# getter = ['storage', 256, 0, ['add', ['cd', 36], ['sha3', ['data', ['cd', 4], 11]]]]
# const = None
# payable = False
def unknowna33014c2(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2 < 10
  return munknowna33014c2m[m_param1m]m[m_param2m]m.field_0


# hash = 0xb59f1f62
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknownb59f1f62(): # not payable
  return munknownb59f1f62


# hash = 0xb6a27b61
# getter = None
# const = None
# payable = False
def unknownb6a27b61(): # not payable
  require caller == mowner
  munknownc51aba2bAddress = 0


# hash = 0xb8b84440
# getter = None
# const = None
# payable = False
def unknownb8b84440(addr m_param1): # not payable
  require caller == mowner
  require m_param1
  munknown464b802bAddress = m_param1


# hash = 0xc51aba2b
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknownc51aba2b(): # not payable
  return munknownc51aba2bAddress


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 m_tokenId): # not payable
  require uint64(mauctionm[m_tokenIdm]m.field_576) > 0
  if block.timestamp <= uint64(mauctionm[m_tokenIdm]m.field_576):
      if 0 >= uint64(mauctionm[m_tokenIdm]m.field_512):
          return uint128(mauctionm[m_tokenIdm]m.field_384)
      if uint64(mauctionm[m_tokenIdm]m.field_512):
          return (uint128(mauctionm[m_tokenIdm]m.field_256) + (0 /′ uint64(mauctionm[m_tokenIdm]m.field_512)))
  else:
      if block.timestamp - uint64(mauctionm[m_tokenIdm]m.field_576) >= uint64(mauctionm[m_tokenIdm]m.field_512):
          return uint128(mauctionm[m_tokenIdm]m.field_384)
      if uint64(mauctionm[m_tokenIdm]m.field_512):
          return (uint128(mauctionm[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_384)) - (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mauctionm[m_tokenIdm]m.field_256)) + (uint64(mauctionm[m_tokenIdm]m.field_576) * uint128(mauctionm[m_tokenIdm]m.field_256)) /′ uint64(mauctionm[m_tokenIdm]m.field_512)))
  ('iszero', ('type', 64, ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'auction', 3))))))
  revert


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return mnonFungibleContractAddress


# hash = 0xf0a4ff80
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknownf0a4ff80(): # not payable
  return munknownf0a4ff80


# hash = 0xf20cd5fb
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknownf20cd5fb(): # not payable
  return munknownf20cd5fb


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf8a7f938
# getter = None
# const = None
# payable = False
def unknownf8a7f938(uint256 m_param1): # not payable
  mem[416] = munknowna33014c2m[m_param1m]m.field_0
  [94midx = 416
  [94ms = 0
  mwhile 736 > [94midx + 32m:
      mem[[94midx + 32] = munknowna33014c2m[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = 0
  mwhile [94midx < 10m:
      if not mem[(32 * [94midx) + 416]:
          return 0
      require [94midx < 10
      [94m_15 = mem[(32 * [94midx) + 416]
      [94midx = [94midx + 1
      [94ms = mem[(32 * [94midx) + 416] + [94ms
      mcontinue 
  return (10 * [94m_15 / 10)


# hash = 0xfda49eb4
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def treasurer(): # not payable
  return mtreasurerAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


