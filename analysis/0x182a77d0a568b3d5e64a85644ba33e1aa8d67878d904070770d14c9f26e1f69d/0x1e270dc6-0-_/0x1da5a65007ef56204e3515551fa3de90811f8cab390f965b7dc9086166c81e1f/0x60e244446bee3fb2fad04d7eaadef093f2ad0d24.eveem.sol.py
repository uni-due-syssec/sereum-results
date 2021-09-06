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
def unknown00289ef3(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require currentStage < 11
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(tokenAddress)
  call tokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args tokenHolderAddress, addr(_param1), 10^18 * unknownc563af55[stor7]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require currentStage < 11
  if unknown8e7c820c[stor7] < 0 / ext_call.return_data[0]:
      currentStage++
  log 0xa611a711: (10^18 * unknownc563af55[stor7]), _param1


# hash = 0x01a32329
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 45]]]
# const = None
# payable = True
def unknown01a32329(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown01a32329[_param1]


# hash = 0x0365abe7
# getter = None
# const = None
# payable = True
def unknown0365abe7() payable: 
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require currentStage < 11
  if unknown8e7c820c[stor7] < 0 / ext_call.return_data[0]:
      currentStage++


# hash = 0x05ab421d
# getter = None
# const = None
# payable = True
def sendTokens(address _to, uint256 _amount) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(tokenAddress)
  call tokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args tokenHolderAddress, addr(_to), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0]
  require currentStage < 11
  if unknown8e7c820c[stor7] < 0 / ext_call.return_data[0]:
      currentStage++
  log 0xa611a711: _amount, _to


