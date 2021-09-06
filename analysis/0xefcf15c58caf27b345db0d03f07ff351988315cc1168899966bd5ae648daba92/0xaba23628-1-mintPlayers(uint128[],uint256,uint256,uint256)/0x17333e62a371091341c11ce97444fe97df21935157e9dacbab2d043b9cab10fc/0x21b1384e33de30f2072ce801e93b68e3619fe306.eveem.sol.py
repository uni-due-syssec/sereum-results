# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x21b1384e33dE30F2072ce801E93b68e3619fe306 
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
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    listenerAddress # mask: a s
# hash = 0x09e0a9eb
# getter = None
# const = None
# payable = True
def batchBid(uint256[] m_tokenIds) payable: 
  mem[64] = (32 * m_tokenIds.length) + 128
  mem[96] = m_tokenIds.length
  mem[128 len 32 * m_tokenIds.length] = call.data[m_tokenIds + 36 len 32 * m_tokenIds.length]
  require not mpaused
  [94ms = 0
  [94mt = 0
  [94midx = 0
  [94mu = 0
  mwhile uint32([94midx) < m_tokenIds.lengthm:
      require uint32([94midx) < m_tokenIds.length
      mem[0] = mem[(32 * uint32([94midx)) + 128]
      mem[32] = 3
      if block.timestamp <= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
          if 0 >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              [94ms = sha3(mem[(32 * uint32([94midx)) + 128], 3)
              [94mt = mem[(32 * uint32([94midx)) + 128]
              [94midx = [94midx + 1
              [94mu = [94mu + uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
              mcontinue 
          if uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              [94ms = sha3(mem[(32 * uint32([94midx)) + 128], 3)
              [94mt = mem[(32 * uint32([94midx)) + 128]
              [94midx = [94midx + 1
              [94mu = [94mu + uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
              mcontinue 
      else:
          if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              [94ms = sha3(mem[(32 * uint32([94midx)) + 128], 3)
              [94mt = mem[(32 * uint32([94midx)) + 128]
              [94midx = [94midx + 1
              [94mu = [94mu + uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
              mcontinue 
          if uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              [94ms = sha3(mem[(32 * uint32([94midx)) + 128], 3)
              [94mt = mem[(32 * uint32([94midx)) + 128]
              [94midx = [94midx + 1
              [94mu = [94mu + uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
              mcontinue 
      ('iszero', ('type', 64, ('field', 512, ('stor', ('map', ('mem', ('range', ('add', 128, ('mask_shl', 32, 0, 5, ('var', 0))), 32)), ('name', 'stor3', 3))))))
      revert
  require [94mu <= call.value
  [94mu = 0
  [94mu = 0
  [94mu = 0
  [94mu = [94ms
  [94mu = [94mt
  [94midx = 0
  mwhile uint32([94midx) < m_tokenIds.lengthm:
      require uint32([94midx) < mem[96]
      [94m_668 = mem[(32 * uint32([94midx)) + 128]
      [94m_669 = sha3(mem[(32 * uint32([94midx)) + 128], 3)
      if block.timestamp <= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
          if 0 >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              [94m_670 = sha3(mem[(32 * uint32([94midx)) + 128], 3)
              require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) > 0
              if block.timestamp <= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
                  if 0 >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
                      require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
                      mem[0] = mem[(32 * uint32([94midx)) + 128]
                      mem[32] = 3
                      mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
                      uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
                      uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
                      if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                          mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                          mem[mem[64] + 64] = caller
                          log AuctionSuccessful(
                                uint256 tokenId=mem[mem[64]],
                                uint256 totalPrice=uint128(stor1[_670].field_0),
                                address bidder=caller)
                      else:
                          call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                             value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                               gas 2300 * is_zero(value) wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                          mem[mem[64] + 64] = uint128(mstor1m[[94m_670m]m.field_128) - (uint128(mstor1m[[94m_670m]m.field_128) * mstor2m.length / 10000)
                          mem[mem[64] + 96] = mstor[[94m_670m]
                          mem[mem[64] + 128] = caller
                          log AuctionSettled(
                                uint256 tokenId=mem[mem[64]],
                                uint256 price=uint128(stor1[_670].field_0),
                                uint256 sellerProceeds=uint128(stor1[_670].field_128) - (uint128(stor1[_670].field_128) * stor2.length / 10000),
                                address seller=stor[_670],
                                address buyer=caller)
                          log AuctionSuccessful(
                                uint256 tokenId=_668,
                                uint256 totalPrice=uint128(stor1[_670].field_0),
                                address bidder=caller)
                      require ext_code.size(addr(mstor1m.length))
                      call addr(mstor1m.length).approve(address spender, uint256 value) with:
                           gas gas_remaining wei
                          args caller, [94m_668
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = this.address
                      mem[mem[64] + 36] = caller
                      mem[mem[64] + 68] = [94m_668
                      require ext_code.size(addr(mstor1m.length))
                      call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args this.address, caller, [94m_668
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if mlistenerAddress:
                          mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = [94m_668
                          mem[mem[64] + 36] = uint128(mstor1m[[94m_670m]m.field_128)
                          mem[mem[64] + 68] = mstor[[94m_669m]
                          mem[mem[64] + 100] = caller
                          require ext_code.size(mlistenerAddress)
                          call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                               gas gas_remaining wei
                              args [94m_668, uint128(mstor1m[[94m_670m]m.field_0), mstor[[94m_669m], caller
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                      [94mu = uint128(mstor1m[[94m_670m]m.field_128)
                      [94mu = uint128(mstor1m[[94m_669m]m.field_128)
                      [94mu = mstor[[94m_669m]
                      [94mu = [94m_669
                      [94mu = [94m_668
                      [94midx = [94midx + 1
                      mcontinue 
                  require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
                  require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
                  mem[0] = mem[(32 * uint32([94midx)) + 128]
                  mem[32] = 3
                  mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
                  uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
                  uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
                  if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = caller
                      log AuctionSuccessful(
                            uint256 tokenId=mem[mem[64]],
                            uint256 totalPrice=uint128(stor1[_670].field_0) + (0 /′ uint64(stor2[_670].field_0)),
                            address bidder=caller)
                  else:
                      call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                         value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = uint128(mstor1m[[94m_670m]m.field_0) + (0 /′ uint64(mstor2m[[94m_670m]m.field_0)) - ((uint128(mstor1m[[94m_670m]m.field_0) * mstor2m.length) + (0 /′ uint64(mstor2m[[94m_670m]m.field_0) * mstor2m.length) / 10000)
                      mem[mem[64] + 96] = mstor[[94m_670m]
                      mem[mem[64] + 128] = caller
                      log AuctionSettled(
                            uint256 tokenId=mem[mem[64]],
                            uint256 price=uint128(stor1[_670].field_0) + (0 /′ uint64(stor2[_670].field_0)),
                            uint256 sellerProceeds=uint128(stor1[_670].field_0) + (0 /′ uint64(stor2[_670].field_0)) - ((uint128(stor1[_670].field_0) * stor2.length) + (0 /′ uint64(stor2[_670].field_0) * stor2.length) / 10000),
                            address seller=stor[_670],
                            address buyer=caller)
                      log AuctionSuccessful(
                            uint256 tokenId=_668,
                            uint256 totalPrice=uint128(stor1[_670].field_0) + (0 /′ uint64(stor2[_670].field_0)),
                            address bidder=caller)
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = this.address
                  mem[mem[64] + 36] = caller
                  mem[mem[64] + 68] = [94m_668
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args this.address, caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if mlistenerAddress:
                      mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = [94m_668
                      mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_670m]m.field_0) + (0 /′ uint64(mstor2m[[94m_670m]m.field_0)))
                      mem[mem[64] + 68] = mstor[[94m_669m]
                      mem[mem[64] + 100] = caller
                      require ext_code.size(mlistenerAddress)
                      call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                           gas gas_remaining wei
                          args [94m_668, uint128(mstor1m[[94m_670m]m.field_0) + (0 /′ uint64(mstor2m[[94m_670m]m.field_0)) << 128, mstor[[94m_669m], caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  [94mu = uint128(mstor1m[[94m_670m]m.field_0) + (0 /′ uint64(mstor2m[[94m_670m]m.field_0))
                  [94mu = uint128(mstor1m[[94m_669m]m.field_128)
                  [94mu = mstor[[94m_669m]
                  [94mu = [94m_669
                  [94mu = [94m_668
                  [94midx = [94midx + 1
                  mcontinue 
              if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
                  require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
                  mem[0] = mem[(32 * uint32([94midx)) + 128]
                  mem[32] = 3
                  mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
                  uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
                  uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
                  if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = caller
                      log AuctionSuccessful(
                            uint256 tokenId=mem[mem[64]],
                            uint256 totalPrice=uint128(stor1[_670].field_0),
                            address bidder=caller)
                  else:
                      call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                         value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = uint128(mstor1m[[94m_670m]m.field_128) - (uint128(mstor1m[[94m_670m]m.field_128) * mstor2m.length / 10000)
                      mem[mem[64] + 96] = mstor[[94m_670m]
                      mem[mem[64] + 128] = caller
                      log AuctionSettled(
                            uint256 tokenId=mem[mem[64]],
                            uint256 price=uint128(stor1[_670].field_0),
                            uint256 sellerProceeds=uint128(stor1[_670].field_128) - (uint128(stor1[_670].field_128) * stor2.length / 10000),
                            address seller=stor[_670],
                            address buyer=caller)
                      log AuctionSuccessful(
                            uint256 tokenId=_668,
                            uint256 totalPrice=uint128(stor1[_670].field_0),
                            address bidder=caller)
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = this.address
                  mem[mem[64] + 36] = caller
                  mem[mem[64] + 68] = [94m_668
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args this.address, caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if mlistenerAddress:
                      mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = [94m_668
                      mem[mem[64] + 36] = uint128(mstor1m[[94m_670m]m.field_128)
                      mem[mem[64] + 68] = mstor[[94m_669m]
                      mem[mem[64] + 100] = caller
                      require ext_code.size(mlistenerAddress)
                      call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                           gas gas_remaining wei
                          args [94m_668, uint128(mstor1m[[94m_670m]m.field_0), mstor[[94m_669m], caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  [94mu = uint128(mstor1m[[94m_670m]m.field_128)
                  [94mu = uint128(mstor1m[[94m_669m]m.field_128)
                  [94mu = mstor[[94m_669m]
                  [94mu = [94m_669
                  [94mu = [94m_668
                  [94midx = [94midx + 1
                  mcontinue 
              require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
              require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_670].field_0) + ((block.timestamp * uint128(stor1[_670].field_128)) - (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_128)) - (block.timestamp * uint128(stor1[_670].field_0)) + (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_0)) /′ uint64(stor2[_670].field_0)),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_670m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_670m]m.field_128)) - (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_670m]m.field_0)) + (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_0)) /′ uint64(mstor2m[[94m_670m]m.field_0)) - ((uint128(mstor1m[[94m_670m]m.field_0) * mstor2m.length) + ((block.timestamp * uint128(mstor1m[[94m_670m]m.field_128)) - (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_670m]m.field_0)) + (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_0)) /′ uint64(mstor2m[[94m_670m]m.field_0) * mstor2m.length) / 10000)
                  mem[mem[64] + 96] = mstor[[94m_670m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_670].field_0) + ((block.timestamp * uint128(stor1[_670].field_128)) - (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_128)) - (block.timestamp * uint128(stor1[_670].field_0)) + (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_0)) /′ uint64(stor2[_670].field_0)),
                        uint256 sellerProceeds=uint128(stor1[_670].field_0) + ((block.timestamp * uint128(stor1[_670].field_128)) - (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_128)) - (block.timestamp * uint128(stor1[_670].field_0)) + (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_0)) /′ uint64(stor2[_670].field_0)) - ((uint128(stor1[_670].field_0) * stor2.length) + ((block.timestamp * uint128(stor1[_670].field_128)) - (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_128)) - (block.timestamp * uint128(stor1[_670].field_0)) + (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_0)) /′ uint64(stor2[_670].field_0) * stor2.length) / 10000),
                        address seller=stor[_670],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_670].field_0) + ((block.timestamp * uint128(stor1[_670].field_128)) - (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_128)) - (block.timestamp * uint128(stor1[_670].field_0)) + (uint64(stor2[_670].field_64) * uint128(stor1[_670].field_0)) /′ uint64(stor2[_670].field_0)),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_670m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_670m]m.field_128)) - (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_670m]m.field_0)) + (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_0)) /′ uint64(mstor2m[[94m_670m]m.field_0)))
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_670m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_670m]m.field_128)) - (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_670m]m.field_0)) + (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_0)) /′ uint64(mstor2m[[94m_670m]m.field_0)) << 128, mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_670m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_670m]m.field_128)) - (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_670m]m.field_0)) + (uint64(mstor2m[[94m_670m]m.field_64) * uint128(mstor1m[[94m_670m]m.field_0)) /′ uint64(mstor2m[[94m_670m]m.field_0))
              [94mu = uint128(mstor1m[[94m_669m]m.field_128)
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
          [94m_671 = sha3(mem[(32 * uint32([94midx)) + 128], 3)
          require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) > 0
          if block.timestamp <= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
              if 0 < uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
                  require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
                  mem[0] = mem[(32 * uint32([94midx)) + 128]
                  mem[32] = 3
                  mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
                  uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
                  uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
                  if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = caller
                      log AuctionSuccessful(
                            uint256 tokenId=mem[mem[64]],
                            uint256 totalPrice=uint128(stor1[_671].field_0) + (0 /′ uint64(stor2[_671].field_0)),
                            address bidder=caller)
                  else:
                      call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                         value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = uint128(mstor1m[[94m_671m]m.field_0) + (0 /′ uint64(mstor2m[[94m_671m]m.field_0)) - ((uint128(mstor1m[[94m_671m]m.field_0) * mstor2m.length) + (0 /′ uint64(mstor2m[[94m_671m]m.field_0) * mstor2m.length) / 10000)
                      mem[mem[64] + 96] = mstor[[94m_671m]
                      mem[mem[64] + 128] = caller
                      log AuctionSettled(
                            uint256 tokenId=mem[mem[64]],
                            uint256 price=uint128(stor1[_671].field_0) + (0 /′ uint64(stor2[_671].field_0)),
                            uint256 sellerProceeds=uint128(stor1[_671].field_0) + (0 /′ uint64(stor2[_671].field_0)) - ((uint128(stor1[_671].field_0) * stor2.length) + (0 /′ uint64(stor2[_671].field_0) * stor2.length) / 10000),
                            address seller=stor[_671],
                            address buyer=caller)
                      log AuctionSuccessful(
                            uint256 tokenId=_668,
                            uint256 totalPrice=uint128(stor1[_671].field_0) + (0 /′ uint64(stor2[_671].field_0)),
                            address bidder=caller)
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = this.address
                  mem[mem[64] + 36] = caller
                  mem[mem[64] + 68] = [94m_668
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args this.address, caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if mlistenerAddress:
                      mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = [94m_668
                      mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_671m]m.field_0) + (0 /′ uint64(mstor2m[[94m_671m]m.field_0)))
                      mem[mem[64] + 68] = mstor[[94m_669m]
                      mem[mem[64] + 100] = caller
                      require ext_code.size(mlistenerAddress)
                      call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                           gas gas_remaining wei
                          args [94m_668, uint128(mstor1m[[94m_671m]m.field_0) + (0 /′ uint64(mstor2m[[94m_671m]m.field_0)) << 128, mstor[[94m_669m], caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  [94mu = uint128(mstor1m[[94m_671m]m.field_0) + (0 /′ uint64(mstor2m[[94m_671m]m.field_0))
                  [94mu = uint128(mstor1m[[94m_669m]m.field_0) + (0 /′ uint64(mstor2m[[94m_669m]m.field_0))
                  [94mu = mstor[[94m_669m]
                  [94mu = [94m_669
                  [94mu = [94m_668
                  [94midx = [94midx + 1
                  mcontinue 
              require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_671].field_0),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_671m]m.field_128) - (uint128(mstor1m[[94m_671m]m.field_128) * mstor2m.length / 10000)
                  mem[mem[64] + 96] = mstor[[94m_671m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_671].field_0),
                        uint256 sellerProceeds=uint128(stor1[_671].field_128) - (uint128(stor1[_671].field_128) * stor2.length / 10000),
                        address seller=stor[_671],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_671].field_0),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(mstor1m[[94m_671m]m.field_128)
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_671m]m.field_0), mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_671m]m.field_128)
              [94mu = uint128(mstor1m[[94m_669m]m.field_0) + (0 /′ uint64(mstor2m[[94m_669m]m.field_0))
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_671].field_0),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_671m]m.field_128) - (uint128(mstor1m[[94m_671m]m.field_128) * mstor2m.length / 10000)
                  mem[mem[64] + 96] = mstor[[94m_671m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_671].field_0),
                        uint256 sellerProceeds=uint128(stor1[_671].field_128) - (uint128(stor1[_671].field_128) * stor2.length / 10000),
                        address seller=stor[_671],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_671].field_0),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(mstor1m[[94m_671m]m.field_128)
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_671m]m.field_0), mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_671m]m.field_128)
              [94mu = uint128(mstor1m[[94m_669m]m.field_0) + (0 /′ uint64(mstor2m[[94m_669m]m.field_0))
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
          require 0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) >= (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
          mem[0] = mem[(32 * uint32([94midx)) + 128]
          mem[32] = 3
          mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
          uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
          uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
          if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = caller
              log AuctionSuccessful(
                    uint256 tokenId=mem[mem[64]],
                    uint256 totalPrice=uint128(stor1[_671].field_0) + ((block.timestamp * uint128(stor1[_671].field_128)) - (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_128)) - (block.timestamp * uint128(stor1[_671].field_0)) + (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_0)) /′ uint64(stor2[_671].field_0)),
                    address bidder=caller)
          else:
              call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                 value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = uint128(mstor1m[[94m_671m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_671m]m.field_128)) - (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_671m]m.field_0)) + (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_0)) /′ uint64(mstor2m[[94m_671m]m.field_0)) - ((uint128(mstor1m[[94m_671m]m.field_0) * mstor2m.length) + ((block.timestamp * uint128(mstor1m[[94m_671m]m.field_128)) - (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_671m]m.field_0)) + (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_0)) /′ uint64(mstor2m[[94m_671m]m.field_0) * mstor2m.length) / 10000)
              mem[mem[64] + 96] = mstor[[94m_671m]
              mem[mem[64] + 128] = caller
              log AuctionSettled(
                    uint256 tokenId=mem[mem[64]],
                    uint256 price=uint128(stor1[_671].field_0) + ((block.timestamp * uint128(stor1[_671].field_128)) - (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_128)) - (block.timestamp * uint128(stor1[_671].field_0)) + (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_0)) /′ uint64(stor2[_671].field_0)),
                    uint256 sellerProceeds=uint128(stor1[_671].field_0) + ((block.timestamp * uint128(stor1[_671].field_128)) - (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_128)) - (block.timestamp * uint128(stor1[_671].field_0)) + (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_0)) /′ uint64(stor2[_671].field_0)) - ((uint128(stor1[_671].field_0) * stor2.length) + ((block.timestamp * uint128(stor1[_671].field_128)) - (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_128)) - (block.timestamp * uint128(stor1[_671].field_0)) + (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_0)) /′ uint64(stor2[_671].field_0) * stor2.length) / 10000),
                    address seller=stor[_671],
                    address buyer=caller)
              log AuctionSuccessful(
                    uint256 tokenId=_668,
                    uint256 totalPrice=uint128(stor1[_671].field_0) + ((block.timestamp * uint128(stor1[_671].field_128)) - (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_128)) - (block.timestamp * uint128(stor1[_671].field_0)) + (uint64(stor2[_671].field_64) * uint128(stor1[_671].field_0)) /′ uint64(stor2[_671].field_0)),
                    address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = this.address
          mem[mem[64] + 36] = caller
          mem[mem[64] + 68] = [94m_668
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = [94m_668
              mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_671m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_671m]m.field_128)) - (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_671m]m.field_0)) + (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_0)) /′ uint64(mstor2m[[94m_671m]m.field_0)))
              mem[mem[64] + 68] = mstor[[94m_669m]
              mem[mem[64] + 100] = caller
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args [94m_668, uint128(mstor1m[[94m_671m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_671m]m.field_128)) - (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_671m]m.field_0)) + (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_0)) /′ uint64(mstor2m[[94m_671m]m.field_0)) << 128, mstor[[94m_669m], caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94mu = uint128(mstor1m[[94m_671m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_671m]m.field_128)) - (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_671m]m.field_0)) + (uint64(mstor2m[[94m_671m]m.field_64) * uint128(mstor1m[[94m_671m]m.field_0)) /′ uint64(mstor2m[[94m_671m]m.field_0))
          [94mu = uint128(mstor1m[[94m_669m]m.field_0) + (0 /′ uint64(mstor2m[[94m_669m]m.field_0))
          [94mu = mstor[[94m_669m]
          [94mu = [94m_669
          [94mu = [94m_668
          [94midx = [94midx + 1
          mcontinue 
      if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
          [94m_672 = sha3(mem[(32 * uint32([94midx)) + 128], 3)
          require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) > 0
          if block.timestamp <= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
              if 0 >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
                  require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
                  mem[0] = mem[(32 * uint32([94midx)) + 128]
                  mem[32] = 3
                  mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
                  uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
                  uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
                  if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = caller
                      log AuctionSuccessful(
                            uint256 tokenId=mem[mem[64]],
                            uint256 totalPrice=uint128(stor1[_672].field_0),
                            address bidder=caller)
                  else:
                      call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                         value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                      mem[mem[64] + 64] = uint128(mstor1m[[94m_672m]m.field_128) - (uint128(mstor1m[[94m_672m]m.field_128) * mstor2m.length / 10000)
                      mem[mem[64] + 96] = mstor[[94m_672m]
                      mem[mem[64] + 128] = caller
                      log AuctionSettled(
                            uint256 tokenId=mem[mem[64]],
                            uint256 price=uint128(stor1[_672].field_0),
                            uint256 sellerProceeds=uint128(stor1[_672].field_128) - (uint128(stor1[_672].field_128) * stor2.length / 10000),
                            address seller=stor[_672],
                            address buyer=caller)
                      log AuctionSuccessful(
                            uint256 tokenId=_668,
                            uint256 totalPrice=uint128(stor1[_672].field_0),
                            address bidder=caller)
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = this.address
                  mem[mem[64] + 36] = caller
                  mem[mem[64] + 68] = [94m_668
                  require ext_code.size(addr(mstor1m.length))
                  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args this.address, caller, [94m_668
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if mlistenerAddress:
                      mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = [94m_668
                      mem[mem[64] + 36] = uint128(mstor1m[[94m_672m]m.field_128)
                      mem[mem[64] + 68] = mstor[[94m_669m]
                      mem[mem[64] + 100] = caller
                      require ext_code.size(mlistenerAddress)
                      call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                           gas gas_remaining wei
                          args [94m_668, uint128(mstor1m[[94m_672m]m.field_0), mstor[[94m_669m], caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  [94mu = uint128(mstor1m[[94m_672m]m.field_128)
                  [94mu = uint128(mstor1m[[94m_669m]m.field_128)
                  [94mu = mstor[[94m_669m]
                  [94mu = [94m_669
                  [94mu = [94m_668
                  [94midx = [94midx + 1
                  mcontinue 
              require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
              require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_672].field_0) + (0 /′ uint64(stor2[_672].field_0)),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_672m]m.field_0) + (0 /′ uint64(mstor2m[[94m_672m]m.field_0)) - ((uint128(mstor1m[[94m_672m]m.field_0) * mstor2m.length) + (0 /′ uint64(mstor2m[[94m_672m]m.field_0) * mstor2m.length) / 10000)
                  mem[mem[64] + 96] = mstor[[94m_672m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_672].field_0) + (0 /′ uint64(stor2[_672].field_0)),
                        uint256 sellerProceeds=uint128(stor1[_672].field_0) + (0 /′ uint64(stor2[_672].field_0)) - ((uint128(stor1[_672].field_0) * stor2.length) + (0 /′ uint64(stor2[_672].field_0) * stor2.length) / 10000),
                        address seller=stor[_672],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_672].field_0) + (0 /′ uint64(stor2[_672].field_0)),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_672m]m.field_0) + (0 /′ uint64(mstor2m[[94m_672m]m.field_0)))
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_672m]m.field_0) + (0 /′ uint64(mstor2m[[94m_672m]m.field_0)) << 128, mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_672m]m.field_0) + (0 /′ uint64(mstor2m[[94m_672m]m.field_0))
              [94mu = uint128(mstor1m[[94m_669m]m.field_128)
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_672].field_0),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_672m]m.field_128) - (uint128(mstor1m[[94m_672m]m.field_128) * mstor2m.length / 10000)
                  mem[mem[64] + 96] = mstor[[94m_672m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_672].field_0),
                        uint256 sellerProceeds=uint128(stor1[_672].field_128) - (uint128(stor1[_672].field_128) * stor2.length / 10000),
                        address seller=stor[_672],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_672].field_0),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(mstor1m[[94m_672m]m.field_128)
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_672m]m.field_0), mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_672m]m.field_128)
              [94mu = uint128(mstor1m[[94m_669m]m.field_128)
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
          require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512))
          mem[0] = mem[(32 * uint32([94midx)) + 128]
          mem[32] = 3
          mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
          uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
          uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
          if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = caller
              log AuctionSuccessful(
                    uint256 tokenId=mem[mem[64]],
                    uint256 totalPrice=uint128(stor1[_672].field_0) + ((block.timestamp * uint128(stor1[_672].field_128)) - (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_128)) - (block.timestamp * uint128(stor1[_672].field_0)) + (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_0)) /′ uint64(stor2[_672].field_0)),
                    address bidder=caller)
          else:
              call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                 value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = uint128(mstor1m[[94m_672m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_672m]m.field_128)) - (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_672m]m.field_0)) + (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_0)) /′ uint64(mstor2m[[94m_672m]m.field_0)) - ((uint128(mstor1m[[94m_672m]m.field_0) * mstor2m.length) + ((block.timestamp * uint128(mstor1m[[94m_672m]m.field_128)) - (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_672m]m.field_0)) + (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_0)) /′ uint64(mstor2m[[94m_672m]m.field_0) * mstor2m.length) / 10000)
              mem[mem[64] + 96] = mstor[[94m_672m]
              mem[mem[64] + 128] = caller
              log AuctionSettled(
                    uint256 tokenId=mem[mem[64]],
                    uint256 price=uint128(stor1[_672].field_0) + ((block.timestamp * uint128(stor1[_672].field_128)) - (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_128)) - (block.timestamp * uint128(stor1[_672].field_0)) + (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_0)) /′ uint64(stor2[_672].field_0)),
                    uint256 sellerProceeds=uint128(stor1[_672].field_0) + ((block.timestamp * uint128(stor1[_672].field_128)) - (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_128)) - (block.timestamp * uint128(stor1[_672].field_0)) + (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_0)) /′ uint64(stor2[_672].field_0)) - ((uint128(stor1[_672].field_0) * stor2.length) + ((block.timestamp * uint128(stor1[_672].field_128)) - (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_128)) - (block.timestamp * uint128(stor1[_672].field_0)) + (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_0)) /′ uint64(stor2[_672].field_0) * stor2.length) / 10000),
                    address seller=stor[_672],
                    address buyer=caller)
              log AuctionSuccessful(
                    uint256 tokenId=_668,
                    uint256 totalPrice=uint128(stor1[_672].field_0) + ((block.timestamp * uint128(stor1[_672].field_128)) - (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_128)) - (block.timestamp * uint128(stor1[_672].field_0)) + (uint64(stor2[_672].field_64) * uint128(stor1[_672].field_0)) /′ uint64(stor2[_672].field_0)),
                    address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = this.address
          mem[mem[64] + 36] = caller
          mem[mem[64] + 68] = [94m_668
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = [94m_668
              mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_672m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_672m]m.field_128)) - (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_672m]m.field_0)) + (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_0)) /′ uint64(mstor2m[[94m_672m]m.field_0)))
              mem[mem[64] + 68] = mstor[[94m_669m]
              mem[mem[64] + 100] = caller
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args [94m_668, uint128(mstor1m[[94m_672m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_672m]m.field_128)) - (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_672m]m.field_0)) + (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_0)) /′ uint64(mstor2m[[94m_672m]m.field_0)) << 128, mstor[[94m_669m], caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94mu = uint128(mstor1m[[94m_672m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_672m]m.field_128)) - (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_672m]m.field_0)) + (uint64(mstor2m[[94m_672m]m.field_64) * uint128(mstor1m[[94m_672m]m.field_0)) /′ uint64(mstor2m[[94m_672m]m.field_0))
          [94mu = uint128(mstor1m[[94m_669m]m.field_128)
          [94mu = mstor[[94m_669m]
          [94mu = [94m_669
          [94mu = [94m_668
          [94midx = [94midx + 1
          mcontinue 
      require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
      [94m_673 = sha3(mem[(32 * uint32([94midx)) + 128], 3)
      require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) > 0
      if block.timestamp > uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576):
          if block.timestamp - uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) < uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
              require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
              mem[0] = mem[(32 * uint32([94midx)) + 128]
              mem[32] = 3
              mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
              uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
              uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
              if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = caller
                  log AuctionSuccessful(
                        uint256 tokenId=mem[mem[64]],
                        uint256 totalPrice=uint128(stor1[_673].field_0) + ((block.timestamp * uint128(stor1[_673].field_128)) - (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_128)) - (block.timestamp * uint128(stor1[_673].field_0)) + (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_0)) /′ uint64(stor2[_673].field_0)),
                        address bidder=caller)
              else:
                  call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                     value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
                  mem[mem[64] + 64] = uint128(mstor1m[[94m_673m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_673m]m.field_128)) - (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_673m]m.field_0)) + (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_0)) /′ uint64(mstor2m[[94m_673m]m.field_0)) - ((uint128(mstor1m[[94m_673m]m.field_0) * mstor2m.length) + ((block.timestamp * uint128(mstor1m[[94m_673m]m.field_128)) - (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_673m]m.field_0)) + (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_0)) /′ uint64(mstor2m[[94m_673m]m.field_0) * mstor2m.length) / 10000)
                  mem[mem[64] + 96] = mstor[[94m_673m]
                  mem[mem[64] + 128] = caller
                  log AuctionSettled(
                        uint256 tokenId=mem[mem[64]],
                        uint256 price=uint128(stor1[_673].field_0) + ((block.timestamp * uint128(stor1[_673].field_128)) - (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_128)) - (block.timestamp * uint128(stor1[_673].field_0)) + (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_0)) /′ uint64(stor2[_673].field_0)),
                        uint256 sellerProceeds=uint128(stor1[_673].field_0) + ((block.timestamp * uint128(stor1[_673].field_128)) - (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_128)) - (block.timestamp * uint128(stor1[_673].field_0)) + (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_0)) /′ uint64(stor2[_673].field_0)) - ((uint128(stor1[_673].field_0) * stor2.length) + ((block.timestamp * uint128(stor1[_673].field_128)) - (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_128)) - (block.timestamp * uint128(stor1[_673].field_0)) + (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_0)) /′ uint64(stor2[_673].field_0) * stor2.length) / 10000),
                        address seller=stor[_673],
                        address buyer=caller)
                  log AuctionSuccessful(
                        uint256 tokenId=_668,
                        uint256 totalPrice=uint128(stor1[_673].field_0) + ((block.timestamp * uint128(stor1[_673].field_128)) - (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_128)) - (block.timestamp * uint128(stor1[_673].field_0)) + (uint64(stor2[_673].field_64) * uint128(stor1[_673].field_0)) /′ uint64(stor2[_673].field_0)),
                        address bidder=caller)
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = this.address
              mem[mem[64] + 36] = caller
              mem[mem[64] + 68] = [94m_668
              require ext_code.size(addr(mstor1m.length))
              call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args this.address, caller, [94m_668
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if mlistenerAddress:
                  mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = [94m_668
                  mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_673m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_673m]m.field_128)) - (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_673m]m.field_0)) + (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_0)) /′ uint64(mstor2m[[94m_673m]m.field_0)))
                  mem[mem[64] + 68] = mstor[[94m_669m]
                  mem[mem[64] + 100] = caller
                  require ext_code.size(mlistenerAddress)
                  call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                       gas gas_remaining wei
                      args [94m_668, uint128(mstor1m[[94m_673m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_673m]m.field_128)) - (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_673m]m.field_0)) + (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_0)) /′ uint64(mstor2m[[94m_673m]m.field_0)) << 128, mstor[[94m_669m], caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              [94mu = uint128(mstor1m[[94m_673m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_673m]m.field_128)) - (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_673m]m.field_0)) + (uint64(mstor2m[[94m_673m]m.field_64) * uint128(mstor1m[[94m_673m]m.field_0)) /′ uint64(mstor2m[[94m_673m]m.field_0))
              [94mu = uint128(mstor1m[[94m_669m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_669m]m.field_128)) - (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_669m]m.field_0)) + (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_0)) /′ uint64(mstor2m[[94m_669m]m.field_0))
              [94mu = mstor[[94m_669m]
              [94mu = [94m_669
              [94mu = [94m_668
              [94midx = [94midx + 1
              mcontinue 
          require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
          mem[0] = mem[(32 * uint32([94midx)) + 128]
          mem[32] = 3
          mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
          uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
          uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
          if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = caller
              log AuctionSuccessful(
                    uint256 tokenId=mem[mem[64]],
                    uint256 totalPrice=uint128(stor1[_673].field_0),
                    address bidder=caller)
          else:
              call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                 value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = uint128(mstor1m[[94m_673m]m.field_128) - (uint128(mstor1m[[94m_673m]m.field_128) * mstor2m.length / 10000)
              mem[mem[64] + 96] = mstor[[94m_673m]
              mem[mem[64] + 128] = caller
              log AuctionSettled(
                    uint256 tokenId=mem[mem[64]],
                    uint256 price=uint128(stor1[_673].field_0),
                    uint256 sellerProceeds=uint128(stor1[_673].field_128) - (uint128(stor1[_673].field_128) * stor2.length / 10000),
                    address seller=stor[_673],
                    address buyer=caller)
              log AuctionSuccessful(
                    uint256 tokenId=_668,
                    uint256 totalPrice=uint128(stor1[_673].field_0),
                    address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = this.address
          mem[mem[64] + 36] = caller
          mem[mem[64] + 68] = [94m_668
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = [94m_668
              mem[mem[64] + 36] = uint128(mstor1m[[94m_673m]m.field_128)
              mem[mem[64] + 68] = mstor[[94m_669m]
              mem[mem[64] + 100] = caller
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args [94m_668, uint128(mstor1m[[94m_673m]m.field_0), mstor[[94m_669m], caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94mu = uint128(mstor1m[[94m_673m]m.field_128)
          [94mu = uint128(mstor1m[[94m_669m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_669m]m.field_128)) - (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_669m]m.field_0)) + (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_0)) /′ uint64(mstor2m[[94m_669m]m.field_0))
          [94mu = mstor[[94m_669m]
          [94mu = [94m_669
          [94mu = [94m_668
          [94midx = [94midx + 1
          mcontinue 
      if 0 >= uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512):
          require uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) >= uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)
          mem[0] = mem[(32 * uint32([94midx)) + 128]
          mem[32] = 3
          mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
          uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
          uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
          if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) <= 0:
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = caller
              log AuctionSuccessful(
                    uint256 tokenId=mem[mem[64]],
                    uint256 totalPrice=uint128(stor1[_673].field_0),
                    address bidder=caller)
          else:
              call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
                 value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) - (uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384) * mstor2m.length / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
              mem[mem[64] + 64] = uint128(mstor1m[[94m_673m]m.field_128) - (uint128(mstor1m[[94m_673m]m.field_128) * mstor2m.length / 10000)
              mem[mem[64] + 96] = mstor[[94m_673m]
              mem[mem[64] + 128] = caller
              log AuctionSettled(
                    uint256 tokenId=mem[mem[64]],
                    uint256 price=uint128(stor1[_673].field_0),
                    uint256 sellerProceeds=uint128(stor1[_673].field_128) - (uint128(stor1[_673].field_128) * stor2.length / 10000),
                    address seller=stor[_673],
                    address buyer=caller)
              log AuctionSuccessful(
                    uint256 tokenId=_668,
                    uint256 totalPrice=uint128(stor1[_673].field_0),
                    address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = this.address
          mem[mem[64] + 36] = caller
          mem[mem[64] + 68] = [94m_668
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, [94m_668
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = [94m_668
              mem[mem[64] + 36] = uint128(mstor1m[[94m_673m]m.field_128)
              mem[mem[64] + 68] = mstor[[94m_669m]
              mem[mem[64] + 100] = caller
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args [94m_668, uint128(mstor1m[[94m_673m]m.field_0), mstor[[94m_669m], caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94mu = uint128(mstor1m[[94m_673m]m.field_128)
          [94mu = uint128(mstor1m[[94m_669m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_669m]m.field_128)) - (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_669m]m.field_0)) + (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_0)) /′ uint64(mstor2m[[94m_669m]m.field_0))
          [94mu = mstor[[94m_669m]
          [94mu = [94m_669
          [94mu = [94m_668
          [94midx = [94midx + 1
          mcontinue 
      require uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
      require (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_576) * uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) >= 0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)
      mem[0] = mem[(32 * uint32([94midx)) + 128]
      mem[32] = 3
      mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 = 0
      uint256(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) = 0
      uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) = 0
      if uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) <= 0:
          mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 64] = caller
          log AuctionSuccessful(
                uint256 tokenId=mem[mem[64]],
                uint256 totalPrice=uint128(stor1[_673].field_0) + (0 /′ uint64(stor2[_673].field_0)),
                address bidder=caller)
      else:
          call mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_0 with:
             value uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512)) - ((uint128(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_256) * mstor2m.length) + (0 /′ uint64(mstor3m[mem[(32 * uint32([94midx)) + 128]m]m.field_512) * mstor2m.length) / 10000) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64]] = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 64] = uint128(mstor1m[[94m_673m]m.field_0) + (0 /′ uint64(mstor2m[[94m_673m]m.field_0)) - ((uint128(mstor1m[[94m_673m]m.field_0) * mstor2m.length) + (0 /′ uint64(mstor2m[[94m_673m]m.field_0) * mstor2m.length) / 10000)
          mem[mem[64] + 96] = mstor[[94m_673m]
          mem[mem[64] + 128] = caller
          log AuctionSettled(
                uint256 tokenId=mem[mem[64]],
                uint256 price=uint128(stor1[_673].field_0) + (0 /′ uint64(stor2[_673].field_0)),
                uint256 sellerProceeds=uint128(stor1[_673].field_0) + (0 /′ uint64(stor2[_673].field_0)) - ((uint128(stor1[_673].field_0) * stor2.length) + (0 /′ uint64(stor2[_673].field_0) * stor2.length) / 10000),
                address seller=stor[_673],
                address buyer=caller)
          log AuctionSuccessful(
                uint256 tokenId=_668,
                uint256 totalPrice=uint128(stor1[_673].field_0) + (0 /′ uint64(stor2[_673].field_0)),
                address bidder=caller)
      require ext_code.size(addr(mstor1m.length))
      call addr(mstor1m.length).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args caller, [94m_668
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mem[mem[64]] = 0x23b872dd00000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 4] = this.address
      mem[mem[64] + 36] = caller
      mem[mem[64] + 68] = [94m_668
      require ext_code.size(addr(mstor1m.length))
      call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args this.address, caller, [94m_668
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if mlistenerAddress:
          mem[mem[64]] = 0x3d83230f00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = [94m_668
          mem[mem[64] + 36] = uint128(uint128(mstor1m[[94m_673m]m.field_0) + (0 /′ uint64(mstor2m[[94m_673m]m.field_0)))
          mem[mem[64] + 68] = mstor[[94m_669m]
          mem[mem[64] + 100] = caller
          require ext_code.size(mlistenerAddress)
          call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
               gas gas_remaining wei
              args [94m_668, uint128(mstor1m[[94m_673m]m.field_0) + (0 /′ uint64(mstor2m[[94m_673m]m.field_0)) << 128, mstor[[94m_669m], caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      [94mu = uint128(mstor1m[[94m_673m]m.field_0) + (0 /′ uint64(mstor2m[[94m_673m]m.field_0))
      [94mu = uint128(mstor1m[[94m_669m]m.field_0) + ((block.timestamp * uint128(mstor1m[[94m_669m]m.field_128)) - (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_128)) - (block.timestamp * uint128(mstor1m[[94m_669m]m.field_0)) + (uint64(mstor2m[[94m_669m]m.field_64) * uint128(mstor1m[[94m_669m]m.field_0)) /′ uint64(mstor2m[[94m_669m]m.field_0))
      [94mu = mstor[[94m_669m]
      [94mu = [94m_669
      [94mu = [94m_668
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x27ebe40a
# getter = None
# const = None
# payable = False
def createAuction(uint256 m_tokenId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration, address m_seller): # not payable
  require m_startingPrice < 0xffffffffffffffffffffffffffffffff
  require m_endingPrice < 0xffffffffffffffffffffffffffffffff
  require m_duration <= 18446744073709551615
  require caller == addr(mstor1m.length)
  require ext_code.size(addr(mstor1m.length))
  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_seller), this.address, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require uint64(m_duration) >= 60
  mstor3m[m_tokenIdm]m.field_0 = m_seller
  uint128(mstor3m[m_tokenIdm]m.field_256) = uint128(m_startingPrice)
  uint128(mstor3m[m_tokenIdm]m.field_384) = uint128(m_endingPrice)
  uint64(mstor3m[m_tokenIdm]m.field_512) = uint64(m_duration)
  uint64(mstor3m[m_tokenIdm]m.field_576) = uint64(block.timestamp)
  log AuctionCreated(
        uint256 tokenId=_tokenId,
        address seller=addr(_seller),
        uint256 startingPrice=_startingPrice << 128,
        uint256 endingPrice=_endingPrice << 128,
        uint256 duration=uint64(_duration))
  if mlistenerAddress:
      require ext_code.size(mlistenerAddress)
      call mlistenerAddress.auctionCreated(uint256 param1, address param2, uint128 param3, uint128 param4, uint64 param5) with:
           gas gas_remaining wei
          args m_tokenId, addr(m_seller), m_startingPrice << 128, m_endingPrice << 128, uint64(m_duration)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3eedf7d8
# getter = None
# const = None
# payable = False
def getCurrentAuctionPrices(uint128[] m_tokenIds): # not payable
  mem[128 len 32 * m_tokenIds.length] = call.data[m_tokenIds + 36 len 32 * m_tokenIds.length]
  mem[(32 * m_tokenIds.length) + 128 len 1600] = code.data[5211 len 1600]
  mem[(32 * m_tokenIds.length) + 1728 len 1600] = code.data[5211 len 1600]
  require m_tokenIds.length <= 50
  [94ms = 0
  [94mt = 0
  [94midx = 0
  mwhile uint8([94midx) < m_tokenIds.lengthm:
      require uint8([94midx) < m_tokenIds.length
      mem[0] = mem[(32 * uint8([94midx)) + 144 len 16]
      mem[32] = 3
      if uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) <= 0:
          [94ms = [94ms
          [94mt = sha3(mem[(32 * uint8([94midx)) + 144 len 16], 3)
          [94midx = [94midx + 1
          mcontinue 
      if block.timestamp <= uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576):
          if 0 >= uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512):
              require uint8([94midx) < 50
              mem[(32 * uint8([94midx)) + (32 * m_tokenIds.length) + 1728] = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)
              [94ms = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)
              [94mt = sha3(mem[(32 * uint8([94midx)) + 144 len 16], 3)
              [94midx = [94midx + 1
              mcontinue 
          require uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512)
          require uint8([94midx) < 50
          mem[(32 * uint8([94midx)) + (32 * m_tokenIds.length) + 1728] = uint128(uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512)))
          [94ms = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256) + (0 /′ uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512))
          [94mt = sha3(mem[(32 * uint8([94midx)) + 144 len 16], 3)
          [94midx = [94midx + 1
          mcontinue 
      if block.timestamp - uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) >= uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512):
          require uint8([94midx) < 50
          mem[(32 * uint8([94midx)) + (32 * m_tokenIds.length) + 1728] = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)
          [94ms = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)
          [94mt = sha3(mem[(32 * uint8([94midx)) + 144 len 16], 3)
          [94midx = [94midx + 1
          mcontinue 
      require uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512)
      require uint8([94midx) < 50
      mem[(32 * uint8([94midx)) + (32 * m_tokenIds.length) + 1728] = uint128(uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512)))
      [94ms = uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256) + ((block.timestamp * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)) - (uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_384)) - (block.timestamp * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256)) + (uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_576) * uint128(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_256)) /′ uint64(mstor3m[mem[(32 * uint8([94midx)) + 144 len 16]m]m.field_512))
      [94mt = sha3(mem[(32 * uint8([94midx)) + 144 len 16], 3)
      [94midx = [94midx + 1
      mcontinue 
  return memory
    from (32 * m_tokenIds.length) + 1728
     [93mlen 1600


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mowner
  require mpaused
  mpaused = 0
  log Unpause()


# hash = 0x454a2ab3
# getter = None
# const = None
# payable = True
def bid(uint256 m_tokenId) payable: 
  require not mpaused
  require uint64(mstor3m[m_tokenIdm]m.field_576) > 0
  if block.timestamp <= uint64(mstor3m[m_tokenIdm]m.field_576):
      if 0 >= uint64(mstor3m[m_tokenIdm]m.field_512):
          require call.value >= uint128(mstor3m[m_tokenIdm]m.field_384)
          mstor3m[m_tokenIdm]m.field_0 = 0
          uint256(mstor3m[m_tokenIdm]m.field_256) = 0
          uint128(mstor3m[m_tokenIdm]m.field_512) = 0
          if uint128(mstor3m[m_tokenIdm]m.field_384) > 0:
              call mstor3m[m_tokenIdm]m.field_0 with:
                 value uint128(mstor3m[m_tokenIdm]m.field_384) - (uint128(mstor3m[m_tokenIdm]m.field_384) * mstor2m.length / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              log AuctionSettled(
                    uint256 tokenId=_tokenId,
                    uint256 price=uint128(stor3[_tokenId].field_256),
                    uint256 sellerProceeds=uint128(stor3[_tokenId].field_384) - (uint128(stor3[_tokenId].field_384) * stor2.length / 10000),
                    address seller=stor3[_tokenId].field_0,
                    address buyer=caller)
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(stor3[_tokenId].field_256),
                address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args 0, uint32(m_tokenId), uint128(mstor3m[m_tokenIdm]m.field_256), mstor3m[m_tokenIdm]m.field_0, caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
      else:
          require uint64(mstor3m[m_tokenIdm]m.field_512)
          require call.value >= uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512))
          mstor3m[m_tokenIdm]m.field_0 = 0
          uint256(mstor3m[m_tokenIdm]m.field_256) = 0
          uint128(mstor3m[m_tokenIdm]m.field_512) = 0
          if uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512)) > 0:
              call mstor3m[m_tokenIdm]m.field_0 with:
                 value uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512)) - ((uint128(mstor3m[m_tokenIdm]m.field_256) * mstor2m.length) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512) * mstor2m.length) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              log AuctionSettled(
                    uint256 tokenId=_tokenId,
                    uint256 price=uint128(stor3[_tokenId].field_256) + (0 /′ uint64(stor3[_tokenId].field_512)),
                    uint256 sellerProceeds=uint128(stor3[_tokenId].field_256) + (0 /′ uint64(stor3[_tokenId].field_512)) - ((uint128(stor3[_tokenId].field_256) * stor2.length) + (0 /′ uint64(stor3[_tokenId].field_512) * stor2.length) / 10000),
                    address seller=stor3[_tokenId].field_0,
                    address buyer=caller)
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(stor3[_tokenId].field_256) + (0 /′ uint64(stor3[_tokenId].field_512)),
                address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args 0, uint32(m_tokenId), uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512)) << 128, mstor3m[m_tokenIdm]m.field_0, caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
  else:
      if block.timestamp - uint64(mstor3m[m_tokenIdm]m.field_576) >= uint64(mstor3m[m_tokenIdm]m.field_512):
          require call.value >= uint128(mstor3m[m_tokenIdm]m.field_384)
          mstor3m[m_tokenIdm]m.field_0 = 0
          uint256(mstor3m[m_tokenIdm]m.field_256) = 0
          uint128(mstor3m[m_tokenIdm]m.field_512) = 0
          if uint128(mstor3m[m_tokenIdm]m.field_384) > 0:
              call mstor3m[m_tokenIdm]m.field_0 with:
                 value uint128(mstor3m[m_tokenIdm]m.field_384) - (uint128(mstor3m[m_tokenIdm]m.field_384) * mstor2m.length / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              log AuctionSettled(
                    uint256 tokenId=_tokenId,
                    uint256 price=uint128(stor3[_tokenId].field_256),
                    uint256 sellerProceeds=uint128(stor3[_tokenId].field_384) - (uint128(stor3[_tokenId].field_384) * stor2.length / 10000),
                    address seller=stor3[_tokenId].field_0,
                    address buyer=caller)
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(stor3[_tokenId].field_256),
                address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args 0, uint32(m_tokenId), uint128(mstor3m[m_tokenIdm]m.field_256), mstor3m[m_tokenIdm]m.field_0, caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
      else:
          require uint64(mstor3m[m_tokenIdm]m.field_512)
          require call.value >= uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512))
          mstor3m[m_tokenIdm]m.field_0 = 0
          uint256(mstor3m[m_tokenIdm]m.field_256) = 0
          uint128(mstor3m[m_tokenIdm]m.field_512) = 0
          if uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512)) > 0:
              call mstor3m[m_tokenIdm]m.field_0 with:
                 value uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512)) - ((uint128(mstor3m[m_tokenIdm]m.field_256) * mstor2m.length) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512) * mstor2m.length) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              log AuctionSettled(
                    uint256 tokenId=_tokenId,
                    uint256 price=uint128(stor3[_tokenId].field_256) + ((block.timestamp * uint128(stor3[_tokenId].field_384)) - (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_384)) - (block.timestamp * uint128(stor3[_tokenId].field_256)) + (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_256)) /′ uint64(stor3[_tokenId].field_512)),
                    uint256 sellerProceeds=uint128(stor3[_tokenId].field_256) + ((block.timestamp * uint128(stor3[_tokenId].field_384)) - (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_384)) - (block.timestamp * uint128(stor3[_tokenId].field_256)) + (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_256)) /′ uint64(stor3[_tokenId].field_512)) - ((uint128(stor3[_tokenId].field_256) * stor2.length) + ((block.timestamp * uint128(stor3[_tokenId].field_384)) - (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_384)) - (block.timestamp * uint128(stor3[_tokenId].field_256)) + (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_256)) /′ uint64(stor3[_tokenId].field_512) * stor2.length) / 10000),
                    address seller=stor3[_tokenId].field_0,
                    address buyer=caller)
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=uint128(stor3[_tokenId].field_256) + ((block.timestamp * uint128(stor3[_tokenId].field_384)) - (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_384)) - (block.timestamp * uint128(stor3[_tokenId].field_256)) + (uint64(stor3[_tokenId].field_576) * uint128(stor3[_tokenId].field_256)) /′ uint64(stor3[_tokenId].field_512)),
                address bidder=caller)
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(mstor1m.length))
          call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, caller, m_tokenId
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if mlistenerAddress:
              require ext_code.size(mlistenerAddress)
              call mlistenerAddress.auctionSuccessful(uint256 tokenId, uint128 totalPrice, address seller, address winner) with:
                   gas gas_remaining wei
                  args 0, uint32(m_tokenId), uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512)) << 128, mstor3m[m_tokenIdm]m.field_0, caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  require addr(mstor1m.length) == caller
  call addr(mstor1m.length) with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x78bd7935
# getter = None
# const = None
# payable = False
def getAuction(uint256 m_tokenId): # not payable
  require uint64(mstor3m[m_tokenIdm]m.field_576) > 0
  if block.timestamp <= uint64(mstor3m[m_tokenIdm]m.field_576):
      if 0 >= uint64(mstor3m[m_tokenIdm]m.field_512):
          return mstor3m[m_tokenIdm]m.field_0, 
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint64(mstor3m[m_tokenIdm]m.field_512),
                 uint64(mstor3m[m_tokenIdm]m.field_512)
      if uint64(mstor3m[m_tokenIdm]m.field_512):
          return mstor3m[m_tokenIdm]m.field_0, 
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512)),
                 uint64(mstor3m[m_tokenIdm]m.field_512),
                 uint64(mstor3m[m_tokenIdm]m.field_512)
  else:
      if block.timestamp - uint64(mstor3m[m_tokenIdm]m.field_576) >= uint64(mstor3m[m_tokenIdm]m.field_512):
          return mstor3m[m_tokenIdm]m.field_0, 
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint64(mstor3m[m_tokenIdm]m.field_512),
                 uint64(mstor3m[m_tokenIdm]m.field_512)
      if uint64(mstor3m[m_tokenIdm]m.field_512):
          return mstor3m[m_tokenIdm]m.field_0, 
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256),
                 uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512)),
                 uint64(mstor3m[m_tokenIdm]m.field_512),
                 uint64(mstor3m[m_tokenIdm]m.field_512)
  ('iszero', ('type', 64, ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'stor3', 3))))))
  revert


# hash = 0x83b5ff8b
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def ownerCut(): # not payable
  return mstor2m.length


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == mowner
  require not mpaused
  mpaused = 1
  log Pause()


# hash = 0x85b86188
# getter = None
# const = ['return', 1]
# payable = False
const isSaleClockAuction = 1


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 m_tokenId): # not payable
  require mpaused
  require caller == mowner
  require uint64(mstor3m[m_tokenIdm]m.field_576) > 0
  mstor3m[m_tokenIdm]m.field_0 = 0
  uint256(mstor3m[m_tokenIdm]m.field_256) = 0
  uint128(mstor3m[m_tokenIdm]m.field_512) = 0
  require ext_code.size(addr(mstor1m.length))
  call addr(mstor1m.length).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor3m[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(mstor1m.length))
  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args this.address, mstor3m[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=_tokenId)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9551dd58
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def listener(): # not payable
  return mlistenerAddress


# hash = 0x96b5a755
# getter = None
# const = None
# payable = False
def cancelAuction(uint256 m_tokenId): # not payable
  require uint64(mstor3m[m_tokenIdm]m.field_576) > 0
  require mstor3m[m_tokenIdm]m.field_0 == caller
  mstor3m[m_tokenIdm]m.field_0 = 0
  uint256(mstor3m[m_tokenIdm]m.field_256) = 0
  uint128(mstor3m[m_tokenIdm]m.field_512) = 0
  require ext_code.size(addr(mstor1m.length))
  call addr(mstor1m.length).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor3m[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(mstor1m.length))
  call addr(mstor1m.length).transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args this.address, mstor3m[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=_tokenId)
  if mlistenerAddress:
      require ext_code.size(mlistenerAddress)
      call mlistenerAddress.auctionCancelled(uint256 tokenId, address seller) with:
           gas gas_remaining wei
          args m_tokenId, caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xadcd905b
# getter = None
# const = None
# payable = False
def setListener(address m_listener): # not payable
  require not mlistenerAddress
  require ext_code.size(m_listener)
  call m_listener.implementsSaleClockAuctionListener() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mlistenerAddress = m_listener


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 m_tokenId): # not payable
  require uint64(mstor3m[m_tokenIdm]m.field_576) > 0
  if block.timestamp <= uint64(mstor3m[m_tokenIdm]m.field_576):
      if 0 >= uint64(mstor3m[m_tokenIdm]m.field_512):
          return uint128(mstor3m[m_tokenIdm]m.field_384)
      if uint64(mstor3m[m_tokenIdm]m.field_512):
          return (uint128(mstor3m[m_tokenIdm]m.field_256) + (0 /′ uint64(mstor3m[m_tokenIdm]m.field_512)))
  else:
      if block.timestamp - uint64(mstor3m[m_tokenIdm]m.field_576) >= uint64(mstor3m[m_tokenIdm]m.field_512):
          return uint128(mstor3m[m_tokenIdm]m.field_384)
      if uint64(mstor3m[m_tokenIdm]m.field_512):
          return (uint128(mstor3m[m_tokenIdm]m.field_256) + ((block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_384)) - (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_384)) - (block.timestamp * uint128(mstor3m[m_tokenIdm]m.field_256)) + (uint64(mstor3m[m_tokenIdm]m.field_576) * uint128(mstor3m[m_tokenIdm]m.field_256)) /′ uint64(mstor3m[m_tokenIdm]m.field_512)))
  ('iszero', ('type', 64, ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'stor3', 3))))))
  revert


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return addr(mstor1m.length)


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


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  stop


