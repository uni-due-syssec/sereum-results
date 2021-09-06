# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x60E244446bEe3fb2fAd04D7eAaDef093f2ad0d24 
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
    unknown3767377e # mask: a s
    # storage address 13
    unknown8e7c820c
    # storage address 24
    unknownc563af55
    # storage address 35
    stor35
    # storage address 36
    unknowna5b39cfb
    # storage address 37
    unknown624d1b1f
    # storage address 38
    unknown84bcd3c6
    # storage address 39
    unknown7a49f350
    # storage address 40
    unknowna1825b6a
    # storage address 41
    unknown873426ff
    # storage address 42
    unknown9b1c8ec5
    # storage address 43
    unknown8897c906
    # storage address 44
    unknown3b85bda6
    # storage address 45
    unknown01a32329
    # storage address 46
    unknown7eae0ccb
    # storage address 47
    unknown9f9de645
# hash = 0x00289ef3
# getter = None
# const = None
# payable = True
def unknown00289ef3(addr m_param1) payable: 
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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 45]]]
# const = None
# payable = True
def unknown01a32329(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown01a32329m[m_param1m]


# hash = 0x0365abe7
# getter = None
# const = None
# payable = True
def unknown0365abe7() payable: 
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
# payable = True
def sendTokens(address m_to, uint256 m_amount) payable: 
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
# payable = True
def unknown084a4faf() payable: 
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
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  [94m_11 = mem[[94m_8 + 96]
  mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_8 + 96])] = mem[[94m_8 + 128 len floor32(mem[[94m_8 + 96])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
      static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
              gas gas_remaining wei
      mem[(32 * [94m_11) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_2757 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  mem[0] = mcurrentCycle
  mem[32] = 41
  munknown873426ffm[mstor8m] = [94m_2757 * ext_call.return_data[0]
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_11) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[(32 * [94m_11) + ceil32(return_data.size) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (32 * [94m_11) + (2 * ceil32(return_data.size)) + 128
  require return_data.size >= 32
  [94m_2762 = mem[(32 * [94m_11) + ceil32(return_data.size) + 128]
  require mem[(32 * [94m_11) + ceil32(return_data.size) + 128] <= 4294967296
  require mem[(32 * [94m_11) + ceil32(return_data.size) + 128] + 32 <= return_data.size
  require mem[(32 * [94m_11) + ceil32(return_data.size) + mem[(32 * [94m_11) + ceil32(return_data.size) + 128] + 128] <= 4294967296 and mem[(32 * [94m_11) + ceil32(return_data.size) + 128] + (32 * mem[(32 * [94m_11) + ceil32(return_data.size) + mem[(32 * [94m_11) + ceil32(return_data.size) + 128] + 128]) + 32 <= return_data.size
  mem[(32 * [94m_11) + (2 * ceil32(return_data.size)) + 128] = mem[(32 * [94m_11) + ceil32(return_data.size) + mem[(32 * [94m_11) + ceil32(return_data.size) + 128] + 128]
  [94m_2765 = mem[(32 * [94m_11) + ceil32(return_data.size) + [94m_2762 + 128]
  mem[(32 * [94m_11) + (2 * ceil32(return_data.size)) + 160 len floor32(mem[(32 * [94m_11) + ceil32(return_data.size) + [94m_2762 + 128])] = mem[(32 * [94m_11) + ceil32(return_data.size) + [94m_2762 + 160 len floor32(mem[(32 * [94m_11) + ceil32(return_data.size) + [94m_2762 + 128])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[(32 * [94m_11) + (2 * ceil32(return_data.size)) + 128]
      require ext_code.size(mem[(32 * [94midx) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 172 len 20])
      static call mem[(32 * [94midx) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 172 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_5475 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  munknown9b1c8ec5m[mstor8m] = [94m_5475 * ext_call.return_data[0]
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown8897c906m[mstor8m] = ext_call.return_data[0]
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown3b85bda6m[mstor8m] = ext_call.return_data[0]
  munknown01a32329m[mstor8m] = munknownc18df55f
  mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 164] = mtokenHolderAddress
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
  munknown7a49f350m[mstor8m] = 0
  munknown7eae0ccbm[mstor8m] = mcurrentStage
  mem[0] = mcurrentCycle
  mem[32] = 47
  munknown9f9de645m[mstor8m] = mtotalStaked
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  mstor35m[mstor8m] = 0
                  munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - munknown873426ffm[mstor8m]
              else:
                  mstor35m[mstor8m] = 1
                  munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
          else:
              if mstor35m[mstor8 - 1m]:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m]
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
              else:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m]
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
      else:
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  mstor35m[mstor8m] = 0
                  munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - munknown873426ffm[mstor8m]
              else:
                  mstor35m[mstor8m] = 1
                  munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
          else:
              if mstor35m[mstor8 - 1m]:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m]
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
              else:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m]
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
  else:
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.getGames() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160 len return_data.size] = ext_call.return_data[0 len return_data.size]
      mem[64] = (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 160
      require return_data.size >= 32
      [94m_5504 = mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160]
      require mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] <= 4294967296
      require mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] + 32 <= return_data.size
      require mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] + 160] <= 4294967296 and mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] + (32 * mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] + 160]) + 32 <= return_data.size
      mem[(32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 160] = mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] + 160]
      [94m_5508 = mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + [94m_5504 + 160]
      mem[(32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192 len floor32(mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + [94m_5504 + 160])] = mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + [94m_5504 + 192 len floor32(mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + [94m_5504 + 160])]
      [94midx = 0
      [94ms = 0
      mwhile [94midx < ext_call.return_data[0]m:
          require [94midx < mem[(32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 160]
          require ext_code.size(mem[(32 * [94midx) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 204 len 20])
          static call mem[(32 * [94midx) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 204 len 20].0xaefecb5 with:
                  gas gas_remaining wei
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_7914 = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] + [94ms
          mcontinue 
      if mcurrentCycle != mcurrentCycle:
          if munknown3767377e != mcurrentCycle:
              if not mcurrentCycle:
                  if munknown9b1c8ec5m[mstor8m] + ([94m_7914 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - ([94m_7914 * ext_call.return_data[0])
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] + ([94m_7914 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
              else:
                  if mstor35m[mstor8 - 1m]:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
                  else:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not mcurrentCycle:
                  if munknown9b1c8ec5m[mstor8m] + ([94m_7914 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                      mstor35m[mstor8m] = 0
                      munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - ([94m_7914 * ext_call.return_data[0])
                  else:
                      mstor35m[mstor8m] = 1
                      munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] + ([94m_7914 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
              else:
                  if mstor35m[mstor8 - 1m]:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
                  else:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 192
          require return_data.size >= 32
          [94m_7922 = mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192]
          require mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] <= 4294967296
          require mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] + 32 <= return_data.size
          require mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] + 192] <= 4294967296 and mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] + (32 * mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] + 192]) + 32 <= return_data.size
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 192] = mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] + 192]
          [94m_7927 = mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + [94m_7922 + 192]
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 224 len floor32(mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + [94m_7922 + 192])] = mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + [94m_7922 + 224 len floor32(mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + [94m_7922 + 192])]
          [94midx = 0
          [94ms = 0
          mwhile [94midx < ext_call.return_data[0]m:
              require [94midx < mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 192]
              require ext_code.size(mem[(32 * [94midx) + (32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 236 len 20])
              static call mem[(32 * [94midx) + (32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 236 len 20].0x7952ea9d with:
                      gas gas_remaining wei
              mem[(32 * [94m_7927) + (32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (6 * ceil32(return_data.size)) + 224] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_9868 = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0] + [94ms
              mcontinue 
          if mcurrentCycle != mcurrentCycle:
              if munknown3767377e != mcurrentCycle:
                  if not mcurrentCycle:
                      if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
                  else:
                      if mstor35m[mstor8 - 1m]:
                          if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
                      else:
                          if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not mcurrentCycle:
                      if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                          mstor35m[mstor8m] = 0
                          munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                      else:
                          mstor35m[mstor8m] = 1
                          munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m]
                  else:
                      if mstor35m[mstor8 - 1m]:
                          if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
                      else:
                          if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m]
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if mcurrentCycle != mcurrentCycle:
                  if munknown3767377e != mcurrentCycle:
                      if not mcurrentCycle:
                          if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - ext_call.return_data[0]
                      else:
                          if mstor35m[mstor8 - 1m]:
                              if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m]
                          else:
                              if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m]
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not mcurrentCycle:
                          if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m]:
                              mstor35m[mstor8m] = 0
                              munknowna1825b6am[mstor8m] = (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                          else:
                              mstor35m[mstor8m] = 1
                              munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m]
                      else:
                          if mstor35m[mstor8 - 1m]:
                              if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                          else:
                              if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if mcurrentCycle == mcurrentCycle:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = munknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - munknownc18df55f - (2 * ext_call.return_data[0])
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = (3 * ext_call.return_data[0]) + munknownc18df55f - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                  else:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0]):
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0]) - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - (2 * ext_call.return_data[0])
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m]:
                                  mstor35m[mstor8m] = 0
                                  munknowna1825b6am[mstor8m] = (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  mstor35m[mstor8m] = 1
                                  munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m]
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      mstor35m[mstor8m] = 0
                                      munknowna1825b6am[mstor8m] = munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_9868 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_7914 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m]
                                  else:
                                      mstor35m[mstor8m] = 1
                                      munknowna1825b6am[mstor8m] = ([94m_9868 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_7914 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m]
  if mstor35m[mstor8m]:
      require ext_code.size(mtokenAddress)
      static call mtokenAddress.totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require mcurrentStage < 11
      require mcurrentStage < 11
      require mcurrentStage < 11
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m]
      require ext_code.size(mcasinoAddress)
      call mcasinoAddress.0x5815caa with:
           gas gas_remaining wei
          args munknown0a6554e9Address, ((100 * munknowna1825b6am[mstor8m]) - (munknown8e7c820cm[mstor7m] * munknowna1825b6am[mstor8m]) / 100) + ((ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100 * munknowna1825b6am[mstor8m]) - (munknown7a49f350m[mstor8m] * munknowna1825b6am[mstor8m]) + (munknown9f9de645m[mstor8m] * munknowna1825b6am[mstor8m]) - (munknown9f9de645m[mstor8m] * munknowna1825b6am[mstor8m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) - munknown7a49f350m[mstor8m] + munknown9f9de645m[mstor8m] * munknown8e7c820cm[mstor7m] / 100)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0x4878ecf9: currentCycle
  mcurrentCycle++


# hash = 0x0a6554e9
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def unknown0a6554e9() payable: 
  return munknown0a6554e9Address


# hash = 0x14794830
# getter = None
# const = None
# payable = True
def unknown14794830(addr m_param1, uint256 m_param2) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 64
  mem[0] = m_param1
  mem[32] = 36
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[addr(m_param1)m]
  mwhile [94midx < m_param2m:
      mem[0] = [94midx
      mem[32] = 47
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != mcurrentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if munknown3767377e != [94midx:
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_231 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_233 = mem[[94m_231]
          require mem[[94m_231] <= 4294967296
          require mem[[94m_231] + 32 <= return_data.size
          require mem[[94m_231 + mem[[94m_231]] <= 4294967296 and mem[[94m_231] + (32 * mem[[94m_231 + mem[[94m_231]]) + 32 <= return_data.size
          mem[[94m_231 + ceil32(return_data.size)] = mem[[94m_231 + mem[[94m_231]]
          [94m_237 = mem[[94m_231 + [94m_233]
          [94ms = 0
          mwhile [94ms < 32 * [94m_237m:
              mem[[94ms + [94m_231 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_231 + [94m_233 + 32]
              [94ms = [94ms + 32
              mcontinue 
          mem[64] = (32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          mwhile [94ms < ext_call.return_data[0]m:
              require [94ms < mem[[94m_231 + ceil32(return_data.size)]
              require ext_code.size(mem[(32 * [94ms) + [94m_231 + ceil32(return_data.size) + 44 len 20])
              static call mem[(32 * [94ms) + [94m_231 + ceil32(return_data.size) + 44 len 20].0xaefecb5 with:
                      gas gas_remaining wei
              mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_597 = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mt = ext_call.return_data[0] + [94mt
              mcontinue 
          if [94midx != mcurrentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if munknown3767377e != [94midx:
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_597 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_597 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
          else:
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 32
              require return_data.size >= 32
              [94m_605 = mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32]
              require mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] <= 4294967296
              require mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] + 32 <= return_data.size
              require mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] + 32] <= 4294967296 and mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] + (32 * mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] + 32]) + 32 <= return_data.size
              mem[(32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 32] = mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] + 32]
              [94m_610 = mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + [94m_605 + 32]
              [94ms = 0
              mwhile [94ms < 32 * [94m_610m:
                  mem[[94ms + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_237) + [94m_231 + ceil32(return_data.size) + [94m_605 + 64]
                  [94ms = [94ms + 32
                  mcontinue 
              mem[64] = (32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              mwhile [94ms < ext_call.return_data[0]m:
                  require [94ms < mem[(32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 32]
                  require ext_code.size(mem[(32 * [94ms) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 76 len 20])
                  static call mem[(32 * [94ms) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 76 len 20].0x7952ea9d with:
                          gas gas_remaining wei
                  mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_877 = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mt = ext_call.return_data[0] + [94mt
                  mcontinue 
              if [94midx != mcurrentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if munknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != mcurrentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if munknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == mcurrentCycle:
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_597 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
      mem[0] = [94midx
      mem[32] = 46
      require munknown7eae0ccbm[[94midxm] < 11
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor46m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  return 0


# hash = 0x15344630
# getter = None
# const = None
# payable = True
def unknown15344630() payable: 
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  return munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - munknown873426ffm[mstor8m], 
                         0
              return munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                     1
          if mstor35m[mstor8 - 1m]:
              if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                  return munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m], 
                         0
              return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                     1
          if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m], 
                     0
          return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not mcurrentCycle:
          if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - munknown873426ffm[mstor8m], 
                     0
          return munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                 1
      if mstor35m[mstor8 - 1m]:
          if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m], 
                     0
          return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - munknown873426ffm[mstor8m] + munknown873426ffm[mstor8 - 1m], 
                 0
      return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
             1
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
  [94m_12 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  [94m_16 = mem[[94m_12 + 96]
  mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_12 + 96])] = mem[[94m_12 + 128 len floor32(mem[[94m_12 + 96])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
      static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
              gas gas_remaining wei
      mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_574 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  return munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - ([94m_574 * ext_call.return_data[0]), 
                         0
              return munknown9b1c8ec5m[mstor8m] + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                     1
          if mstor35m[mstor8 - 1m]:
              if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                  return munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                         0
              return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                     1
          if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not mcurrentCycle:
          if munknown9b1c8ec5m[mstor8m] + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - munknown9b1c8ec5m[mstor8m] - ([94m_574 * ext_call.return_data[0]), 
                     0
          return munknown9b1c8ec5m[mstor8m] + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                 1
      if mstor35m[mstor8 - 1m]:
          if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - munknown9b1c8ec5m[mstor8m] + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
             1
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (32 * [94m_16) + (2 * ceil32(return_data.size)) + 128
  require return_data.size >= 32
  [94m_582 = mem[(32 * [94m_16) + ceil32(return_data.size) + 128]
  require mem[(32 * [94m_16) + ceil32(return_data.size) + 128] <= 4294967296
  require mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 32 <= return_data.size
  require mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128] <= 4294967296 and mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + (32 * mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128]) + 32 <= return_data.size
  mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 128] = mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128]
  [94m_587 = mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128]
  mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 160 len floor32(mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128])] = mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 160 len floor32(mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 128]
      require ext_code.size(mem[(32 * [94midx) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 172 len 20])
      static call mem[(32 * [94midx) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 172 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[(32 * [94m_587) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_1016 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  return munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                     1
          if mstor35m[mstor8 - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                  return munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not mcurrentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m], 
                 1
      if mstor35m[mstor8 - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0]:
                  return munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - ext_call.return_data[0], 
                     1
          if mstor35m[mstor8 - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
                  return munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
              return munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not mcurrentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m]:
              return (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m], 
                 1
      if mstor35m[mstor8 - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
              return (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mcurrentCycle == mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                  return munknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknownc18df55f - (2 * ext_call.return_data[0]), 
                     1
          if mstor35m[mstor8 - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                  return munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
              return munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not mcurrentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
              return (3 * ext_call.return_data[0]) + munknownc18df55f - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f, 
                 1
      if mstor35m[mstor8 - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
              return (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
             1
  if munknown3767377e != mcurrentCycle:
      if not mcurrentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0]):
              return munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - (2 * ext_call.return_data[0]), 
                 1
      if mstor35m[mstor8 - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
              return munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
          return munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not mcurrentCycle:
      if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m]:
          return (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                 0
      return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m], 
             1
  if mstor35m[mstor8 - 1m]:
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
          return (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
             1
  if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
      return munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[mstor8 - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[mstor8 - 1m], 
             0
  return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m], 
         1


# hash = 0x246d95ca
# getter = None
# const = None
# payable = True
def unknown246d95ca(uint256 m_param1) payable: 
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


# hash = 0x2623f687
# getter = None
# const = None
# payable = True
def getRevenue(uint256 m_amount) payable: 
  require calldata.size - 4 >= 32
  if m_amount != mcurrentCycle:
      if munknown3767377e != m_amount:
          if not m_amount:
              if munknown9b1c8ec5m[m_amountm] + munknown873426ffm[m_amountm] <= munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
                  return munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - munknown9b1c8ec5m[m_amountm] - munknown873426ffm[m_amountm], 
                         0
              return munknown9b1c8ec5m[m_amountm] + munknown873426ffm[m_amountm] - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                     1
          if mstor35m[m_amount - 1m]:
              if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] <= munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
                  return munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - munknown873426ffm[m_amountm] + munknown873426ffm[m_amount - 1m], 
                         0
              return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                     1
          if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - munknown873426ffm[m_amountm] + munknown873426ffm[m_amount - 1m], 
                     0
          return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not m_amount:
          if munknown9b1c8ec5m[m_amountm] + munknown873426ffm[m_amountm] <= ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - munknown9b1c8ec5m[m_amountm] - munknown873426ffm[m_amountm], 
                     0
          return munknown9b1c8ec5m[m_amountm] + munknown873426ffm[m_amountm] - ext_call.return_data[0] - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                 1
      if mstor35m[m_amount - 1m]:
          if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] <= ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - munknown873426ffm[m_amountm] + munknown873426ffm[m_amount - 1m], 
                     0
          return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - munknown873426ffm[m_amountm] + munknown873426ffm[m_amount - 1m], 
                 0
      return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + munknown873426ffm[m_amountm] - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
             1
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
  [94m_12 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  [94m_16 = mem[[94m_12 + 96]
  mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_12 + 96])] = mem[[94m_12 + 128 len floor32(mem[[94m_12 + 96])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
      static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
              gas gas_remaining wei
      mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_574 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  if m_amount != mcurrentCycle:
      if munknown3767377e != m_amount:
          if not m_amount:
              if munknown9b1c8ec5m[m_amountm] + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
                  return munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - munknown9b1c8ec5m[m_amountm] - ([94m_574 * ext_call.return_data[0]), 
                         0
              return munknown9b1c8ec5m[m_amountm] + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                     1
          if mstor35m[m_amount - 1m]:
              if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
                  return munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                         0
              return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                     1
          if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not m_amount:
          if munknown9b1c8ec5m[m_amountm] + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - munknown9b1c8ec5m[m_amountm] - ([94m_574 * ext_call.return_data[0]), 
                     0
          return munknown9b1c8ec5m[m_amountm] + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                 1
      if mstor35m[m_amount - 1m]:
          if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      if munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - munknown9b1c8ec5m[m_amountm] + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return munknown9b1c8ec5m[m_amountm] - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
             1
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.getGames() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (32 * [94m_16) + (2 * ceil32(return_data.size)) + 128
  require return_data.size >= 32
  [94m_582 = mem[(32 * [94m_16) + ceil32(return_data.size) + 128]
  require mem[(32 * [94m_16) + ceil32(return_data.size) + 128] <= 4294967296
  require mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 32 <= return_data.size
  require mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128] <= 4294967296 and mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + (32 * mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128]) + 32 <= return_data.size
  mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 128] = mem[(32 * [94m_16) + ceil32(return_data.size) + mem[(32 * [94m_16) + ceil32(return_data.size) + 128] + 128]
  [94m_587 = mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128]
  mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 160 len floor32(mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128])] = mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 160 len floor32(mem[(32 * [94m_16) + ceil32(return_data.size) + [94m_582 + 128])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[(32 * [94m_16) + (2 * ceil32(return_data.size)) + 128]
      require ext_code.size(mem[(32 * [94midx) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 172 len 20])
      static call mem[(32 * [94midx) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 172 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[(32 * [94m_587) + (32 * [94m_16) + (2 * ceil32(return_data.size)) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_1016 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  if m_amount != mcurrentCycle:
      if munknown3767377e != m_amount:
          if not m_amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
                  return munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                     1
          if mstor35m[m_amount - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
                  return munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not m_amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + munknown8897c906m[m_amountm] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - munknown8897c906m[m_amountm], 
                 1
      if mstor35m[m_amount - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
              return ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + ext_call.return_data[0] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amountm] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - ext_call.return_data[0] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amountm] + munknown8897c906m[m_amount - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_amount != mcurrentCycle:
      if munknown3767377e != m_amount:
          if not m_amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + ext_call.return_data[0]:
                  return munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] + ext_call.return_data[0] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm] - ext_call.return_data[0], 
                     1
          if mstor35m[m_amount - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + ext_call.return_data[0] - munknown8897c906m[m_amount - 1m]:
                  return munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + ext_call.return_data[0] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - ext_call.return_data[0] + munknown8897c906m[m_amount - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + ext_call.return_data[0] - munknown8897c906m[m_amount - 1m]:
              return munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] + ext_call.return_data[0] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] - ext_call.return_data[0] + munknown8897c906m[m_amount - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not m_amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm]:
              return (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] + munknown3b85bda6m[m_amountm] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] - munknown3b85bda6m[m_amountm], 
                 1
      if mstor35m[m_amount - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
              return (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amountm] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amountm] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_amount == mcurrentCycle:
      if munknown3767377e != m_amount:
          if not m_amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                  return munknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknownc18df55f - (2 * ext_call.return_data[0]), 
                     1
          if mstor35m[m_amount - 1m]:
              if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknownc18df55f - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
                  return munknownc18df55f - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknownc18df55f + munknown01a32329m[m_amount - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknownc18df55f - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
              return munknowna1825b6am[m_amount - 1m] + munknownc18df55f - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknownc18df55f + munknown01a32329m[m_amount - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
                 1
      require ext_code.size(mcasinoAddress)
      static call mcasinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not m_amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
              return (3 * ext_call.return_data[0]) + munknownc18df55f - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f, 
                 1
      if mstor35m[m_amount - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
              return (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
             1
  if munknown3767377e != m_amount:
      if not m_amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= munknown01a32329m[m_amountm] + (2 * ext_call.return_data[0]):
              return munknown01a32329m[m_amountm] + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] - (2 * ext_call.return_data[0]), 
                 1
      if mstor35m[m_amount - 1m]:
          if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
              return munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
          return munknowna1825b6am[m_amount - 1m] + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
             1
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not m_amount:
      if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm]:
          return (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                 0
      return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknown01a32329m[m_amountm], 
             1
  if mstor35m[m_amount - 1m]:
      if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
          return (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
             1
  if ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] <= munknowna1825b6am[m_amount - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m]:
      return munknowna1825b6am[m_amount - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[m_amountm] - munknown01a32329m[m_amount - 1m] - munknown3b85bda6m[m_amount - 1m] - munknown8897c906m[m_amount - 1m] - ([94m_1016 * ext_call.return_data[0]) + munknown9b1c8ec5m[m_amount - 1m] - ([94m_574 * ext_call.return_data[0]) + munknown873426ffm[m_amount - 1m], 
             0
  return ([94m_1016 * ext_call.return_data[0]) - munknown9b1c8ec5m[m_amount - 1m] + ([94m_574 * ext_call.return_data[0]) - munknown873426ffm[m_amount - 1m] - munknowna1825b6am[m_amount - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[m_amountm] + munknown01a32329m[m_amount - 1m] + munknown3b85bda6m[m_amount - 1m] + munknown8897c906m[m_amount - 1m], 
         1


# hash = 0x26f35b85
# getter = None
# const = None
# payable = True
def unknown26f35b85(uint256 m_param1, uint256 m_param2) payable: 
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
# payable = True
def unknown2e17de78(uint256 m_param1) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 32
  require block.number >= munknown624d1b1fm[callerm]
  require m_param1 <= munknowna5b39cfbm[callerm]
  require mcurrentCycle <= mcurrentCycle
  mem[0] = caller
  mem[32] = 36
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[callerm]
  mwhile [94midx < mcurrentCyclem:
      mem[0] = [94midx
      mem[32] = 47
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != mcurrentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if munknown3767377e != [94midx:
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_245 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_247 = mem[[94m_245]
          require mem[[94m_245] <= 4294967296
          require mem[[94m_245] + 32 <= return_data.size
          require mem[[94m_245 + mem[[94m_245]] <= 4294967296 and mem[[94m_245] + (32 * mem[[94m_245 + mem[[94m_245]]) + 32 <= return_data.size
          mem[[94m_245 + ceil32(return_data.size)] = mem[[94m_245 + mem[[94m_245]]
          [94m_251 = mem[[94m_245 + [94m_247]
          [94ms = 0
          mwhile [94ms < 32 * [94m_251m:
              mem[[94ms + [94m_245 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_245 + [94m_247 + 32]
              [94ms = [94ms + 32
              mcontinue 
          mem[64] = (32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          mwhile [94ms < ext_call.return_data[0]m:
              require [94ms < mem[[94m_245 + ceil32(return_data.size)]
              require ext_code.size(mem[(32 * [94ms) + [94m_245 + ceil32(return_data.size) + 44 len 20])
              static call mem[(32 * [94ms) + [94m_245 + ceil32(return_data.size) + 44 len 20].0xaefecb5 with:
                      gas gas_remaining wei
              mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_611 = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mt = ext_call.return_data[0] + [94mt
              mcontinue 
          if [94midx != mcurrentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if munknown3767377e != [94midx:
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_611 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_611 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
          else:
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 32
              require return_data.size >= 32
              [94m_619 = mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32]
              require mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] <= 4294967296
              require mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] + 32 <= return_data.size
              require mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] + 32] <= 4294967296 and mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] + (32 * mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] + 32]) + 32 <= return_data.size
              mem[(32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 32] = mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] + 32]
              [94m_624 = mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + [94m_619 + 32]
              [94ms = 0
              mwhile [94ms < 32 * [94m_624m:
                  mem[[94ms + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_251) + [94m_245 + ceil32(return_data.size) + [94m_619 + 64]
                  [94ms = [94ms + 32
                  mcontinue 
              mem[64] = (32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              mwhile [94ms < ext_call.return_data[0]m:
                  require [94ms < mem[(32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 32]
                  require ext_code.size(mem[(32 * [94ms) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 76 len 20])
                  static call mem[(32 * [94ms) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 76 len 20].0x7952ea9d with:
                          gas gas_remaining wei
                  mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_891 = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mt = ext_call.return_data[0] + [94mt
                  mcontinue 
              if [94midx != mcurrentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if munknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != mcurrentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if munknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == mcurrentCycle:
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_611 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
      mem[0] = [94midx
      mem[32] = 46
      require munknown7eae0ccbm[[94midxm] < 11
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor46m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
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
# payable = True
def unknown31e5901b() payable: 
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
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  [94m_11 = mem[[94m_8 + 96]
  mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_8 + 96])] = mem[[94m_8 + 128 len floor32(mem[[94m_8 + 96])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
      static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
              gas gas_remaining wei
      mem[(32 * [94m_11) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_37 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  return ([94m_37 * ext_call.return_data[0])


# hash = 0x33ae47ea
# getter = None
# const = None
# payable = True
def unknown33ae47ea(uint256 m_param1, uint256 m_param2, bool m_param3, uint256 m_param4) payable: 
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


# hash = 0x3767377e
# getter = ['storage', 256, 0, 12]
# const = None
# payable = True
def unknown3767377e() payable: 
  return munknown3767377e


# hash = 0x38c67b73
# getter = None
# const = None
# payable = True
def setCurrentStage(uint256 m_stage) payable: 
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
# payable = True
def unknown38cff46e(uint256 m_param1, uint256 m_param2) payable: 
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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 44]]]
# const = None
# payable = True
def unknown3b85bda6(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown3b85bda6m[m_param1m]


# hash = 0x3f60f1f3
# getter = None
# const = None
# payable = True
def unknown3f60f1f3(addr m_param1, uint256 m_param2) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 64
  require m_param2 <= mcurrentCycle
  mem[0] = m_param1
  mem[32] = 36
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[addr(m_param1)m]
  mwhile [94midx < m_param2m:
      mem[0] = [94midx
      mem[32] = 47
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != mcurrentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if munknown3767377e != [94midx:
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_227 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_229 = mem[[94m_227]
          require mem[[94m_227] <= 4294967296
          require mem[[94m_227] + 32 <= return_data.size
          require mem[[94m_227 + mem[[94m_227]] <= 4294967296 and mem[[94m_227] + (32 * mem[[94m_227 + mem[[94m_227]]) + 32 <= return_data.size
          mem[[94m_227 + ceil32(return_data.size)] = mem[[94m_227 + mem[[94m_227]]
          [94m_233 = mem[[94m_227 + [94m_229]
          [94ms = 0
          mwhile [94ms < 32 * [94m_233m:
              mem[[94ms + [94m_227 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_227 + [94m_229 + 32]
              [94ms = [94ms + 32
              mcontinue 
          mem[64] = (32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          mwhile [94ms < ext_call.return_data[0]m:
              require [94ms < mem[[94m_227 + ceil32(return_data.size)]
              require ext_code.size(mem[(32 * [94ms) + [94m_227 + ceil32(return_data.size) + 44 len 20])
              static call mem[(32 * [94ms) + [94m_227 + ceil32(return_data.size) + 44 len 20].0xaefecb5 with:
                      gas gas_remaining wei
              mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_593 = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mt = ext_call.return_data[0] + [94mt
              mcontinue 
          if [94midx != mcurrentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if munknown3767377e != [94midx:
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_593 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_593 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
          else:
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 32
              require return_data.size >= 32
              [94m_601 = mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32]
              require mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] <= 4294967296
              require mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] + 32 <= return_data.size
              require mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] + 32] <= 4294967296 and mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] + (32 * mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] + 32]) + 32 <= return_data.size
              mem[(32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 32] = mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] + 32]
              [94m_606 = mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + [94m_601 + 32]
              [94ms = 0
              mwhile [94ms < 32 * [94m_606m:
                  mem[[94ms + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_233) + [94m_227 + ceil32(return_data.size) + [94m_601 + 64]
                  [94ms = [94ms + 32
                  mcontinue 
              mem[64] = (32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              mwhile [94ms < ext_call.return_data[0]m:
                  require [94ms < mem[(32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 32]
                  require ext_code.size(mem[(32 * [94ms) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 76 len 20])
                  static call mem[(32 * [94ms) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 76 len 20].0x7952ea9d with:
                          gas gas_remaining wei
                  mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_873 = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mt = ext_call.return_data[0] + [94mt
                  mcontinue 
              if [94midx != mcurrentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if munknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != mcurrentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if munknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == mcurrentCycle:
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_593 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
      mem[0] = [94midx
      mem[32] = 46
      require munknown7eae0ccbm[[94midxm] < 11
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor46m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4068ed2b
# getter = None
# const = None
# payable = True
def unknown4068ed2b(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  mem[0] = m_param1
  mem[32] = 36
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
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  return 0
              if mcurrentStage < 11:
                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                      return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
          else:
              if mstor35m[mstor8 - 1m]:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
      else:
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not mcurrentCycle:
              if munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                  return 0
              if mcurrentStage < 11:
                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                      return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
          else:
              if mstor35m[mstor8 - 1m]:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown873426ffm[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
  else:
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
      [94m_27 = mem[96]
      require mem[96] <= 4294967296
      require mem[96] + 32 <= return_data.size
      require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
      mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
      [94m_31 = mem[[94m_27 + 96]
      mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_27 + 96])] = mem[[94m_27 + 128 len floor32(mem[[94m_27 + 96])]
      [94midx = 0
      [94ms = 0
      mwhile [94midx < ext_call.return_data[0]m:
          require [94midx < mem[ceil32(return_data.size) + 96]
          require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
          static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
                  gas gas_remaining wei
          mem[(32 * [94m_31) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_589 = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] + [94ms
          mcontinue 
      if mcurrentCycle != mcurrentCycle:
          if munknown3767377e != mcurrentCycle:
              if not mcurrentCycle:
                  if munknown9b1c8ec5m[mstor8m] + ([94m_589 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  if mstor35m[mstor8 - 1m]:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not mcurrentCycle:
                  if munknown9b1c8ec5m[mstor8m] + ([94m_589 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                      return 0
                  if mcurrentStage < 11:
                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                          return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  if mstor35m[mstor8 - 1m]:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      if munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return ((munknown9b1c8ec5m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_31) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * [94m_31) + ceil32(return_data.size) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * [94m_31) + (2 * ceil32(return_data.size)) + 128
          require return_data.size >= 32
          [94m_597 = mem[(32 * [94m_31) + ceil32(return_data.size) + 128]
          require mem[(32 * [94m_31) + ceil32(return_data.size) + 128] <= 4294967296
          require mem[(32 * [94m_31) + ceil32(return_data.size) + 128] + 32 <= return_data.size
          require mem[(32 * [94m_31) + ceil32(return_data.size) + mem[(32 * [94m_31) + ceil32(return_data.size) + 128] + 128] <= 4294967296 and mem[(32 * [94m_31) + ceil32(return_data.size) + 128] + (32 * mem[(32 * [94m_31) + ceil32(return_data.size) + mem[(32 * [94m_31) + ceil32(return_data.size) + 128] + 128]) + 32 <= return_data.size
          mem[(32 * [94m_31) + (2 * ceil32(return_data.size)) + 128] = mem[(32 * [94m_31) + ceil32(return_data.size) + mem[(32 * [94m_31) + ceil32(return_data.size) + 128] + 128]
          [94m_602 = mem[(32 * [94m_31) + ceil32(return_data.size) + [94m_597 + 128]
          mem[(32 * [94m_31) + (2 * ceil32(return_data.size)) + 160 len floor32(mem[(32 * [94m_31) + ceil32(return_data.size) + [94m_597 + 128])] = mem[(32 * [94m_31) + ceil32(return_data.size) + [94m_597 + 160 len floor32(mem[(32 * [94m_31) + ceil32(return_data.size) + [94m_597 + 128])]
          [94midx = 0
          [94ms = 0
          mwhile [94midx < ext_call.return_data[0]m:
              require [94midx < mem[(32 * [94m_31) + (2 * ceil32(return_data.size)) + 128]
              require ext_code.size(mem[(32 * [94midx) + (32 * [94m_31) + (2 * ceil32(return_data.size)) + 172 len 20])
              static call mem[(32 * [94midx) + (32 * [94m_31) + (2 * ceil32(return_data.size)) + 172 len 20].0x7952ea9d with:
                      gas gas_remaining wei
              mem[(32 * [94m_602) + (32 * [94m_31) + (2 * ceil32(return_data.size)) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1031 = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0] + [94ms
              mcontinue 
          if mcurrentCycle != mcurrentCycle:
              if munknown3767377e != mcurrentCycle:
                  if not mcurrentCycle:
                      if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      if mstor35m[mstor8 - 1m]:
                          if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not mcurrentCycle:
                      if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]:
                          return 0
                      if mcurrentStage < 11:
                          if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                              return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      if mstor35m[mstor8 - 1m]:
                          if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown8897c906m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if mcurrentCycle != mcurrentCycle:
                  if munknown3767377e != mcurrentCycle:
                      if not mcurrentCycle:
                          if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          if mstor35m[mstor8 - 1m]:
                              if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not mcurrentCycle:
                          if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m]:
                              return 0
                          if mcurrentStage < 11:
                              if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          if mstor35m[mstor8 - 1m]:
                              if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown3b85bda6m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if mcurrentCycle == mcurrentCycle:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknownc18df55f * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                  else:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0]):
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m]:
                                  return 0
                              if mcurrentStage < 11:
                                  if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_589 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] <= munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]:
                                      return 0
                                  if mcurrentStage < 11:
                                      if (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown9b1c8ec5m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) + ([94m_589 * ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown873426ffm[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (munknowna1825b6am[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) - (munknown01a32329m[mstor8m] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown01a32329m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown3b85bda6m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) - (ext_call.return_data[0] * munknowna5b39cfbm[addr(m_param1)m]) + (munknown8897c906m[mstor8 - 1m] * munknowna5b39cfbm[addr(m_param1)m]) / (ext_call.return_data[0] * munknown8e7c820cm[mstor7m] / 100) + mtotalStaked * munknown8e7c820cm[mstor7m] / 100)
  revert


# hash = 0x420a83e7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def tokenHolder() payable: 
  return mtokenHolderAddress


# hash = 0x5bf5d54c
# getter = ['storage', 256, 0, 7]
# const = None
# payable = True
def currentStage() payable: 
  return mcurrentStage


# hash = 0x624d1b1f
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 37]]]
# const = None
# payable = True
def unknown624d1b1f(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown624d1b1fm[m_param1m]


# hash = 0x65e86f0c
# getter = None
# const = None
# payable = True
def unknown65e86f0c() payable: 
  require mcurrentStage < 11
  return (10^18 * munknownc563af55m[mstor7m])


# hash = 0x7710c6d8
# getter = None
# const = None
# payable = True
def unknown7710c6d8(uint256 m_param1) payable: 
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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 39]]]
# const = None
# payable = True
def unknown7a49f350(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown7a49f350m[m_param1m]


# hash = 0x7eae0ccb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 46]]]
# const = None
# payable = True
def unknown7eae0ccb(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown7eae0ccbm[m_param1m]


# hash = 0x817b1cd2
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def totalStaked() payable: 
  return mtotalStaked


# hash = 0x81f83692
# getter = ['storage', 256, 0, 10]
# const = None
# payable = True
def unknown81f83692() payable: 
  return munknown81f83692


# hash = 0x8209e742
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def unknown8209e742() payable: 
  return munknown8209e742


# hash = 0x84bcd3c6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 38]]]
# const = None
# payable = True
def unknown84bcd3c6(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown84bcd3c6m[m_param1m]


# hash = 0x873426ff
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 41]]]
# const = None
# payable = True
def unknown873426ff(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown873426ffm[m_param1m]


# hash = 0x87e0e9ab
# getter = None
# const = None
# payable = True
def unknown87e0e9ab() payable: 
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x8897c906
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 43]]]
# const = None
# payable = True
def unknown8897c906(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown8897c906m[m_param1m]


# hash = 0x8e7c820c
# getter = ['storage', 256, 0, ['add', 13, ['cd', 4]]]
# const = None
# payable = True
def unknown8e7c820c(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1 < 11
  return munknown8e7c820cm[m_param1m]


# hash = 0x9403e8dd
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def casino() payable: 
  return mcasinoAddress


# hash = 0x9b1c8ec5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 42]]]
# const = None
# payable = True
def unknown9b1c8ec5(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown9b1c8ec5m[m_param1m]


# hash = 0x9f9de645
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 47]]]
# const = None
# payable = True
def unknown9f9de645(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown9f9de645m[m_param1m]


# hash = 0xa1825b6a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 40]]]
# const = None
# payable = True
def unknowna1825b6a(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknowna1825b6am[m_param1m]


# hash = 0xa5b39cfb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 36]]]
# const = None
# payable = True
def unknowna5b39cfb(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknowna5b39cfbm[m_param1m]


# hash = 0xa694fc3a
# getter = None
# const = None
# payable = True
def stake(uint256 m_amount) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 32
  require mcurrentCycle <= mcurrentCycle
  mem[0] = caller
  mem[32] = 36
  require ext_code.size(mtokenAddress)
  static call mtokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = munknown84bcd3c6m[callerm]
  mwhile [94midx < mcurrentCyclem:
      mem[0] = [94midx
      mem[32] = 47
      if not munknown9f9de645m[[94midxm]:
          [94midx = [94midx + 1
          mcontinue 
      require munknown7eae0ccbm[[94midxm] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != mcurrentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if munknown3767377e != [94midx:
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if munknown9b1c8ec5m[[94midxm] + munknown873426ffm[[94midxm] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if mstor35m[[94midx - 1m]:
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + munknown873426ffm[[94midxm] - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_243 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_245 = mem[[94m_243]
          require mem[[94m_243] <= 4294967296
          require mem[[94m_243] + 32 <= return_data.size
          require mem[[94m_243 + mem[[94m_243]] <= 4294967296 and mem[[94m_243] + (32 * mem[[94m_243 + mem[[94m_243]]) + 32 <= return_data.size
          mem[[94m_243 + ceil32(return_data.size)] = mem[[94m_243 + mem[[94m_243]]
          [94m_249 = mem[[94m_243 + [94m_245]
          [94ms = 0
          mwhile [94ms < 32 * [94m_249m:
              mem[[94ms + [94m_243 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_243 + [94m_245 + 32]
              [94ms = [94ms + 32
              mcontinue 
          mem[64] = (32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          mwhile [94ms < ext_call.return_data[0]m:
              require [94ms < mem[[94m_243 + ceil32(return_data.size)]
              require ext_code.size(mem[(32 * [94ms) + [94m_243 + ceil32(return_data.size) + 44 len 20])
              static call mem[(32 * [94ms) + [94m_243 + ceil32(return_data.size) + 44 len 20].0xaefecb5 with:
                      gas gas_remaining wei
              mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_609 = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mt = ext_call.return_data[0] + [94mt
              mcontinue 
          if [94midx != mcurrentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if munknown3767377e != [94midx:
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_609 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if munknown9b1c8ec5m[[94midxm] + ([94m_609 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if mstor35m[[94midx - 1m]:
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94midxm] - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                              [94midx = [94midx + 1
                              mcontinue 
          else:
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 32
              require return_data.size >= 32
              [94m_617 = mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32]
              require mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] <= 4294967296
              require mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] + 32 <= return_data.size
              require mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] + 32] <= 4294967296 and mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] + (32 * mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] + 32]) + 32 <= return_data.size
              mem[(32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 32] = mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] + 32]
              [94m_622 = mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + [94m_617 + 32]
              [94ms = 0
              mwhile [94ms < 32 * [94m_622m:
                  mem[[94ms + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_249) + [94m_243 + ceil32(return_data.size) + [94m_617 + 64]
                  [94ms = [94ms + 32
                  mcontinue 
              mem[64] = (32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              mwhile [94ms < ext_call.return_data[0]m:
                  require [94ms < mem[(32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 32]
                  require ext_code.size(mem[(32 * [94ms) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 76 len 20])
                  static call mem[(32 * [94ms) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 76 len 20].0x7952ea9d with:
                          gas gas_remaining wei
                  mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_889 = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mt = ext_call.return_data[0] + [94mt
                  mcontinue 
              if [94midx != mcurrentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if munknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + munknown8897c906m[[94midxm]:
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if mstor35m[[94midx - 1m]:
                              if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + ext_call.return_data[0] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + munknown8897c906m[[94midxm] - munknown8897c906m[[94midx - 1m]:
                                  [94midx = [94midx + 1
                                  mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != mcurrentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if munknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] + ext_call.return_data[0] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] + munknown3b85bda6m[[94midxm]:
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if mstor35m[[94midx - 1m]:
                                  if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + munknown3b85bda6m[[94midxm] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == mcurrentCycle:
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknownc18df55f - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if munknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= munknown01a32329m[[94midxm] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm]:
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if mstor35m[[94midx - 1m]:
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94midx - 1m] + ([94m_609 * ext_call.return_data[0]) - munknown873426ffm[[94midx - 1m] <= munknowna1825b6am[[94midx - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[[94midxm] - munknown01a32329m[[94midx - 1m] - munknown3b85bda6m[[94midx - 1m] - munknown8897c906m[[94midx - 1m]:
                                          [94midx = [94midx + 1
                                          mcontinue 
      mem[0] = [94midx
      mem[32] = 46
      require munknown7eae0ccbm[[94midxm] < 11
      require (ext_call.return_data[0] * munknown8e7c820cm[mstor46m[[94midxm]m] / 100) - munknown7a49f350m[[94midxm] + munknown9f9de645m[[94midxm]
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
# payable = True
def unknowna88379c6() payable: 
  return munknowna88379c6


# hash = 0xbab2f552
# getter = ['storage', 256, 0, 8]
# const = None
# payable = True
def currentCycle() payable: 
  return mcurrentCycle


# hash = 0xbc105ab5
# getter = None
# const = None
# payable = True
def unknownbc105ab5(addr m_param1) payable: 
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
  if mcurrentCycle != mcurrentCycle:
      if munknown3767377e != mcurrentCycle:
          if not mcurrentCycle:
              require munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] > munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0x12d15611 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              if mstor35m[mstor8 - 1m]:
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] > munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
      else:
          require ext_code.size(mcasinoAddress)
          static call mcasinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not mcurrentCycle:
              require munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] > ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0x12d15611 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require munknown9b1c8ec5m[mstor8m] + munknown873426ffm[mstor8m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              if mstor35m[mstor8 - 1m]:
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] > ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + munknown873426ffm[mstor8m] - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
  else:
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
      mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
      [94m_28 = mem[[94m_24 + 96]
      mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_24 + 96])] = mem[[94m_24 + 128 len floor32(mem[[94m_24 + 96])]
      [94midx = 0
      [94ms = 0
      mwhile [94midx < ext_call.return_data[0]m:
          require [94midx < mem[ceil32(return_data.size) + 96]
          require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
          static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0xaefecb5 with:
                  gas gas_remaining wei
          mem[(32 * [94m_28) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_784 = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] + [94ms
          mcontinue 
      if mcurrentCycle != mcurrentCycle:
          if munknown3767377e != mcurrentCycle:
              if not mcurrentCycle:
                  require munknown9b1c8ec5m[mstor8m] + ([94m_784 * ext_call.return_data[0]) > munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] + ([94m_784 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  if mstor35m[mstor8 - 1m]:
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not mcurrentCycle:
                  require munknown9b1c8ec5m[mstor8m] + ([94m_784 * ext_call.return_data[0]) > ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require munknown9b1c8ec5m[mstor8m] + ([94m_784 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  if mstor35m[mstor8 - 1m]:
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require munknown9b1c8ec5m[mstor8m] - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
      else:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_28) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.getGames() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * [94m_28) + ceil32(return_data.size) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * [94m_28) + (2 * ceil32(return_data.size)) + 128
          require return_data.size >= 32
          [94m_792 = mem[(32 * [94m_28) + ceil32(return_data.size) + 128]
          require mem[(32 * [94m_28) + ceil32(return_data.size) + 128] <= 4294967296
          require mem[(32 * [94m_28) + ceil32(return_data.size) + 128] + 32 <= return_data.size
          require mem[(32 * [94m_28) + ceil32(return_data.size) + mem[(32 * [94m_28) + ceil32(return_data.size) + 128] + 128] <= 4294967296 and mem[(32 * [94m_28) + ceil32(return_data.size) + 128] + (32 * mem[(32 * [94m_28) + ceil32(return_data.size) + mem[(32 * [94m_28) + ceil32(return_data.size) + 128] + 128]) + 32 <= return_data.size
          mem[(32 * [94m_28) + (2 * ceil32(return_data.size)) + 128] = mem[(32 * [94m_28) + ceil32(return_data.size) + mem[(32 * [94m_28) + ceil32(return_data.size) + 128] + 128]
          [94m_797 = mem[(32 * [94m_28) + ceil32(return_data.size) + [94m_792 + 128]
          mem[(32 * [94m_28) + (2 * ceil32(return_data.size)) + 160 len floor32(mem[(32 * [94m_28) + ceil32(return_data.size) + [94m_792 + 128])] = mem[(32 * [94m_28) + ceil32(return_data.size) + [94m_792 + 160 len floor32(mem[(32 * [94m_28) + ceil32(return_data.size) + [94m_792 + 128])]
          [94midx = 0
          [94ms = 0
          mwhile [94midx < ext_call.return_data[0]m:
              require [94midx < mem[(32 * [94m_28) + (2 * ceil32(return_data.size)) + 128]
              require ext_code.size(mem[(32 * [94midx) + (32 * [94m_28) + (2 * ceil32(return_data.size)) + 172 len 20])
              static call mem[(32 * [94midx) + (32 * [94m_28) + (2 * ceil32(return_data.size)) + 172 len 20].0x7952ea9d with:
                      gas gas_remaining wei
              mem[(32 * [94m_797) + (32 * [94m_28) + (2 * ceil32(return_data.size)) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1388 = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0] + [94ms
              mcontinue 
          if mcurrentCycle != mcurrentCycle:
              if munknown3767377e != mcurrentCycle:
                  if not mcurrentCycle:
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if mstor35m[mstor8 - 1m]:
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not mcurrentCycle:
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > ext_call.return_data[0] + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + munknown8897c906m[mstor8m]
                      require ext_code.size(msettingsAddress)
                      static call msettingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - ext_call.return_data[0] - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - munknown8897c906m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if mstor35m[mstor8 - 1m]:
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + ext_call.return_data[0] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8m] - munknown8897c906m[mstor8 - 1m]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - ext_call.return_data[0] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              require ext_code.size(mcasinoAddress)
              static call mcasinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if mcurrentCycle != mcurrentCycle:
                  if munknown3767377e != mcurrentCycle:
                      if not mcurrentCycle:
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m] + ext_call.return_data[0]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] - ext_call.return_data[0] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          if mstor35m[mstor8 - 1m]:
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] + ext_call.return_data[0] - munknown8897c906m[mstor8 - 1m]
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] - ext_call.return_data[0] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not mcurrentCycle:
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] + munknown3b85bda6m[mstor8m]
                          require ext_code.size(msettingsAddress)
                          static call msettingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - munknown3b85bda6m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          if mstor35m[mstor8 - 1m]:
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (2 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if mcurrentCycle == mcurrentCycle:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > munknownc18df55f + (2 * ext_call.return_data[0])
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - munknownc18df55f - (2 * ext_call.return_data[0]) > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknownc18df55f - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknownc18df55f + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (3 * ext_call.return_data[0]) + munknownc18df55f
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknownc18df55f > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknownc18df55f + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if munknown3767377e != mcurrentCycle:
                          if not mcurrentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > munknown01a32329m[mstor8m] + (2 * ext_call.return_data[0])
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] - (2 * ext_call.return_data[0]) > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] - (2 * ext_call.return_data[0]) + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not mcurrentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m]
                              require ext_code.size(msettingsAddress)
                              static call msettingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if mstor35m[mstor8 - 1m]:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] > munknowna1825b6am[mstor8 - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[mstor8m] - munknown01a32329m[mstor8 - 1m] - munknown3b85bda6m[mstor8 - 1m] - munknown8897c906m[mstor8 - 1m]
                                  require ext_code.size(msettingsAddress)
                                  static call msettingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - munknown9b1c8ec5m[mstor8 - 1m] + ([94m_784 * ext_call.return_data[0]) - munknown873426ffm[mstor8 - 1m] - munknowna1825b6am[mstor8 - 1m] - (3 * ext_call.return_data[0]) - munknown01a32329m[mstor8m] + munknown01a32329m[mstor8 - 1m] + munknown3b85bda6m[mstor8 - 1m] + munknown8897c906m[mstor8 - 1m] > ext_call.return_data[0] * ext_call.return_data[0]
  call m_param1 with:
     value ext_call.return_data[0] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(mcasinoAddress)
  call mcasinoAddress.0xc63e0c05 with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  munknown3767377e = mcurrentCycle


# hash = 0xc18df55f
# getter = ['storage', 256, 0, 11]
# const = None
# payable = True
def unknownc18df55f() payable: 
  return munknownc18df55f


# hash = 0xc563af55
# getter = ['storage', 256, 0, ['add', 24, ['cd', 4]]]
# const = None
# payable = True
def unknownc563af55(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1 < 11
  return munknownc563af55m[m_param1m]


# hash = 0xcaa9828c
# getter = None
# const = None
# payable = True
def unknowncaa9828c(addr m_param1) payable: 
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


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def settings() payable: 
  return msettingsAddress


# hash = 0xe0aecca7
# getter = None
# const = None
# payable = True
def unknowne0aecca7(array m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[64] = (32 * m_param1.length) + 128
  mem[96] = m_param1.length
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = 0
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < mem[96]
      require m_param2 <= mcurrentCycle
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 36
      require ext_code.size(mtokenAddress)
      static call mtokenAddress.totalSupply() with:
              gas gas_remaining wei
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94ms = munknown84bcd3c6m[mem[0]m]
      mwhile [94ms < m_param2m:
          mem[0] = [94ms
          mem[32] = 47
          if not munknown9f9de645m[[94msm]:
              [94ms = [94ms + 1
              mcontinue 
          require munknown7eae0ccbm[[94msm] < 11
          mem[0] = [94ms
          mem[32] = 39
          if [94ms != mcurrentCycle:
              mem[0] = [94ms
              mem[32] = 45
              if munknown3767377e != [94ms:
                  if not [94ms:
                      if munknown9b1c8ec5m[[94msm] + munknown873426ffm[[94msm] <= munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                          [94ms = [94ms + 1
                          mcontinue 
                  else:
                      mem[0] = [94ms - 1
                      mem[32] = 35
                      if mstor35m[[94ms - 1m]:
                          if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + munknown873426ffm[[94msm] - munknown873426ffm[[94ms - 1m] <= munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                              [94ms = [94ms + 1
                              mcontinue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + munknown873426ffm[[94msm] - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                              [94ms = [94ms + 1
                              mcontinue 
              else:
                  require ext_code.size(mcasinoAddress)
                  static call mcasinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94ms:
                      if munknown9b1c8ec5m[[94msm] + munknown873426ffm[[94msm] <= ext_call.return_data[0] + munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                          [94ms = [94ms + 1
                          mcontinue 
                  else:
                      mem[0] = [94ms - 1
                      mem[32] = 35
                      if mstor35m[[94ms - 1m]:
                          if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + munknown873426ffm[[94msm] - munknown873426ffm[[94ms - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                              [94ms = [94ms + 1
                              mcontinue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 40
                          if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + munknown873426ffm[[94msm] - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                              [94ms = [94ms + 1
                              mcontinue 
          else:
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(msettingsAddress)
              static call msettingsAddress.getGames() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_446 = mem[64]
              mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >= 32
              [94m_448 = mem[[94m_446]
              require mem[[94m_446] <= 4294967296
              require mem[[94m_446] + 32 <= return_data.size
              require mem[[94m_446 + mem[[94m_446]] <= 4294967296 and mem[[94m_446] + (32 * mem[[94m_446 + mem[[94m_446]]) + 32 <= return_data.size
              mem[[94m_446 + ceil32(return_data.size)] = mem[[94m_446 + mem[[94m_446]]
              [94m_452 = mem[[94m_446 + [94m_448]
              [94midx = 0
              mwhile [94midx < 32 * [94m_452m:
                  mem[[94midx + [94m_446 + ceil32(return_data.size) + 32] = mem[[94midx + [94m_446 + [94m_448 + 32]
                  [94midx = [94midx + 32
                  mcontinue 
              mem[64] = (32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32
              [94midx = 0
              [94mt = 0
              mwhile [94midx < ext_call.return_data[0]m:
                  require [94midx < mem[[94m_446 + ceil32(return_data.size)]
                  require ext_code.size(mem[(32 * [94midx) + [94m_446 + ceil32(return_data.size) + 44 len 20])
                  static call mem[(32 * [94midx) + [94m_446 + ceil32(return_data.size) + 44 len 20].0xaefecb5 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_812 = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94mt = ext_call.return_data[0] + [94mt
                  mcontinue 
              if [94ms != mcurrentCycle:
                  mem[0] = [94ms
                  mem[32] = 45
                  if munknown3767377e != [94ms:
                      if not [94ms:
                          if munknown9b1c8ec5m[[94msm] + ([94m_812 * ext_call.return_data[0]) <= munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                              [94ms = [94ms + 1
                              mcontinue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 35
                          if mstor35m[[94ms - 1m]:
                              if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                  [94ms = [94ms + 1
                                  mcontinue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 40
                              if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                  [94ms = [94ms + 1
                                  mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94ms:
                          if munknown9b1c8ec5m[[94msm] + ([94m_812 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                              [94ms = [94ms + 1
                              mcontinue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 35
                          if mstor35m[[94ms - 1m]:
                              if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                  [94ms = [94ms + 1
                                  mcontinue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 40
                              if munknown9b1c8ec5m[[94msm] - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                  [94ms = [94ms + 1
                                  mcontinue 
              else:
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.0xdd2f4ebd with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
                  require ext_code.size(msettingsAddress)
                  static call msettingsAddress.getGames() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  mem[64] = (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 32
                  require return_data.size >= 32
                  [94m_820 = mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32]
                  require mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] <= 4294967296
                  require mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] + 32 <= return_data.size
                  require mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] + 32] <= 4294967296 and mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] + (32 * mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] + 32]) + 32 <= return_data.size
                  mem[(32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 32] = mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] + 32]
                  [94m_825 = mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + [94m_820 + 32]
                  [94midx = 0
                  mwhile [94midx < 32 * [94m_825m:
                      mem[[94midx + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = mem[[94midx + (32 * [94m_452) + [94m_446 + ceil32(return_data.size) + [94m_820 + 64]
                      [94midx = [94midx + 32
                      mcontinue 
                  mem[64] = (32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64
                  [94midx = 0
                  [94mt = 0
                  mwhile [94midx < ext_call.return_data[0]m:
                      require [94midx < mem[(32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 32]
                      require ext_code.size(mem[(32 * [94midx) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 76 len 20])
                      static call mem[(32 * [94midx) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 76 len 20].0x7952ea9d with:
                              gas gas_remaining wei
                      mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1092 = ext_call.return_data[0]
                      [94midx = [94midx + 1
                      [94mt = ext_call.return_data[0] + [94mt
                      mcontinue 
                  if [94ms != mcurrentCycle:
                      mem[0] = [94ms
                      mem[32] = 45
                      if munknown3767377e != [94ms:
                          if not [94ms:
                              if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                                  [94ms = [94ms + 1
                                  mcontinue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 35
                              if mstor35m[[94ms - 1m]:
                                  if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 40
                                  if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94ms:
                              if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= ext_call.return_data[0] + munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + munknown8897c906m[[94msm]:
                                  [94ms = [94ms + 1
                                  mcontinue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 35
                              if mstor35m[[94ms - 1m]:
                                  if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 40
                                  if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + ext_call.return_data[0] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + munknown8897c906m[[94msm] - munknown8897c906m[[94ms - 1m]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                  else:
                      require ext_code.size(mcasinoAddress)
                      static call mcasinoAddress.0x610fe551 with:
                              gas gas_remaining wei
                      mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94ms != mcurrentCycle:
                          mem[0] = [94ms
                          mem[32] = 45
                          if munknown3767377e != [94ms:
                              if not [94ms:
                                  if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm] + ext_call.return_data[0]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 35
                                  if mstor35m[[94ms - 1m]:
                                      if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + ext_call.return_data[0] - munknown8897c906m[[94ms - 1m]:
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 40
                                      if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] + ext_call.return_data[0] - munknown8897c906m[[94ms - 1m]:
                                          [94ms = [94ms + 1
                                          mcontinue 
                          else:
                              require ext_code.size(mcasinoAddress)
                              static call mcasinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94ms:
                                  if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94msm] + munknown3b85bda6m[[94msm]:
                                      [94ms = [94ms + 1
                                      mcontinue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 35
                                  if mstor35m[[94ms - 1m]:
                                      if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= (2 * ext_call.return_data[0]) + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 40
                                      if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + (2 * ext_call.return_data[0]) + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + munknown3b85bda6m[[94msm] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                          [94ms = [94ms + 1
                                          mcontinue 
                      else:
                          require ext_code.size(mcasinoAddress)
                          static call mcasinoAddress.0x236e5e4c with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if [94ms == mcurrentCycle:
                              if munknown3767377e != [94ms:
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= munknownc18df55f + (2 * ext_call.return_data[0]):
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if mstor35m[[94ms - 1m]:
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknownc18df55f - munknown01a32329m[[94ms - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknownc18df55f - munknown01a32329m[[94ms - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                              else:
                                  require ext_code.size(mcasinoAddress)
                                  static call mcasinoAddress.0x397425fb with:
                                          gas gas_remaining wei
                                  mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknownc18df55f:
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if mstor35m[[94ms - 1m]:
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94ms - 1m] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + (3 * ext_call.return_data[0]) + munknownc18df55f - munknown01a32329m[[94ms - 1m] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                          else:
                              mem[0] = [94ms
                              mem[32] = 45
                              if munknown3767377e != [94ms:
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= munknown01a32329m[[94msm] + (2 * ext_call.return_data[0]):
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if mstor35m[[94ms - 1m]:
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] + (2 * ext_call.return_data[0]) - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                              else:
                                  require ext_code.size(mcasinoAddress)
                                  static call mcasinoAddress.0x397425fb with:
                                          gas gas_remaining wei
                                  mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94msm]:
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if mstor35m[[94ms - 1m]:
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= (3 * ext_call.return_data[0]) + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - munknown9b1c8ec5m[[94ms - 1m] + ([94m_812 * ext_call.return_data[0]) - munknown873426ffm[[94ms - 1m] <= munknowna1825b6am[[94ms - 1m] + (3 * ext_call.return_data[0]) + munknown01a32329m[[94msm] - munknown01a32329m[[94ms - 1m] - munknown3b85bda6m[[94ms - 1m] - munknown8897c906m[[94ms - 1m]:
                                              [94ms = [94ms + 1
                                              mcontinue 
          mem[0] = [94ms
          mem[32] = 46
          require munknown7eae0ccbm[[94msm] < 11
          require (ext_call.return_data[0] * munknown8e7c820cm[mstor46m[[94msm]m] / 100) - munknown7a49f350m[[94msm] + munknown9f9de645m[[94msm]
          [94ms = [94ms + 1
          mcontinue 
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xe239b026
# getter = None
# const = None
# payable = True
def unknowne239b026() payable: 
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
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  [94m_11 = mem[[94m_8 + 96]
  mem[ceil32(return_data.size) + 128 len floor32(mem[[94m_8 + 96])] = mem[[94m_8 + 128 len floor32(mem[[94m_8 + 96])]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < ext_call.return_data[0]m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      require ext_code.size(mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20])
      static call mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20].0x7952ea9d with:
              gas gas_remaining wei
      mem[(32 * [94m_11) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_37 = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0] + [94ms
      mcontinue 
  return ([94m_37 * ext_call.return_data[0])


# hash = 0xf145ff23
# getter = None
# const = None
# payable = True
def getDistributedTokens() payable: 
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


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def token() payable: 
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