# hash = 0x084a4faf
# getter = None
# const = None
# payable = True
def unknown084a4faf() payable: 
  require block.number >= unknown81f83692
  unknown81f83692 = block.number + unknown8209e742
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  mem[0] = currentCycle
  mem[32] = 41
  unknown873426ff[stor8] = [94m_2757 * ext_call.return_data[0]
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_11) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  unknown9b1c8ec5[stor8] = [94m_5475 * ext_call.return_data[0]
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown8897c906[stor8] = ext_call.return_data[0]
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown3b85bda6[stor8] = ext_call.return_data[0]
  unknown01a32329[stor8] = unknownc18df55f
  mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 164] = tokenHolderAddress
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown7a49f350[stor8] = 0
  unknown7eae0ccb[stor8] = currentStage
  mem[0] = currentCycle
  mem[32] = 47
  unknown9f9de645[stor8] = totalStaked
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  stor35[stor8] = 0
                  unknowna1825b6a[stor8] = unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - unknown873426ff[stor8]
              else:
                  stor35[stor8] = 1
                  unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
          else:
              if stor35[stor8 - 1]:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1]
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
              else:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1]
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
      else:
          require ext_code.size(casinoAddress)
          static call casinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  stor35[stor8] = 0
                  unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - unknown873426ff[stor8]
              else:
                  stor35[stor8] = 1
                  unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
          else:
              if stor35[stor8 - 1]:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1]
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
              else:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1]
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
  else:
      require ext_code.size(settingsAddress)
      static call settingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(32 * [94m_2765) + (32 * [94m_11) + (2 * ceil32(return_data.size)) + 160] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(settingsAddress)
      static call settingsAddress.getGames() with:
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
      while [94midx < ext_call.return_data[0]:
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
          continue 
      if currentCycle != currentCycle:
          if unknown3767377e != currentCycle:
              if not currentCycle:
                  if unknown9b1c8ec5[stor8] + ([94m_7914 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - ([94m_7914 * ext_call.return_data[0])
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] + ([94m_7914 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
              else:
                  if stor35[stor8 - 1]:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
                  else:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not currentCycle:
                  if unknown9b1c8ec5[stor8] + ([94m_7914 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                      stor35[stor8] = 0
                      unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - ([94m_7914 * ext_call.return_data[0])
                  else:
                      stor35[stor8] = 1
                      unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] + ([94m_7914 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
              else:
                  if stor35[stor8 - 1]:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
                  else:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_5508) + (32 * [94m_2765) + (32 * [94m_11) + (4 * ceil32(return_data.size)) + 192] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94midx < ext_call.return_data[0]:
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
              continue 
          if currentCycle != currentCycle:
              if unknown3767377e != currentCycle:
                  if not currentCycle:
                      if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
                  else:
                      if stor35[stor8 - 1]:
                          if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
                      else:
                          if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not currentCycle:
                      if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                          stor35[stor8] = 0
                          unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                      else:
                          stor35[stor8] = 1
                          unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8]
                  else:
                      if stor35[stor8 - 1]:
                          if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
                      else:
                          if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1]
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if currentCycle != currentCycle:
                  if unknown3767377e != currentCycle:
                      if not currentCycle:
                          if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - ext_call.return_data[0]
                      else:
                          if stor35[stor8 - 1]:
                              if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1]
                          else:
                              if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1]
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not currentCycle:
                          if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8]:
                              stor35[stor8] = 0
                              unknowna1825b6a[stor8] = (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                          else:
                              stor35[stor8] = 1
                              unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8]
                      else:
                          if stor35[stor8 - 1]:
                              if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                          else:
                              if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if currentCycle == currentCycle:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = unknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - unknownc18df55f - (2 * ext_call.return_data[0])
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = (3 * ext_call.return_data[0]) + unknownc18df55f - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknownc18df55f
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                  else:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= unknown01a32329[stor8] + (2 * ext_call.return_data[0]):
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = unknown01a32329[stor8] + (2 * ext_call.return_data[0]) - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - unknown01a32329[stor8] - (2 * ext_call.return_data[0])
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              if ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8]:
                                  stor35[stor8] = 0
                                  unknowna1825b6a[stor8] = (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - ([94m_9868 * ext_call.return_data[0]) - ([94m_7914 * ext_call.return_data[0])
                              else:
                                  stor35[stor8] = 1
                                  unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) + ([94m_7914 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknown01a32329[stor8]
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
                              else:
                                  if ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      stor35[stor8] = 0
                                      unknowna1825b6a[stor8] = unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_9868 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_7914 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1]
                                  else:
                                      stor35[stor8] = 1
                                      unknowna1825b6a[stor8] = ([94m_9868 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_7914 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1]
  if stor35[stor8]:
      require ext_code.size(tokenAddress)
      static call tokenAddress.totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require currentStage < 11
      require currentStage < 11
      require currentStage < 11
      require (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) - unknown7a49f350[stor8] + unknown9f9de645[stor8]
      require ext_code.size(casinoAddress)
      call casinoAddress.0x5815caa with:
           gas gas_remaining wei
          args unknown0a6554e9Address, ((100 * unknowna1825b6a[stor8]) - (unknown8e7c820c[stor7] * unknowna1825b6a[stor8]) / 100) + ((ext_call.return_data[0] * unknown8e7c820c[stor7] / 100 * unknowna1825b6a[stor8]) - (unknown7a49f350[stor8] * unknowna1825b6a[stor8]) + (unknown9f9de645[stor8] * unknowna1825b6a[stor8]) - (unknown9f9de645[stor8] * unknowna1825b6a[stor8]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) - unknown7a49f350[stor8] + unknown9f9de645[stor8] * unknown8e7c820c[stor7] / 100)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0x4878ecf9: currentCycle
  currentCycle++


# hash = 0x0a6554e9
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def unknown0a6554e9() payable: 
  return unknown0a6554e9Address


# hash = 0x14794830
# getter = None
# const = None
# payable = True
def unknown14794830(addr _param1, uint256 _param2) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 64
  mem[0] = _param1
  mem[32] = 36
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = unknown84bcd3c6[addr(_param1)]
  while [94midx < _param2:
      mem[0] = [94midx
      mem[32] = 47
      if not unknown9f9de645[[94midx]:
          [94midx = [94midx + 1
          continue 
      require unknown7eae0ccb[[94midx] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != currentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if unknown3767377e != [94midx:
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94ms < 32 * [94m_237:
              mem[[94ms + [94m_231 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_231 + [94m_233 + 32]
              [94ms = [94ms + 32
              continue 
          mem[64] = (32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          while [94ms < ext_call.return_data[0]:
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
              continue 
          if [94midx != currentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if unknown3767377e != [94midx:
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_597 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_597 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
          else:
              require ext_code.size(settingsAddress)
              static call settingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_237) + [94m_231 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(settingsAddress)
              static call settingsAddress.getGames() with:
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
              while [94ms < 32 * [94m_610:
                  mem[[94ms + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_237) + [94m_231 + ceil32(return_data.size) + [94m_605 + 64]
                  [94ms = [94ms + 32
                  continue 
              mem[64] = (32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              while [94ms < ext_call.return_data[0]:
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
                  continue 
              if [94midx != currentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if unknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != currentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if unknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] + unknown3b85bda6[[94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == currentCycle:
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_610) + (32 * [94m_237) + [94m_231 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_877 * ext_call.return_data[0]) + ([94m_597 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_877 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_597 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
      mem[0] = [94midx
      mem[32] = 46
      require unknown7eae0ccb[[94midx] < 11
      require (ext_call.return_data[0] * unknown8e7c820c[stor46[[94midx]] / 100) - unknown7a49f350[[94midx] + unknown9f9de645[[94midx]
      [94midx = [94midx + 1
      continue 
  return 0


# hash = 0x15344630
# getter = None
# const = None
# payable = True
def unknown15344630() payable: 
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  return unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - unknown873426ff[stor8], 
                         0
              return unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                     1
          if stor35[stor8 - 1]:
              if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                  return unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1], 
                         0
              return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                     1
          if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1], 
                     0
          return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not currentCycle:
          if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
              return ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - unknown873426ff[stor8], 
                     0
          return unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                 1
      if stor35[stor8 - 1]:
          if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1], 
                     0
          return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - unknown873426ff[stor8] + unknown873426ff[stor8 - 1], 
                 0
      return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
             1
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  return unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - ([94m_574 * ext_call.return_data[0]), 
                         0
              return unknown9b1c8ec5[stor8] + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                     1
          if stor35[stor8 - 1]:
              if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                  return unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                         0
              return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                     1
          if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not currentCycle:
          if unknown9b1c8ec5[stor8] + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
              return ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - unknown9b1c8ec5[stor8] - ([94m_574 * ext_call.return_data[0]), 
                     0
          return unknown9b1c8ec5[stor8] + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                 1
      if stor35[stor8 - 1]:
          if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - unknown9b1c8ec5[stor8] + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
             1
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  return unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                     1
          if stor35[stor8 - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                  return unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not currentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
              return ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8], 
                 1
      if stor35[stor8 - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
              return ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0]:
                  return unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - ext_call.return_data[0], 
                     1
          if stor35[stor8 - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
                  return unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
              return unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not currentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8]:
              return (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8], 
                 1
      if stor35[stor8 - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
              return (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if currentCycle == currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                  return unknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknownc18df55f - (2 * ext_call.return_data[0]), 
                     1
          if stor35[stor8 - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                  return unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
              return unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not currentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
              return (3 * ext_call.return_data[0]) + unknownc18df55f - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknownc18df55f, 
                 1
      if stor35[stor8 - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
              return (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
             1
  if unknown3767377e != currentCycle:
      if not currentCycle:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[stor8] + (2 * ext_call.return_data[0]):
              return unknown01a32329[stor8] + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[stor8] - (2 * ext_call.return_data[0]), 
                 1
      if stor35[stor8 - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
              return unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
          return unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not currentCycle:
      if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8]:
          return (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                 0
      return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknown01a32329[stor8], 
             1
  if stor35[stor8 - 1]:
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
          return (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
             1
  if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
      return unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[stor8 - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[stor8 - 1], 
             0
  return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1], 
         1


# hash = 0x246d95ca
# getter = None
# const = None
# payable = True
def unknown246d95ca(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknowna88379c6 = _param1


# hash = 0x2623f687
# getter = None
# const = None
# payable = True
def getRevenue(uint256 _amount) payable: 
  require calldata.size - 4 >= 32
  if _amount != currentCycle:
      if unknown3767377e != _amount:
          if not _amount:
              if unknown9b1c8ec5[_amount] + unknown873426ff[_amount] <= unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
                  return unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - unknown9b1c8ec5[_amount] - unknown873426ff[_amount], 
                         0
              return unknown9b1c8ec5[_amount] + unknown873426ff[_amount] - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                     1
          if stor35[_amount - 1]:
              if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] <= unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
                  return unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - unknown873426ff[_amount] + unknown873426ff[_amount - 1], 
                         0
              return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                     1
          if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - unknown873426ff[_amount] + unknown873426ff[_amount - 1], 
                     0
          return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not _amount:
          if unknown9b1c8ec5[_amount] + unknown873426ff[_amount] <= ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
              return ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - unknown9b1c8ec5[_amount] - unknown873426ff[_amount], 
                     0
          return unknown9b1c8ec5[_amount] + unknown873426ff[_amount] - ext_call.return_data[0] - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                 1
      if stor35[_amount - 1]:
          if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] <= ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - unknown873426ff[_amount] + unknown873426ff[_amount - 1], 
                     0
          return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - unknown873426ff[_amount] + unknown873426ff[_amount - 1], 
                 0
      return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + unknown873426ff[_amount] - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
             1
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  if _amount != currentCycle:
      if unknown3767377e != _amount:
          if not _amount:
              if unknown9b1c8ec5[_amount] + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
                  return unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - unknown9b1c8ec5[_amount] - ([94m_574 * ext_call.return_data[0]), 
                         0
              return unknown9b1c8ec5[_amount] + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                     1
          if stor35[_amount - 1]:
              if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
                  return unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                         0
              return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                     1
          if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not _amount:
          if unknown9b1c8ec5[_amount] + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
              return ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - unknown9b1c8ec5[_amount] - ([94m_574 * ext_call.return_data[0]), 
                     0
          return unknown9b1c8ec5[_amount] + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                 1
      if stor35[_amount - 1]:
          if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      if unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - unknown9b1c8ec5[_amount] + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return unknown9b1c8ec5[_amount] - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
             1
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[(32 * [94m_16) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  if _amount != currentCycle:
      if unknown3767377e != _amount:
          if not _amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
                  return unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                     1
          if stor35[_amount - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
                  return unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not _amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount]:
              return ext_call.return_data[0] + unknown01a32329[_amount] + unknown3b85bda6[_amount] + unknown8897c906[_amount] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[_amount] - unknown3b85bda6[_amount] - unknown8897c906[_amount], 
                 1
      if stor35[_amount - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
              return ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + ext_call.return_data[0] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + unknown8897c906[_amount] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - ext_call.return_data[0] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - unknown8897c906[_amount] + unknown8897c906[_amount - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x610fe551 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _amount != currentCycle:
      if unknown3767377e != _amount:
          if not _amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[_amount] + unknown3b85bda6[_amount] + ext_call.return_data[0]:
                  return unknown01a32329[_amount] + unknown3b85bda6[_amount] + ext_call.return_data[0] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[_amount] - unknown3b85bda6[_amount] - ext_call.return_data[0], 
                     1
          if stor35[_amount - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + ext_call.return_data[0] - unknown8897c906[_amount - 1]:
                  return unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + ext_call.return_data[0] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - ext_call.return_data[0] + unknown8897c906[_amount - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + ext_call.return_data[0] - unknown8897c906[_amount - 1]:
              return unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] + ext_call.return_data[0] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] - ext_call.return_data[0] + unknown8897c906[_amount - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not _amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[_amount] + unknown3b85bda6[_amount]:
              return (2 * ext_call.return_data[0]) + unknown01a32329[_amount] + unknown3b85bda6[_amount] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - unknown01a32329[_amount] - unknown3b85bda6[_amount], 
                 1
      if stor35[_amount - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
              return (2 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + unknown3b85bda6[_amount] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - unknown3b85bda6[_amount] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _amount == currentCycle:
      if unknown3767377e != _amount:
          if not _amount:
              if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                  return unknownc18df55f + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                         0
              return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknownc18df55f - (2 * ext_call.return_data[0]), 
                     1
          if stor35[_amount - 1]:
              if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknownc18df55f - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
                  return unknownc18df55f - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                         0
              return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknownc18df55f + unknown01a32329[_amount - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
                     1
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknownc18df55f - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
              return unknowna1825b6a[_amount - 1] + unknownc18df55f - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknownc18df55f + unknown01a32329[_amount - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
                 1
      require ext_code.size(casinoAddress)
      static call casinoAddress.0x397425fb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not _amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
              return (3 * ext_call.return_data[0]) + unknownc18df55f - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknownc18df55f, 
                 1
      if stor35[_amount - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
              return (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[_amount - 1] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[_amount - 1] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
             1
  if unknown3767377e != _amount:
      if not _amount:
          if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= unknown01a32329[_amount] + (2 * ext_call.return_data[0]):
              return unknown01a32329[_amount] + (2 * ext_call.return_data[0]) - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                     0
          return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - unknown01a32329[_amount] - (2 * ext_call.return_data[0]), 
                 1
      if stor35[_amount - 1]:
          if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknown01a32329[_amount] - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
              return unknown01a32329[_amount] - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                     0
          return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
                 1
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
          return unknowna1825b6a[_amount - 1] + unknown01a32329[_amount] - unknown01a32329[_amount - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - unknown01a32329[_amount] + unknown01a32329[_amount - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
             1
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _amount:
      if ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[_amount]:
          return (3 * ext_call.return_data[0]) + unknown01a32329[_amount] - ([94m_1016 * ext_call.return_data[0]) - ([94m_574 * ext_call.return_data[0]), 
                 0
      return ([94m_1016 * ext_call.return_data[0]) + ([94m_574 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknown01a32329[_amount], 
             1
  if stor35[_amount - 1]:
      if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
          return (3 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
                 0
      return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[_amount] + unknown01a32329[_amount - 1] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
             1
  if ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] <= unknowna1825b6a[_amount - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1]:
      return unknowna1825b6a[_amount - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[_amount] - unknown01a32329[_amount - 1] - unknown3b85bda6[_amount - 1] - unknown8897c906[_amount - 1] - ([94m_1016 * ext_call.return_data[0]) + unknown9b1c8ec5[_amount - 1] - ([94m_574 * ext_call.return_data[0]) + unknown873426ff[_amount - 1], 
             0
  return ([94m_1016 * ext_call.return_data[0]) - unknown9b1c8ec5[_amount - 1] + ([94m_574 * ext_call.return_data[0]) - unknown873426ff[_amount - 1] - unknowna1825b6a[_amount - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[_amount] + unknown01a32329[_amount - 1] + unknown3b85bda6[_amount - 1] + unknown8897c906[_amount - 1], 
         1


# hash = 0x26f35b85
# getter = None
# const = None
# payable = True
def unknown26f35b85(uint256 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 < 11
  unknownc563af55[_param1] = _param2


# hash = 0x2e17de78
# getter = None
# const = None
# payable = True
def unknown2e17de78(uint256 _param1) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 32
  require block.number >= unknown624d1b1f[caller]
  require _param1 <= unknowna5b39cfb[caller]
  require currentCycle <= currentCycle
  mem[0] = caller
  mem[32] = 36
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = unknown84bcd3c6[caller]
  while [94midx < currentCycle:
      mem[0] = [94midx
      mem[32] = 47
      if not unknown9f9de645[[94midx]:
          [94midx = [94midx + 1
          continue 
      require unknown7eae0ccb[[94midx] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != currentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if unknown3767377e != [94midx:
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94ms < 32 * [94m_251:
              mem[[94ms + [94m_245 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_245 + [94m_247 + 32]
              [94ms = [94ms + 32
              continue 
          mem[64] = (32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          while [94ms < ext_call.return_data[0]:
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
              continue 
          if [94midx != currentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if unknown3767377e != [94midx:
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_611 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_611 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
          else:
              require ext_code.size(settingsAddress)
              static call settingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_251) + [94m_245 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(settingsAddress)
              static call settingsAddress.getGames() with:
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
              while [94ms < 32 * [94m_624:
                  mem[[94ms + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_251) + [94m_245 + ceil32(return_data.size) + [94m_619 + 64]
                  [94ms = [94ms + 32
                  continue 
              mem[64] = (32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              while [94ms < ext_call.return_data[0]:
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
                  continue 
              if [94midx != currentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if unknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != currentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if unknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] + unknown3b85bda6[[94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == currentCycle:
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_624) + (32 * [94m_251) + [94m_245 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_891 * ext_call.return_data[0]) + ([94m_611 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_891 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_611 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
      mem[0] = [94midx
      mem[32] = 46
      require unknown7eae0ccb[[94midx] < 11
      require (ext_call.return_data[0] * unknown8e7c820c[stor46[[94midx]] / 100) - unknown7a49f350[[94midx] + unknown9f9de645[[94midx]
      [94midx = [94midx + 1
      continue 
  require _param1 <= unknowna5b39cfb[caller]
  unknowna5b39cfb[caller] -= _param1
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown84bcd3c6[caller] = currentCycle
  totalStaked -= _param1
  log 0x9845e367: _param1, caller


# hash = 0x31e5901b
# getter = None
# const = None
# payable = True
def unknown31e5901b() payable: 
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  return ([94m_37 * ext_call.return_data[0])


# hash = 0x33ae47ea
# getter = None
# const = None
# payable = True
def unknown33ae47ea(uint256 _param1, uint256 _param2, bool _param3, uint256 _param4) payable: 
  require calldata.size - 4 >= 224
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xfcddaa0c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_code.size(settingsAddress)
      static call settingsAddress.0xd77a3c5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if _param4 >= 101:
              require _param3
              require _param2 - _param1
              require _param3
              revert
          else:
              require _param3
              require _param2 - _param1
              require _param3
              revert


# hash = 0x3767377e
# getter = ['storage', 256, 0, 12]
# const = None
# payable = True
def unknown3767377e() payable: 
  return unknown3767377e


# hash = 0x38c67b73
# getter = None
# const = None
# payable = True
def setCurrentStage(uint256 _stage) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  currentStage = _stage


# hash = 0x38cff46e
# getter = None
# const = None
# payable = True
def unknown38cff46e(uint256 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 < 11
  unknown8e7c820c[_param1] = _param2


# hash = 0x3b85bda6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 44]]]
# const = None
# payable = True
def unknown3b85bda6(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown3b85bda6[_param1]


# hash = 0x3f60f1f3
# getter = None
# const = None
# payable = True
def unknown3f60f1f3(addr _param1, uint256 _param2) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 64
  require _param2 <= currentCycle
  mem[0] = _param1
  mem[32] = 36
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = unknown84bcd3c6[addr(_param1)]
  while [94midx < _param2:
      mem[0] = [94midx
      mem[32] = 47
      if not unknown9f9de645[[94midx]:
          [94midx = [94midx + 1
          continue 
      require unknown7eae0ccb[[94midx] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != currentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if unknown3767377e != [94midx:
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94ms < 32 * [94m_233:
              mem[[94ms + [94m_227 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_227 + [94m_229 + 32]
              [94ms = [94ms + 32
              continue 
          mem[64] = (32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          while [94ms < ext_call.return_data[0]:
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
              continue 
          if [94midx != currentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if unknown3767377e != [94midx:
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_593 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_593 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
          else:
              require ext_code.size(settingsAddress)
              static call settingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_233) + [94m_227 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(settingsAddress)
              static call settingsAddress.getGames() with:
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
              while [94ms < 32 * [94m_606:
                  mem[[94ms + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_233) + [94m_227 + ceil32(return_data.size) + [94m_601 + 64]
                  [94ms = [94ms + 32
                  continue 
              mem[64] = (32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              while [94ms < ext_call.return_data[0]:
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
                  continue 
              if [94midx != currentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if unknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != currentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if unknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] + unknown3b85bda6[[94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == currentCycle:
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_606) + (32 * [94m_233) + [94m_227 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_873 * ext_call.return_data[0]) + ([94m_593 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_873 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_593 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
      mem[0] = [94midx
      mem[32] = 46
      require unknown7eae0ccb[[94midx] < 11
      require (ext_call.return_data[0] * unknown8e7c820c[stor46[[94midx]] / 100) - unknown7a49f350[[94midx] + unknown9f9de645[[94midx]
      [94midx = [94midx + 1
      continue 


# hash = 0x4068ed2b
# getter = None
# const = None
# payable = True
def unknown4068ed2b(addr _param1) payable: 
  require calldata.size - 4 >= 32
  mem[0] = _param1
  mem[32] = 36
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknowna5b39cfb[addr(_param1)]:
      return 0
  require currentStage < 11
  mem[100] = tokenHolderAddress
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  return 0
              if currentStage < 11:
                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                      return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
          else:
              if stor35[stor8 - 1]:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
      else:
          require ext_code.size(casinoAddress)
          static call casinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not currentCycle:
              if unknown9b1c8ec5[stor8] + unknown873426ff[stor8] <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                  return 0
              if currentStage < 11:
                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                      return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
          else:
              if stor35[stor8 - 1]:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + (unknown873426ff[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
  else:
      require ext_code.size(settingsAddress)
      static call settingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(settingsAddress)
      static call settingsAddress.getGames() with:
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
      while [94midx < ext_call.return_data[0]:
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
          continue 
      if currentCycle != currentCycle:
          if unknown3767377e != currentCycle:
              if not currentCycle:
                  if unknown9b1c8ec5[stor8] + ([94m_589 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  if stor35[stor8 - 1]:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not currentCycle:
                  if unknown9b1c8ec5[stor8] + ([94m_589 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                      return 0
                  if currentStage < 11:
                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                          return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  if stor35[stor8 - 1]:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      if unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return ((unknown9b1c8ec5[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_31) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94midx < ext_call.return_data[0]:
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
              continue 
          if currentCycle != currentCycle:
              if unknown3767377e != currentCycle:
                  if not currentCycle:
                      if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      if stor35[stor8 - 1]:
                          if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not currentCycle:
                      if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]:
                          return 0
                      if currentStage < 11:
                          if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                              return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      if stor35[stor8 - 1]:
                          if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown8897c906[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if currentCycle != currentCycle:
                  if unknown3767377e != currentCycle:
                      if not currentCycle:
                          if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          if stor35[stor8 - 1]:
                              if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not currentCycle:
                          if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8]:
                              return 0
                          if currentStage < 11:
                              if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                  return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          if stor35[stor8 - 1]:
                              if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown3b85bda6[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if currentCycle == currentCycle:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknownc18df55f * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                  else:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= unknown01a32329[stor8] + (2 * ext_call.return_data[0]):
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              if ([94m_1031 * ext_call.return_data[0]) + ([94m_589 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8]:
                                  return 0
                              if currentStage < 11:
                                  if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                      return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                          else:
                              if stor35[stor8 - 1]:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
                              else:
                                  if ([94m_1031 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_589 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] <= unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]:
                                      return 0
                                  if currentStage < 11:
                                      if (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked:
                                          return (([94m_1031 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown9b1c8ec5[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) + ([94m_589 * ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown873426ff[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (unknowna1825b6a[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) - (unknown01a32329[stor8] * unknowna5b39cfb[addr(_param1)]) + (unknown01a32329[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown3b85bda6[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) - (ext_call.return_data[0] * unknowna5b39cfb[addr(_param1)]) + (unknown8897c906[stor8 - 1] * unknowna5b39cfb[addr(_param1)]) / (ext_call.return_data[0] * unknown8e7c820c[stor7] / 100) + totalStaked * unknown8e7c820c[stor7] / 100)
  revert


# hash = 0x420a83e7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def tokenHolder() payable: 
  return tokenHolderAddress


# hash = 0x5bf5d54c
# getter = ['storage', 256, 0, 7]
# const = None
# payable = True
def currentStage() payable: 
  return currentStage


# hash = 0x624d1b1f
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 37]]]
# const = None
# payable = True
def unknown624d1b1f(addr _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown624d1b1f[_param1]


# hash = 0x65e86f0c
# getter = None
# const = None
# payable = True
def unknown65e86f0c() payable: 
  require currentStage < 11
  return (10^18 * unknownc563af55[stor7])


# hash = 0x7710c6d8
# getter = None
# const = None
# payable = True
def unknown7710c6d8(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown8209e742 = _param1


# hash = 0x7a49f350
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 39]]]
# const = None
# payable = True
def unknown7a49f350(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown7a49f350[_param1]


# hash = 0x7eae0ccb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 46]]]
# const = None
# payable = True
def unknown7eae0ccb(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown7eae0ccb[_param1]


# hash = 0x817b1cd2
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def totalStaked() payable: 
  return totalStaked


# hash = 0x81f83692
# getter = ['storage', 256, 0, 10]
# const = None
# payable = True
def unknown81f83692() payable: 
  return unknown81f83692


# hash = 0x8209e742
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def unknown8209e742() payable: 
  return unknown8209e742


# hash = 0x84bcd3c6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 38]]]
# const = None
# payable = True
def unknown84bcd3c6(addr _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown84bcd3c6[_param1]


# hash = 0x873426ff
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 41]]]
# const = None
# payable = True
def unknown873426ff(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown873426ff[_param1]


# hash = 0x87e0e9ab
# getter = None
# const = None
# payable = True
def unknown87e0e9ab() payable: 
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x236e5e4c with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x8897c906
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 43]]]
# const = None
# payable = True
def unknown8897c906(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown8897c906[_param1]


# hash = 0x8e7c820c
# getter = ['storage', 256, 0, ['add', 13, ['cd', 4]]]
# const = None
# payable = True
def unknown8e7c820c(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 < 11
  return unknown8e7c820c[_param1]


# hash = 0x9403e8dd
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def casino() payable: 
  return casinoAddress


# hash = 0x9b1c8ec5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 42]]]
# const = None
# payable = True
def unknown9b1c8ec5(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown9b1c8ec5[_param1]


# hash = 0x9f9de645
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 47]]]
# const = None
# payable = True
def unknown9f9de645(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown9f9de645[_param1]


# hash = 0xa1825b6a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 40]]]
# const = None
# payable = True
def unknowna1825b6a(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknowna1825b6a[_param1]


# hash = 0xa5b39cfb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 36]]]
# const = None
# payable = True
def unknowna5b39cfb(addr _param1) payable: 
  require calldata.size - 4 >= 32
  return unknowna5b39cfb[_param1]


# hash = 0xa694fc3a
# getter = None
# const = None
# payable = True
def stake(uint256 _amount) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 32
  require currentCycle <= currentCycle
  mem[0] = caller
  mem[32] = 36
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
          gas gas_remaining wei
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = unknown84bcd3c6[caller]
  while [94midx < currentCycle:
      mem[0] = [94midx
      mem[32] = 47
      if not unknown9f9de645[[94midx]:
          [94midx = [94midx + 1
          continue 
      require unknown7eae0ccb[[94midx] < 11
      mem[0] = [94midx
      mem[32] = 39
      if [94midx != currentCycle:
          mem[0] = [94midx
          mem[32] = 45
          if unknown3767377e != [94midx:
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not [94midx:
                  if unknown9b1c8ec5[[94midx] + unknown873426ff[[94midx] <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                      [94midx = [94midx + 1
                      continue 
              else:
                  mem[0] = [94midx - 1
                  mem[32] = 35
                  if stor35[[94midx - 1]:
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 40
                      if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + unknown873426ff[[94midx] - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                          [94midx = [94midx + 1
                          continue 
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94ms < 32 * [94m_249:
              mem[[94ms + [94m_243 + ceil32(return_data.size) + 32] = mem[[94ms + [94m_243 + [94m_245 + 32]
              [94ms = [94ms + 32
              continue 
          mem[64] = (32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32
          [94ms = 0
          [94mt = 0
          while [94ms < ext_call.return_data[0]:
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
              continue 
          if [94midx != currentCycle:
              mem[0] = [94midx
              mem[32] = 45
              if unknown3767377e != [94midx:
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_609 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94midx:
                      if unknown9b1c8ec5[[94midx] + ([94m_609 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[0] = [94midx - 1
                      mem[32] = 35
                      if stor35[[94midx - 1]:
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94midx] - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                              [94midx = [94midx + 1
                              continue 
          else:
              require ext_code.size(settingsAddress)
              static call settingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[(32 * [94m_249) + [94m_243 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(settingsAddress)
              static call settingsAddress.getGames() with:
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
              while [94ms < 32 * [94m_622:
                  mem[[94ms + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = mem[[94ms + (32 * [94m_249) + [94m_243 + ceil32(return_data.size) + [94m_617 + 64]
                  [94ms = [94ms + 32
                  continue 
              mem[64] = (32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64
              [94ms = 0
              [94mt = 0
              while [94ms < ext_call.return_data[0]:
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
                  continue 
              if [94midx != currentCycle:
                  mem[0] = [94midx
                  mem[32] = 45
                  if unknown3767377e != [94midx:
                      if not [94midx:
                          if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94midx:
                          if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + unknown8897c906[[94midx]:
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = [94midx - 1
                          mem[32] = 35
                          if stor35[[94midx - 1]:
                              if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 40
                              if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + ext_call.return_data[0] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + unknown8897c906[[94midx] - unknown8897c906[[94midx - 1]:
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x610fe551 with:
                          gas gas_remaining wei
                  mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if [94midx != currentCycle:
                      mem[0] = [94midx
                      mem[32] = 45
                      if unknown3767377e != [94midx:
                          if not [94midx:
                              if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + unknown3b85bda6[[94midx] + ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] + ext_call.return_data[0] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94midx:
                              if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] + unknown3b85bda6[[94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = [94midx - 1
                              mem[32] = 35
                              if stor35[[94midx - 1]:
                                  if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 40
                                  if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + unknown3b85bda6[[94midx] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                      [94midx = [94midx + 1
                                      continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x236e5e4c with:
                              gas gas_remaining wei
                      mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94midx == currentCycle:
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknownc18df55f - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                      else:
                          mem[0] = [94midx
                          mem[32] = 45
                          if unknown3767377e != [94midx:
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= unknown01a32329[[94midx] + (2 * ext_call.return_data[0]):
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_622) + (32 * [94m_249) + [94m_243 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94midx:
                                  if ([94m_889 * ext_call.return_data[0]) + ([94m_609 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  mem[0] = [94midx - 1
                                  mem[32] = 35
                                  if stor35[[94midx - 1]:
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[0] = [94midx - 1
                                      mem[32] = 40
                                      if ([94m_889 * ext_call.return_data[0]) - unknown9b1c8ec5[[94midx - 1] + ([94m_609 * ext_call.return_data[0]) - unknown873426ff[[94midx - 1] <= unknowna1825b6a[[94midx - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[[94midx] - unknown01a32329[[94midx - 1] - unknown3b85bda6[[94midx - 1] - unknown8897c906[[94midx - 1]:
                                          [94midx = [94midx + 1
                                          continue 
      mem[0] = [94midx
      mem[32] = 46
      require unknown7eae0ccb[[94midx] < 11
      require (ext_call.return_data[0] * unknown8e7c820c[stor46[[94midx]] / 100) - unknown7a49f350[[94midx] + unknown9f9de645[[94midx]
      [94midx = [94midx + 1
      continue 
  unknown624d1b1f[caller] = unknowna88379c6 + block.number
  require ext_code.size(tokenAddress)
  call tokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, this.address, _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknowna5b39cfb[caller] += _amount
  unknown84bcd3c6[caller] = currentCycle
  totalStaked += _amount
  log 0xb539ca1e: _amount, caller


# hash = 0xa88379c6
# getter = ['storage', 256, 0, 5]
# const = None
# payable = True
def unknowna88379c6() payable: 
  return unknowna88379c6


# hash = 0xbab2f552
# getter = ['storage', 256, 0, 8]
# const = None
# payable = True
def currentCycle() payable: 
  return currentCycle


# hash = 0xbc105ab5
# getter = None
# const = None
# payable = True
def unknownbc105ab5(addr _param1) payable: 
  require calldata.size - 4 >= 32
  mem[100] = caller
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x397425fb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(casinoAddress)
  static call casinoAddress.0xbd874dff with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if currentCycle != currentCycle:
      if unknown3767377e != currentCycle:
          if not currentCycle:
              require unknown9b1c8ec5[stor8] + unknown873426ff[stor8] > unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
              require ext_code.size(settingsAddress)
              static call settingsAddress.0x12d15611 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              if stor35[stor8 - 1]:
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] > unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
      else:
          require ext_code.size(casinoAddress)
          static call casinoAddress.0x397425fb with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not currentCycle:
              require unknown9b1c8ec5[stor8] + unknown873426ff[stor8] > ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
              require ext_code.size(settingsAddress)
              static call settingsAddress.0x12d15611 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require unknown9b1c8ec5[stor8] + unknown873426ff[stor8] - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              if stor35[stor8 - 1]:
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] > ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + unknown873426ff[stor8] - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
  else:
      require ext_code.size(settingsAddress)
      static call settingsAddress.0xdd2f4ebd with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
      require ext_code.size(settingsAddress)
      static call settingsAddress.getGames() with:
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
      while [94midx < ext_call.return_data[0]:
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
          continue 
      if currentCycle != currentCycle:
          if unknown3767377e != currentCycle:
              if not currentCycle:
                  require unknown9b1c8ec5[stor8] + ([94m_784 * ext_call.return_data[0]) > unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] + ([94m_784 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  if stor35[stor8 - 1]:
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x397425fb with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not currentCycle:
                  require unknown9b1c8ec5[stor8] + ([94m_784 * ext_call.return_data[0]) > ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0x12d15611 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require unknown9b1c8ec5[stor8] + ([94m_784 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  if stor35[stor8 - 1]:
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require unknown9b1c8ec5[stor8] - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
      else:
          require ext_code.size(settingsAddress)
          static call settingsAddress.0xdd2f4ebd with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[(32 * [94m_28) + ceil32(return_data.size) + 128] = 0xc04c594700000000000000000000000000000000000000000000000000000000
          require ext_code.size(settingsAddress)
          static call settingsAddress.getGames() with:
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
          while [94midx < ext_call.return_data[0]:
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
              continue 
          if currentCycle != currentCycle:
              if unknown3767377e != currentCycle:
                  if not currentCycle:
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if stor35[stor8 - 1]:
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not currentCycle:
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > ext_call.return_data[0] + unknown01a32329[stor8] + unknown3b85bda6[stor8] + unknown8897c906[stor8]
                      require ext_code.size(settingsAddress)
                      static call settingsAddress.0x12d15611 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - ext_call.return_data[0] - unknown01a32329[stor8] - unknown3b85bda6[stor8] - unknown8897c906[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if stor35[stor8 - 1]:
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + ext_call.return_data[0] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8] - unknown8897c906[stor8 - 1]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - ext_call.return_data[0] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
          else:
              require ext_code.size(casinoAddress)
              static call casinoAddress.0x610fe551 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if currentCycle != currentCycle:
                  if unknown3767377e != currentCycle:
                      if not currentCycle:
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > unknown01a32329[stor8] + unknown3b85bda6[stor8] + ext_call.return_data[0]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] - ext_call.return_data[0] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          if stor35[stor8 - 1]:
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] + ext_call.return_data[0] - unknown8897c906[stor8 - 1]
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] - ext_call.return_data[0] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not currentCycle:
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (2 * ext_call.return_data[0]) + unknown01a32329[stor8] + unknown3b85bda6[stor8]
                          require ext_code.size(settingsAddress)
                          static call settingsAddress.0x12d15611 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] - unknown3b85bda6[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          if stor35[stor8 - 1]:
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (2 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x236e5e4c with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if currentCycle == currentCycle:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > unknownc18df55f + (2 * ext_call.return_data[0])
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - unknownc18df55f - (2 * ext_call.return_data[0]) > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if stor35[stor8 - 1]:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknownc18df55f - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknownc18df55f + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (3 * ext_call.return_data[0]) + unknownc18df55f
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknownc18df55f > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if stor35[stor8 - 1]:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknownc18df55f + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                  else:
                      if unknown3767377e != currentCycle:
                          if not currentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > unknown01a32329[stor8] + (2 * ext_call.return_data[0])
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - unknown01a32329[stor8] - (2 * ext_call.return_data[0]) > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if stor35[stor8 - 1]:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] - (2 * ext_call.return_data[0]) + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not currentCycle:
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) > (3 * ext_call.return_data[0]) + unknown01a32329[stor8]
                              require ext_code.size(settingsAddress)
                              static call settingsAddress.0x12d15611 with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ([94m_1388 * ext_call.return_data[0]) + ([94m_784 * ext_call.return_data[0]) - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] > ext_call.return_data[0] * ext_call.return_data[0]
                          else:
                              if stor35[stor8 - 1]:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
                              else:
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] > unknowna1825b6a[stor8 - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[stor8] - unknown01a32329[stor8 - 1] - unknown3b85bda6[stor8 - 1] - unknown8897c906[stor8 - 1]
                                  require ext_code.size(settingsAddress)
                                  static call settingsAddress.0x12d15611 with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ([94m_1388 * ext_call.return_data[0]) - unknown9b1c8ec5[stor8 - 1] + ([94m_784 * ext_call.return_data[0]) - unknown873426ff[stor8 - 1] - unknowna1825b6a[stor8 - 1] - (3 * ext_call.return_data[0]) - unknown01a32329[stor8] + unknown01a32329[stor8 - 1] + unknown3b85bda6[stor8 - 1] + unknown8897c906[stor8 - 1] > ext_call.return_data[0] * ext_call.return_data[0]
  call _param1 with:
     value ext_call.return_data[0] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(casinoAddress)
  call casinoAddress.0xc63e0c05 with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknown3767377e = currentCycle


# hash = 0xc18df55f
# getter = ['storage', 256, 0, 11]
# const = None
# payable = True
def unknownc18df55f() payable: 
  return unknownc18df55f


# hash = 0xc563af55
# getter = ['storage', 256, 0, ['add', 24, ['cd', 4]]]
# const = None
# payable = True
def unknownc563af55(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 < 11
  return unknownc563af55[_param1]


# hash = 0xcaa9828c
# getter = None
# const = None
# payable = True
def unknowncaa9828c(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown0a6554e9Address = _param1


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def settings() payable: 
  return settingsAddress


# hash = 0xe0aecca7
# getter = None
# const = None
# payable = True
def unknowne0aecca7(array _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[64] = (32 * _param1.length) + 128
  mem[96] = _param1.length
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = 0
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < mem[96]
      require _param2 <= currentCycle
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 36
      require ext_code.size(tokenAddress)
      static call tokenAddress.totalSupply() with:
              gas gas_remaining wei
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94ms = unknown84bcd3c6[mem[0]]
      while [94ms < _param2:
          mem[0] = [94ms
          mem[32] = 47
          if not unknown9f9de645[[94ms]:
              [94ms = [94ms + 1
              continue 
          require unknown7eae0ccb[[94ms] < 11
          mem[0] = [94ms
          mem[32] = 39
          if [94ms != currentCycle:
              mem[0] = [94ms
              mem[32] = 45
              if unknown3767377e != [94ms:
                  if not [94ms:
                      if unknown9b1c8ec5[[94ms] + unknown873426ff[[94ms] <= unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                          [94ms = [94ms + 1
                          continue 
                  else:
                      mem[0] = [94ms - 1
                      mem[32] = 35
                      if stor35[[94ms - 1]:
                          if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + unknown873426ff[[94ms] - unknown873426ff[[94ms - 1] <= unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                              [94ms = [94ms + 1
                              continue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + unknown873426ff[[94ms] - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                              [94ms = [94ms + 1
                              continue 
              else:
                  require ext_code.size(casinoAddress)
                  static call casinoAddress.0x397425fb with:
                          gas gas_remaining wei
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not [94ms:
                      if unknown9b1c8ec5[[94ms] + unknown873426ff[[94ms] <= ext_call.return_data[0] + unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                          [94ms = [94ms + 1
                          continue 
                  else:
                      mem[0] = [94ms - 1
                      mem[32] = 35
                      if stor35[[94ms - 1]:
                          if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + unknown873426ff[[94ms] - unknown873426ff[[94ms - 1] <= ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                              [94ms = [94ms + 1
                              continue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 40
                          if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + unknown873426ff[[94ms] - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                              [94ms = [94ms + 1
                              continue 
          else:
              require ext_code.size(settingsAddress)
              static call settingsAddress.0xdd2f4ebd with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[mem[64]] = 0xc04c594700000000000000000000000000000000000000000000000000000000
              require ext_code.size(settingsAddress)
              static call settingsAddress.getGames() with:
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
              while [94midx < 32 * [94m_452:
                  mem[[94midx + [94m_446 + ceil32(return_data.size) + 32] = mem[[94midx + [94m_446 + [94m_448 + 32]
                  [94midx = [94midx + 32
                  continue 
              mem[64] = (32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32
              [94midx = 0
              [94mt = 0
              while [94midx < ext_call.return_data[0]:
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
                  continue 
              if [94ms != currentCycle:
                  mem[0] = [94ms
                  mem[32] = 45
                  if unknown3767377e != [94ms:
                      if not [94ms:
                          if unknown9b1c8ec5[[94ms] + ([94m_812 * ext_call.return_data[0]) <= unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                              [94ms = [94ms + 1
                              continue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 35
                          if stor35[[94ms - 1]:
                              if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                  [94ms = [94ms + 1
                                  continue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 40
                              if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                  [94ms = [94ms + 1
                                  continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x397425fb with:
                              gas gas_remaining wei
                      mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not [94ms:
                          if unknown9b1c8ec5[[94ms] + ([94m_812 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                              [94ms = [94ms + 1
                              continue 
                      else:
                          mem[0] = [94ms - 1
                          mem[32] = 35
                          if stor35[[94ms - 1]:
                              if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                  [94ms = [94ms + 1
                                  continue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 40
                              if unknown9b1c8ec5[[94ms] - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                  [94ms = [94ms + 1
                                  continue 
              else:
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.0xdd2f4ebd with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[(32 * [94m_452) + [94m_446 + ceil32(return_data.size) + 32] = 0xc04c594700000000000000000000000000000000000000000000000000000000
                  require ext_code.size(settingsAddress)
                  static call settingsAddress.getGames() with:
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
                  while [94midx < 32 * [94m_825:
                      mem[[94midx + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = mem[[94midx + (32 * [94m_452) + [94m_446 + ceil32(return_data.size) + [94m_820 + 64]
                      [94midx = [94midx + 32
                      continue 
                  mem[64] = (32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64
                  [94midx = 0
                  [94mt = 0
                  while [94midx < ext_call.return_data[0]:
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
                      continue 
                  if [94ms != currentCycle:
                      mem[0] = [94ms
                      mem[32] = 45
                      if unknown3767377e != [94ms:
                          if not [94ms:
                              if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                                  [94ms = [94ms + 1
                                  continue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 35
                              if stor35[[94ms - 1]:
                                  if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                      [94ms = [94ms + 1
                                      continue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 40
                                  if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                      [94ms = [94ms + 1
                                      continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x397425fb with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not [94ms:
                              if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= ext_call.return_data[0] + unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + unknown8897c906[[94ms]:
                                  [94ms = [94ms + 1
                                  continue 
                          else:
                              mem[0] = [94ms - 1
                              mem[32] = 35
                              if stor35[[94ms - 1]:
                                  if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                      [94ms = [94ms + 1
                                      continue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 40
                                  if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + ext_call.return_data[0] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + unknown8897c906[[94ms] - unknown8897c906[[94ms - 1]:
                                      [94ms = [94ms + 1
                                      continue 
                  else:
                      require ext_code.size(casinoAddress)
                      static call casinoAddress.0x610fe551 with:
                              gas gas_remaining wei
                      mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if [94ms != currentCycle:
                          mem[0] = [94ms
                          mem[32] = 45
                          if unknown3767377e != [94ms:
                              if not [94ms:
                                  if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= unknown01a32329[[94ms] + unknown3b85bda6[[94ms] + ext_call.return_data[0]:
                                      [94ms = [94ms + 1
                                      continue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 35
                                  if stor35[[94ms - 1]:
                                      if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + ext_call.return_data[0] - unknown8897c906[[94ms - 1]:
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 40
                                      if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] + ext_call.return_data[0] - unknown8897c906[[94ms - 1]:
                                          [94ms = [94ms + 1
                                          continue 
                          else:
                              require ext_code.size(casinoAddress)
                              static call casinoAddress.0x397425fb with:
                                      gas gas_remaining wei
                              mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not [94ms:
                                  if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (2 * ext_call.return_data[0]) + unknown01a32329[[94ms] + unknown3b85bda6[[94ms]:
                                      [94ms = [94ms + 1
                                      continue 
                              else:
                                  mem[0] = [94ms - 1
                                  mem[32] = 35
                                  if stor35[[94ms - 1]:
                                      if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= (2 * ext_call.return_data[0]) + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 40
                                      if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + (2 * ext_call.return_data[0]) + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + unknown3b85bda6[[94ms] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                          [94ms = [94ms + 1
                                          continue 
                      else:
                          require ext_code.size(casinoAddress)
                          static call casinoAddress.0x236e5e4c with:
                                  gas gas_remaining wei
                          mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if [94ms == currentCycle:
                              if unknown3767377e != [94ms:
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= unknownc18df55f + (2 * ext_call.return_data[0]):
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if stor35[[94ms - 1]:
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknownc18df55f - unknown01a32329[[94ms - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknownc18df55f - unknown01a32329[[94ms - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                              else:
                                  require ext_code.size(casinoAddress)
                                  static call casinoAddress.0x397425fb with:
                                          gas gas_remaining wei
                                  mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknownc18df55f:
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if stor35[[94ms - 1]:
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94ms - 1] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + (3 * ext_call.return_data[0]) + unknownc18df55f - unknown01a32329[[94ms - 1] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                          else:
                              mem[0] = [94ms
                              mem[32] = 45
                              if unknown3767377e != [94ms:
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= unknown01a32329[[94ms] + (2 * ext_call.return_data[0]):
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if stor35[[94ms - 1]:
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] + (2 * ext_call.return_data[0]) - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                              else:
                                  require ext_code.size(casinoAddress)
                                  static call casinoAddress.0x397425fb with:
                                          gas gas_remaining wei
                                  mem[(32 * [94m_825) + (32 * [94m_452) + [94m_446 + (2 * ceil32(return_data.size)) + 64] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if not [94ms:
                                      if ([94m_1092 * ext_call.return_data[0]) + ([94m_812 * ext_call.return_data[0]) <= (3 * ext_call.return_data[0]) + unknown01a32329[[94ms]:
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      mem[0] = [94ms - 1
                                      mem[32] = 35
                                      if stor35[[94ms - 1]:
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= (3 * ext_call.return_data[0]) + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
                                      else:
                                          mem[0] = [94ms - 1
                                          mem[32] = 40
                                          if ([94m_1092 * ext_call.return_data[0]) - unknown9b1c8ec5[[94ms - 1] + ([94m_812 * ext_call.return_data[0]) - unknown873426ff[[94ms - 1] <= unknowna1825b6a[[94ms - 1] + (3 * ext_call.return_data[0]) + unknown01a32329[[94ms] - unknown01a32329[[94ms - 1] - unknown3b85bda6[[94ms - 1] - unknown8897c906[[94ms - 1]:
                                              [94ms = [94ms + 1
                                              continue 
          mem[0] = [94ms
          mem[32] = 46
          require unknown7eae0ccb[[94ms] < 11
          require (ext_call.return_data[0] * unknown8e7c820c[stor46[[94ms]] / 100) - unknown7a49f350[[94ms] + unknown9f9de645[[94ms]
          [94ms = [94ms + 1
          continue 
      [94midx = [94midx + 1
      continue 


# hash = 0xe239b026
# getter = None
# const = None
# payable = True
def unknowne239b026() payable: 
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xdd2f4ebd with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[96] = 0xc04c594700000000000000000000000000000000000000000000000000000000
  require ext_code.size(settingsAddress)
  static call settingsAddress.getGames() with:
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
  while [94midx < ext_call.return_data[0]:
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
      continue 
  return ([94m_37 * ext_call.return_data[0])


# hash = 0xf145ff23
# getter = None
# const = None
# payable = True
def getDistributedTokens() payable: 
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args tokenHolderAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(tokenAddress)
  static call tokenAddress.totalSupply() with:
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
  return tokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


