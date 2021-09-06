# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x86F0C0A87699171802FAdCabE2fC3B17EC134993 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x1cdb3a4e': 'unknown1cdb3a4e(?)'} 

# storage definitions
def storage:
    # storage address 0
    tokenAddress # mask: a s
    # storage address 1
    settingsAddress # mask: a s
    # storage address 2
    casinoAddress # mask: a s
    # storage address 3
    tokenHolderAddress # mask: a s
    # storage address 4
    unknown0a6554e9Address # mask: a s
    # storage address 5
    unknowna88379c6 # mask: a s
    # storage address 6
    unknown8209e742 # mask: a s
    # storage address 7
    currentStage # mask: a s
    # storage address 8
    currentCycle # mask: a s
    # storage address 9
    totalStaked # mask: a s
    # storage address 10
    unknown81f83692 # mask: a s
    # storage address 11
    unknownc18df55f # mask: a s
    # storage address 12
    unknown8e7c820c
    # storage address 23
    unknownc563af55
    # storage address 34
    unknowna5b39cfb
    # storage address 35
    unknown624d1b1f
    # storage address 36
    unknown84bcd3c6
    # storage address 37
    unknown7a49f350
    # storage address 38
    unknownf987d986
    # storage address 39
    unknown873426ff
    # storage address 40
    unknown9b1c8ec5
    # storage address 41
    unknown8897c906
    # storage address 42
    unknown3b85bda6
    # storage address 43
    unknown01a32329
    # storage address 44
    unknown7eae0ccb
    # storage address 45
    unknown9f9de645
    # storage address 46684357771790699681650667107281205066648344018449976797659717826852644377516
    stor6736 # mask: a s
