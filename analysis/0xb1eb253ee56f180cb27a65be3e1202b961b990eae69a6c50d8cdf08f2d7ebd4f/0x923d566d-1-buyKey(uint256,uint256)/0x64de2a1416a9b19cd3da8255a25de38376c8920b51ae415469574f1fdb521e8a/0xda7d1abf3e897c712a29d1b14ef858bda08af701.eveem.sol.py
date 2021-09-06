# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xDa7d1AbF3E897C712a29D1b14ef858BDa08aF701 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x923d566d': 'unknown923d566d(?)'} 

# storage definitions
def storage:
    # storage address 0
    name
    # storage address 1
    version
    # storage address 2
    roundNum # mask: a s
    # storage address 3
    unknown7479aa04
    # storage address 4
    players
    # storage address 5
    unknowncd2bd04b
    # storage address 6
    unknowne55ca97f # mask: a s
    # storage address 7
    unknown5dae14a8 # mask: a s
    # storage address 8
    keyprice # mask: a s
    # storage address 9
    unknowne78b6785 # mask: a s
    # storage address 10
    unknownb82a74a1Address # mask: a s
    # storage address 11
    unknown0d55c28bAddress # mask: a s
    # storage address 12
    unknown6fbf2f19 # mask: a s
    # storage address 13
    unknownc11c7885 # mask: a s
    # storage address 14
    unknown64a2ffc5 # mask: a s
    # storage address 15
    unknowna56f09f2 # mask: a s
    # storage address 16
    unknown849df984 # mask: a s
    # storage address 17
    unknownc2d50185Address # mask: a s
    # storage address 18
    unknown879dd862Address # mask: a s
    # storage address 19
    tokens
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 0]]]], ['loc', 0]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x0b4ce60f
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def keyprice(): # not payable
  return keyprice


# hash = 0x0d55c28b
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def unknown0d55c28b(): # not payable
  return unknown0d55c28bAddress


