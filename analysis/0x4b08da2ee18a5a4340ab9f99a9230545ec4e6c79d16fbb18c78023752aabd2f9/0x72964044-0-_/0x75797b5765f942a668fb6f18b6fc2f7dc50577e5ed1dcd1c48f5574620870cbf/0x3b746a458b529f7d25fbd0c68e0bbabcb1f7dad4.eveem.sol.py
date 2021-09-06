# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3B746a458b529f7d25fbd0C68E0bbABCB1f7dAD4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    updaterAddress # mask: a s
    # storage address 1
    paused # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    nonFungibleContractAddress # mask: a s
    # storage address 3
    ownerCut # mask: a s
    # storage address 4
    auction
    # storage address 5
    unknown7f7b4759Address # mask: a s
    # storage address 5
    isSaleClockAuction # mask: a s
    # storage address 6
    exchangeRate # mask: a s
    # storage address 7
    discount # mask: a s
# hash = 0x0fc8a393
# getter = None
# const = None
# payable = False
def transferUpdater(address m_newUpdater): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newUpdater
  log UpdaterTransferred(
        address previousUpdater=updaterAddress,
        address newUpdater=_newUpdater)
  mupdaterAddress = m_newUpdater


# hash = 0x3ba0b9a9
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def exchangeRate(): # not payable
  return mexchangeRate