# hash = 0x00289ef3
# getter = None
# const = None
# payable = False
def unknown00289ef3(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require mcurrentStage < 11
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mtokenHolderAddress, addr(m_param1), 10^18 * munknownc563af55m[mstor7m]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require mcurrentStage < 11
  if munknown8e7c820cm[mstor7m] < 0 / ext_call.return_data[0]:
      mcurrentStage++
  log 0xa611a711: (10^18 * unknownc563af55[stor7]), _param1


# hash = 0x01a32329
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 43]]]
# const = None
# payable = False
def unknown01a32329(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown01a32329m[m_param1m]


# hash = 0x0365abe7
# getter = None
# const = None
# payable = False
def unknown0365abe7(): # not payable
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require mcurrentStage < 11
  if munknown8e7c820cm[mstor7m] < 0 / ext_call.return_data[0]:
      mcurrentStage++


# hash = 0x05ab421d
# getter = None
# const = None
# payable = False
def sendTokens(address m_to, uint256 m_amount): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mtokenHolderAddress, addr(m_to), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require mcurrentStage < 11
  if munknown8e7c820cm[mstor7m] < 0 / ext_call.return_data[0]:
      mcurrentStage++
  log 0xa611a711: _amount, _to


# hash = 0x084a4faf
# getter = None
# const = None
# payable = False
def unknown084a4faf(): # not payable
  require block.number >= munknown81f83692
  munknown81f83692 = block.number + munknown8209e742
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_8 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_8 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_8 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_8 + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_384 = mem[ceil32(return_data.size) + 96]
  require mem[ceil32(return_data.size) + 96] <= 4294967296
  require mem[ceil32(return_data.size) + 96] + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + [94m_384 + 96]
      [94m_735 = mem[(32 * [94midx) + ceil32(return_data.size) + [94m_384 + 128]
      mem[(2 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
      require ext_code.size(addr([94m_735))
      static call addr([94m_735).0xaefecb5 with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_741 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  mem[(2 * ceil32(return_data.size)) + 96] = 0x610fe55100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
         args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ([94m_741 * ext_call.return_data[0]) + ([94m_379 * ext_call.return_data[0]) <= ext_call.return_data[0]:
      munknownf987d986m[mstor8m] = 0
      mem[(2 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(2 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.getGames() with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mem[(2 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_756 = mem[(2 * ceil32(return_data.size)) + 96]
      require mem[(2 * ceil32(return_data.size)) + 96] <= 4294967296
      require mem[(2 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
      require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 96] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
      [94midx = 0
      [94ms = 0
      mwhile [94midx < ext_call.return_data[0]m:
          require [94midx < mem[(2 * ceil32(return_data.size)) + [94m_756 + 96]
          [94m_1083 = mem[(32 * [94midx) + (2 * ceil32(return_data.size)) + [94m_756 + 128]
          mem[(4 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
          require ext_code.size(addr([94m_1083))
          static call addr([94m_1083).0xaefecb5 with:
                  gas gas_remaining wei
                 args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
          mem[(4 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_1111 = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] + [94ms
          mcontinue 
      mem[0] = mcurrentCycle
      mem[32] = 39
      munknown873426ffm[mstor8m] = [94m_1111 * ext_call.return_data[0]
      mem[(4 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
             args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(4 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.getGames() with:
              gas gas_remaining wei
             args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mem[(4 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
      mem[64] = (6 * ceil32(return_data.size)) + 96
      require return_data.size >= 32
      [94m_1134 = mem[(4 * ceil32(return_data.size)) + 96]
      require mem[(4 * ceil32(return_data.size)) + 96] <= 4294967296
      require mem[(4 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
      require mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(4 * ceil32(return_data.size)) + 96] + (32 * mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
      [94midx = 0
      [94ms = 0
      mwhile [94midx < ext_call.return_data[0]m:
          require [94midx < mem[(4 * ceil32(return_data.size)) + [94m_1134 + 96]
          [94m_1369 = mem[(32 * [94midx) + (4 * ceil32(return_data.size)) + [94m_1134 + 128]
          mem[(6 * ceil32(return_data.size)) + 96] = 0x7952ea9d00000000000000000000000000000000000000000000000000000000
          require ext_code.size(addr([94m_1369))
          static call addr([94m_1369).0x7952ea9d with:
                  gas gas_remaining wei
                 args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
          mem[(6 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_1400 = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] + [94ms
          mcontinue 
      munknown9b1c8ec5m[mstor8m] = [94m_1400 * ext_call.return_data[0]
  else:
      mem[(2 * ceil32(return_data.size)) + 96] = '#n^L'
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.'#n^L' with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ([94m_741 * ext_call.return_data[0]) + ([94m_379 * ext_call.return_data[0]) - ext_call.return_data[0] <= ext_call.return_data[0] + munknownc18df55f:
          munknownf987d986m[mstor8m] = 0
          mem[(2 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(2 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(2 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_782 = mem[(2 * ceil32(return_data.size)) + 96]
          require mem[(2 * ceil32(return_data.size)) + 96] <= 4294967296
          require mem[(2 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
          require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 96] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
          [94midx = 0
          [94ms = 0
          mwhile [94midx < ext_call.return_data[0]m:
              require [94midx < mem[(2 * ceil32(return_data.size)) + [94m_782 + 96]
              [94m_1087 = mem[(32 * [94midx) + (2 * ceil32(return_data.size)) + [94m_782 + 128]
              mem[(4 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
              require ext_code.size(addr([94m_1087))
              static call addr([94m_1087).0xaefecb5 with:
                      gas gas_remaining wei
                     args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
              mem[(4 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1113 = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0] + [94ms
              mcontinue 
          mem[0] = mcurrentCycle
          mem[32] = 39
          munknown873426ffm[mstor8m] = [94m_1113 * ext_call.return_data[0]
          mem[(4 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
                 args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(4 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
                 args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(4 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (6 * ceil32(return_data.size)) + 96
          require return_data.size >= 32
          [94m_1135 = mem[(4 * ceil32(return_data.size)) + 96]
          require mem[(4 * ceil32(return_data.size)) + 96] <= 4294967296
          require mem[(4 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
          require mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(4 * ceil32(return_data.size)) + 96] + (32 * mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
          [94midx = 0
          [94ms = 0
          mwhile [94midx < ext_call.return_data[0]m:
              require [94midx < mem[(4 * ceil32(return_data.size)) + [94m_1135 + 96]
              [94m_1375 = mem[(32 * [94midx) + (4 * ceil32(return_data.size)) + [94m_1135 + 128]
              mem[(6 * ceil32(return_data.size)) + 96] = 0x7952ea9d00000000000000000000000000000000000000000000000000000000
              require ext_code.size(addr([94m_1375))
              static call addr([94m_1375).0x7952ea9d with:
                      gas gas_remaining wei
                     args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
              mem[(6 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1403 = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0] + [94ms
              mcontinue 
          munknown9b1c8ec5m[mstor8m] = [94m_1403 * ext_call.return_data[0]
      else:
          mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ([94m_741 * ext_call.return_data[0]) + ([94m_379 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknownc18df55f <= ext_call.return_data[0]:
              munknownf987d986m[mstor8m] = 0
              mem[(2 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(2 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(2 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_801 = mem[(2 * ceil32(return_data.size)) + 96]
              require mem[(2 * ceil32(return_data.size)) + 96] <= 4294967296
              require mem[(2 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
              require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 96] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
              [94midx = 0
              [94ms = 0
              mwhile [94midx < ext_call.return_data[0]m:
                  require [94midx < mem[(2 * ceil32(return_data.size)) + [94m_801 + 96]
                  [94m_1091 = mem[(32 * [94midx) + (2 * ceil32(return_data.size)) + [94m_801 + 128]
                  mem[(4 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
                  require ext_code.size(addr([94m_1091))
                  static call addr([94m_1091).0xaefecb5 with:
                          gas gas_remaining wei
                         args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
                  mem[(4 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_1115 = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] + [94ms
                  mcontinue 
              mem[0] = mcurrentCycle
              mem[32] = 39
              munknown873426ffm[mstor8m] = [94m_1115 * ext_call.return_data[0]
              mem[(4 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
                     args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(4 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
                     args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(4 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (6 * ceil32(return_data.size)) + 96
              require return_data.size >= 32
              [94m_1136 = mem[(4 * ceil32(return_data.size)) + 96]
              require mem[(4 * ceil32(return_data.size)) + 96] <= 4294967296
              require mem[(4 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
              require mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(4 * ceil32(return_data.size)) + 96] + (32 * mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
              [94midx = 0
              [94ms = 0
              mwhile [94midx < ext_call.return_data[0]m:
                  require [94midx < mem[(4 * ceil32(return_data.size)) + [94m_1136 + 96]
                  [94m_1381 = mem[(32 * [94midx) + (4 * ceil32(return_data.size)) + [94m_1136 + 128]
                  mem[(6 * ceil32(return_data.size)) + 96] = 0x7952ea9d00000000000000000000000000000000000000000000000000000000
                  require ext_code.size(addr([94m_1381))
                  static call addr([94m_1381).0x7952ea9d with:
                          gas gas_remaining wei
                         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
                  mem[(6 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_1406 = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] + [94ms
                  mcontinue 
              munknown9b1c8ec5m[mstor8m] = [94m_1406 * ext_call.return_data[0]
          else:
              mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              munknownf987d986m[mstor8m] = ([94m_741 * ext_call.return_data[0]) + ([94m_379 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f
              mem[(2 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(2 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(2 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_816 = mem[(2 * ceil32(return_data.size)) + 96]
              require mem[(2 * ceil32(return_data.size)) + 96] <= 4294967296
              require mem[(2 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
              require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 96] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
              [94midx = 0
              [94ms = 0
              mwhile [94midx < ext_call.return_data[0]m:
                  require [94midx < mem[(2 * ceil32(return_data.size)) + [94m_816 + 96]
                  [94m_1095 = mem[(32 * [94midx) + (2 * ceil32(return_data.size)) + [94m_816 + 128]
                  mem[(4 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
                  require ext_code.size(addr([94m_1095))
                  static call addr([94m_1095).0xaefecb5 with:
                          gas gas_remaining wei
                         args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
                  mem[(4 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_1117 = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] + [94ms
                  mcontinue 
              mem[0] = mcurrentCycle
              mem[32] = 39
              munknown873426ffm[mstor8m] = [94m_1117 * ext_call.return_data[0]
              mem[(4 * ceil32(return_data.size)) + 96] = 0xdd2f4ebd00000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
                     args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(4 * ceil32(return_data.size)) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
                     args mem[(4 * ceil32(return_data.size)) + 100 len 5 * ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(4 * ceil32(return_data.size)) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (6 * ceil32(return_data.size)) + 96
              require return_data.size >= 32
              [94m_1137 = mem[(4 * ceil32(return_data.size)) + 96]
              require mem[(4 * ceil32(return_data.size)) + 96] <= 4294967296
              require mem[(4 * ceil32(return_data.size)) + 96] + 32 <= return_data.size
              require mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96] <= 4294967296 and mem[(4 * ceil32(return_data.size)) + 96] + (32 * mem[(4 * ceil32(return_data.size)) + mem[(4 * ceil32(return_data.size)) + 96] + 96]) + 32 <= return_data.size
              [94midx = 0
              [94ms = 0
              mwhile [94midx < ext_call.return_data[0]m:
                  require [94midx < mem[(4 * ceil32(return_data.size)) + [94m_1137 + 96]
                  [94m_1387 = mem[(32 * [94midx) + (4 * ceil32(return_data.size)) + [94m_1137 + 128]
                  mem[(6 * ceil32(return_data.size)) + 96] = 0x7952ea9d00000000000000000000000000000000000000000000000000000000
                  require ext_code.size(addr([94m_1387))
                  static call addr([94m_1387).0x7952ea9d with:
                          gas gas_remaining wei
                         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
                  mem[(6 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_1409 = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] + [94ms
                  mcontinue 
              munknown9b1c8ec5m[mstor8m] = [94m_1409 * ext_call.return_data[0]
  mem[(6 * ceil32(return_data.size)) + 96] = 0x610fe55100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown8897c906m[mstor8m] = ext_call.return_data[0]
  mem[(6 * ceil32(return_data.size)) + 96] = '#n^L'
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.'#n^L' with:
          gas gas_remaining wei
         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown3b85bda6m[mstor8m] = ext_call.return_data[0]
  munknown01a32329m[mstor8m] = munknownc18df55f
  mem[(6 * ceil32(return_data.size)) + 100] = mtokenHolderAddress
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress, mem[(6 * ceil32(return_data.size)) + 132 len 9 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(6 * ceil32(return_data.size)) + 96] = 0x18160ddd00000000000000000000000000000000000000000000000000000000
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown7a49f350m[mstor8m] = 0
  munknown7eae0ccbm[mstor8m] = mcurrentStage
  munknown9f9de645m[mstor8m] = mtotalStaked
  mem[(6 * ceil32(return_data.size)) + 96] = 0x18160ddd00000000000000000000000000000000000000000000000000000000
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
         args mem[(6 * ceil32(return_data.size)) + 100 len 8 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require mcurrentStage < 11
  require mcurrentStage < 11
  require mcurrentStage < 11
  require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m]
  require ext_code.size(mcasinoAddress)
  if not mcurrentCycle:
      call mcasinoAddress.0x5815caa with:
           gas gas_remaining wei
          args munknown0a6554e9Address, ((100 * mstor6736) - (munknown8e7c820cm[mstor7m] * mstor6736) / 100) + ((ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100 * mstor6736) - (munknown7a49f350m[mstor8m] * mstor6736) + (munknown9f9de645m[mstor8m] * mstor6736) - (munknown9f9de645m[mstor8m] * mstor6736) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m] * munknown8e7c820cm[mstor7m] / 100), mem[(6 * ceil32(return_data.size)) + 164 len 9 * ceil32(return_data.size)]
  else:
      if munknownf987d986m[mstor8m] <= munknownf987d986m[mstor8 - 1m]:
          call mcasinoAddress.0x5815caa with:
               gas gas_remaining wei
              args munknown0a6554e9Address, 0 / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m] * munknown8e7c820cm[mstor7m] / 100, mem[(6 * ceil32(return_data.size)) + 164 len 9 * ceil32(return_data.size)]
      else:
          call mcasinoAddress.0x5815caa with:
               gas gas_remaining wei
              args munknown0a6554e9Address, ((100 * munknownf987d986m[mstor8m]) - (munknown8e7c820cm[mstor7m] * munknownf987d986m[mstor8m]) - (100 * munknownf987d986m[mstor8 - 1m]) + (munknown8e7c820cm[mstor7m] * munknownf987d986m[mstor8 - 1m]) / 100) + ((ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100 * munknownf987d986m[mstor8m]) - (munknown7a49f350m[mstor8m] * munknownf987d986m[mstor8m]) + (munknown9f9de645m[mstor8m] * munknownf987d986m[mstor8m]) - (munknown9f9de645m[mstor8m] * munknownf987d986m[mstor8m]) - (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100 * munknownf987d986m[mstor8 - 1m]) + (munknown7a49f350m[mstor8m] * munknownf987d986m[mstor8 - 1m]) - (munknown9f9de645m[mstor8m] * munknownf987d986m[mstor8 - 1m]) + (munknown9f9de645m[mstor8m] * munknownf987d986m[mstor8 - 1m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m] * munknown8e7c820cm[mstor7m] / 100), mem[(6 * ceil32(return_data.size)) + 164 len 9 * ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x4878ecf9: currentCycle
  mcurrentCycle++


# hash = 0x0a6554e9
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknown0a6554e9(): # not payable
  return munknown0a6554e9Address


# hash = 0x14794830
# getter = None
# const = None
# payable = False
def unknown14794830(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[addr(m_param1)m]
  mwhile [94midx < m_param2m:
      mem[0] = [94midx
      mem[32] = 45
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      require munknown7eae0ccbm[[94midxm] < 11
      if not [94midx:
          mem[0] = 0
          mem[32] = 38
      else:
          mem[32] = 38
          mem[0] = [94midx
          if munknownf987d986m[[94midxm] > munknownf987d986m[[94midx - 1m]:
              mem[32] = 38
              mem[0] = [94midx
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor44m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  return 0


# hash = 0x246d95ca
# getter = None
# const = None
# payable = False
def unknown246d95ca(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknowna88379c6 = m_param1


# hash = 0x26f35b85
# getter = None
# const = None
# payable = False
def unknown26f35b85(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require m_param1 < 11
  munknownc563af55m[m_param1m] = m_param2


# hash = 0x2e17de78
# getter = None
# const = None
# payable = False
def unknown2e17de78(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require block.number >= munknown624d1b1fm[callerm]
  require m_param1 <= munknowna5b39cfbm[callerm]
  require mcurrentCycle <= mcurrentCycle
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[callerm]
  mwhile [94midx < mcurrentCyclem:
      mem[0] = [94midx
      mem[32] = 45
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      require munknown7eae0ccbm[[94midxm] < 11
      if not [94midx:
          mem[0] = 0
          mem[32] = 38
      else:
          mem[32] = 38
          mem[0] = [94midx
          if munknownf987d986m[[94midxm] > munknownf987d986m[[94midx - 1m]:
              mem[32] = 38
              mem[0] = [94midx
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor44m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require m_param1 <= munknowna5b39cfbm[callerm]
  munknowna5b39cfbm[callerm] -= m_param1
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown84bcd3c6m[callerm] = mcurrentCycle
  mtotalStaked -= m_param1
  log 0x9845e367: _param1, caller


# hash = 0x31e5901b
# getter = None
# const = None
# payable = False
def unknown31e5901b(): # not payable
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_8 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_8 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_8 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_8 + 140 len 20].0xaefecb5 with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  return ([94m_25 * ext_call.return_data[0])


# hash = 0x33ae47ea
# getter = None
# const = None
# payable = False
def unknown33ae47ea(uint256 m_param1, uint256 m_param2, bool m_param3, uint256 m_param4): # not payable
  require calldata.size - 4 >= 224
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xfcddaa0c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.0xd77a3c5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if m_param4 >= 101:
              require m_param3
              require m_param2 - m_param1
              require m_param3
              revert
          else:
              require m_param3
              require m_param2 - m_param1
              require m_param3
              revert


# hash = 0x38c67b73
# getter = None
# const = None
# payable = False
def setCurrentStage(uint256 m_stage): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mcurrentStage = m_stage


# hash = 0x38cff46e
# getter = None
# const = None
# payable = False
def unknown38cff46e(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require m_param1 < 11
  munknown8e7c820cm[m_param1m] = m_param2


# hash = 0x3b85bda6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 42]]]
# const = None
# payable = False
def unknown3b85bda6(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown3b85bda6m[m_param1m]


# hash = 0x3f60f1f3
# getter = None
# const = None
# payable = False
def unknown3f60f1f3(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 <= mcurrentCycle
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[addr(m_param1)m]
  mwhile [94midx < m_param2m:
      mem[0] = [94midx
      mem[32] = 45
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      require munknown7eae0ccbm[[94midxm] < 11
      if not [94midx:
          mem[0] = 0
          mem[32] = 38
      else:
          mem[32] = 38
          mem[0] = [94midx
          if munknownf987d986m[[94midxm] > munknownf987d986m[[94midx - 1m]:
              mem[32] = 38
              mem[0] = [94midx
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor44m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4068ed2b
# getter = None
# const = None
# payable = False
def unknown4068ed2b(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  mem[0] = m_param1
  mem[32] = 34
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not munknowna5b39cfbm[addr(m_param1)m]:
      return 0
  require mcurrentStage < 11
  mem[100] = mtokenHolderAddress
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_23 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_23 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_23 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_23 + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_107 = mem[ceil32(return_data.size) + 96]
  require mem[ceil32(return_data.size) + 96] <= 4294967296
  require mem[ceil32(return_data.size) + 96] + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + [94m_107 + 96]
      [94m_166 = mem[(32 * [94midx) + ceil32(return_data.size) + [94m_107 + 128]
      mem[(2 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
      require ext_code.size(addr([94m_166))
      static call addr([94m_166).0xaefecb5 with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_172 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  mem[(2 * ceil32(return_data.size)) + 96] = 0x610fe55100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
         args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ([94m_172 * ext_call.return_data[0]) + ([94m_102 * ext_call.return_data[0]) <= ext_call.return_data[0]:
      if mcurrentCycle <= 0:
          require mcurrentStage < 11
          require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
          mem[(2 * ceil32(return_data.size)) + 96] = 0 / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
      else:
          if 0 <= munknownf987d986m[mstor8 - 1m]:
              mem[(2 * ceil32(return_data.size)) + 96] = 0
          else:
              require mcurrentStage < 11
              require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
              mem[(2 * ceil32(return_data.size)) + 96] = -1 * munknownf987d986m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m] / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
  else:
      mem[(2 * ceil32(return_data.size)) + 96] = '#n^L'
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.'#n^L' with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ([94m_172 * ext_call.return_data[0]) + ([94m_102 * ext_call.return_data[0]) - ext_call.return_data[0] <= ext_call.return_data[0] + munknownc18df55f:
          if mcurrentCycle <= 0:
              require mcurrentStage < 11
              require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
              mem[(2 * ceil32(return_data.size)) + 96] = 0 / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
          else:
              if 0 <= munknownf987d986m[mstor8 - 1m]:
                  mem[(2 * ceil32(return_data.size)) + 96] = 0
              else:
                  require mcurrentStage < 11
                  require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
                  mem[(2 * ceil32(return_data.size)) + 96] = -1 * munknownf987d986m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m] / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
      else:
          mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ([94m_172 * ext_call.return_data[0]) + ([94m_102 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknownc18df55f <= ext_call.return_data[0]:
              if mcurrentCycle <= 0:
                  require mcurrentStage < 11
                  require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
                  mem[(2 * ceil32(return_data.size)) + 96] = 0 / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
              else:
                  if 0 <= munknownf987d986m[mstor8 - 1m]:
                      mem[(2 * ceil32(return_data.size)) + 96] = 0
                  else:
                      require mcurrentStage < 11
                      require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
                      mem[(2 * ceil32(return_data.size)) + 96] = -1 * munknownf987d986m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m] / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
          else:
              mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if mcurrentCycle <= 0:
                  require mcurrentStage < 11
                  require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
                  mem[(2 * ceil32(return_data.size)) + 96] = ([94m_172 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_102 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
              else:
                  if ([94m_172 * ext_call.return_data[0]) + ([94m_102 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f <= munknownf987d986m[mstor8 - 1m]:
                      mem[(2 * ceil32(return_data.size)) + 96] = 0
                  else:
                      require mcurrentStage < 11
                      require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked
                      mem[(2 * ceil32(return_data.size)) + 96] = ([94m_172 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_102 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownf987d986m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100
  return memory
    from (2 * ceil32(return_data.size)) + 96
     [93mlen ceil32(return_data.size) + 32


# hash = 0x420a83e7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def tokenHolder(): # not payable
  return mtokenHolderAddress


# hash = 0x48d7d9eb
# getter = None
# const = None
# payable = False
def unknown48d7d9eb(): # not payable
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_8 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_8 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_8 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_8 + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_68 = mem[ceil32(return_data.size) + 96]
  require mem[ceil32(return_data.size) + 96] <= 4294967296
  require mem[ceil32(return_data.size) + 96] + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + [94m_68 + 96]
      [94m_103 = mem[(32 * [94midx) + ceil32(return_data.size) + [94m_68 + 128]
      mem[(2 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
      require ext_code.size(addr([94m_103))
      static call addr([94m_103).0xaefecb5 with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_109 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  mem[(2 * ceil32(return_data.size)) + 96] = 0x610fe55100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
         args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ([94m_109 * ext_call.return_data[0]) + ([94m_63 * ext_call.return_data[0]) <= ext_call.return_data[0]:
      mem[(2 * ceil32(return_data.size)) + 96] = 0
  else:
      mem[(2 * ceil32(return_data.size)) + 96] = '#n^L'
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.'#n^L' with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ([94m_109 * ext_call.return_data[0]) + ([94m_63 * ext_call.return_data[0]) - ext_call.return_data[0] <= ext_call.return_data[0] + munknownc18df55f:
          mem[(2 * ceil32(return_data.size)) + 96] = 0
      else:
          mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ([94m_109 * ext_call.return_data[0]) + ([94m_63 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknownc18df55f <= ext_call.return_data[0]:
              mem[(2 * ceil32(return_data.size)) + 96] = 0
          else:
              mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(2 * ceil32(return_data.size)) + 96] = ([94m_109 * ext_call.return_data[0]) + ([94m_63 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f
  return memory
    from (2 * ceil32(return_data.size)) + 96
     [93mlen ceil32(return_data.size) + 32


# hash = 0x5bf5d54c
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def currentStage(): # not payable
  return mcurrentStage


# hash = 0x624d1b1f
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 35]]]
# const = None
# payable = False
def unknown624d1b1f(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown624d1b1fm[m_param1m]


# hash = 0x65e86f0c
# getter = None
# const = None
# payable = False
def unknown65e86f0c(): # not payable
  require mcurrentStage < 11
  return (10^18 * munknownc563af55m[mstor7m])


# hash = 0x7710c6d8
# getter = None
# const = None
# payable = False
def unknown7710c6d8(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown8209e742 = m_param1


# hash = 0x7a49f350
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 37]]]
# const = None
# payable = False
def unknown7a49f350(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown7a49f350m[m_param1m]


# hash = 0x7eae0ccb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 44]]]
# const = None
# payable = False
def unknown7eae0ccb(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown7eae0ccbm[m_param1m]


# hash = 0x817b1cd2
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def totalStaked(): # not payable
  return mtotalStaked


# hash = 0x81f83692
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown81f83692(): # not payable
  return munknown81f83692


# hash = 0x8209e742
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown8209e742(): # not payable
  return munknown8209e742


# hash = 0x84bcd3c6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 36]]]
# const = None
# payable = False
def unknown84bcd3c6(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown84bcd3c6m[m_param1m]


# hash = 0x873426ff
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 39]]]
# const = None
# payable = False
def unknown873426ff(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown873426ffm[m_param1m]


# hash = 0x87e0e9ab
# getter = None
# const = None
# payable = False
def unknown87e0e9ab(): # not payable
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.'#n^L' with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x8897c906
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 41]]]
# const = None
# payable = False
def unknown8897c906(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown8897c906m[m_param1m]


# hash = 0x8e7c820c
# getter = ['storage', 256, 0, ['add', 12, ['cd', 4]]]
# const = None
# payable = False
def unknown8e7c820c(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 11
  return munknown8e7c820cm[m_param1m]


# hash = 0x9403e8dd
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def casino(): # not payable
  return mcasinoAddress


# hash = 0x9b1c8ec5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 40]]]
# const = None
# payable = False
def unknown9b1c8ec5(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown9b1c8ec5m[m_param1m]


# hash = 0x9f9de645
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 45]]]
# const = None
# payable = False
def unknown9f9de645(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown9f9de645m[m_param1m]


# hash = 0xa5b39cfb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 34]]]
# const = None
# payable = False
def unknowna5b39cfb(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknowna5b39cfbm[m_param1m]


# hash = 0xa694fc3a
# getter = None
# const = None
# payable = False
def stake(uint256 m_amount): # not payable
  require calldata.size - 4 >= 32
  require mcurrentCycle <= mcurrentCycle
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[callerm]
  mwhile [94midx < mcurrentCyclem:
      mem[0] = [94midx
      mem[32] = 45
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      require munknown7eae0ccbm[[94midxm] < 11
      if not [94midx:
          mem[0] = 0
          mem[32] = 38
      else:
          mem[32] = 38
          mem[0] = [94midx
          if munknownf987d986m[[94midxm] > munknownf987d986m[[94midx - 1m]:
              mem[32] = 38
              mem[0] = [94midx
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor44m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  munknown624d1b1fm[callerm] = munknowna88379c6 + block.number
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, this.address, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknowna5b39cfbm[callerm] += m_amount
  munknown84bcd3c6m[callerm] = mcurrentCycle
  mtotalStaked += m_amount
  log 0xb539ca1e: _amount, caller


# hash = 0xa88379c6
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknowna88379c6(): # not payable
  return munknowna88379c6


# hash = 0xbab2f552
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def currentCycle(): # not payable
  return mcurrentCycle


# hash = 0xbc105ab5
# getter = None
# const = None
# payable = False
def unknownbc105ab5(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  mem[100] = caller
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0xbd874dff with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x12d15611 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_24 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_24 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_24 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_24 + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_88 = mem[ceil32(return_data.size) + 96]
  require mem[ceil32(return_data.size) + 96] <= 4294967296
  require mem[ceil32(return_data.size) + 96] + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + [94m_88 + 96]
      [94m_127 = mem[(32 * [94midx) + ceil32(return_data.size) + [94m_88 + 128]
      mem[(2 * ceil32(return_data.size)) + 96] = 0xaefecb500000000000000000000000000000000000000000000000000000000
      require ext_code.size(addr([94m_127))
      static call addr([94m_127).0xaefecb5 with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_133 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  mem[(2 * ceil32(return_data.size)) + 96] = 0x610fe55100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
         args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ([94m_133 * ext_call.return_data[0]) + ([94m_83 * ext_call.return_data[0]) <= ext_call.return_data[0]:
      require 0 > ext_call.return_data[0] * ext_call.return_data[0]
  else:
      mem[(2 * ceil32(return_data.size)) + 96] = '#n^L'
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.'#n^L' with:
              gas gas_remaining wei
             args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ([94m_133 * ext_call.return_data[0]) + ([94m_83 * ext_call.return_data[0]) - ext_call.return_data[0] <= ext_call.return_data[0] + munknownc18df55f:
          require 0 > ext_call.return_data[0] * ext_call.return_data[0]
      else:
          mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
                 args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ([94m_133 * ext_call.return_data[0]) + ([94m_83 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknownc18df55f <= ext_call.return_data[0]:
              require 0 > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              mem[(2 * ceil32(return_data.size)) + 96] = 0x397425fb00000000000000000000000000000000000000000000000000000000
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
                     args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ([94m_133 * ext_call.return_data[0]) + ([94m_83 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f > ext_call.return_data[0] * ext_call.return_data[0]
  call m_param1 with:
     value ext_call.return_data[0] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[(2 * ceil32(return_data.size)) + 100] = ext_call.return_data[0]
  require ext_code.size(mcasinoAddress)
  call mcasinoAddress.0xc63e0c05 with:
       gas gas_remaining wei
      args mem[(2 * ceil32(return_data.size)) + 100 len ceil32(return_data.size) + 32]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xc18df55f
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknownc18df55f(): # not payable
  return munknownc18df55f


# hash = 0xc563af55
# getter = ['storage', 256, 0, ['add', 23, ['cd', 4]]]
# const = None
# payable = False
def unknownc563af55(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 11
  return munknownc563af55m[m_param1m]


# hash = 0xcaa9828c
# getter = None
# const = None
# payable = False
def unknowncaa9828c(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown0a6554e9Address = m_param1


# hash = 0xd82cead8
# getter = None
# const = None
# payable = False
def unknownd82cead8(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not m_param1:
      return mstor6736
  if munknownf987d986m[m_param1m] <= munknownf987d986m[m_param1 - 1m]:
      return 0
  return (munknownf987d986m[m_param1m] - munknownf987d986m[m_param1 - 1m])


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def settings(): # not payable
  return msettingsAddress


# hash = 0xe0aecca7
# getter = None
# const = None
# payable = False
def unknowne0aecca7(array m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = 0
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require m_param2 <= mcurrentCycle
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 34
      require ext_code.size(mtokenAddress)
      static call mtokenAddress.totalSupply() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94ms = munknown84bcd3c6m[mem[0]m]
      mwhile [94ms < m_param2m:
          mem[0] = [94ms
          mem[32] = 45
          if not munknown9f9de645m[[94msm]:
              [94ms = [94ms + 1
              mcontinue 
          require munknown7eae0ccbm[[94msm] < 11
          require munknown7eae0ccbm[[94msm] < 11
          if not [94ms:
              mem[0] = 0
              mem[32] = 38
          else:
              mem[32] = 38
              mem[0] = [94ms
              if munknownf987d986m[[94msm] > munknownf987d986m[[94ms - 1m]:
                  mem[32] = 38
                  mem[0] = [94ms
          require (ext_call.return_data[0] * munknown8e7c820cm[mstor44m[[94msm]m] / 100) - munknown7a49f350m[[94msm] + munknown9f9de645m[[94msm]
          [94ms = [94ms + 1
          mcontinue 
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xe239b026
# getter = None
# const = None
# payable = False
def unknowne239b026(): # not payable
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_8 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[[94m_8 + 96]
      require ext_code.size(mem[(32 * [94midx) + [94m_8 + 140 len 20])
      static call mem[(32 * [94midx) + [94m_8 + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  return ([94m_25 * ext_call.return_data[0])


# hash = 0xf145ff23
# getter = None
# const = None
# payable = False
def getDistributedTokens(): # not payable
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mtokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 0


# hash = 0xf987d986
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 38]]]
# const = None
# payable = False
def unknownf987d986(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknownf987d986m[m_param1m]


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def token(): # not payable
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