# hash = 0x119b22b3
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def roundNum(): # not payable
  return roundNum


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  if block.timestamp > unknown7479aa04[stor2].field_256:
      require unknown7479aa04[stor2].field_1536 + players[stor3[stor2].field_2048].field_1280 >= players[stor3[stor2].field_2048].field_1280
      players[stor3[stor2].field_2048].field_1280 += unknown7479aa04[stor2].field_1536
      if not tokens.length:
          require ext_code.size(unknown0d55c28bAddress)
          call unknown0d55c28bAddress.0xf1b6cee5 with:
               gas gas_remaining wei
              args 32, tokens.length
      else:
          mem[164] = uint256(tokens.field_0)
          [94midx = 164
          [94ms = 0
          while (32 * tokens.length) + 164 > [94midx + 32:
              mem[[94midx + 32] = tokens[[94ms].field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
          require ext_code.size(unknown0d55c28bAddress)
          call unknown0d55c28bAddress.0xf1b6cee5 with:
               gas gas_remaining wei
              args Array(len=tokens.length, data=mem[164 len 32 * tokens.length])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log 0x5ece034c: roundNum, unknown7479aa04[stor2].field_2048, unknown7479aa04[stor2].field_1536
      unknown7479aa04[stor2].field_512 = 1
      roundNum++
      require unknowne55ca97f + block.timestamp >= block.timestamp
      unknown7479aa04[stor2].field_0 = block.timestamp
      unknown7479aa04[stor2].field_256 = unknowne55ca97f + block.timestamp
      unknown7479aa04[stor2].field_512 = 0
      unknown7479aa04[stor2].field_768 = 0
      unknown7479aa04[stor2].field_1024 = 0
      unknown7479aa04[stor2].field_1280 = 0
      unknown7479aa04[stor2].field_1536 = 0
      unknown7479aa04[stor2].field_1792 = 0
      unknown7479aa04[stor2].field_2048 = 0
      log 0x5a7408a8: roundNum, 0, unknown7479aa04[stor2].field_0, unknown7479aa04[stor2].field_256
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerIdByAddress(address addr) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerAddressById(uint256 id) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[12 len 20]:
      revert with 0, 'showPlayerEtherById wrong'
  if players[ext_call.return_data[0]].field_512 <= 0:
      require players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768
      require players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
      if players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 <= 0:
          revert with 0, 'withdraw wrong'
      if players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 > eth.balance(this.address):
          revert with 0, 'withdraw wrong'
      require players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
      players[ext_call.return_data[0]].field_1536 = players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768
      call caller with:
         value players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log 0x566f61a6: roundNum, ext_call.return_data[0], players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536
  else:
      require players[ext_call.return_data[0]].field_512 <= roundNum
      if not unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792:
          require unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024
          require (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768
          require players[ext_call.return_data[0]].field_1280 >= 0
          require players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
          if players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 <= 0:
              revert with 0, 'withdraw wrong'
          if players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 > eth.balance(this.address):
              revert with 0, 'withdraw wrong'
          require players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
          players[ext_call.return_data[0]].field_1536 = players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768
          call caller with:
             value players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log 0x566f61a6: roundNum, ext_call.return_data[0], players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536
      else:
          require unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 == unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256
          require unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024
          require (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768
          require players[ext_call.return_data[0]].field_1280 >= 0
          require players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
          if players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 <= 0:
              revert with 0, 'withdraw wrong'
          if players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 > eth.balance(this.address):
              revert with 0, 'withdraw wrong'
          require players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536
          players[ext_call.return_data[0]].field_1536 = players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768
          call caller with:
             value players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536 wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log 0x566f61a6: roundNum, ext_call.return_data[0], players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536


# hash = 0x49afc6e5
# getter = None
# const = None
# payable = False
def unknown49afc6e5(uint256 _param1): # not payable
  if _param1 >= tokens.length:
      revert with 0, 'tokenBalance wrong'
  require ext_code.size(unknown0d55c28bAddress)
  call unknown0d55c28bAddress.0x49afc6e5 with:
       gas gas_remaining wei
      args tokens[_param1].field_0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x4dd1e81c
# getter = None
# const = None
# payable = False
def unknown4dd1e81c(uint256 _param1, uint256 _param2): # not payable
  if _param1 >= tokens.length:
      revert with 0, 'tokenBuyable wrong'
  if not _param2:
      require ext_code.size(unknown0d55c28bAddress)
      call unknown0d55c28bAddress.0x4dd1e81c with:
           gas gas_remaining wei
          args tokens[_param1].field_0, 0
  else:
      require unknown64a2ffc5 * _param2 / _param2 == unknown64a2ffc5
      require ext_code.size(unknown0d55c28bAddress)
      call unknown0d55c28bAddress.0x4dd1e81c with:
           gas gas_remaining wei
          args tokens[_param1].field_0, unknown64a2ffc5 * _param2 / 100
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x4f64b2be
# getter = ['storage', 256, 0, ['add', ['sha3', 19], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 _param1): # not payable
  require _param1 < tokens.length
  return tokens[_param1].field_0


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x5dae14a8
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknown5dae14a8(): # not payable
  return unknown5dae14a8


# hash = 0x64a2ffc5
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown64a2ffc5(): # not payable
  return unknown64a2ffc5


# hash = 0x6fbf2f19
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown6fbf2f19(): # not payable
  return unknown6fbf2f19


# hash = 0x7479aa04
# getter = ['storage', 256, 0, ['sha3', ['data', ['storage', 256, 0, 2], 3]]]
# const = None
# payable = False
def unknown7479aa04(): # not payable
  if roundNum <= 0:
      revert with 0, 'getCurrentRoundStartTime wrong'
  return unknown7479aa04[stor2].field_0


# hash = 0x849df984
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown849df984(): # not payable
  return unknown849df984


# hash = 0x879dd862
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def unknown879dd862(): # not payable
  return unknown879dd862Address


# hash = 0x8aaaa197
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['storage', 256, 0, 2], 3]]]]
# const = None
# payable = False
def unknown8aaaa197(): # not payable
  if roundNum <= 0:
      revert with 0, 'getCurrentRoundEndTime wrong'
  return unknown7479aa04[stor2].field_256


# hash = 0x8c65c81f
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def rounds(uint256 _param1): # not payable
  return unknown7479aa04[_param1].field_0, 
         unknown7479aa04[_param1].field_256,
         bool(unknown7479aa04[_param1].field_512),
         unknown7479aa04[_param1].field_768,
         unknown7479aa04[_param1].field_1024,
         unknown7479aa04[_param1].field_1280,
         unknown7479aa04[_param1].field_1536,
         unknown7479aa04[_param1].field_1792,
         unknown7479aa04[_param1].field_2048


# hash = 0x9f519589
# getter = None
# const = None
# payable = False
def unknown9f519589(addr _param1): # not payable
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerIdByAddress(address addr) with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= 0:
      revert with 0, 'showPlayerEtherByAddress wrong'
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerAddressById(uint256 id) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[12 len 20]:
      revert with 0, 'showPlayerEtherById wrong'
  if players[ext_call.return_data[0]].field_512 <= 0:
      if players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768:
          if players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536:
              return players[ext_call.return_data[0]].field_768, 
                     players[ext_call.return_data[0]].field_1280,
                     players[ext_call.return_data[0]].field_1280 + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536
  else:
      if players[ext_call.return_data[0]].field_512 <= roundNum:
          if not unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792:
              if unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024:
                  if (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768:
                      if players[ext_call.return_data[0]].field_1280 >= 0:
                          if players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536:
                              return (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768, 
                                     players[ext_call.return_data[0]].field_1280,
                                     players[ext_call.return_data[0]].field_1280 + (0 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536
          else:
              if unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 == unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256:
                  if unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024:
                      if (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_768:
                          if players[ext_call.return_data[0]].field_1280 >= 0:
                              if players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 >= players[ext_call.return_data[0]].field_1536:
                                  return (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768, 
                                         players[ext_call.return_data[0]].field_1280,
                                         players[ext_call.return_data[0]].field_1280 + (unknowncd2bd04b[stor4[ext_call.return_data[0]].field_512][ext_call.return_data[0]].field_256 * unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1792 / unknown7479aa04[stor4[ext_call.return_data[0]].field_512].field_1024) + players[ext_call.return_data[0]].field_768 - players[ext_call.return_data[0]].field_1536
  revert


# hash = 0xa56f09f2
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknowna56f09f2(): # not payable
  return unknowna56f09f2


# hash = 0xa59eca54
# getter = None
# const = None
# payable = False
def getPlayerIdByAddress(address _addr): # not payable
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerIdByAddress(address addr) with:
       gas gas_remaining wei
      args _addr
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xaa6ca808
# getter = None
# const = None
# payable = False
def getTokens(): # not payable
  if not tokens.length:
      mem[(32 * tokens.length) + 128] = 32
      mem[(32 * tokens.length) + 160] = tokens.length
      mem[(32 * tokens.length) + 192 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
      return memory
        from (32 * tokens.length) + 128
         [93mlen (96 * tokens.length) + 64
  mem[128] = uint256(tokens.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * tokens.length) + 96 > [94midx:
      mem[[94midx + 32] = tokens[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * tokens.length) + 192 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
  return Array(len=tokens.length, data=mem[128 len floor32(tokens.length)], mem[(32 * tokens.length) + floor32(tokens.length) + 192 len (32 * tokens.length) - floor32(tokens.length)]), 


# hash = 0xb82a74a1
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknownb82a74a1(): # not payable
  return unknownb82a74a1Address


# hash = 0xc11aac11
# getter = None
# const = None
# payable = False
def unknownc11aac11(uint256 _param1): # not payable
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.getPlayerAddressById(uint256 id) with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[12 len 20]:
      revert with 0, 'showPlayerEtherById wrong'
  if players[_param1].field_512 <= 0:
      if players[_param1].field_1280 + players[_param1].field_768 >= players[_param1].field_768:
          if players[_param1].field_1280 + players[_param1].field_768 >= players[_param1].field_1536:
              return players[_param1].field_768, 
                     players[_param1].field_1280,
                     players[_param1].field_1280 + players[_param1].field_768 - players[_param1].field_1536
  else:
      if players[_param1].field_512 <= roundNum:
          if not unknown7479aa04[stor4[_param1].field_512].field_1792:
              if unknown7479aa04[stor4[_param1].field_512].field_1024:
                  if (0 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 >= players[_param1].field_768:
                      if players[_param1].field_1280 >= 0:
                          if players[_param1].field_1280 + (0 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 >= players[_param1].field_1536:
                              return (0 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768, 
                                     players[_param1].field_1280,
                                     players[_param1].field_1280 + (0 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 - players[_param1].field_1536
          else:
              if unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256 * unknown7479aa04[stor4[_param1].field_512].field_1792 / unknown7479aa04[stor4[_param1].field_512].field_1792 == unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256:
                  if unknown7479aa04[stor4[_param1].field_512].field_1024:
                      if (unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256 * unknown7479aa04[stor4[_param1].field_512].field_1792 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 >= players[_param1].field_768:
                          if players[_param1].field_1280 >= 0:
                              if players[_param1].field_1280 + (unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256 * unknown7479aa04[stor4[_param1].field_512].field_1792 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 >= players[_param1].field_1536:
                                  return (unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256 * unknown7479aa04[stor4[_param1].field_512].field_1792 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768, 
                                         players[_param1].field_1280,
                                         players[_param1].field_1280 + (unknowncd2bd04b[stor4[_param1].field_512][_param1].field_256 * unknown7479aa04[stor4[_param1].field_512].field_1792 / unknown7479aa04[stor4[_param1].field_512].field_1024) + players[_param1].field_768 - players[_param1].field_1536
  revert


# hash = 0xc11c7885
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownc11c7885(): # not payable
  return unknownc11c7885


# hash = 0xc2d50185
# getter = ['storage', 160, 0, 17]
# const = None
# payable = False
def unknownc2d50185(): # not payable
  return unknownc2d50185Address


# hash = 0xcd2bd04b
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 5]]]]]
# const = None
# payable = False
def unknowncd2bd04b(uint256 _param1, uint256 _param2): # not payable
  return unknowncd2bd04b[_param1][_param2].field_0, unknowncd2bd04b[_param1][_param2].field_256


# hash = 0xd7290181
# getter = None
# const = None
# payable = False
def emptyWrongToken(address _addr): # not payable
  require ext_code.size(unknownb82a74a1Address)
  call unknownb82a74a1Address.isAdmin(address param1) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'isAdmin wrong'
  require ext_code.size(_addr)
  call _addr.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'emptyWrongToken need more balance'
  require ext_code.size(_addr)
  call _addr.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'emptyWrongToken transfer wrong'
  log WrongTokenEmptied(
        address token=ext_call.return_data[0],
        address addr=_addr,
        uint256 amount=caller)


# hash = 0xe55ca97f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknowne55ca97f(): # not payable
  return unknowne55ca97f


# hash = 0xe78b6785
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknowne78b6785(): # not payable
  return unknowne78b6785


# hash = 0xf71d96cb
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def players(uint256 _param1): # not payable
  return players[_param1].field_0, 
         players[_param1].field_256,
         players[_param1].field_512,
         players[_param1].field_768,
         players[_param1].field_1024,
         players[_param1].field_1280,
         players[_param1].field_1536


# hash = 0xfc51daef
# getter = ['storage', 256, 0, ['add', 8, ['sha3', ['data', ['storage', 256, 0, 2], 3]]]]
# const = None
# payable = False
def unknownfc51daef(): # not payable
  if roundNum <= 0:
      revert with 0, 'getCurrentRoundWinner wrong'
  if block.timestamp <= unknown7479aa04[stor2].field_256:
      revert with 0, 'getCurrentRoundWinner wrong'
  return unknown7479aa04[stor2].field_2048


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