# hash = 0x3c927e1a
# getter = None
# const = None
# payable = False
def unknown3c927e1a(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require not mpaused
  require mauctionm[m_param1m]m.field_1536 > 0
  require mauctionm[m_param1m]m.field_1792 <= 2
  if mauctionm[m_param1m]m.field_1792 != 1:
      require mauctionm[m_param1m]m.field_1792 <= 2
      require mauctionm[m_param1m]m.field_1792 == 2
  if block.timestamp <= mauctionm[m_param1m]m.field_1536:
      if 0 >= mauctionm[m_param1m]m.field_1280:
          require mauctionm[m_param1m]m.field_1792 <= 2
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          mauctionm[m_param1m]m.field_768 = 0
          mauctionm[m_param1m]m.field_1024 = 0
          mauctionm[m_param1m]m.field_1280 = 0
          mauctionm[m_param1m]m.field_1536 = 0
          mauctionm[m_param1m]m.field_1792 = 0
          if (mauctionm[m_param1m]m.field_768 * mexchangeRate) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000) > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_768 * mexchangeRate) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mauctionm[m_param1m]m.field_1024 / 10000)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mowner, mauctionm[m_param1m]m.field_768 * mexchangeRate * mauctionm[m_param1m]m.field_1024 / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          if mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000 > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args mowner, mauctionm[m_param1m]m.field_256, mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log 0x43d6c6c8: auction[_param1].field_0, _param1, (auction[_param1].field_768 * exchangeRate) - (auction[_param1].field_768 * exchangeRate * discount / 10000), caller, block.timestamp, auction[_param1].field_256
      else:
          require mauctionm[m_param1m]m.field_1280
          require mauctionm[m_param1m]m.field_1792 <= 2
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          mauctionm[m_param1m]m.field_768 = 0
          mauctionm[m_param1m]m.field_1024 = 0
          mauctionm[m_param1m]m.field_1280 = 0
          mauctionm[m_param1m]m.field_1536 = 0
          mauctionm[m_param1m]m.field_1792 = 0
          if (mauctionm[m_param1m]m.field_512 * mexchangeRate) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000) > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_512 * mexchangeRate) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mauctionm[m_param1m]m.field_1024) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mauctionm[m_param1m]m.field_1024) / 10000)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mowner, (mauctionm[m_param1m]m.field_512 * mexchangeRate * mauctionm[m_param1m]m.field_1024) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mauctionm[m_param1m]m.field_1024) / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          if (mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000 > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args mowner, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log 0x43d6c6c8: auction[_param1].field_0, _param1, (auction[_param1].field_512 * exchangeRate) + (0 /′ auction[_param1].field_1280 * exchangeRate) - ((auction[_param1].field_512 * exchangeRate * discount) + (0 /′ auction[_param1].field_1280 * exchangeRate * discount) / 10000), caller, block.timestamp, auction[_param1].field_256
  else:
      if block.timestamp - mauctionm[m_param1m]m.field_1536 >= mauctionm[m_param1m]m.field_1280:
          require mauctionm[m_param1m]m.field_1792 <= 2
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          mauctionm[m_param1m]m.field_768 = 0
          mauctionm[m_param1m]m.field_1024 = 0
          mauctionm[m_param1m]m.field_1280 = 0
          mauctionm[m_param1m]m.field_1536 = 0
          mauctionm[m_param1m]m.field_1792 = 0
          if (mauctionm[m_param1m]m.field_768 * mexchangeRate) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000) > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_768 * mexchangeRate) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000) - (mauctionm[m_param1m]m.field_768 * mexchangeRate * mauctionm[m_param1m]m.field_1024 / 10000)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mowner, mauctionm[m_param1m]m.field_768 * mexchangeRate * mauctionm[m_param1m]m.field_1024 / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          if mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000 > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args mowner, mauctionm[m_param1m]m.field_256, mauctionm[m_param1m]m.field_768 * mexchangeRate * mdiscount / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log 0x43d6c6c8: auction[_param1].field_0, _param1, (auction[_param1].field_768 * exchangeRate) - (auction[_param1].field_768 * exchangeRate * discount / 10000), caller, block.timestamp, auction[_param1].field_256
      else:
          require mauctionm[m_param1m]m.field_1280
          require mauctionm[m_param1m]m.field_1792 <= 2
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          mauctionm[m_param1m]m.field_768 = 0
          mauctionm[m_param1m]m.field_1024 = 0
          mauctionm[m_param1m]m.field_1280 = 0
          mauctionm[m_param1m]m.field_1536 = 0
          mauctionm[m_param1m]m.field_1792 = 0
          if (mauctionm[m_param1m]m.field_512 * mexchangeRate) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000) > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_512 * mexchangeRate) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000) - ((mauctionm[m_param1m]m.field_512 * mexchangeRate * mauctionm[m_param1m]m.field_1024) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mauctionm[m_param1m]m.field_1024) / 10000)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mowner, (mauctionm[m_param1m]m.field_512 * mexchangeRate * mauctionm[m_param1m]m.field_1024) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mauctionm[m_param1m]m.field_1024) / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          if (mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000 > 0:
              require ext_code.size(munknown7f7b4759Address)
              call munknown7f7b4759Address.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args mowner, mauctionm[m_param1m]m.field_256, (mauctionm[m_param1m]m.field_512 * mexchangeRate * mdiscount) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate * mdiscount) / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log 0x43d6c6c8: auction[_param1].field_0, _param1, (auction[_param1].field_512 * exchangeRate) + ((block.timestamp * auction[_param1].field_768) - (auction[_param1].field_1536 * auction[_param1].field_768) - (block.timestamp * auction[_param1].field_512) + (auction[_param1].field_1536 * auction[_param1].field_512) /′ auction[_param1].field_1280 * exchangeRate) - ((auction[_param1].field_512 * exchangeRate * discount) + ((block.timestamp * auction[_param1].field_768) - (auction[_param1].field_1536 * auction[_param1].field_768) - (block.timestamp * auction[_param1].field_512) + (auction[_param1].field_1536 * auction[_param1].field_512) /′ auction[_param1].field_1280 * exchangeRate * discount) / 10000), caller, block.timestamp, auction[_param1].field_256
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(this.address), caller, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if mauctionm[m_param1m]m.field_256 != caller:
      require ext_code.size(mnonFungibleContractAddress)
      call mnonFungibleContractAddress.0x31a8d27e with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mowner
  require mpaused
  mstor1 = 0
  log Unpause()
  return 1


