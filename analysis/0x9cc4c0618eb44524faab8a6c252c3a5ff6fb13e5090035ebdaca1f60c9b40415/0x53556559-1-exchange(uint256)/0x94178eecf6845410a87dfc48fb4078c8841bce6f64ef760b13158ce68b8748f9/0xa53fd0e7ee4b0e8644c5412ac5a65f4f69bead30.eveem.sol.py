# contract source code retrieved from eveem.org
# retrieved on 2020-04-01

#  addr = 0xA53fD0e7eE4B0E8644c5412ac5A65F4F69bEaD30 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x6861130a': 'unknown6861130a(?)', '0x933949bf': 'unknown933949bf(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 6
    stor6 # mask: a s
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
    stor12
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    user
    # storage address 16
    stor16
    # storage address 17
    stor17
    # storage address 19
    stor19
    # storage address 20
    stor20 # mask: a s
    # storage address 21
    unknownfba71153
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 25
    stor25 # mask: a s
    # storage address 26
    stor26 # mask: a s
    # storage address 28
    stor28 # mask: a s
    # storage address 29
    stor29 # mask: a s
    # storage address 31
    stor31 # mask: a s
    # storage address 35
    stor35 # mask: a s
    # storage address 36
    stor36
    # storage address 37
    stor37 # mask: a s
    # storage address 38
    stor38 # mask: a s
    # storage address 39
    stor39 # mask: a s
    # storage address 40
    stor40 # mask: a s
    # storage address 41
    stor41 # mask: a s
    # storage address 42
    stor42 # mask: a s
    # storage address 43
    stor43 # mask: a s
    # storage address 44
    stor44 # mask: a s
    # storage address 45
    stor45 # mask: a s
    # storage address 46
    stor46 # mask: a s
    # storage address 47
    stor47 # mask: a s
    # storage address 48
    stor48
    # storage address 57
    stor57
    # storage address 58
    stor58
    # storage address 67
    stor67
    # storage address 68
    stor68
    # storage address 78
    stor78 # mask: a s
    # storage address 79
    stor79 # mask: a s
    # storage address 80
    stor80 # mask: a s
    # storage address 81
    stor81
    # storage address 84
    stor84
    # storage address 85
    stor85
    # storage address 87
    stor87 # mask: a s
    # storage address 88
    stor88 # mask: a s
    # storage address 89
    stor89 # mask: a s
    # storage address 90
    stor90 # mask: a s
    # storage address 91
    stor91 # mask: a s
    # storage address 92
    stor92 # mask: a s
    # storage address 93
    stor93 # mask: a s
    # storage address 94
    unknown7879b5ef
    # storage address 95
    unknownab47fd76
    # storage address 96
    unknowne288fc38
    # storage address 97
    stor97 # mask: a s
    # storage address 98
    stor98 # mask: a s
    # storage address 101
    stor101
    # storage address 110
    stor110 # mask: a s
    # storage address 111
    stor111 # mask: a s
    # storage address 112
    stor112 # mask: a s
    # storage address 114
    stor114 # mask: a s
    # storage address 115
    stor115 # mask: a s
    # storage address 116
    stor116
    # storage address 117
    stor117
    # storage address 118
    stor118 # mask: a s
    # storage address 119
    stor119
    # storage address 120
    stor120
    # storage address 121
    stor121 # mask: a s
    # storage address 122
    stor122 # mask: a s
    # storage address 123
    stor123 # mask: a s
    # storage address 10750624430388119320849790643207901758612995790504547427134551617187322478595
    stor17C4 # mask: a s
    # storage address 10750624430388119320849790643207901758612995790504547427134551617187322478595
    stor17C4 # mask: a s
    # storage address 23559813839190175782219524221755743204735595000890393379779893329588711786431
    stor3416 # mask: a s
    # storage address 23559813839190175782219524221755743204735595000890393379779893329588711786431
    stor3416 # mask: a s
    # storage address 42234865624494891382798413269907358927548514282952878344152767142002251650848
    stor5D60 # mask: a s
    # storage address 54733025029901088831001604925566009236597535723592674609900492207440442601457
    stor54733025029901088831001604925566009236597535723592674609900492207440442601457
    # storage address 56762212109192015273441635517470881407847468840448203594774465305961653915957
    stor7D7E # mask: a s
    # storage address 80412407951332822115984620622198171326963871116709475001860841838294605961812
    storB1C7 # mask: a s
    # storage address 87230068782330289384573683168046325727686260835800696112278801295981949472727
    storC0DA # mask: a s
    # storage address 102074595867737739970317380845844748195963543191234868951366086900378710738708
    storE1AC # mask: a s
    # storage address 108424226490316951273733703572506837616353843851404383028575015010235193531459
    storEFB5 # mask: a s
    # storage address 108424226490316951273733703572506837616353843851404383028575015010235193531459
    storEFB5 # mask: a s
# hash = 0x008e0f1b
# getter = None
# const = None
# payable = False
def getTeam(uint256 _tokenId): # not payable
  require calldata.size - 4 >= 32
  if 3 <= uint256(stor19[_tokenId].field_1536):
      return addr(stor19[_tokenId].field_256), 
             uint256(stor19[stor87].field_1280),
             uint256(stor19[_tokenId].field_1280),
             uint256(stor19[_tokenId].field_2048),
             uint256(stor19[_tokenId].field_1536),
             uint256(stor19[_tokenId].field_1792)
  if not uint256(stor19[_tokenId].field_1536):
      return addr(stor19[_tokenId].field_256), 
             uint256(stor19[stor87].field_1280),
             uint256(stor19[_tokenId].field_1280),
             uint256(stor19[_tokenId].field_2048),
             uint256(stor19[_tokenId].field_1536),
             uint256(stor19[_tokenId].field_1792)
  require uint256(stor19[_tokenId].field_1536) - 1 < 3
  return addr(stor19[_tokenId].field_256), 
         uint256(stor19[stor84[uint256(stor19[_tokenId].field_1536)]].field_1280),
         uint256(stor19[_tokenId].field_1280),
         uint256(stor19[_tokenId].field_2048),
         uint256(stor19[_tokenId].field_1536),
         uint256(stor19[_tokenId].field_1792)


# hash = 0x0e1a1dc4
# getter = None
# const = None
# payable = False
def unknown0e1a1dc4(): # not payable
  return stor46, stor47, stor45, stor79, stor80, stor78, stor84.length, stor119.length, stor13, stor14, 0, 0