# hash = 0x454a2ab3
# getter = None
# const = None
# payable = True
def bid(uint256 m_tokenId) payable: 
  require calldata.size - 4 >= 32
  require not mpaused
  require mauctionm[m_tokenIdm]m.field_1792 <= 2
  if mauctionm[m_tokenIdm]m.field_1792:
      require mauctionm[m_tokenIdm]m.field_1792 <= 2
      require mauctionm[m_tokenIdm]m.field_1792 == 2
  require mauctionm[m_tokenIdm]m.field_1536 > 0
  if block.timestamp <= mauctionm[m_tokenIdm]m.field_1536:
      if 0 >= mauctionm[m_tokenIdm]m.field_1280:
          require call.value >= mauctionm[m_tokenIdm]m.field_768
          require mauctionm[m_tokenIdm]m.field_1792 <= 2
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          mauctionm[m_tokenIdm]m.field_768 = 0
          mauctionm[m_tokenIdm]m.field_1024 = 0
          mauctionm[m_tokenIdm]m.field_1280 = 0
          mauctionm[m_tokenIdm]m.field_1536 = 0
          mauctionm[m_tokenIdm]m.field_1792 = 0
          if mauctionm[m_tokenIdm]m.field_768 <= 0:
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_768 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_256 with:
                 value mauctionm[m_tokenIdm]m.field_768 - (mauctionm[m_tokenIdm]m.field_768 * mauctionm[m_tokenIdm]m.field_1024 / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_768 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dc2a2bf: auction[_tokenId].field_0, _tokenId, auction[_tokenId].field_768, caller, block.timestamp, auction[_tokenId].field_256
      else:
          require mauctionm[m_tokenIdm]m.field_1280
          require call.value >= mauctionm[m_tokenIdm]m.field_512 + (0 /′ mauctionm[m_tokenIdm]m.field_1280)
          require mauctionm[m_tokenIdm]m.field_1792 <= 2
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          mauctionm[m_tokenIdm]m.field_768 = 0
          mauctionm[m_tokenIdm]m.field_1024 = 0
          mauctionm[m_tokenIdm]m.field_1280 = 0
          mauctionm[m_tokenIdm]m.field_1536 = 0
          mauctionm[m_tokenIdm]m.field_1792 = 0
          if mauctionm[m_tokenIdm]m.field_512 + (0 /′ mauctionm[m_tokenIdm]m.field_1280) <= 0:
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_512 - (0 /′ mauctionm[m_tokenIdm]m.field_1280) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_256 with:
                 value mauctionm[m_tokenIdm]m.field_512 + (0 /′ mauctionm[m_tokenIdm]m.field_1280) - ((mauctionm[m_tokenIdm]m.field_512 * mauctionm[m_tokenIdm]m.field_1024) + (0 /′ mauctionm[m_tokenIdm]m.field_1280 * mauctionm[m_tokenIdm]m.field_1024) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_512 - (0 /′ mauctionm[m_tokenIdm]m.field_1280) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dc2a2bf: auction[_tokenId].field_0, _tokenId, auction[_tokenId].field_512 + (0 /′ auction[_tokenId].field_1280), caller, block.timestamp, auction[_tokenId].field_256
  else:
      if block.timestamp - mauctionm[m_tokenIdm]m.field_1536 >= mauctionm[m_tokenIdm]m.field_1280:
          require call.value >= mauctionm[m_tokenIdm]m.field_768
          require mauctionm[m_tokenIdm]m.field_1792 <= 2
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          mauctionm[m_tokenIdm]m.field_768 = 0
          mauctionm[m_tokenIdm]m.field_1024 = 0
          mauctionm[m_tokenIdm]m.field_1280 = 0
          mauctionm[m_tokenIdm]m.field_1536 = 0
          mauctionm[m_tokenIdm]m.field_1792 = 0
          if mauctionm[m_tokenIdm]m.field_768 <= 0:
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_768 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_256 with:
                 value mauctionm[m_tokenIdm]m.field_768 - (mauctionm[m_tokenIdm]m.field_768 * mauctionm[m_tokenIdm]m.field_1024 / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_768 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dc2a2bf: auction[_tokenId].field_0, _tokenId, auction[_tokenId].field_768, caller, block.timestamp, auction[_tokenId].field_256
      else:
          require mauctionm[m_tokenIdm]m.field_1280
          require call.value >= mauctionm[m_tokenIdm]m.field_512 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280)
          require mauctionm[m_tokenIdm]m.field_1792 <= 2
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          mauctionm[m_tokenIdm]m.field_768 = 0
          mauctionm[m_tokenIdm]m.field_1024 = 0
          mauctionm[m_tokenIdm]m.field_1280 = 0
          mauctionm[m_tokenIdm]m.field_1536 = 0
          mauctionm[m_tokenIdm]m.field_1792 = 0
          if mauctionm[m_tokenIdm]m.field_512 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280) <= 0:
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_512 - ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_256 with:
                 value mauctionm[m_tokenIdm]m.field_512 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280) - ((mauctionm[m_tokenIdm]m.field_512 * mauctionm[m_tokenIdm]m.field_1024) + ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280 * mauctionm[m_tokenIdm]m.field_1024) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - mauctionm[m_tokenIdm]m.field_512 - ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dc2a2bf: auction[_tokenId].field_0, _tokenId, auction[_tokenId].field_512 + ((block.timestamp * auction[_tokenId].field_768) - (auction[_tokenId].field_1536 * auction[_tokenId].field_768) - (block.timestamp * auction[_tokenId].field_512) + (auction[_tokenId].field_1536 * auction[_tokenId].field_512) /′ auction[_tokenId].field_1280), caller, block.timestamp, auction[_tokenId].field_256
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(this.address), caller, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if mauctionm[m_tokenIdm]m.field_256 != caller:
      require ext_code.size(mnonFungibleContractAddress)
      call mnonFungibleContractAddress.0x31a8d27e with:
           gas gas_remaining wei
          args m_tokenId
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x5b0bc07b
# getter = None
# const = None
# payable = False
def unknown5b0bc07b(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  munknown7f7b4759Address = m_param1
  return 1


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  if mowner != caller:
      require caller == mnonFungibleContractAddress
  call mnonFungibleContractAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x6a2ede29
# getter = None
# const = None
# payable = False
def unknown6a2ede29(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mauctionm[m_param1m]m.field_1536 > 0
  if block.timestamp <= mauctionm[m_param1m]m.field_1536:
      if 0 >= mauctionm[m_param1m]m.field_1280:
          return (mauctionm[m_param1m]m.field_768 * mexchangeRate)
      if mauctionm[m_param1m]m.field_1280:
          return ((mauctionm[m_param1m]m.field_512 * mexchangeRate) + (0 /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate))
  else:
      if block.timestamp - mauctionm[m_param1m]m.field_1536 >= mauctionm[m_param1m]m.field_1280:
          return (mauctionm[m_param1m]m.field_768 * mexchangeRate)
      if mauctionm[m_param1m]m.field_1280:
          return ((mauctionm[m_param1m]m.field_512 * mexchangeRate) + ((block.timestamp * mauctionm[m_param1m]m.field_768) - (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_768) - (block.timestamp * mauctionm[m_param1m]m.field_512) + (mauctionm[m_param1m]m.field_1536 * mauctionm[m_param1m]m.field_512) /′ mauctionm[m_param1m]m.field_1280 * mexchangeRate))
  ('iszero', ('field', 1280, ('stor', ('map', ('param', '_param1'), ('name', 'auction', 4)))))
  revert


# hash = 0x6b6f4a9d
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def discount(): # not payable
  return mdiscount


# hash = 0x757de573
# getter = None
# const = None
# payable = False
def setOwnerCut(uint256 m_cut): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require not mpaused
  require m_cut <= 10000
  mownerCut = m_cut
  log 0x7ac8718c: _cut


# hash = 0x78bd7935
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def getAuction(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  require mauctionm[m_tokenIdm]m.field_1536 > 0
  require mauctionm[m_tokenIdm]m.field_1792 <= 2
  return mauctionm[m_tokenIdm]m.field_256, 
         mauctionm[m_tokenIdm]m.field_512,
         mauctionm[m_tokenIdm]m.field_768,
         mauctionm[m_tokenIdm]m.field_1024,
         mauctionm[m_tokenIdm]m.field_1280,
         mauctionm[m_tokenIdm]m.field_1536,
         mauctionm[m_tokenIdm]m.field_1792


# hash = 0x7f7b4759
# getter = ['storage', 160, 8, 5]
# const = None
# payable = False
def unknown7f7b4759(): # not payable
  return munknown7f7b4759Address


# hash = 0x83b5ff8b
# getter = ['storage', 256, 0, 3]
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
  mstor1 = 1
  log Pause()
  return 1


# hash = 0x85b86188
# getter = ['bool', ['storage', 8, 0, 5]]
# const = None
# payable = False
def isSaleClockAuction(): # not payable
  return bool(misSaleClockAuction)


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  require mpaused
  require caller == mowner
  require mauctionm[m_tokenIdm]m.field_1536 > 0
  require mauctionm[m_tokenIdm]m.field_1792 <= 2
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  mauctionm[m_tokenIdm]m.field_768 = 0
  mauctionm[m_tokenIdm]m.field_1024 = 0
  mauctionm[m_tokenIdm]m.field_1280 = 0
  mauctionm[m_tokenIdm]m.field_1536 = 0
  mauctionm[m_tokenIdm]m.field_1792 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(this.address), mauctionm[m_tokenIdm]m.field_256, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x3d079bbf: auction[_tokenId].field_0, _tokenId, block.timestamp, auction[_tokenId].field_256


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
  require mauctionm[m_tokenIdm]m.field_1536 > 0
  require caller == mauctionm[m_tokenIdm]m.field_256
  require mauctionm[m_tokenIdm]m.field_1792 <= 2
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  mauctionm[m_tokenIdm]m.field_768 = 0
  mauctionm[m_tokenIdm]m.field_1024 = 0
  mauctionm[m_tokenIdm]m.field_1280 = 0
  mauctionm[m_tokenIdm]m.field_1536 = 0
  mauctionm[m_tokenIdm]m.field_1792 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(this.address), mauctionm[m_tokenIdm]m.field_256, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x3d079bbf: auction[_tokenId].field_0, _tokenId, block.timestamp, auction[_tokenId].field_256


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  require mauctionm[m_tokenIdm]m.field_1536 > 0
  if block.timestamp <= mauctionm[m_tokenIdm]m.field_1536:
      if 0 >= mauctionm[m_tokenIdm]m.field_1280:
          return mauctionm[m_tokenIdm]m.field_768
      if mauctionm[m_tokenIdm]m.field_1280:
          return (mauctionm[m_tokenIdm]m.field_512 + (0 /′ mauctionm[m_tokenIdm]m.field_1280))
  else:
      if block.timestamp - mauctionm[m_tokenIdm]m.field_1536 >= mauctionm[m_tokenIdm]m.field_1280:
          return mauctionm[m_tokenIdm]m.field_768
      if mauctionm[m_tokenIdm]m.field_1280:
          return (mauctionm[m_tokenIdm]m.field_512 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_768) - (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_768) - (block.timestamp * mauctionm[m_tokenIdm]m.field_512) + (mauctionm[m_tokenIdm]m.field_1536 * mauctionm[m_tokenIdm]m.field_512) /′ mauctionm[m_tokenIdm]m.field_1280))
  ('iszero', ('field', 1280, ('stor', ('map', ('param', '_tokenId'), ('name', 'auction', 4)))))
  revert


# hash = 0xdabd2719
# getter = None
# const = None
# payable = False
def setDiscount(uint256 m_discountPrice): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  mdiscount = m_discountPrice
  log 0x4380d185: _discountPrice
  return m_discountPrice


# hash = 0xdb068e0e
# getter = None
# const = None
# payable = False
def setExchangeRate(uint256 m_exchangeRate): # not payable
  require calldata.size - 4 >= 32
  require caller == mupdaterAddress
  mexchangeRate = m_exchangeRate
  log 0x388f446e: _exchangeRate
  return m_exchangeRate


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return mnonFungibleContractAddress


# hash = 0xdf034cd0
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def updater(): # not payable
  return mupdaterAddress


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf33073ff
# getter = None
# const = None
# payable = False
def unknownf33073ff(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, addr m_param6, uint256 m_param7): # not payable
  require calldata.size - 4 >= 224
  require not mpaused
  require m_param4 <= m_param3
  require 2 >= m_param7
  require caller == mnonFungibleContractAddress
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param6), addr(this.address), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require m_param7 <= 2
  require m_param7 <= 2
  require m_param5 >= 60
  mauctionm[m_param2m]m.field_0 = m_param1
  mauctionm[m_param2m]m.field_256 = m_param6
  mauctionm[m_param2m]m.field_512 = m_param3
  mauctionm[m_param2m]m.field_768 = m_param4
  mauctionm[m_param2m]m.field_1024 = mownerCut
  mauctionm[m_param2m]m.field_1280 = m_param5
  mauctionm[m_param2m]m.field_1536 = block.timestamp
  require m_param7 <= 2
  mauctionm[m_param2m]m.field_1792 = m_param7 or Mask(248, 8, mauctionm[m_param2m]m.field_1792)
  require m_param7 <= 2
  log 0x8ef0e7f1: _param1, _param2, _param3, _param4, ownerCut, _param5, block.timestamp, uint8(_param7), _param6


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