# hash = 0x132265b2
# getter = None
# const = None
# payable = False
def unknown132265b2(addr _param1): # not payable
  require calldata.size - 4 >= 32
  [94midx = 2976
  [94ms = 14
  while 3072 > [94midx + 32:
      mem[[94midx + 32] = uint256(user[addr(_param1)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return uint256(user[addr(_param1)].field_5888), 
         uint256(unknownfba71153[addr(_param1)].field_0),
         uint256(user[addr(_param1)].field_6400),
         uint256(user[addr(_param1)].field_6656),
         uint256(user[addr(_param1)].field_6912),
         uint256(user[addr(_param1)].field_1024),
         uint256(user[addr(_param1)].field_4352),
         uint256(user[addr(_param1)].field_4608),
         uint256(user[addr(_param1)].field_4864),
         uint256(user[addr(_param1)].field_3584),
         mem[3008 len 64]


# hash = 0x192db62f
# getter = None
# const = None
# payable = True
def unknown192db62f() payable: 
  mem[64] = 96
  require not call.value
  if stor79 > block.timestamp:
      revert with 0, 'SafeMath sub failed'
  if block.timestamp - stor79 <= stor78:
      revert with 0, '1'
  stor80 = stor79
  stor79 = block.timestamp
  [94midx = 0
  while [94midx < 3:
      require [94midx < 3
      if not stor85[[94midx]:
          mem[0] = stor98
          mem[32] = 15
          uint256(user[stor98].field_3072) += stor81[[94midx] * stor14 * stor35 / 10000
      else:
          require [94midx < 3
          if [94midx:
              uint256(stor19[stor85[[94midx]].field_1792) = [94midx
              uint256(stor19[stor85[[94midx]].field_1536) = 999
              uint256(stor19[stor85[[94midx]].field_2048) = uint256(stor19[stor85[[94midx]].field_1280)
              if stor81[[94midx] * stor14 * stor35 / 10000 <= uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328):
                  mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                  mem[32] = 21
                  [94m_148 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_148] = block.timestamp
                  mem[[94m_148 + 32] = 26
                  mem[[94m_148 + 64] = stor81[[94midx] * stor14 * stor35 / 10000
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = stor81[[94midx] * stor14 * stor35 / 10000
                  if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                  mem[32] = 15
                  uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += stor81[[94midx] * stor14 * stor35 / 10000
                  uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) -= stor81[[94midx] * stor14 * stor35 / 10000
              else:
                  uint256(user[stor98].field_3072) = (stor81[[94midx] * stor14 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  mem[0] = stor98
                  mem[32] = 21
                  [94m_154 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_154] = block.timestamp
                  mem[[94m_154 + 32] = 26
                  mem[[94m_154 + 64] = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  uint256(unknownfba71153[stor98].field_0)++
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 26
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  if uint256(unknownfba71153[stor98].field_0) <= stor121:
                      mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      mem[32] = 21
                      [94m_187 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_187] = block.timestamp
                      mem[[94m_187 + 32] = 26
                      mem[[94m_187 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  else:
                      require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      mem[32] = 21
                      [94m_211 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_211] = block.timestamp
                      mem[[94m_211 + 32] = 26
                      mem[[94m_211 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                  uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                  mem[32] = 15
                  uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                  uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) = 0
          else:
              if uint256(user[addr(stor19[stor85[[94midx]].field_256)].field_10240):
                  uint256(stor19[stor85[[94midx]].field_1792) = [94midx
                  uint256(stor19[stor85[[94midx]].field_1536) = 999
                  uint256(stor19[stor85[[94midx]].field_2048) = uint256(stor19[stor85[[94midx]].field_1280)
                  if stor81[[94midx] * stor14 * stor35 / 10000 <= uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328):
                      mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      mem[32] = 21
                      [94m_165 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_165] = block.timestamp
                      mem[[94m_165 + 32] = 26
                      mem[[94m_165 + 64] = stor81[[94midx] * stor14 * stor35 / 10000
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = stor81[[94midx] * stor14 * stor35 / 10000
                      if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      mem[32] = 15
                      uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += stor81[[94midx] * stor14 * stor35 / 10000
                      uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) -= stor81[[94midx] * stor14 * stor35 / 10000
                  else:
                      uint256(user[stor98].field_3072) = (stor81[[94midx] * stor14 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      mem[0] = stor98
                      mem[32] = 21
                      [94m_171 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_171] = block.timestamp
                      mem[[94m_171 + 32] = 26
                      mem[[94m_171 + 64] = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      uint256(unknownfba71153[stor98].field_0)++
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 26
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 21
                          [94m_218 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_218] = block.timestamp
                          mem[[94m_218 + 32] = 26
                          mem[[94m_218 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      else:
                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 21
                          [94m_242 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_242] = block.timestamp
                          mem[[94m_242 + 32] = 26
                          mem[[94m_242 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                      uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      mem[32] = 15
                      uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                      uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) = 0
              else:
                  if not stor110:
                      stor110 = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      uint256(user[addr(stor19[stor85[[94midx]].field_256)].field_10240) = 1
                      uint256(stor19[stor85[[94midx]].field_1792) = [94midx
                      uint256(stor19[stor85[[94midx]].field_1536) = 999
                      uint256(stor19[stor85[[94midx]].field_2048) = uint256(stor19[stor85[[94midx]].field_1280)
                      if stor81[[94midx] * stor14 * stor35 / 10000 <= uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328):
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 21
                          [94m_196 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_196] = block.timestamp
                          mem[[94m_196 + 32] = 26
                          mem[[94m_196 + 64] = stor81[[94midx] * stor14 * stor35 / 10000
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = stor81[[94midx] * stor14 * stor35 / 10000
                          if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += stor81[[94midx] * stor14 * stor35 / 10000
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) -= stor81[[94midx] * stor14 * stor35 / 10000
                      else:
                          uint256(user[stor98].field_3072) = (stor81[[94midx] * stor14 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          mem[0] = stor98
                          mem[32] = 21
                          [94m_202 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_202] = block.timestamp
                          mem[[94m_202 + 32] = 26
                          mem[[94m_202 + 64] = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(unknownfba71153[stor98].field_0)++
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 26
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          if uint256(unknownfba71153[stor98].field_0) <= stor121:
                              mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                              mem[32] = 21
                              [94m_260 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_260] = block.timestamp
                              mem[[94m_260 + 32] = 26
                              mem[[94m_260 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          else:
                              require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                              mem[32] = 21
                              [94m_274 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_274] = block.timestamp
                              mem[[94m_274 + 32] = 26
                              mem[[94m_274 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) = 0
                  else:
                      uint256(user[stor110].field_10240) = 0
                      stor110 = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                      uint256(user[addr(stor19[stor85[[94midx]].field_256)].field_10240) = 1
                      uint256(stor19[stor85[[94midx]].field_1792) = [94midx
                      uint256(stor19[stor85[[94midx]].field_1536) = 999
                      uint256(stor19[stor85[[94midx]].field_2048) = uint256(stor19[stor85[[94midx]].field_1280)
                      if stor81[[94midx] * stor14 * stor35 / 10000 <= uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328):
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 21
                          [94m_226 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_226] = block.timestamp
                          mem[[94m_226 + 32] = 26
                          mem[[94m_226 + 64] = stor81[[94midx] * stor14 * stor35 / 10000
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = stor81[[94midx] * stor14 * stor35 / 10000
                          if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += stor81[[94midx] * stor14 * stor35 / 10000
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) -= stor81[[94midx] * stor14 * stor35 / 10000
                      else:
                          uint256(user[stor98].field_3072) = (stor81[[94midx] * stor14 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          mem[0] = stor98
                          mem[32] = 21
                          [94m_232 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_232] = block.timestamp
                          mem[[94m_232 + 32] = 26
                          mem[[94m_232 + 64] = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(unknownfba71153[stor98].field_0)++
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 26
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor81[[94midx] * stor14 * stor35 / 10000) - uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          if uint256(unknownfba71153[stor98].field_0) <= stor121:
                              mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                              mem[32] = 21
                              [94m_281 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_281] = block.timestamp
                              mem[[94m_281 + 32] = 26
                              mem[[94m_281 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          else:
                              require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                              mem[32] = 21
                              [94m_292 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_292] = block.timestamp
                              mem[[94m_292 + 32] = 26
                              mem[[94m_292 + 64] = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_256) = 26
                          uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)][uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)].field_512) = uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          if uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor85', 85))), ('name', 'stor19', 19))))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3072) += uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328)
                          uint256(user[addr(user[addr(stor19[stor85[[94midx]].field_256)].field_256)].field_3328) = 0
      [94midx = [94midx + 1
      continue 
  [94m_135 = mem[64]
  mem[64] = mem[64] + 96
  mem[[94m_135] = 0
  mem[[94m_135 + 32] = 0
  mem[[94m_135 + 64] = 0
  [94ms = 85
  [94midx = [94m_135
  while [94m_135 + 96 > [94midx:
      uint8(stor[[94ms].field_0) = mem[[94midx + 31 len 1]
      Mask(248, 0, stor[[94ms].field_8) = 0
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 88
  while 88 > [94midx:
      uint256(stor[[94midx].field_0) = 0
      [94midx = [94midx + 1
      continue 
  [94midx = 0
  while [94midx < stor20:
      mem[0] = [94midx
      mem[32] = 19
      uint256(stor19[[94midx].field_1280) = 0
      [94midx = [94midx + 1
      continue 
  stor14 = 0


# hash = 0x1af21c67
# getter = None
# const = None
# payable = True
def unknown1af21c67() payable: 
  mem[64] = 96
  require not call.value
  if stor46 > block.timestamp:
      revert with 0, 'SafeMath sub failed'
  if block.timestamp - stor46 <= stor45:
      revert with 0, '1'
  stor47 = stor46
  stor46 = block.timestamp
  [94midx = 0
  while [94midx < 10:
      require [94midx < 10
      if not stor58[[94midx]:
          uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
          require [94midx < 10
          if not stor68[[94midx]:
              mem[0] = stor98
              mem[32] = 15
              uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
          else:
              require [94midx < 10
              mem[32] = 15
              mem[mem[64] + 32] = stor48[[94midx]
              mem[mem[64] + 64] = stor13
              mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
              log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
              uint256(user[stor68[[94midx]].field_7936) = [94midx
              uint256(user[stor68[[94midx]].field_7424) = 999
              uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
              if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                  mem[0] = addr(user[stor68[[94midx]].field_256)
                  mem[32] = 21
                  [94m_493 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_493] = block.timestamp
                  mem[[94m_493 + 32] = 25
                  mem[[94m_493 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                  if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = addr(user[stor68[[94midx]].field_256)
                  mem[32] = 15
                  uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                  uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
              else:
                  uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  mem[0] = stor98
                  mem[32] = 21
                  [94m_499 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_499] = block.timestamp
                  mem[[94m_499 + 32] = 25
                  mem[[94m_499 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  uint256(unknownfba71153[stor98].field_0)++
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                  uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  if uint256(unknownfba71153[stor98].field_0) <= stor121:
                      mem[0] = addr(user[stor68[[94midx]].field_256)
                      mem[32] = 21
                      [94m_521 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_521] = block.timestamp
                      mem[[94m_521 + 32] = 25
                      mem[[94m_521 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  else:
                      require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = addr(user[stor68[[94midx]].field_256)
                      mem[32] = 21
                      [94m_529 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_529] = block.timestamp
                      mem[[94m_529 + 32] = 25
                      mem[[94m_529 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                  uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = addr(user[stor68[[94midx]].field_256)
                  mem[32] = 15
                  uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                  uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
              require [94midx < 10
              mem[mem[64]] = stor58[[94midx]
              mem[mem[64] + 32] = stor48[[94midx]
              mem[mem[64] + 64] = stor13
              mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
              mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
              mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
              log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
      else:
          require [94midx < 10
          uint256(user[stor58[[94midx]].field_7680) = [94midx
          uint256(user[stor58[[94midx]].field_7168) = 999
          uint256(user[stor58[[94midx]].field_8192) = uint256(user[stor58[[94midx]].field_1536)
          if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328):
              mem[0] = addr(user[stor58[[94midx]].field_256)
              mem[32] = 21
              [94m_457 = mem[64]
              mem[64] = mem[64] + 96
              mem[[94m_457] = block.timestamp
              mem[[94m_457 + 32] = 24
              mem[[94m_457 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
              uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)++
              uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_0) = block.timestamp
              uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_256) = 24
              uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
              if uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) <= stor121:
                  uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                  uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                  require [94midx < 10
                  if not stor68[[94midx]:
                      mem[0] = stor98
                      mem[32] = 15
                      uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                  else:
                      require [94midx < 10
                      mem[32] = 15
                      mem[mem[64] + 32] = stor48[[94midx]
                      mem[mem[64] + 64] = stor13
                      mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                      log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                      uint256(user[stor68[[94midx]].field_7936) = [94midx
                      uint256(user[stor68[[94midx]].field_7424) = 999
                      uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                      if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 21
                          [94m_561 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_561] = block.timestamp
                          mem[[94m_561 + 32] = 25
                          mem[[94m_561 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                          if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          mem[0] = stor98
                          mem[32] = 21
                          [94m_567 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_567] = block.timestamp
                          mem[[94m_567 + 32] = 25
                          mem[[94m_567 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(unknownfba71153[stor98].field_0)++
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          if uint256(unknownfba71153[stor98].field_0) <= stor121:
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_617 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_617] = block.timestamp
                              mem[[94m_617 + 32] = 25
                              mem[[94m_617 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          else:
                              require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_644 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_644] = block.timestamp
                              mem[[94m_644 + 32] = 25
                              mem[[94m_644 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      mem[mem[64]] = stor58[[94midx]
                      mem[mem[64] + 32] = stor48[[94midx]
                      mem[mem[64] + 64] = stor13
                      mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                      mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                      mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                      log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
              else:
                  require uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)
                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                  uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                  require [94midx < 10
                  if not stor68[[94midx]:
                      mem[0] = stor98
                      mem[32] = 15
                      uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                  else:
                      require [94midx < 10
                      mem[32] = 15
                      mem[mem[64] + 32] = stor48[[94midx]
                      mem[mem[64] + 64] = stor13
                      mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                      log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                      uint256(user[stor68[[94midx]].field_7936) = [94midx
                      uint256(user[stor68[[94midx]].field_7424) = 999
                      uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                      if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 21
                          [94m_582 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_582] = block.timestamp
                          mem[[94m_582 + 32] = 25
                          mem[[94m_582 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                          if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          mem[0] = stor98
                          mem[32] = 21
                          [94m_588 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_588] = block.timestamp
                          mem[[94m_588 + 32] = 25
                          mem[[94m_588 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(unknownfba71153[stor98].field_0)++
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                          uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          if uint256(unknownfba71153[stor98].field_0) <= stor121:
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_651 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_651] = block.timestamp
                              mem[[94m_651 + 32] = 25
                              mem[[94m_651 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          else:
                              require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_691 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_691] = block.timestamp
                              mem[[94m_691 + 32] = 25
                              mem[[94m_691 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                          uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = addr(user[stor68[[94midx]].field_256)
                          mem[32] = 15
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                          uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      mem[mem[64]] = stor58[[94midx]
                      mem[mem[64] + 32] = stor48[[94midx]
                      mem[mem[64] + 64] = stor13
                      mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                      mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                      mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                      log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
          else:
              uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
              mem[0] = stor98
              mem[32] = 21
              [94m_463 = mem[64]
              mem[64] = mem[64] + 96
              mem[[94m_463] = block.timestamp
              mem[[94m_463 + 32] = 24
              mem[[94m_463 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
              uint256(unknownfba71153[stor98].field_0)++
              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 24
              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                  mem[0] = addr(user[stor58[[94midx]].field_256)
                  mem[32] = 21
                  [94m_478 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_478] = block.timestamp
                  mem[[94m_478 + 32] = 24
                  mem[[94m_478 + 64] = uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_256) = 24
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                  if uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) <= stor121:
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      if not stor68[[94midx]:
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          require [94midx < 10
                          mem[32] = 15
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                          uint256(user[stor68[[94midx]].field_7936) = [94midx
                          uint256(user[stor68[[94midx]].field_7424) = 999
                          uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                          if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_626 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_626] = block.timestamp
                              mem[[94m_626 + 32] = 25
                              mem[[94m_626 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                          else:
                              uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_632 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_632] = block.timestamp
                              mem[[94m_632 + 32] = 25
                              mem[[94m_632 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_727 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_727] = block.timestamp
                                  mem[[94m_727 + 32] = 25
                                  mem[[94m_727 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_748 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_748] = block.timestamp
                                  mem[[94m_748 + 32] = 25
                                  mem[[94m_748 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                          require [94midx < 10
                          mem[mem[64]] = stor58[[94midx]
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                          mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                  else:
                      require uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      if not stor68[[94midx]:
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          require [94midx < 10
                          mem[32] = 15
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                          uint256(user[stor68[[94midx]].field_7936) = [94midx
                          uint256(user[stor68[[94midx]].field_7424) = 999
                          uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                          if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_659 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_659] = block.timestamp
                              mem[[94m_659 + 32] = 25
                              mem[[94m_659 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                          else:
                              uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_665 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_665] = block.timestamp
                              mem[[94m_665 + 32] = 25
                              mem[[94m_665 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_755 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_755] = block.timestamp
                                  mem[[94m_755 + 32] = 25
                                  mem[[94m_755 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_780 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_780] = block.timestamp
                                  mem[[94m_780 + 32] = 25
                                  mem[[94m_780 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                          require [94midx < 10
                          mem[mem[64]] = stor58[[94midx]
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                          mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
              else:
                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = addr(user[stor58[[94midx]].field_256)
                  mem[32] = 21
                  [94m_487 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_487] = block.timestamp
                  mem[[94m_487 + 32] = 24
                  mem[[94m_487 + 64] = uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_256) = 24
                  uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                  if uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) <= stor121:
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      if not stor68[[94midx]:
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          require [94midx < 10
                          mem[32] = 15
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                          uint256(user[stor68[[94midx]].field_7936) = [94midx
                          uint256(user[stor68[[94midx]].field_7424) = 999
                          uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                          if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_671 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_671] = block.timestamp
                              mem[[94m_671 + 32] = 25
                              mem[[94m_671 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                          else:
                              uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_677 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_677] = block.timestamp
                              mem[[94m_677 + 32] = 25
                              mem[[94m_677 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_762 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_762] = block.timestamp
                                  mem[[94m_762 + 32] = 25
                                  mem[[94m_762 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_787 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_787] = block.timestamp
                                  mem[[94m_787 + 32] = 25
                                  mem[[94m_787 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                          require [94midx < 10
                          mem[mem[64]] = stor58[[94midx]
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                          mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                  else:
                      require uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor58[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor58', 58))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328)
                      uint256(user[addr(user[stor58[[94midx]].field_256)].field_3328) = 0
                      require [94midx < 10
                      if not stor68[[94midx]:
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                      else:
                          require [94midx < 10
                          mem[32] = 15
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
                          uint256(user[stor68[[94midx]].field_7936) = [94midx
                          uint256(user[stor68[[94midx]].field_7424) = 999
                          uint256(user[stor68[[94midx]].field_8448) = uint256(user[stor68[[94midx]].field_1792)
                          if stor48[[94midx] * stor13 * stor35 / 10000 <= uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328):
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 21
                              [94m_704 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_704] = block.timestamp
                              mem[[94m_704 + 32] = 25
                              mem[[94m_704 + 64] = stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = stor48[[94midx] * stor13 * stor35 / 10000
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += stor48[[94midx] * stor13 * stor35 / 10000
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) -= stor48[[94midx] * stor13 * stor35 / 10000
                          else:
                              uint256(user[stor98].field_3072) = (stor48[[94midx] * stor13 * stor35 / 10000) + uint256(user[stor98].field_3072) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_710 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_710] = block.timestamp
                              mem[[94m_710 + 32] = 25
                              mem[[94m_710 + 64] = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 25
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = (stor48[[94midx] * stor13 * stor35 / 10000) - uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_794 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_794] = block.timestamp
                                  mem[[94m_794 + 32] = 25
                                  mem[[94m_794 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = addr(user[stor68[[94midx]].field_256)
                                  mem[32] = 21
                                  [94m_822 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_822] = block.timestamp
                                  mem[[94m_822 + 32] = 25
                                  mem[[94m_822 + 64] = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_256) = 25
                              uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)][uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)].field_512) = uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              if uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) > stor121:
                                  require uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[stor68[[94midx]].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor68', 68))), ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = addr(user[stor68[[94midx]].field_256)
                              mem[32] = 15
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3072) += uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328)
                              uint256(user[addr(user[stor68[[94midx]].field_256)].field_3328) = 0
                          require [94midx < 10
                          mem[mem[64]] = stor58[[94midx]
                          mem[mem[64] + 32] = stor48[[94midx]
                          mem[mem[64] + 64] = stor13
                          mem[mem[64] + 96] = stor48[[94midx] * stor13 * stor35 / 10000
                          mem[mem[64] + 128] = uint256(user[stor68[[94midx]].field_3328)
                          mem[mem[64] + 160] = uint256(user[stor68[[94midx]].field_3072)
                          log 0xeebb963e: stor58[idx], stor48[idx], stor13, stor48[idx] * stor13 * stor35 / 10000, uint256(user[stor68[idx]].field_3328), uint256(user[stor68[idx]].field_3072)
      [94midx = [94midx + 1
      continue 
  [94m_447 = mem[64]
  mem[64] = mem[64] + 320
  mem[[94m_447] = 0
  mem[[94m_447 + 32] = 0
  mem[[94m_447 + 64] = 0
  mem[[94m_447 + 96] = 0
  mem[[94m_447 + 128] = 0
  mem[[94m_447 + 160] = 0
  mem[[94m_447 + 192] = 0
  mem[[94m_447 + 224] = 0
  mem[[94m_447 + 256] = 0
  mem[[94m_447 + 288] = 0
  [94ms = 58
  [94midx = [94m_447
  while [94m_447 + 320 > [94midx:
      addr(stor[[94ms].field_0) = mem[[94midx + 12 len 20]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 68
  while 68 > [94midx:
      addr(stor[[94midx].field_0) = 0
      [94midx = [94midx + 1
      continue 
  [94m_894 = mem[64]
  mem[64] = mem[64] + 320
  mem[[94m_894] = 0
  mem[[94m_894 + 32] = 0
  mem[[94m_894 + 64] = 0
  mem[[94m_894 + 96] = 0
  mem[[94m_894 + 128] = 0
  mem[[94m_894 + 160] = 0
  mem[[94m_894 + 192] = 0
  mem[[94m_894 + 224] = 0
  mem[[94m_894 + 256] = 0
  mem[[94m_894 + 288] = 0
  [94ms = 68
  [94midx = [94m_894
  while [94m_894 + 320 > [94midx:
      addr(stor[[94ms].field_0) = mem[[94midx + 12 len 20]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 78
  while 78 > [94midx:
      addr(stor[[94midx].field_0) = 0
      [94midx = [94midx + 1
      continue 
  [94midx = 0
  while [94midx < stor16.length:
      uint256(user[stor16[[94midx]].field_1536) = 0
      mem[0] = stor16[[94midx]
      mem[32] = 15
      uint256(user[stor16[[94midx]].field_1792) = 0
      [94midx = [94midx + 1
      continue 
  stor13 = 0


# hash = 0x200d2ed2
# getter = None
# const = None
# payable = False
def status(): # not payable
  return stor28, stor25, stor24, stor29, stor26, stor22, bool(stor23), stor6, stor20, stor10, stor112


# hash = 0x3262fd9a
# getter = None
# const = None
# payable = False
def getMoney(uint256 _lockId): # not payable
  require calldata.size - 4 >= 32
  mem[32] = sha3(_lockId, 120)
  mem[96] = stor117[_lockId][2].length
  mem[0] = sha3(_lockId, 117) + 2
  mem[128] = uint256(stor117[_lockId][2].field_0)
  [94midx = 128
  [94ms = 0
  while stor117[_lockId][2].length + 96 > [94midx:
      mem[[94midx + 32] = uint256(stor117[_lockId][[94ms + 2].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 160
  mem[ceil32(stor117[_lockId][2].length) + 128] = stor117[_lockId][3].length
  mem[ceil32(stor117[_lockId][2].length) + 160] = uint256(stor117[_lockId][3].field_0)
  [94midx = ceil32(stor117[_lockId][2].length) + 160
  [94ms = 0
  while ceil32(stor117[_lockId][2].length) + stor117[_lockId][3].length + 128 > [94midx:
      mem[[94midx + 32] = uint256(stor117[_lockId][[94ms + 3].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 224] = uint256(stor117[_lockId].field_1024)
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 256] = uint256(stor117[_lockId].field_1280)
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 288] = uint256(stor117[_lockId].field_1536)
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 320] = uint256(stor117[_lockId].field_1792)
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 352] = stor120[_lockId][caller]
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 160] = 224
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 384] = stor117[_lockId][2].length
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 416 len ceil32(stor117[_lockId][2].length)] = mem[128 len ceil32(stor117[_lockId][2].length)]
  mem[ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 192] = stor117[_lockId][2].length + 256
  mem[stor117[_lockId][2].length + ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 416] = stor117[_lockId][3].length
  mem[stor117[_lockId][2].length + ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 448 len ceil32(stor117[_lockId][3].length)] = mem[ceil32(stor117[_lockId][2].length) + 160 len ceil32(stor117[_lockId][3].length)]
  if not stor117[_lockId][3].length % 32:
      return Array(len=stor117[_lockId][2].length, data=mem[128 len ceil32(stor117[_lockId][2].length)], mem[(2 * ceil32(stor117[_lockId][2].length)) + ceil32(stor117[_lockId][3].length) + 416 len stor117[_lockId][3].length + stor117[_lockId][2].length + -ceil32(stor117[_lockId][2].length) + 32]), 
             stor117[_lockId][2].length + 256,
             uint256(stor117[_lockId].field_1024),
             uint256(stor117[_lockId].field_1280),
             uint256(stor117[_lockId].field_1536),
             uint256(stor117[_lockId].field_1792),
             stor120[_lockId][caller]
  mem[floor32(stor117[_lockId][3].length) + stor117[_lockId][2].length + ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + 448] = mem[floor32(stor117[_lockId][3].length) + stor117[_lockId][2].length + ceil32(stor117[_lockId][2].length) + ceil32(stor117[_lockId][3].length) + -stor117[_lockId][3].length % 32 + 480 len stor117[_lockId][3].length % 32]
  return Array(len=stor117[_lockId][2].length, data=mem[128 len ceil32(stor117[_lockId][2].length)], mem[(2 * ceil32(stor117[_lockId][2].length)) + ceil32(stor117[_lockId][3].length) + 416 len floor32(stor117[_lockId][3].length) + stor117[_lockId][2].length + -ceil32(stor117[_lockId][2].length) + 64]), 
         stor117[_lockId][2].length + 256,
         uint256(stor117[_lockId].field_1024),
         uint256(stor117[_lockId].field_1280),
         uint256(stor117[_lockId].field_1536),
         uint256(stor117[_lockId].field_1792),
         stor120[_lockId][caller]


# hash = 0x4225b0a0
# getter = None
# const = None
# payable = False
def unknown4225b0a0(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if not uint256(user[caller].field_2304):
      if uint256(stor19[_param1].field_3072) >= stor114:
          uint256(user[caller].field_2304) = _param1


# hash = 0x53556559
# getter = None
# const = None
# payable = False
def unknown53556559(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if _param1 * stor123 <= uint256(user[caller].field_2816):
      uint256(user[caller].field_2816) += -1 * _param1 * stor123
      uint256(unknownfba71153[caller].field_0)++
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 14
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = _param1 * stor123
      if uint256(unknownfba71153[caller].field_0) > stor121:
          require uint256(unknownfba71153[caller].field_0) + -stor121 - 1 < uint256(unknownfba71153[caller].field_0)
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
      require ext_code.size(stor1.length)
      call stor1.length.0x9141402f with:
           gas gas_remaining - 50 wei
          args _param1, caller
      require ext_call.success
      uint256(unknownfba71153[caller].field_0)++
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 32
      uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = _param1
      if uint256(unknownfba71153[caller].field_0) > stor121:
          require uint256(unknownfba71153[caller].field_0) + -stor121 - 1 < uint256(unknownfba71153[caller].field_0)
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0


# hash = 0x535bc316
# getter = None
# const = None
# payable = False
def unknown535bc316(addr _param1): # not payable
  require calldata.size - 4 >= 32
  [94midx = 2880
  [94ms = 14
  while 2976 > [94midx + 32:
      mem[[94midx + 32] = uint256(user[addr(_param1)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return uint256(user[addr(_param1)].field_9984), 
         uint256(user[addr(_param1)].field_10496),
         uint256(user[addr(_param1)].field_6144),
         uint256(stor17C4.field_0),
         uint256(stor3416.field_0),
         uint256(storEFB5.field_0),
         uint256(user[addr(_param1)].field_10752),
         uint256(user[addr(_param1)].field_9472)


# hash = 0x66d2021f
# getter = None
# const = None
# payable = False
def unknown66d2021f(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if not stor0:
      stor0 = _param1
      stor1.length = _param1


# hash = 0x6a619497
# getter = None
# const = None
# payable = False
def unknown6a619497(addr _param1): # not payable
  require calldata.size - 4 >= 32
  [94midx = 2880
  [94ms = 14
  while 2976 > [94midx + 32:
      mem[[94midx + 32] = uint256(user[addr(_param1)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  if 10 <= uint256(user[addr(_param1)].field_7168):
      if uint256(user[addr(_param1)].field_7424) >= 10:
          return uint256(user[addr(_param1)].field_1536), 
                 uint256(user[addr(_param1)].field_7168),
                 uint256(user[addr(_param1)].field_1792),
                 uint256(user[addr(_param1)].field_7424),
                 uint256(user[addr(_param1)].field_8192),
                 uint256(user[addr(_param1)].field_7680),
                 uint256(user[addr(_param1)].field_8448),
                 uint256(user[addr(_param1)].field_7936),
                 uint256(user[addr(_param1)].field_8704),
                 uint256(user[stor67.length].field_1536),
                 uint256(user[stor67.length].field_1792),
                 uint256(user[addr(_param1)].field_10240)
      if uint256(user[addr(_param1)].field_7424) <= 0:
          return uint256(user[addr(_param1)].field_1536), 
                 uint256(user[addr(_param1)].field_7168),
                 uint256(user[addr(_param1)].field_1792),
                 uint256(user[addr(_param1)].field_7424),
                 uint256(user[addr(_param1)].field_8192),
                 uint256(user[addr(_param1)].field_7680),
                 uint256(user[addr(_param1)].field_8448),
                 uint256(user[addr(_param1)].field_7936),
                 uint256(user[addr(_param1)].field_8704),
                 uint256(user[stor67.length].field_1536),
                 uint256(user[stor67.length].field_1792),
                 uint256(user[addr(_param1)].field_10240)
      if uint256(user[addr(_param1)].field_7424) - 1 < 10:
          return uint256(user[addr(_param1)].field_1536), 
                 uint256(user[addr(_param1)].field_7168),
                 uint256(user[addr(_param1)].field_1792),
                 uint256(user[addr(_param1)].field_7424),
                 uint256(user[addr(_param1)].field_8192),
                 uint256(user[addr(_param1)].field_7680),
                 uint256(user[addr(_param1)].field_8448),
                 uint256(user[addr(_param1)].field_7936),
                 uint256(user[addr(_param1)].field_8704),
                 uint256(user[stor67.length].field_1536),
                 uint256(user[stor67[uint256(user[addr(_param1)].field_7424)]].field_1792),
                 uint256(user[addr(_param1)].field_10240)
  else:
      if uint256(user[addr(_param1)].field_7168) <= 0:
          if uint256(user[addr(_param1)].field_7424) >= 10:
              return uint256(user[addr(_param1)].field_1536), 
                     uint256(user[addr(_param1)].field_7168),
                     uint256(user[addr(_param1)].field_1792),
                     uint256(user[addr(_param1)].field_7424),
                     uint256(user[addr(_param1)].field_8192),
                     uint256(user[addr(_param1)].field_7680),
                     uint256(user[addr(_param1)].field_8448),
                     uint256(user[addr(_param1)].field_7936),
                     uint256(user[addr(_param1)].field_8704),
                     uint256(user[stor67.length].field_1536),
                     uint256(user[stor67.length].field_1792),
                     uint256(user[addr(_param1)].field_10240)
          if uint256(user[addr(_param1)].field_7424) <= 0:
              return uint256(user[addr(_param1)].field_1536), 
                     uint256(user[addr(_param1)].field_7168),
                     uint256(user[addr(_param1)].field_1792),
                     uint256(user[addr(_param1)].field_7424),
                     uint256(user[addr(_param1)].field_8192),
                     uint256(user[addr(_param1)].field_7680),
                     uint256(user[addr(_param1)].field_8448),
                     uint256(user[addr(_param1)].field_7936),
                     uint256(user[addr(_param1)].field_8704),
                     uint256(user[stor67.length].field_1536),
                     uint256(user[stor67.length].field_1792),
                     uint256(user[addr(_param1)].field_10240)
          if uint256(user[addr(_param1)].field_7424) - 1 < 10:
              return uint256(user[addr(_param1)].field_1536), 
                     uint256(user[addr(_param1)].field_7168),
                     uint256(user[addr(_param1)].field_1792),
                     uint256(user[addr(_param1)].field_7424),
                     uint256(user[addr(_param1)].field_8192),
                     uint256(user[addr(_param1)].field_7680),
                     uint256(user[addr(_param1)].field_8448),
                     uint256(user[addr(_param1)].field_7936),
                     uint256(user[addr(_param1)].field_8704),
                     uint256(user[stor67.length].field_1536),
                     uint256(user[stor67[uint256(user[addr(_param1)].field_7424)]].field_1792),
                     uint256(user[addr(_param1)].field_10240)
      else:
          if uint256(user[addr(_param1)].field_7168) - 1 < 10:
              if uint256(user[addr(_param1)].field_7424) >= 10:
                  return uint256(user[addr(_param1)].field_1536), 
                         uint256(user[addr(_param1)].field_7168),
                         uint256(user[addr(_param1)].field_1792),
                         uint256(user[addr(_param1)].field_7424),
                         uint256(user[addr(_param1)].field_8192),
                         uint256(user[addr(_param1)].field_7680),
                         uint256(user[addr(_param1)].field_8448),
                         uint256(user[addr(_param1)].field_7936),
                         uint256(user[addr(_param1)].field_8704),
                         uint256(user[stor57[uint256(user[addr(_param1)].field_7168)]].field_1536),
                         uint256(user[stor67.length].field_1792),
                         uint256(user[addr(_param1)].field_10240)
              if uint256(user[addr(_param1)].field_7424) <= 0:
                  return uint256(user[addr(_param1)].field_1536), 
                         uint256(user[addr(_param1)].field_7168),
                         uint256(user[addr(_param1)].field_1792),
                         uint256(user[addr(_param1)].field_7424),
                         uint256(user[addr(_param1)].field_8192),
                         uint256(user[addr(_param1)].field_7680),
                         uint256(user[addr(_param1)].field_8448),
                         uint256(user[addr(_param1)].field_7936),
                         uint256(user[addr(_param1)].field_8704),
                         uint256(user[stor57[uint256(user[addr(_param1)].field_7168)]].field_1536),
                         uint256(user[stor67.length].field_1792),
                         uint256(user[addr(_param1)].field_10240)
              if uint256(user[addr(_param1)].field_7424) - 1 < 10:
                  return uint256(user[addr(_param1)].field_1536), 
                         uint256(user[addr(_param1)].field_7168),
                         uint256(user[addr(_param1)].field_1792),
                         uint256(user[addr(_param1)].field_7424),
                         uint256(user[addr(_param1)].field_8192),
                         uint256(user[addr(_param1)].field_7680),
                         uint256(user[addr(_param1)].field_8448),
                         uint256(user[addr(_param1)].field_7936),
                         uint256(user[addr(_param1)].field_8704),
                         uint256(user[stor57[uint256(user[addr(_param1)].field_7168)]].field_1536),
                         uint256(user[stor67[uint256(user[addr(_param1)].field_7424)]].field_1792),
                         uint256(user[addr(_param1)].field_10240)
  revert


# hash = 0x6f77926b
# getter = ['struct', ['loc', 15]]
# const = None
# payable = False
def getUser(address _addr): # not payable
  require calldata.size - 4 >= 32
  [94midx = 2880
  [94ms = 14
  while 2976 > [94midx + 32:
      mem[[94midx + 32] = uint256(user[addr(_addr)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return addr(user[addr(_addr)].field_512), 
         uint256(user[addr(_addr)].field_2048),
         uint256(user[addr(_addr)].field_2304),
         uint256(user[addr(_addr)].field_2560),
         uint256(user[addr(_addr)].field_2816),
         uint256(user[addr(_addr)].field_3072),
         uint256(user[addr(_addr)].field_3328),
         uint256(user[addr(_addr)].field_5120),
         uint256(user[addr(_addr)].field_5376),
         uint256(user[addr(_addr)].field_5632),
         uint256(user[addr(_addr)].field_8960)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['add', 12, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 15]]]]
# const = None
# payable = False
def balanceOf(address _tokenOwner): # not payable
  require calldata.size - 4 >= 32
  return uint256(user[addr(_tokenOwner)].field_3072)


# hash = 0x7879b5ef
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 94]]]
# const = None
# payable = False
def unknown7879b5ef(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return uint256(unknown7879b5ef[_param1].field_0), 
         uint256(unknown7879b5ef[_param1].field_256),
         uint256(unknown7879b5ef[_param1].field_512),
         uint256(unknown7879b5ef[_param1].field_768),
         uint256(unknown7879b5ef[_param1].field_1024)


# hash = 0x7898d07e
# getter = None
# const = None
# payable = False
def unknown7898d07e(): # not payable
  uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)++
  uint256(unknownfba71153[addr(stor15[caller].field_256)][uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)].field_0) = block.timestamp
  uint256(unknownfba71153[addr(stor15[caller].field_256)][uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)].field_256) = 23
  if uint256(user[caller].field_2560) <= uint256(user[caller].field_3072):
      uint256(unknownfba71153[addr(stor15[caller].field_256)][uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)].field_512) = uint256(user[caller].field_2560)
      if uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0) > stor121:
          require uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(user[caller].field_2560) = 0
      uint256(user[caller].field_3072) -= uint256(user[caller].field_2560)
      if stor28 > eth.balance(this.address):
          revert with 0, 'SafeMath sub failed'
      if stor25 > eth.balance(this.address) - stor28:
          revert with 0, 'SafeMath sub failed'
      if stor24 > eth.balance(this.address) - stor28 - stor25:
          revert with 0, 'SafeMath sub failed'
      if stor26 > eth.balance(this.address) - stor28 - stor25 - stor24:
          revert with 0, 'SafeMath sub failed'
      if eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 < 2 * 10^16 * uint256(user[caller].field_2560):
          uint256(user[caller].field_6912) = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 + uint256(user[caller].field_6912)
          call caller with:
             value eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          stor9 = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 + stor9
          uint256(unknownfba71153[caller].field_0)++
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 4
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26
      else:
          uint256(user[caller].field_6912) += 2 * 10^16 * uint256(user[caller].field_2560)
          call caller with:
             value 2 * 10^16 * uint256(user[caller].field_2560) wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          stor9 += 2 * 10^16 * uint256(user[caller].field_2560)
          uint256(unknownfba71153[caller].field_0)++
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 4
          bool(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = 0
          uint255(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_513) = uint255(10^16 * uint256(user[caller].field_2560))
  else:
      uint256(unknownfba71153[addr(stor15[caller].field_256)][uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)].field_512) = uint256(user[caller].field_3072)
      if uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0) > stor121:
          require uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
          uint256(stor[(3 * uint256(unknownfba71153[addr(stor15[caller].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', 'caller', ('name', 'stor15', 15))))), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(user[caller].field_2560) -= uint256(user[caller].field_3072)
      uint256(user[caller].field_3072) = 0
      if stor28 > eth.balance(this.address):
          revert with 0, 'SafeMath sub failed'
      if stor25 > eth.balance(this.address) - stor28:
          revert with 0, 'SafeMath sub failed'
      if stor24 > eth.balance(this.address) - stor28 - stor25:
          revert with 0, 'SafeMath sub failed'
      if stor26 > eth.balance(this.address) - stor28 - stor25 - stor24:
          revert with 0, 'SafeMath sub failed'
      if eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 < 2 * 10^16 * uint256(user[caller].field_3072):
          uint256(user[caller].field_6912) = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 + uint256(user[caller].field_6912)
          call caller with:
             value eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          stor9 = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26 + stor9
          uint256(unknownfba71153[caller].field_0)++
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 4
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = eth.balance(this.address) - stor28 - stor25 - stor24 - stor26
      else:
          uint256(user[caller].field_6912) += 2 * 10^16 * uint256(user[caller].field_3072)
          call caller with:
             value 2 * 10^16 * uint256(user[caller].field_3072) wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          stor9 += 2 * 10^16 * uint256(user[caller].field_3072)
          uint256(unknownfba71153[caller].field_0)++
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_0) = block.timestamp
          uint256(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_256) = 4
          bool(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_512) = 0
          uint255(unknownfba71153[caller][uint256(unknownfba71153[caller].field_0)].field_513) = uint255(10^16 * uint256(user[caller].field_3072))
  if uint256(unknownfba71153[caller].field_0) > stor121:
      require uint256(unknownfba71153[caller].field_0) + -stor121 - 1 < uint256(unknownfba71153[caller].field_0)
      uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(stor[(3 * uint256(unknownfba71153[caller].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, 'caller'), ('name', 'unknownfba71153', 21))].field_0) = 0
  if eth.balance(this.address) < stor31:
      stor22++
      uint256(stor17C4.field_0) = uint255(stor17C4.field_1)
      uint256(stor3416.field_0) = uint255(stor3416.field_1)
      uint256(storEFB5.field_0) = uint255(storEFB5.field_1)


# hash = 0x78ef7f02
# getter = None
# const = None
# payable = False
def unknown78ef7f02(): # not payable
  return stor88, stor89, stor90, stor91, stor92, stor93


# hash = 0x7ba41561
# getter = None
# const = None
# payable = False
def unknown7ba41561(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if stor97 != caller:
      if uint256(user[caller].field_10240) != 1:
          revert with 0, '2'
  if stor120[_param1][caller]:
      revert with 0, '2'
  if uint256(stor117[_param1].field_1792):
      revert with 0, '2'
  stor120[_param1][caller] = _param2
  if stor97 != caller:
      if _param2 != 1:
          uint256(stor117[_param1].field_1536) += stor111
      else:
          uint256(stor117[_param1].field_1280) += stor111
  else:
      if _param2 != 1:
          uint256(stor117[_param1].field_1536) += 30
      else:
          uint256(stor117[_param1].field_1280) += 30
  if 51 <= uint256(stor117[_param1].field_1280):
      uint256(stor117[_param1].field_1792) = 2
      uint256(user[stor97].field_10496)--
      stor120[_param1][stor97] = 0
      [94midx = 0
      while [94midx < 10:
          if stor101[[94midx]:
              require [94midx < 10
              uint256(user[stor101[[94midx]].field_10496)--
              mem[0] = stor101[[94midx]
              mem[32] = sha3(_param1, 120)
              stor120[_param1][stor101[[94midx]] = 0
          [94midx = [94midx + 1
          continue 
      uint256(user[addr(stor19[_param1].field_256)].field_9984) = 0
      stor118 = 0
      [94midx = 0
      while [94midx < stor119.length:
          mem[0] = 119
          if 0 == stor119[[94midx]:
              [94midx = [94midx + 1
              continue 
          require [94midx < stor119.length
          require [94midx < stor119.length
          if stor119[[94midx] == stor118:
              mem[0] = 119
              stor119[[94midx] = 0
              [94midx = [94midx + 1
              continue 
          stor118 = stor119[[94midx]
          if 51 <= uint256(stor117[_param1].field_1280):
              uint256(stor117[_param1].field_1792) = 1
              if uint256(stor117[_param1].field_256):
                  require ext_code.size(stor1.length)
                  call stor1.length.0x994635c9 with:
                       gas gas_remaining - 50 wei
                      args uint256(stor117[_param1].field_1024) / 10^18, addr(stor19[_param1].field_256)
                  require ext_call.success
                  if ext_call.return_data[0] > 0:
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 71
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024) / 10^18
                      if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
              else:
                  if eth.balance(stor0):
                      if uint256(stor117[_param1].field_1024) <= eth.balance(stor0):
                          uint256(user[addr(stor19[_param1].field_256)].field_6144) += uint256(stor117[_param1].field_1024)
                          stor10 += uint256(stor117[_param1].field_1024)
                          require ext_code.size(stor1.length)
                          call stor1.length.0x107f5111 with:
                               gas gas_remaining - 50 wei
                              args addr(user[addr(stor19[_param1].field_256)].field_256), uint256(stor117[_param1].field_1024)
                          require ext_call.success
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024)
                      else:
                          uint256(user[addr(stor19[_param1].field_256)].field_6144) += eth.balance(stor0)
                          stor10 += eth.balance(stor0)
                          require ext_code.size(stor1.length)
                          call stor1.length.0x107f5111 with:
                               gas gas_remaining - 50 wei
                              args addr(user[addr(stor19[_param1].field_256)].field_256), eth.balance(stor0)
                          require ext_call.success
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = eth.balance(stor0)
                      if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      if eth.balance(this.address) < stor31:
                          stor22++
                          uint256(stor17C4.field_0) = uint255(stor17C4.field_1)
                          uint256(stor3416.field_0) = uint255(stor3416.field_1)
                          uint256(storEFB5.field_0) = uint255(storEFB5.field_1)
          stop
      if 51 <= uint256(stor117[_param1].field_1280):
          uint256(stor117[_param1].field_1792) = 1
          if uint256(stor117[_param1].field_256):
              require ext_code.size(stor1.length)
              call stor1.length.0x994635c9 with:
                   gas gas_remaining - 50 wei
                  args uint256(stor117[_param1].field_1024) / 10^18, addr(stor19[_param1].field_256)
              require ext_call.success
              if ext_call.return_data[0] > 0:
                  uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                  uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 71
                  uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024) / 10^18
                  if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
          else:
              if eth.balance(stor0):
                  if uint256(stor117[_param1].field_1024) <= eth.balance(stor0):
                      uint256(user[addr(stor19[_param1].field_256)].field_6144) += uint256(stor117[_param1].field_1024)
                      stor10 += uint256(stor117[_param1].field_1024)
                      require ext_code.size(stor1.length)
                      call stor1.length.0x107f5111 with:
                           gas gas_remaining - 50 wei
                          args addr(user[addr(stor19[_param1].field_256)].field_256), uint256(stor117[_param1].field_1024)
                      require ext_call.success
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024)
                  else:
                      uint256(user[addr(stor19[_param1].field_256)].field_6144) += eth.balance(stor0)
                      stor10 += eth.balance(stor0)
                      require ext_code.size(stor1.length)
                      call stor1.length.0x107f5111 with:
                           gas gas_remaining - 50 wei
                          args addr(user[addr(stor19[_param1].field_256)].field_256), eth.balance(stor0)
                      require ext_call.success
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = eth.balance(stor0)
                  if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  if eth.balance(this.address) < stor31:
                      stor22++
                      uint256(stor17C4.field_0) = uint255(stor17C4.field_1)
                      uint256(stor3416.field_0) = uint255(stor3416.field_1)
                      uint256(storEFB5.field_0) = uint255(storEFB5.field_1)
  else:
      if 51 <= uint256(stor117[_param1].field_1536):
          uint256(stor117[_param1].field_1792) = 2
          uint256(user[stor97].field_10496)--
          stor120[_param1][stor97] = 0
          [94midx = 0
          while [94midx < 10:
              if stor101[[94midx]:
                  require [94midx < 10
                  uint256(user[stor101[[94midx]].field_10496)--
                  mem[0] = stor101[[94midx]
                  mem[32] = sha3(_param1, 120)
                  stor120[_param1][stor101[[94midx]] = 0
              [94midx = [94midx + 1
              continue 
          uint256(user[addr(stor19[_param1].field_256)].field_9984) = 0
          stor118 = 0
          [94midx = 0
          while [94midx < stor119.length:
              mem[0] = 119
              if 0 == stor119[[94midx]:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < stor119.length
              require [94midx < stor119.length
              if stor119[[94midx] == stor118:
                  mem[0] = 119
                  stor119[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor118 = stor119[[94midx]
              if 51 <= uint256(stor117[_param1].field_1280):
                  uint256(stor117[_param1].field_1792) = 1
                  if uint256(stor117[_param1].field_256):
                      require ext_code.size(stor1.length)
                      call stor1.length.0x994635c9 with:
                           gas gas_remaining - 50 wei
                          args uint256(stor117[_param1].field_1024) / 10^18, addr(stor19[_param1].field_256)
                      require ext_call.success
                      if ext_call.return_data[0] > 0:
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 71
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024) / 10^18
                          if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  else:
                      if eth.balance(stor0):
                          if uint256(stor117[_param1].field_1024) <= eth.balance(stor0):
                              uint256(user[addr(stor19[_param1].field_256)].field_6144) += uint256(stor117[_param1].field_1024)
                              stor10 += uint256(stor117[_param1].field_1024)
                              require ext_code.size(stor1.length)
                              call stor1.length.0x107f5111 with:
                                   gas gas_remaining - 50 wei
                                  args addr(user[addr(stor19[_param1].field_256)].field_256), uint256(stor117[_param1].field_1024)
                              require ext_call.success
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024)
                          else:
                              uint256(user[addr(stor19[_param1].field_256)].field_6144) += eth.balance(stor0)
                              stor10 += eth.balance(stor0)
                              require ext_code.size(stor1.length)
                              call stor1.length.0x107f5111 with:
                                   gas gas_remaining - 50 wei
                                  args addr(user[addr(stor19[_param1].field_256)].field_256), eth.balance(stor0)
                              require ext_call.success
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                              uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = eth.balance(stor0)
                          if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                              require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          if eth.balance(this.address) < stor31:
                              stor22++
                              uint256(stor17C4.field_0) = uint255(stor17C4.field_1)
                              uint256(stor3416.field_0) = uint255(stor3416.field_1)
                              uint256(storEFB5.field_0) = uint255(storEFB5.field_1)
              stop
          if 51 <= uint256(stor117[_param1].field_1280):
              uint256(stor117[_param1].field_1792) = 1
              if uint256(stor117[_param1].field_256):
                  require ext_code.size(stor1.length)
                  call stor1.length.0x994635c9 with:
                       gas gas_remaining - 50 wei
                      args uint256(stor117[_param1].field_1024) / 10^18, addr(stor19[_param1].field_256)
                  require ext_call.success
                  if ext_call.return_data[0] > 0:
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 71
                      uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024) / 10^18
                      if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
              else:
                  if eth.balance(stor0):
                      if uint256(stor117[_param1].field_1024) <= eth.balance(stor0):
                          uint256(user[addr(stor19[_param1].field_256)].field_6144) += uint256(stor117[_param1].field_1024)
                          stor10 += uint256(stor117[_param1].field_1024)
                          require ext_code.size(stor1.length)
                          call stor1.length.0x107f5111 with:
                               gas gas_remaining - 50 wei
                              args addr(user[addr(stor19[_param1].field_256)].field_256), uint256(stor117[_param1].field_1024)
                          require ext_call.success
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = uint256(stor117[_param1].field_1024)
                      else:
                          uint256(user[addr(stor19[_param1].field_256)].field_6144) += eth.balance(stor0)
                          stor10 += eth.balance(stor0)
                          require ext_code.size(stor1.length)
                          call stor1.length.0x107f5111 with:
                               gas gas_remaining - 50 wei
                              args addr(user[addr(stor19[_param1].field_256)].field_256), eth.balance(stor0)
                          require ext_call.success
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)++
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_256) = 7
                          uint256(unknownfba71153[addr(stor19[_param1].field_256)][uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)].field_512) = eth.balance(stor0)
                      if uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor19[_param1].field_256)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor19', 19))))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      if eth.balance(this.address) < stor31:
                          stor22++
                          uint256(stor17C4.field_0) = uint255(stor17C4.field_1)
                          uint256(stor3416.field_0) = uint255(stor3416.field_1)
                          uint256(storEFB5.field_0) = uint255(storEFB5.field_1)


# hash = 0x7c7a32d2
# getter = None
# const = None
# payable = True
def unknown7c7a32d2(uint256 _param1) payable: 
  mem[64] = 96
  require not call.value
  require calldata.size - 4 >= 32
  if block.timestamp < stor43:
      revert with 0, '15'
  if stor99 != caller:
      revert with 0, '1'
  if stor25:
      if stor3.length <= stor44:
          require stor3.length
          [94midx = stor3.length
          [94ms = 0
          while [94midx:
              if stor3.length == [94ms:
                  stor7 = stor7 + stor25 + stor26
                  stor25 = 0
                  stor26 = 0
                  stor40 = block.timestamp
                  stor43 = stor41 + block.timestamp
                  stop
              require [94midx - 1 < stor3.length
              if _param1 != 2:
                  if [94midx - 1 != stor3.length - 1:
                      call stor2[stor3[[94midx]] with:
                         value stor25 / stor3.length wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      mem[0] = stor2[stor3[[94midx]]
                      mem[32] = 21
                      [94m_320 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_320] = block.timestamp
                      mem[[94m_320 + 32] = 3
                      mem[[94m_320 + 64] = stor25 / stor3.length
                      uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 3
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor25 / stor3.length
                      if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) > stor121:
                          require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = stor2[stor3[[94midx]]
                      mem[32] = 15
                      uint256(user[stor2[stor3[[94midx]]].field_6400) += stor25 / stor3.length
                  else:
                      if _param1 != 1:
                          call stor2[stor3[[94midx]] with:
                             value stor26 wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          uint256(user[stor2[stor3[[94midx]]].field_6400) += stor26
                          mem[0] = stor2[stor3[[94midx]]
                          mem[32] = 21
                          [94m_339 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_339] = block.timestamp
                          mem[[94m_339 + 32] = 8
                          mem[[94m_339 + 64] = stor26
                          uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) <= stor121:
                              call stor2[stor3[[94midx]] with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor2[stor3[[94midx]]
                              mem[32] = 21
                              [94m_444 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_444] = block.timestamp
                              mem[[94m_444 + 32] = 3
                              mem[[94m_444 + 64] = stor25 / stor3.length
                          else:
                              require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor2[stor3[[94midx]] with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor2[stor3[[94midx]]
                              mem[32] = 21
                              [94m_465 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_465] = block.timestamp
                              mem[[94m_465 + 32] = 3
                              mem[[94m_465 + 64] = stor25 / stor3.length
                          uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 3
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor25 / stor3.length
                          if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) > stor121:
                              require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = stor2[stor3[[94midx]]
                          mem[32] = 15
                          uint256(user[stor2[stor3[[94midx]]].field_6400) += stor25 / stor3.length
                      else:
                          call stor97 with:
                             value stor26 wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          uint256(user[stor97].field_6400) += stor26
                          mem[0] = stor97
                          mem[32] = 21
                          [94m_373 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_373] = block.timestamp
                          mem[[94m_373 + 32] = 8
                          mem[[94m_373 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_471 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_471] = block.timestamp
                              mem[[94m_471 + 32] = 3
                              mem[[94m_471 + 64] = stor25 / stor3.length
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_508 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_508] = block.timestamp
                              mem[[94m_508 + 32] = 3
                              mem[[94m_508 + 64] = stor25 / stor3.length
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 3
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor25 / stor3.length
                          if uint256(unknownfba71153[stor97].field_0) > stor121:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = stor97
                          mem[32] = 15
                          uint256(user[stor97].field_6400) += stor25 / stor3.length
              else:
                  if [94midx - 1 != stor3.length - 1:
                      call stor97 with:
                         value stor25 / stor3.length wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      mem[0] = stor97
                      mem[32] = 21
                      [94m_346 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_346] = block.timestamp
                      mem[[94m_346 + 32] = 3
                      mem[[94m_346 + 64] = stor25 / stor3.length
                  else:
                      call stor97 with:
                         value stor26 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      uint256(user[stor97].field_6400) += stor26
                      mem[0] = stor97
                      mem[32] = 21
                      if _param1 != 1:
                          [94m_380 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_380] = block.timestamp
                          mem[[94m_380 + 32] = 8
                          mem[[94m_380 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_477 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_477] = block.timestamp
                              mem[[94m_477 + 32] = 3
                              mem[[94m_477 + 64] = stor25 / stor3.length
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_515 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_515] = block.timestamp
                              mem[[94m_515 + 32] = 3
                              mem[[94m_515 + 64] = stor25 / stor3.length
                      else:
                          [94m_411 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_411] = block.timestamp
                          mem[[94m_411 + 32] = 8
                          mem[[94m_411 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_521 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_521] = block.timestamp
                              mem[[94m_521 + 32] = 3
                              mem[[94m_521 + 64] = stor25 / stor3.length
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor3.length wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_560 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_560] = block.timestamp
                              mem[[94m_560 + 32] = 3
                              mem[[94m_560 + 64] = stor25 / stor3.length
                  uint256(unknownfba71153[stor97].field_0)++
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 3
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor25 / stor3.length
                  if uint256(unknownfba71153[stor97].field_0) > stor121:
                      require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = stor97
                  mem[32] = 15
                  uint256(user[stor97].field_6400) += stor25 / stor3.length
              [94midx = [94midx - 1
              [94ms = [94ms + 1
              continue 
      else:
          require stor44
          [94midx = stor3.length
          [94ms = 0
          while [94midx:
              if stor44 == [94ms:
                  stor7 = stor7 + stor25 + stor26
                  stor25 = 0
                  stor26 = 0
                  stor40 = block.timestamp
                  stor43 = stor41 + block.timestamp
                  stop
              require [94midx - 1 < stor3.length
              if _param1 != 2:
                  if [94midx - 1 != stor3.length - 1:
                      call stor2[stor3[[94midx]] with:
                         value stor25 / stor44 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      mem[0] = stor2[stor3[[94midx]]
                      mem[32] = 21
                      [94m_329 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_329] = block.timestamp
                      mem[[94m_329 + 32] = 3
                      mem[[94m_329 + 64] = stor25 / stor44
                      uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 3
                      uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor25 / stor44
                      if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) > stor121:
                          require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      mem[0] = stor2[stor3[[94midx]]
                      mem[32] = 15
                      uint256(user[stor2[stor3[[94midx]]].field_6400) += stor25 / stor44
                  else:
                      if _param1 != 1:
                          call stor2[stor3[[94midx]] with:
                             value stor26 wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          uint256(user[stor2[stor3[[94midx]]].field_6400) += stor26
                          mem[0] = stor2[stor3[[94midx]]
                          mem[32] = 21
                          [94m_355 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_355] = block.timestamp
                          mem[[94m_355 + 32] = 8
                          mem[[94m_355 + 64] = stor26
                          uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) <= stor121:
                              call stor2[stor3[[94midx]] with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor2[stor3[[94midx]]
                              mem[32] = 21
                              [94m_454 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_454] = block.timestamp
                              mem[[94m_454 + 32] = 3
                              mem[[94m_454 + 64] = stor25 / stor44
                          else:
                              require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor2[stor3[[94midx]] with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor2[stor3[[94midx]]
                              mem[32] = 21
                              [94m_485 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_485] = block.timestamp
                              mem[[94m_485 + 32] = 3
                              mem[[94m_485 + 64] = stor25 / stor44
                          uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)++
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_256) = 3
                          uint256(unknownfba71153[stor2[stor3[[94midx]]][uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)].field_512) = stor25 / stor44
                          if uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) > stor121:
                              require uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor2[stor3[[94midx]]].field_0)) - (3 * stor121) + ('map', ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor3', 3))), ('name', 'stor2', 2))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = stor2[stor3[[94midx]]
                          mem[32] = 15
                          uint256(user[stor2[stor3[[94midx]]].field_6400) += stor25 / stor44
                      else:
                          call stor97 with:
                             value stor26 wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          uint256(user[stor97].field_6400) += stor26
                          mem[0] = stor97
                          mem[32] = 21
                          [94m_390 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_390] = block.timestamp
                          mem[[94m_390 + 32] = 8
                          mem[[94m_390 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_491 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_491] = block.timestamp
                              mem[[94m_491 + 32] = 3
                              mem[[94m_491 + 64] = stor25 / stor44
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_531 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_531] = block.timestamp
                              mem[[94m_531 + 32] = 3
                              mem[[94m_531 + 64] = stor25 / stor44
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 3
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor25 / stor44
                          if uint256(unknownfba71153[stor97].field_0) > stor121:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = stor97
                          mem[32] = 15
                          uint256(user[stor97].field_6400) += stor25 / stor44
              else:
                  if [94midx - 1 != stor3.length - 1:
                      call stor97 with:
                         value stor25 / stor44 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      mem[0] = stor97
                      mem[32] = 21
                      [94m_362 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_362] = block.timestamp
                      mem[[94m_362 + 32] = 3
                      mem[[94m_362 + 64] = stor25 / stor44
                  else:
                      call stor97 with:
                         value stor26 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      uint256(user[stor97].field_6400) += stor26
                      mem[0] = stor97
                      mem[32] = 21
                      if _param1 != 1:
                          [94m_397 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_397] = block.timestamp
                          mem[[94m_397 + 32] = 8
                          mem[[94m_397 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_497 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_497] = block.timestamp
                              mem[[94m_497 + 32] = 3
                              mem[[94m_497 + 64] = stor25 / stor44
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_538 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_538] = block.timestamp
                              mem[[94m_538 + 32] = 3
                              mem[[94m_538 + 64] = stor25 / stor44
                      else:
                          [94m_424 = mem[64]
                          mem[64] = mem[64] + 96
                          mem[[94m_424] = block.timestamp
                          mem[[94m_424 + 32] = 8
                          mem[[94m_424 + 64] = stor26
                          uint256(unknownfba71153[stor97].field_0)++
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 8
                          uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor26
                          if uint256(unknownfba71153[stor97].field_0) <= stor121:
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_544 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_544] = block.timestamp
                              mem[[94m_544 + 32] = 3
                              mem[[94m_544 + 64] = stor25 / stor44
                          else:
                              require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                              call stor97 with:
                                 value stor25 / stor44 wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              mem[0] = stor97
                              mem[32] = 21
                              [94m_576 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_576] = block.timestamp
                              mem[[94m_576 + 32] = 3
                              mem[[94m_576 + 64] = stor25 / stor44
                  uint256(unknownfba71153[stor97].field_0)++
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_256) = 3
                  uint256(unknownfba71153[stor97][uint256(unknownfba71153[stor97].field_0)].field_512) = stor25 / stor44
                  if uint256(unknownfba71153[stor97].field_0) > stor121:
                      require uint256(unknownfba71153[stor97].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor97].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[stor97].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor97', 97)), ('name', 'unknownfba71153', 21))].field_0) = 0
                  mem[0] = stor97
                  mem[32] = 15
                  uint256(user[stor97].field_6400) += stor25 / stor44
              [94midx = [94midx - 1
              [94ms = [94ms + 1
              continue 
      stor7 = stor7 + stor25 + stor26
      stor25 = 0
      stor26 = 0
  stor40 = block.timestamp
  stor43 = stor41 + block.timestamp


# hash = 0x7e01660f
# getter = None
# const = None
# payable = False
def unknown7e01660f(): # not payable
  if uint256(user[caller].field_2816):
      if not uint256(user[caller].field_10752):
          uint256(user[caller].field_10752) = 1
          [94midx = 0
          [94ms = 0
          while [94midx < 4:
              if [94midx >= 3:
                  if not [94ms:
                      uint256(user[caller].field_2816)--
                      uint256(user[caller].field_2560)++
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              mem[0] = [94midx
              mem[32] = 94
              if (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000:
                  if uint256(user[caller].field_2816) >= (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000:
                      uint256(user[caller].field_2816) -= (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000
                      uint256(user[caller].field_2560) += (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000
                      require [94midx < 3
                      require [94midx < 3
                      if uint256(user[caller][[94midx].field_3584) <= (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000:
                          uint256(user[caller][[94midx].field_3584) = 0
                      else:
                          uint256(user[caller][[94midx].field_3584) -= (uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000
                  else:
                      uint256(user[caller].field_2816) = 0
                      uint256(user[caller].field_2560) += uint256(user[caller].field_2816)
                      require [94midx < 3
                      require [94midx < 3
                      if uint256(user[caller][[94midx].field_3584) <= uint256(user[caller].field_2816):
                          uint256(user[caller][[94midx].field_3584) = 0
                      else:
                          uint256(user[caller][[94midx].field_3584) -= uint256(user[caller].field_2816)
              [94midx = [94midx + 1
              [94ms = ((uint256(unknownab47fd76[uint256(stor15[caller].field_2048)].field_256) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknown7879b5ef[[94midx].field_1024) * uint256(user[caller][[94midx].field_3584)) + (uint256(unknowne288fc38[uint256(stor19[uint256(stor15[caller].field_2304)].field_512)].field_256) * uint256(user[caller][[94midx].field_3584)) / 10000) + [94ms
              continue 


# hash = 0x8ae9b92b
# getter = None
# const = None
# payable = True
def unknown8ae9b92b() payable: 
  mem[64] = 96
  require not call.value
  if stor37 > block.timestamp:
      revert with 0, 'SafeMath sub failed'
  if block.timestamp - stor37 < stor38:
      revert with 0, '12'
  [94midx = 0
  while [94midx < stor16.length:
      mem[0] = stor16[[94midx]
      mem[32] = 15
      uint256(user[stor16[[94midx]].field_10752) = 0
      [94midx = [94midx + 1
      continue 
  if not stor36.length:
      stor37 = block.timestamp
      if eth.balance(this.address) <= stor28:
          stor28 = 0
      else:
          if stor28:
              [94midx = 0
              while [94midx < 10:
                  require [94midx < 10
                  if stor101[[94midx]:
                      require [94midx < 10
                      call stor101[[94midx] with:
                         value stor28 / 10 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      require [94midx < 10
                      mem[0] = stor101[[94midx]
                      mem[32] = 21
                      [94m_2411 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_2411] = block.timestamp
                      mem[[94m_2411 + 32] = 6
                      mem[[94m_2411 + 64] = stor28 / 10
                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                          require [94midx < 10
                          mem[0] = stor101[[94midx]
                          mem[32] = 15
                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                          [94midx = [94midx + 1
                          continue 
                      else:
                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          require [94midx < 10
                          mem[0] = stor101[[94midx]
                          mem[32] = 15
                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                          [94midx = [94midx + 1
                          continue 
                  else:
                      call stor98 with:
                         value stor28 / 10 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      mem[0] = stor98
                      mem[32] = 21
                      [94m_2378 = mem[64]
                      mem[64] = mem[64] + 96
                      mem[[94m_2378] = block.timestamp
                      mem[[94m_2378 + 32] = 6
                      mem[[94m_2378 + 64] = stor28 / 10
                      uint256(unknownfba71153[stor98].field_0)++
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_5888) += stor28 / 10
                          [94midx = [94midx + 1
                          continue 
                      else:
                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                          mem[0] = stor98
                          mem[32] = 15
                          uint256(user[stor98].field_5888) += stor28 / 10
                          [94midx = [94midx + 1
                          continue 
              stor28 = 0
  else:
      if stor36.length <= stor39:
          require stor36.length
          [94midx = 0
          while [94midx < stor36.length:
              if 1 >= stor36.length:
                  mem[mem[64]] = 0
                  mem[mem[64] + 32] = [94midx
                  mem[mem[64] + 64] = block.timestamp
                  mem[mem[64] + 96] = stor36.length
                  log 0x911a9e78: 0, idx, block.timestamp, stor36.length
                  require 0 < stor36.length
                  call addr(stor36) with:
                     value stor24 / stor36.length wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require 0 < stor36.length
                  mem[0] = addr(stor36)
                  mem[32] = 21
                  [94m_2385 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_2385] = block.timestamp
                  mem[[94m_2385 + 32] = 2
                  mem[[94m_2385 + 64] = stor24 / stor36.length
                  uint256(unknownfba71153[addr(stor36)].field_0)++
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_256) = 2
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_512) = stor24 / stor36.length
                  if uint256(unknownfba71153[addr(stor36)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor36)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  require 0 < stor36.length
                  mem[0] = addr(stor36)
                  mem[32] = 15
                  uint256(user[addr(stor36)].field_6656) += stor24 / stor36.length
              else:
                  [94m_2351 = mem[64]
                  mem[mem[64] + 32] = block.difficulty
                  mem[mem[64] + 64] = block.timestamp + [94midx
                  if not stor36.length:
                      [94m_2357 = mem[64]
                      mem[mem[64]] = 64
                      mem[64] = mem[64] + 96
                      [94m_2359 = sha3(mem[[94m_2357 + 32 len mem[[94m_2357]])
                      require stor36.length - [94midx
                      mem[[94m_2351 + 96] = sha3(mem[[94m_2357 + 32 len mem[[94m_2357]]) % stor36.length - [94midx
                      mem[[94m_2351 + 192] = stor36.length
                      log 0x911a9e78: mem[_2351 + 96], idx, block.timestamp, stor36.length
                      require [94m_2359 % stor36.length - [94midx < stor36.length
                      call addr(stor36[[94m_2359 % stor36.length - [94midx]) with:
                         value stor24 / stor36.length wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      require [94m_2359 % stor36.length - [94midx < stor36.length
                      mem[64] = [94m_2351 + 192
                      mem[[94m_2351 + 96] = block.timestamp
                      mem[[94m_2351 + 128] = 2
                      mem[[94m_2351 + 160] = stor24 / stor36.length
                      uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)++
                      uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)].field_256) = 2
                      uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)].field_512) = stor24 / stor36.length
                      if uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2359'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2359'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2359'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      require [94m_2359 % stor36.length - [94midx < stor36.length
                      mem[0] = addr(stor36[[94m_2359 % stor36.length - [94midx])
                      mem[32] = 15
                      uint256(user[addr(stor36[[94m_2359 % stor36.length - [94midx])].field_6656) += stor24 / stor36.length
                  else:
                      mem[0] = 36
                      mem[mem[64] + 96] = addr(stor36)
                      [94ms = mem[64] + 96
                      [94mt = sha3(36)
                      while mem[64] + (32 * stor36.length) + 96 > [94ms + 32:
                          mem[[94ms + 32] = stor1[[94mt]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 1
                          continue 
                      [94m_4625 = mem[64]
                      mem[mem[64]] = (32 * stor36.length) + 64
                      mem[64] = mem[64] + (32 * stor36.length) + 96
                      [94m_4627 = sha3(mem[[94m_4625 + 32 len mem[[94m_4625]])
                      require stor36.length - [94midx
                      mem[[94m_2351 + (32 * stor36.length) + 96] = sha3(mem[[94m_4625 + 32 len mem[[94m_4625]]) % stor36.length - [94midx
                      mem[[94m_2351 + (32 * stor36.length) + 192] = stor36.length
                      log 0x911a9e78: mem[_2351 + (32 * stor36.length) + 96], idx, block.timestamp, stor36.length
                      require [94m_4627 % stor36.length - [94midx < stor36.length
                      call addr(stor36[[94m_4627 % stor36.length - [94midx]) with:
                         value stor24 / stor36.length wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      require [94m_4627 % stor36.length - [94midx < stor36.length
                      mem[64] = [94m_2351 + (32 * stor36.length) + 192
                      mem[[94m_2351 + (32 * stor36.length) + 96] = block.timestamp
                      mem[[94m_2351 + (32 * stor36.length) + 128] = 2
                      mem[[94m_2351 + (32 * stor36.length) + 160] = stor24 / stor36.length
                      uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)++
                      uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)].field_256) = 2
                      uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)].field_512) = stor24 / stor36.length
                      if uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4627'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4627'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4627'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      require [94m_4627 % stor36.length - [94midx < stor36.length
                      mem[0] = addr(stor36[[94m_4627 % stor36.length - [94midx])
                      mem[32] = 15
                      uint256(user[addr(stor36[[94m_4627 % stor36.length - [94midx])].field_6656) += stor24 / stor36.length
              [94midx = [94midx + 1
              continue 
          stor8 += stor24
          stor24 = 0
          if not stor12[1] + stor5D60 + storC0DA:
              if not storC0DA + stor5D60:
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2369 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2369 len 128] = code.data[24045 len 128]
                      [94m_2383 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2383] = 0
                      mem[[94m_2383 + 32] = 0
                      mem[[94m_2383 + 64] = 0
                      mem[[94m_2383 + 96] = 0
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3601 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2383]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2383] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3666 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3666] = block.timestamp
                              mem[[94m_3666 + 32] = 28
                              mem[[94m_3666 + 64] = [94m_3601
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3601
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3601
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3601
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2383] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3672 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3672] = block.timestamp
                              mem[[94m_3672 + 32] = 28
                              mem[[94m_3672 + 64] = [94m_3601 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3601 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3939 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3939] = block.timestamp
                                  mem[[94m_3939 + 32] = 28
                                  mem[[94m_3939 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4051 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4051] = block.timestamp
                                  mem[[94m_4051 + 32] = 28
                                  mem[[94m_4051 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5162 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5162] = block.timestamp
                                      mem[[94m_5162 + 32] = 6
                                      mem[[94m_5162 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5050 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5050] = block.timestamp
                                      mem[[94m_5050 + 32] = 6
                                      mem[[94m_5050 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2402 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2402 len 128] = code.data[24045 len 128]
                      [94m_2418 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2418] = 0
                      mem[[94m_2418 + 32] = 0
                      mem[[94m_2418 + 64] = 0
                      mem[[94m_2418 + 96] = stor11 * stor7D7E / storC0DA
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3602 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2418]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2418] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3678 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3678] = block.timestamp
                              mem[[94m_3678 + 32] = 28
                              mem[[94m_3678 + 64] = [94m_3602
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3602
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3602
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3602
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2418] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3684 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3684] = block.timestamp
                              mem[[94m_3684 + 32] = 28
                              mem[[94m_3684 + 64] = [94m_3602 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3602 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3946 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3946] = block.timestamp
                                  mem[[94m_3946 + 32] = 28
                                  mem[[94m_3946 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4058 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4058] = block.timestamp
                                  mem[[94m_4058 + 32] = 28
                                  mem[[94m_4058 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5170 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5170] = block.timestamp
                                      mem[[94m_5170 + 32] = 6
                                      mem[[94m_5170 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5056 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5056] = block.timestamp
                                      mem[[94m_5056 + 32] = 6
                                      mem[[94m_5056 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
              else:
                  require storC0DA + stor5D60
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2403 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2403 len 128] = code.data[24045 len 128]
                      [94m_2419 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2419] = 0
                      mem[[94m_2419 + 32] = 0
                      mem[[94m_2419 + 64] = storE1AC * stor11 / storC0DA + stor5D60
                      mem[[94m_2419 + 96] = storE1AC * stor11 / storC0DA + stor5D60
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3603 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2419]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2419] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3690 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3690] = block.timestamp
                              mem[[94m_3690 + 32] = 28
                              mem[[94m_3690 + 64] = [94m_3603
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3603
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3603
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3603
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2419] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3696 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3696] = block.timestamp
                              mem[[94m_3696 + 32] = 28
                              mem[[94m_3696 + 64] = [94m_3603 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3603 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3953 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3953] = block.timestamp
                                  mem[[94m_3953 + 32] = 28
                                  mem[[94m_3953 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4065 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4065] = block.timestamp
                                  mem[[94m_4065 + 32] = 28
                                  mem[[94m_4065 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5178 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5178] = block.timestamp
                                      mem[[94m_5178 + 32] = 6
                                      mem[[94m_5178 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5062 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5062] = block.timestamp
                                      mem[[94m_5062 + 32] = 6
                                      mem[[94m_5062 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2433 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2433 len 128] = code.data[24045 len 128]
                      [94m_2460 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2460] = 0
                      mem[[94m_2460 + 32] = 0
                      mem[[94m_2460 + 64] = storE1AC * stor11 / storC0DA + stor5D60
                      mem[[94m_2460 + 96] = (stor11 * stor7D7E / storC0DA) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3604 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2460]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2460] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3702 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3702] = block.timestamp
                              mem[[94m_3702 + 32] = 28
                              mem[[94m_3702 + 64] = [94m_3604
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3604
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3604
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3604
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2460] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3708 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3708] = block.timestamp
                              mem[[94m_3708 + 32] = 28
                              mem[[94m_3708 + 64] = [94m_3604 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3604 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3960 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3960] = block.timestamp
                                  mem[[94m_3960 + 32] = 28
                                  mem[[94m_3960 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4072 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4072] = block.timestamp
                                  mem[[94m_4072 + 32] = 28
                                  mem[[94m_4072 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5186 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5186] = block.timestamp
                                      mem[[94m_5186 + 32] = 6
                                      mem[[94m_5186 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5068 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5068] = block.timestamp
                                      mem[[94m_5068 + 32] = 6
                                      mem[[94m_5068 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
          else:
              require storC0DA + stor5D60 + stor12[1]
              if not storC0DA + stor5D60:
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2404 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2404 len 128] = code.data[24045 len 128]
                      [94m_2420 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2420] = 0
                      mem[[94m_2420 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2420 + 64] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2420 + 96] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3605 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2420]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2420] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3714 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3714] = block.timestamp
                              mem[[94m_3714 + 32] = 28
                              mem[[94m_3714 + 64] = [94m_3605
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3605
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3605
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3605
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2420] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3720 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3720] = block.timestamp
                              mem[[94m_3720 + 32] = 28
                              mem[[94m_3720 + 64] = [94m_3605 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3605 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3967 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3967] = block.timestamp
                                  mem[[94m_3967 + 32] = 28
                                  mem[[94m_3967 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4079 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4079] = block.timestamp
                                  mem[[94m_4079 + 32] = 28
                                  mem[[94m_4079 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5194 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5194] = block.timestamp
                                      mem[[94m_5194 + 32] = 6
                                      mem[[94m_5194 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5074 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5074] = block.timestamp
                                      mem[[94m_5074 + 32] = 6
                                      mem[[94m_5074 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2434 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2434 len 128] = code.data[24045 len 128]
                      [94m_2461 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2461] = 0
                      mem[[94m_2461 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2461 + 64] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2461 + 96] = (stor11 * stor7D7E / storC0DA) + (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1])
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3606 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2461]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2461] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3726 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3726] = block.timestamp
                              mem[[94m_3726 + 32] = 28
                              mem[[94m_3726 + 64] = [94m_3606
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3606
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3606
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3606
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2461] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3732 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3732] = block.timestamp
                              mem[[94m_3732 + 32] = 28
                              mem[[94m_3732 + 64] = [94m_3606 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3606 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3974 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3974] = block.timestamp
                                  mem[[94m_3974 + 32] = 28
                                  mem[[94m_3974 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4086 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4086] = block.timestamp
                                  mem[[94m_4086 + 32] = 28
                                  mem[[94m_4086 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5202 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5202] = block.timestamp
                                      mem[[94m_5202 + 32] = 6
                                      mem[[94m_5202 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5080 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5080] = block.timestamp
                                      mem[[94m_5080 + 32] = 6
                                      mem[[94m_5080 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
              else:
                  require storC0DA + stor5D60
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2435 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2435 len 128] = code.data[24045 len 128]
                      [94m_2462 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2462] = 0
                      mem[[94m_2462 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2462 + 64] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      mem[[94m_2462 + 96] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3607 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2462]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2462] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3738 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3738] = block.timestamp
                              mem[[94m_3738 + 32] = 28
                              mem[[94m_3738 + 64] = [94m_3607
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3607
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3607
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3607
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2462] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3744 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3744] = block.timestamp
                              mem[[94m_3744 + 32] = 28
                              mem[[94m_3744 + 64] = [94m_3607 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3607 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3981 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3981] = block.timestamp
                                  mem[[94m_3981 + 32] = 28
                                  mem[[94m_3981 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4093 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4093] = block.timestamp
                                  mem[[94m_4093 + 32] = 28
                                  mem[[94m_4093 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5210 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5210] = block.timestamp
                                      mem[[94m_5210 + 32] = 6
                                      mem[[94m_5210 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5086 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5086] = block.timestamp
                                      mem[[94m_5086 + 32] = 6
                                      mem[[94m_5086 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2484 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2484 len 128] = code.data[24045 len 128]
                      [94m_2504 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2504] = 0
                      mem[[94m_2504 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2504 + 64] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      mem[[94m_2504 + 96] = (stor11 * stor7D7E / storC0DA) + (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3608 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2504]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2504] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3750 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3750] = block.timestamp
                              mem[[94m_3750 + 32] = 28
                              mem[[94m_3750 + 64] = [94m_3608
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3608
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3608
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3608
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2504] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3756 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3756] = block.timestamp
                              mem[[94m_3756 + 32] = 28
                              mem[[94m_3756 + 64] = [94m_3608 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3608 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3988 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3988] = block.timestamp
                                  mem[[94m_3988 + 32] = 28
                                  mem[[94m_3988 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4100 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4100] = block.timestamp
                                  mem[[94m_4100 + 32] = 28
                                  mem[[94m_4100 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5218 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5218] = block.timestamp
                                      mem[[94m_5218 + 32] = 6
                                      mem[[94m_5218 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5092 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5092] = block.timestamp
                                      mem[[94m_5092 + 32] = 6
                                      mem[[94m_5092 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
      else:
          require stor39
          [94midx = 0
          while [94midx < stor39:
              if 1 >= stor36.length:
                  mem[mem[64]] = 0
                  mem[mem[64] + 32] = [94midx
                  mem[mem[64] + 64] = block.timestamp
                  mem[mem[64] + 96] = stor39
                  log 0x911a9e78: 0, idx, block.timestamp, stor39
                  require 0 < stor36.length
                  call addr(stor36) with:
                     value stor24 / stor39 wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require 0 < stor36.length
                  mem[0] = addr(stor36)
                  mem[32] = 21
                  [94m_2394 = mem[64]
                  mem[64] = mem[64] + 96
                  mem[[94m_2394] = block.timestamp
                  mem[[94m_2394 + 32] = 2
                  mem[[94m_2394 + 64] = stor24 / stor39
                  uint256(unknownfba71153[addr(stor36)].field_0)++
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_0) = block.timestamp
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_256) = 2
                  uint256(unknownfba71153[addr(stor36)][uint256(unknownfba71153[addr(stor36)].field_0)].field_512) = stor24 / stor39
                  if uint256(unknownfba71153[addr(stor36)].field_0) > stor121:
                      require uint256(unknownfba71153[addr(stor36)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36)].field_0)
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      uint256(stor[(3 * uint256(unknownfba71153[addr(stor36)].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('name', 'stor36', 36))), ('name', 'unknownfba71153', 21))].field_0) = 0
                  require 0 < stor36.length
                  mem[0] = addr(stor36)
                  mem[32] = 15
                  uint256(user[addr(stor36)].field_6656) += stor24 / stor39
              else:
                  [94m_2354 = mem[64]
                  mem[mem[64] + 32] = block.difficulty
                  mem[mem[64] + 64] = block.timestamp + [94midx
                  if not stor36.length:
                      [94m_2363 = mem[64]
                      mem[mem[64]] = 64
                      mem[64] = mem[64] + 96
                      [94m_2365 = sha3(mem[[94m_2363 + 32 len mem[[94m_2363]])
                      require stor36.length - [94midx
                      mem[[94m_2354 + 96] = sha3(mem[[94m_2363 + 32 len mem[[94m_2363]]) % stor36.length - [94midx
                      mem[[94m_2354 + 192] = stor39
                      log 0x911a9e78: mem[_2354 + 96], idx, block.timestamp, stor39
                      require [94m_2365 % stor36.length - [94midx < stor36.length
                      call addr(stor36[[94m_2365 % stor36.length - [94midx]) with:
                         value stor24 / stor39 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      require [94m_2365 % stor36.length - [94midx < stor36.length
                      mem[64] = [94m_2354 + 192
                      mem[[94m_2354 + 96] = block.timestamp
                      mem[[94m_2354 + 128] = 2
                      mem[[94m_2354 + 160] = stor24 / stor39
                      uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)++
                      uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)].field_256) = 2
                      uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)].field_512) = stor24 / stor39
                      if uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2365'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2365'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_2365'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      require [94m_2365 % stor36.length - [94midx < stor36.length
                      mem[0] = addr(stor36[[94m_2365 % stor36.length - [94midx])
                      mem[32] = 15
                      uint256(user[addr(stor36[[94m_2365 % stor36.length - [94midx])].field_6656) += stor24 / stor39
                  else:
                      mem[0] = 36
                      mem[mem[64] + 96] = addr(stor36)
                      [94ms = mem[64] + 96
                      [94mt = sha3(36)
                      while mem[64] + (32 * stor36.length) + 96 > [94ms + 32:
                          mem[[94ms + 32] = stor1[[94mt]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 1
                          continue 
                      [94m_4628 = mem[64]
                      mem[mem[64]] = (32 * stor36.length) + 64
                      mem[64] = mem[64] + (32 * stor36.length) + 96
                      [94m_4630 = sha3(mem[[94m_4628 + 32 len mem[[94m_4628]])
                      require stor36.length - [94midx
                      mem[[94m_2354 + (32 * stor36.length) + 96] = sha3(mem[[94m_4628 + 32 len mem[[94m_4628]]) % stor36.length - [94midx
                      mem[[94m_2354 + (32 * stor36.length) + 192] = stor39
                      log 0x911a9e78: mem[_2354 + (32 * stor36.length) + 96], idx, block.timestamp, stor39
                      require [94m_4630 % stor36.length - [94midx < stor36.length
                      call addr(stor36[[94m_4630 % stor36.length - [94midx]) with:
                         value stor24 / stor39 wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      require [94m_4630 % stor36.length - [94midx < stor36.length
                      mem[64] = [94m_2354 + (32 * stor36.length) + 192
                      mem[[94m_2354 + (32 * stor36.length) + 96] = block.timestamp
                      mem[[94m_2354 + (32 * stor36.length) + 128] = 2
                      mem[[94m_2354 + (32 * stor36.length) + 160] = stor24 / stor39
                      uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)++
                      uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)].field_0) = block.timestamp
                      uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)].field_256) = 2
                      uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])][uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)].field_512) = stor24 / stor39
                      if uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0) > stor121:
                          require uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4630'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4630'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                          uint256(stor[(3 * uint256(unknownfba71153[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_0)) - (3 * stor121) + ('map', ('type', 160, ('stor', ('array', ('mod', ('var', '_4630'), ('add', ('stor', ('length', ('name', 'stor36', 36))), ('mul', -1, ('var', 0)))), ('name', 'stor36', 36)))), ('name', 'unknownfba71153', 21))].field_0) = 0
                      require [94m_4630 % stor36.length - [94midx < stor36.length
                      mem[0] = addr(stor36[[94m_4630 % stor36.length - [94midx])
                      mem[32] = 15
                      uint256(user[addr(stor36[[94m_4630 % stor36.length - [94midx])].field_6656) += stor24 / stor39
              [94midx = [94midx + 1
              continue 
          stor8 += stor24
          stor24 = 0
          if not stor12[1] + stor5D60 + storC0DA:
              if not storC0DA + stor5D60:
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2373 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2373 len 128] = code.data[24045 len 128]
                      [94m_2392 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2392] = 0
                      mem[[94m_2392 + 32] = 0
                      mem[[94m_2392 + 64] = 0
                      mem[[94m_2392 + 96] = 0
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3609 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2392]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2392] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3762 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3762] = block.timestamp
                              mem[[94m_3762 + 32] = 28
                              mem[[94m_3762 + 64] = [94m_3609
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3609
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3609
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3609
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2392] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3768 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3768] = block.timestamp
                              mem[[94m_3768 + 32] = 28
                              mem[[94m_3768 + 64] = [94m_3609 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3609 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_3995 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_3995] = block.timestamp
                                  mem[[94m_3995 + 32] = 28
                                  mem[[94m_3995 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4107 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4107] = block.timestamp
                                  mem[[94m_4107 + 32] = 28
                                  mem[[94m_4107 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5226 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5226] = block.timestamp
                                      mem[[94m_5226 + 32] = 6
                                      mem[[94m_5226 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5098 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5098] = block.timestamp
                                      mem[[94m_5098 + 32] = 6
                                      mem[[94m_5098 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2406 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2406 len 128] = code.data[24045 len 128]
                      [94m_2423 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2423] = 0
                      mem[[94m_2423 + 32] = 0
                      mem[[94m_2423 + 64] = 0
                      mem[[94m_2423 + 96] = stor11 * stor7D7E / storC0DA
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3610 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2423]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2423] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3774 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3774] = block.timestamp
                              mem[[94m_3774 + 32] = 28
                              mem[[94m_3774 + 64] = [94m_3610
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3610
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3610
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3610
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2423] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3780 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3780] = block.timestamp
                              mem[[94m_3780 + 32] = 28
                              mem[[94m_3780 + 64] = [94m_3610 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3610 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4002 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4002] = block.timestamp
                                  mem[[94m_4002 + 32] = 28
                                  mem[[94m_4002 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4114 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4114] = block.timestamp
                                  mem[[94m_4114 + 32] = 28
                                  mem[[94m_4114 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5234 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5234] = block.timestamp
                                      mem[[94m_5234 + 32] = 6
                                      mem[[94m_5234 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5104 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5104] = block.timestamp
                                      mem[[94m_5104 + 32] = 6
                                      mem[[94m_5104 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
              else:
                  require storC0DA + stor5D60
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2407 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2407 len 128] = code.data[24045 len 128]
                      [94m_2424 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2424] = 0
                      mem[[94m_2424 + 32] = 0
                      mem[[94m_2424 + 64] = storE1AC * stor11 / storC0DA + stor5D60
                      mem[[94m_2424 + 96] = storE1AC * stor11 / storC0DA + stor5D60
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3611 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2424]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2424] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3786 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3786] = block.timestamp
                              mem[[94m_3786 + 32] = 28
                              mem[[94m_3786 + 64] = [94m_3611
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3611
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3611
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3611
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2424] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3792 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3792] = block.timestamp
                              mem[[94m_3792 + 32] = 28
                              mem[[94m_3792 + 64] = [94m_3611 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3611 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4009 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4009] = block.timestamp
                                  mem[[94m_4009 + 32] = 28
                                  mem[[94m_4009 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4121 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4121] = block.timestamp
                                  mem[[94m_4121 + 32] = 28
                                  mem[[94m_4121 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5242 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5242] = block.timestamp
                                      mem[[94m_5242 + 32] = 6
                                      mem[[94m_5242 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5110 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5110] = block.timestamp
                                      mem[[94m_5110 + 32] = 6
                                      mem[[94m_5110 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2447 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2447 len 128] = code.data[24045 len 128]
                      [94m_2467 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2467] = 0
                      mem[[94m_2467 + 32] = 0
                      mem[[94m_2467 + 64] = storE1AC * stor11 / storC0DA + stor5D60
                      mem[[94m_2467 + 96] = (stor11 * stor7D7E / storC0DA) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3612 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2467]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2467] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3798 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3798] = block.timestamp
                              mem[[94m_3798 + 32] = 28
                              mem[[94m_3798 + 64] = [94m_3612
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3612
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3612
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3612
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2467] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3804 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3804] = block.timestamp
                              mem[[94m_3804 + 32] = 28
                              mem[[94m_3804 + 64] = [94m_3612 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3612 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4016 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4016] = block.timestamp
                                  mem[[94m_4016 + 32] = 28
                                  mem[[94m_4016 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4128 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4128] = block.timestamp
                                  mem[[94m_4128 + 32] = 28
                                  mem[[94m_4128 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5250 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5250] = block.timestamp
                                      mem[[94m_5250 + 32] = 6
                                      mem[[94m_5250 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5116 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5116] = block.timestamp
                                      mem[[94m_5116 + 32] = 6
                                      mem[[94m_5116 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
          else:
              require storC0DA + stor5D60 + stor12[1]
              if not storC0DA + stor5D60:
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2408 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2408 len 128] = code.data[24045 len 128]
                      [94m_2425 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2425] = 0
                      mem[[94m_2425 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2425 + 64] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2425 + 96] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3613 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2425]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2425] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3810 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3810] = block.timestamp
                              mem[[94m_3810 + 32] = 28
                              mem[[94m_3810 + 64] = [94m_3613
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3613
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3613
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3613
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2425] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3816 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3816] = block.timestamp
                              mem[[94m_3816 + 32] = 28
                              mem[[94m_3816 + 64] = [94m_3613 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3613 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4023 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4023] = block.timestamp
                                  mem[[94m_4023 + 32] = 28
                                  mem[[94m_4023 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4135 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4135] = block.timestamp
                                  mem[[94m_4135 + 32] = 28
                                  mem[[94m_4135 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5258 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5258] = block.timestamp
                                      mem[[94m_5258 + 32] = 6
                                      mem[[94m_5258 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5122 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5122] = block.timestamp
                                      mem[[94m_5122 + 32] = 6
                                      mem[[94m_5122 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2448 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2448 len 128] = code.data[24045 len 128]
                      [94m_2468 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2468] = 0
                      mem[[94m_2468 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2468 + 64] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2468 + 96] = (stor11 * stor7D7E / storC0DA) + (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1])
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3614 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2468]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2468] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3822 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3822] = block.timestamp
                              mem[[94m_3822 + 32] = 28
                              mem[[94m_3822 + 64] = [94m_3614
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3614
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3614
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3614
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2468] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3828 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3828] = block.timestamp
                              mem[[94m_3828 + 32] = 28
                              mem[[94m_3828 + 64] = [94m_3614 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3614 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4030 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4030] = block.timestamp
                                  mem[[94m_4030 + 32] = 28
                                  mem[[94m_4030 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4142 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4142] = block.timestamp
                                  mem[[94m_4142 + 32] = 28
                                  mem[[94m_4142 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5266 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5266] = block.timestamp
                                      mem[[94m_5266 + 32] = 6
                                      mem[[94m_5266 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5128 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5128] = block.timestamp
                                      mem[[94m_5128 + 32] = 6
                                      mem[[94m_5128 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
              else:
                  require storC0DA + stor5D60
                  mem[0] = 3
                  mem[32] = 12
                  if not storC0DA:
                      [94m_2449 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2449 len 128] = code.data[24045 len 128]
                      [94m_2469 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2469] = 0
                      mem[[94m_2469 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2469 + 64] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      mem[[94m_2469 + 96] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3615 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2469]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2469] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3834 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3834] = block.timestamp
                              mem[[94m_3834 + 32] = 28
                              mem[[94m_3834 + 64] = [94m_3615
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3615
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3615
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3615
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2469] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3840 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3840] = block.timestamp
                              mem[[94m_3840 + 32] = 28
                              mem[[94m_3840 + 64] = [94m_3615 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3615 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4037 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4037] = block.timestamp
                                  mem[[94m_4037 + 32] = 28
                                  mem[[94m_4037 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4149 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4149] = block.timestamp
                                  mem[[94m_4149 + 32] = 28
                                  mem[[94m_4149 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5274 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5274] = block.timestamp
                                      mem[[94m_5274 + 32] = 6
                                      mem[[94m_5274 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5134 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5134] = block.timestamp
                                      mem[[94m_5134 + 32] = 6
                                      mem[[94m_5134 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0
                  else:
                      mem[0] = 3
                      mem[32] = 95
                      require storC0DA
                      [94m_2496 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2496 len 128] = code.data[24045 len 128]
                      [94m_2512 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_2512] = 0
                      mem[[94m_2512 + 32] = stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]
                      mem[[94m_2512 + 64] = (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      mem[[94m_2512 + 96] = (stor11 * stor7D7E / storC0DA) + (stor11 * storB1C7 / storC0DA + stor5D60 + stor12[1]) + (storE1AC * stor11 / storC0DA + stor5D60)
                      [94midx = 0
                      while [94midx < stor17.length:
                          mem[0] = stor17[[94midx]
                          mem[32] = 15
                          require uint256(user[stor17[[94midx]].field_2048) < 4
                          [94m_3616 = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2512]
                          if mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2512] <= uint256(user[stor17[[94midx]].field_3328):
                              mem[0] = stor17[[94midx]
                              mem[32] = 21
                              [94m_3846 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3846] = block.timestamp
                              mem[[94m_3846 + 32] = 28
                              mem[[94m_3846 + 64] = [94m_3616
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = [94m_3616
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += [94m_3616
                              uint256(user[stor17[[94midx]].field_3328) -= [94m_3616
                          else:
                              uint256(user[stor98].field_3072) = mem[(32 * uint256(user[stor17[[94midx]].field_2048)) + [94m_2512] + uint256(user[stor98].field_3072) - uint256(user[stor17[[94midx]].field_3328)
                              mem[0] = stor98
                              mem[32] = 21
                              [94m_3852 = mem[64]
                              mem[64] = mem[64] + 96
                              mem[[94m_3852] = block.timestamp
                              mem[[94m_3852 + 32] = 28
                              mem[[94m_3852 + 64] = [94m_3616 - uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor98].field_0)++
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = [94m_3616 - uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4044 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4044] = block.timestamp
                                  mem[[94m_4044 + 32] = 28
                                  mem[[94m_4044 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              else:
                                  require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  mem[0] = stor17[[94midx]
                                  mem[32] = 21
                                  [94m_4156 = mem[64]
                                  mem[64] = mem[64] + 96
                                  mem[[94m_4156] = block.timestamp
                                  mem[[94m_4156 + 32] = 28
                                  mem[[94m_4156 + 64] = uint256(user[stor17[[94midx]].field_3328)
                              uint256(unknownfba71153[stor17[[94midx]].field_0)++
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_0) = block.timestamp
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_256) = 28
                              uint256(unknownfba71153[stor17[[94midx]][uint256(unknownfba71153[stor17[[94midx]].field_0)].field_512) = uint256(user[stor17[[94midx]].field_3328)
                              if uint256(unknownfba71153[stor17[[94midx]].field_0) > stor121:
                                  require uint256(unknownfba71153[stor17[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor17[[94midx]].field_0)
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                  uint256(stor[(3 * uint256(unknownfba71153[stor17[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor17', 17))), ('name', 'unknownfba71153', 21))].field_0) = 0
                              mem[0] = stor17[[94midx]
                              mem[32] = 15
                              uint256(user[stor17[[94midx]].field_3072) += uint256(user[stor17[[94midx]].field_3328)
                              uint256(user[stor17[[94midx]].field_3328) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor36.length = 0
                      [94midx = 0
                      while stor36.length > [94midx:
                          uint256(stor36[[94midx]) = 0
                          [94midx = [94midx + 1
                          continue 
                      stor11 = 0
                      stor37 = block.timestamp
                      if eth.balance(this.address) <= stor28:
                          stor28 = 0
                      else:
                          if stor28:
                              [94midx = 0
                              while [94midx < 10:
                                  require [94midx < 10
                                  if stor101[[94midx]:
                                      require [94midx < 10
                                      call stor101[[94midx] with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      require [94midx < 10
                                      mem[0] = stor101[[94midx]
                                      mem[32] = 21
                                      [94m_5282 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5282] = block.timestamp
                                      mem[[94m_5282 + 32] = 6
                                      mem[[94m_5282 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor101[[94midx]].field_0)++
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor101[[94midx]][uint256(unknownfba71153[stor101[[94midx]].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor101[[94midx]].field_0) <= stor121:
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor101[[94midx]].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor101[[94midx]].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor101[[94midx]].field_0)) - (3 * stor121) + ('map', ('stor', ('array', ('var', 0), ('name', 'stor101', 101))), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          require [94midx < 10
                                          mem[0] = stor101[[94midx]
                                          mem[32] = 15
                                          uint256(user[stor101[[94midx]].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      call stor98 with:
                                         value stor28 / 10 wei
                                           gas 2300 * is_zero(value) wei
                                      require ext_call.success
                                      mem[0] = stor98
                                      mem[32] = 21
                                      [94m_5140 = mem[64]
                                      mem[64] = mem[64] + 96
                                      mem[[94m_5140] = block.timestamp
                                      mem[[94m_5140 + 32] = 6
                                      mem[[94m_5140 + 64] = stor28 / 10
                                      uint256(unknownfba71153[stor98].field_0)++
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_0) = block.timestamp
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_256) = 6
                                      uint256(unknownfba71153[stor98][uint256(unknownfba71153[stor98].field_0)].field_512) = stor28 / 10
                                      if uint256(unknownfba71153[stor98].field_0) <= stor121:
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          require uint256(unknownfba71153[stor98].field_0) + -stor121 - 1 < uint256(unknownfba71153[stor98].field_0)
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          uint256(stor[(3 * uint256(unknownfba71153[stor98].field_0)) - (3 * stor121) + ('map', ('stor', ('name', 'stor98', 98)), ('name', 'unknownfba71153', 21))].field_0) = 0
                                          mem[0] = stor98
                                          mem[32] = 15
                                          uint256(user[stor98].field_5888) += stor28 / 10
                                          [94midx = [94midx + 1
                                          continue 
                              stor28 = 0


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _tokens): # not payable
  require calldata.size - 4 >= 64
  if _tokens > uint256(user[caller].field_3072):
      return 0
  if _tokens > uint256(user[caller].field_3072):
      revert with 0, 'SafeMath sub failed'
  uint256(user[caller].field_3072) -= _tokens
  if _tokens + uint256(user[_to].field_3072) < uint256(user[_to].field_3072):
      revert with 0, 'SafeMath add failed'
  uint256(user[addr(_to)].field_3072) = _tokens + uint256(user[_to].field_3072)
  return 1


# hash = 0xab47fd76
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 95]]]
# const = None
# payable = False
def unknownab47fd76(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return uint256(unknownab47fd76[_param1].field_0), 
         uint256(unknownab47fd76[_param1].field_256),
         uint256(unknownab47fd76[_param1].field_512)


# hash = 0xb2863aeb
# getter = None
# const = None
# payable = False
def unknownb2863aeb(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  uint256(unknownfba71153[addr(_param1)].field_0)++
  uint256(unknownfba71153[addr(_param1)][uint256(unknownfba71153[addr(_param1)].field_0)].field_0) = block.timestamp
  uint256(unknownfba71153[addr(_param1)][uint256(unknownfba71153[addr(_param1)].field_0)].field_256) = 31
  uint256(unknownfba71153[addr(_param1)][uint256(unknownfba71153[addr(_param1)].field_0)].field_512) = _param2
  if uint256(unknownfba71153[addr(_param1)].field_0) > stor121:
      require uint256(unknownfba71153[addr(_param1)].field_0) + -stor121 - 1 < uint256(unknownfba71153[addr(_param1)].field_0)
      uint256(stor[(3 * uint256(unknownfba71153[addr(_param1)].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, ('param', '_param1')), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(stor[(3 * uint256(unknownfba71153[addr(_param1)].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, ('param', '_param1')), ('name', 'unknownfba71153', 21))].field_0) = 0
      uint256(stor[(3 * uint256(unknownfba71153[addr(_param1)].field_0)) - (3 * stor121) + ('map', ('mask_shl', 160, 0, 0, ('param', '_param1')), ('name', 'unknownfba71153', 21))].field_0) = 0


# hash = 0xd5bf4d4b
# getter = None
# const = None
# payable = False
def unknownd5bf4d4b(): # not payable
  if stor99 != caller:
      stop
  [93mselfdestruct([91mstor98[93m)


# hash = 0xd5da6a2b
# getter = None
# const = None
# payable = False
def unknownd5da6a2b(): # not payable
  return stor6, stor11, stor7, stor8, eth.balance(this.address), stor9, stor114, stor115, stor97, stor118, eth.balance(stor0)


# hash = 0xe12a87cc
# getter = None
# const = None
# payable = False
def unknowne12a87cc(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  mem[32] = 117
  mem[96] = stor117[_param1][2].length
  mem[128] = uint256(stor117[_param1][2].field_0)
  [94midx = 128
  [94ms = 0
  while stor117[_param1][2].length + 96 > [94midx:
      mem[[94midx + 32] = uint256(stor117[_param1][[94ms + 2].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 160
  mem[ceil32(stor117[_param1][2].length) + 128] = stor117[_param1][3].length
  mem[0] = sha3(_param1, 117) + 3
  mem[ceil32(stor117[_param1][2].length) + 160] = uint256(stor117[_param1][3].field_0)
  [94midx = ceil32(stor117[_param1][2].length) + 160
  [94ms = 0
  while ceil32(stor117[_param1][2].length) + stor117[_param1][3].length + 128 > [94midx:
      mem[[94midx + 32] = uint256(stor117[_param1][[94ms + 3].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 160] = uint256(stor117[_param1].field_0)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 192] = uint256(stor117[_param1].field_256)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 288] = uint256(stor117[_param1].field_1024)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 320] = uint256(stor117[_param1].field_1280)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 352] = uint256(stor117[_param1].field_1536)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 384] = uint256(stor117[_param1].field_1792)
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 224] = 256
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 416] = stor117[_param1][2].length
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 448 len ceil32(stor117[_param1][2].length)] = mem[128 len ceil32(stor117[_param1][2].length)]
  mem[ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 256] = stor117[_param1][2].length + 288
  mem[stor117[_param1][2].length + ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 448] = stor117[_param1][3].length
  if stor117[_param1][3].length:
      mem[stor117[_param1][2].length + ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 480] = mem[ceil32(stor117[_param1][2].length) + 160]
      mem[stor117[_param1][2].length + ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 512 len floor32(stor117[_param1][3].length - 1)] = mem[ceil32(stor117[_param1][2].length) + 192 len floor32(stor117[_param1][3].length - 1)]
  if not stor117[_param1][3].length % 32:
      return uint256(stor117[_param1].field_0), 
             uint256(stor117[_param1].field_256),
             Array(len=stor117[_param1][2].length, data=mem[128 len ceil32(stor117[_param1][2].length)], mem[(2 * ceil32(stor117[_param1][2].length)) + ceil32(stor117[_param1][3].length) + 448 len stor117[_param1][3].length + stor117[_param1][2].length + -ceil32(stor117[_param1][2].length) + 32]),
             stor117[_param1][2].length + 288,
             uint256(stor117[_param1].field_1024),
             uint256(stor117[_param1].field_1280),
             uint256(stor117[_param1].field_1536),
             uint256(stor117[_param1].field_1792)
  mem[floor32(stor117[_param1][3].length) + stor117[_param1][2].length + ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + 480] = mem[floor32(stor117[_param1][3].length) + stor117[_param1][2].length + ceil32(stor117[_param1][2].length) + ceil32(stor117[_param1][3].length) + -stor117[_param1][3].length % 32 + 512 len stor117[_param1][3].length % 32]
  return uint256(stor117[_param1].field_0), 
         uint256(stor117[_param1].field_256),
         Array(len=stor117[_param1][2].length, data=mem[128 len ceil32(stor117[_param1][2].length)], mem[(2 * ceil32(stor117[_param1][2].length)) + ceil32(stor117[_param1][3].length) + 448 len floor32(stor117[_param1][3].length) + stor117[_param1][2].length + -ceil32(stor117[_param1][2].length) + 64]),
         stor117[_param1][2].length + 288,
         uint256(stor117[_param1].field_1024),
         uint256(stor117[_param1].field_1280),
         uint256(stor117[_param1].field_1536),
         uint256(stor117[_param1].field_1792)


# hash = 0xe288fc38
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 96]]]
# const = None
# payable = False
def unknowne288fc38(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return uint256(unknowne288fc38[_param1].field_0), uint256(unknowne288fc38[_param1].field_256)


# hash = 0xe42aa81d
# getter = None
# const = None
# payable = False
def unknowne42aa81d(array _param1, array _param2, array _param3): # not payable
  require calldata.size - 4 >= 96
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + _param2.length + 36 <= calldata.size
  require _param3 <= 4294967296
  require _param3 + 36 <= calldata.size
  require _param3.length <= 4294967296 and _param3 + _param3.length + 36 <= calldata.size
  if 1 < uint256(user[caller].field_2048):
      if not uint256(user[caller].field_8960):
          if not uint256(user[caller].field_9216):
              uint256(user[caller].field_9216) = 1
              uint256(stor19[stor20].field_0) = stor20
              addr(stor19[stor20].field_256) = caller
              uint256(stor19[stor20][9][].field_0) = Array(len=_param1.length, data=_param1[all])
              uint256(stor19[stor20][10][].field_0) = Array(len=_param2.length, data=_param2[all])
              uint256(stor19[stor20][11][].field_0) = Array(len=_param3.length, data=_param3[all])
              uint8(stor19[stor20].field_3328) = 1
              uint256(stor19[stor20].field_1536) = 999
              uint256(stor19[stor20].field_1792) = 999
              stor20++


# hash = 0xe7ed54a9
# getter = None
# const = None
# payable = True
def unknowne7ed54a9(array _param1, array _param2, uint256 _param3, uint256 _param4) payable: 
  require calldata.size - 4 >= 128
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + _param2.length + 36 <= calldata.size
  if uint256(user[caller].field_8960) != 1:
      revert with 0, '2'
  uint256(user[caller].field_9984) = 1
  uint256(stor117[uint256(stor15[caller].field_2304)].field_0) = uint256(user[caller].field_2304)
  uint256(stor117[uint256(stor15[caller].field_2304)].field_256) = _param4
  uint256(stor117[uint256(stor15[caller].field_2304)][2][].field_0) = Array(len=_param1.length, data=_param1[all])
  uint256(stor117[uint256(stor15[caller].field_2304)][3][].field_0) = Array(len=_param2.length, data=_param2[all])
  uint256(stor117[uint256(stor15[caller].field_2304)].field_1024) = 10^18 * _param3
  uint256(stor117[uint256(stor15[caller].field_2304)].field_1792) = 0
  uint256(stor117[uint256(stor15[caller].field_2304)].field_1280) = 0
  uint256(stor117[uint256(stor15[caller].field_2304)].field_1536) = 0
  stor119.length++
  stor7901[stor119.length] = uint256(user[caller].field_2304)
  if not stor118:
      stor118 = uint256(user[caller].field_2304)
  uint256(user[stor97].field_10496)++
  [94midx = 0
  while [94midx < 10:
      if stor101[[94midx]:
          require [94midx < 10
          mem[0] = stor101[[94midx]
          mem[32] = 15
          uint256(user[stor101[[94midx]].field_10496)++
      [94midx = [94midx + 1
      continue 


# hash = 0xeb1a9419
# getter = None
# const = None
# payable = False
def unknowneb1a9419(): # not payable
  return stor24, stor37, stor38, stor39, stor25, stor40, stor42, stor43, stor26, stor122, stor123, this.address


# hash = 0xf606841e
# getter = None
# const = None
# payable = False
def agree(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if uint256(user[caller].field_1024):
      if not stor116[_param1][caller]:
          uint256(stor19[_param1].field_3072)++
          stor116[_param1][caller] = 1
          if uint256(stor19[_param1].field_3072) >= stor114:
              uint256(user[addr(stor19[_param1].field_256)].field_8960) = 1
              uint256(user[addr(stor19[_param1].field_256)].field_2304) = _param1


# hash = 0xfba71153
# getter = ['struct', ['loc', 21]]
# const = None
# payable = False
def unknownfba71153(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 < uint256(unknownfba71153[addr(_param2)].field_0)
  require _param1 < uint256(unknownfba71153[addr(_param2)].field_0)
  require _param1 < uint256(unknownfba71153[addr(_param2)].field_0)
  return uint256(unknownfba71153[addr(_param2)][_param1].field_0), 
         uint256(unknownfba71153[addr(_param2)][_param1].field_256),
         uint256(unknownfba71153[addr(_param2)][_param1].field_512)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


