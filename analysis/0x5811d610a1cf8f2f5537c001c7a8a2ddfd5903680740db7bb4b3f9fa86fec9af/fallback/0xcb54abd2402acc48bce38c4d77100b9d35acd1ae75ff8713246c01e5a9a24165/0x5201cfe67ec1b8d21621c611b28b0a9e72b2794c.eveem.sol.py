# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5201cFe67eC1B8D21621C611B28b0a9e72B2794C 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    unknown2a46f2c5Address # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    nameFee # mask: a s
    # storage address 4
    gameIDs_
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    pIDxAddr_
    # storage address 8
    pIDxName_
    # storage address 9
    playerAddr
    # storage address 10
    stor10
    # storage address 11
    plyrNameList_
# hash = 0x10f01eba
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def pIDxAddr_(address _param1): # not payable
  return uint256(pIDxAddr_[_param1])


# hash = 0x2614195f
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def getNameFee(): # not payable
  return nameFee


# hash = 0x2660316e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 10]]]]]]
# const = None
# payable = False
def plyrNames_(uint256 _param1, bytes32 _param2): # not payable
  return bool(stor10[_param1][_param2])


# hash = 0x2a46f2c5
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown2a46f2c5(): # not payable
  require caller == stor0
  return unknown2a46f2c5Address


# hash = 0x2e0e0349
# getter = None
# const = None
# payable = False
def unknown2e0e0349(addr _param1): # not payable
  require caller == stor0
  if gameIDs_[addr(_param1)]:
      revert with 0, 'game already registed'
  stor5++
  gameIDs_[addr(_param1)] = stor5 + 1


# hash = 0x2e19ebdc
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def pIDxName_(bytes32 _param1): # not payable
  return pIDxName_[_param1]


# hash = 0x3ddd4698
# getter = None
# const = None
# payable = True
def registerNameXaddr(string _nameString, address _affCode, bool _all) payable: 
  mem[64] = ceil32(_nameString.length) + 128
  mem[96] = _nameString.length
  mem[128 len _nameString.length] = _nameString[all]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < nameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if _nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _nameString.length - 1 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < _nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _nameString.length:
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(pIDxAddr_[caller]):
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          playerAddr[uint256(stor7[caller])].field_512 = 2
          if not stor10[uint256(stor7[caller])][mem[128]]:
              stor10[uint256(stor7[caller])][mem[128]] = 1
              playerAddr[uint256(stor7[caller])].field_768++
              plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                uint256 amountPaid=caller,
                uint256 timeStamp=mem[128])
      else:
          if _affCode == caller:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if uint256(pIDxAddr_[addr(_affCode)]) != playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = uint256(pIDxAddr_[addr(_affCode)])
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not uint256(pIDxAddr_[addr(_affCode)]):
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=uint256(pIDxAddr_[addr(_affCode)]),
                    bytes32 playerName=playerAddr[uint256(stor7[addr(_affCode)])].field_0,
                    bool isNewPlayer=playerAddr[uint256(stor7[addr(_affCode)])].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
  else:
      stor6++
      uint256(pIDxAddr_[caller]) = stor6 + 1
      playerAddr[stor6 + 1].field_0 = caller
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          playerAddr[uint256(stor7[caller])].field_512 = 2
          if not stor10[uint256(stor7[caller])][mem[128]]:
              stor10[uint256(stor7[caller])][mem[128]] = 1
              playerAddr[uint256(stor7[caller])].field_768++
              plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=1,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                uint256 amountPaid=caller,
                uint256 timeStamp=mem[128])
      else:
          if _affCode == caller:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if uint256(pIDxAddr_[addr(_affCode)]) != playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = uint256(pIDxAddr_[addr(_affCode)])
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not uint256(pIDxAddr_[addr(_affCode)]):
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=uint256(pIDxAddr_[addr(_affCode)]),
                    bytes32 playerName=playerAddr[uint256(stor7[addr(_affCode)])].field_0,
                    bool isNewPlayer=playerAddr[uint256(stor7[addr(_affCode)])].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])


# hash = 0x4d0d35ff
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def getPlayerAddr(uint256 _pID): # not payable
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  return playerAddr[_pID].field_0


# hash = 0x685ffd83
# getter = None
# const = None
# payable = True
def registerNameXname(string _nameString, bytes32 _affCode, bool _all) payable: 
  mem[64] = ceil32(_nameString.length) + 128
  mem[96] = _nameString.length
  mem[128 len _nameString.length] = _nameString[all]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < nameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if _nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _nameString.length - 1 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < _nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _nameString.length:
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(pIDxAddr_[caller]):
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          playerAddr[uint256(stor7[caller])].field_512 = 2
          if not stor10[uint256(stor7[caller])][mem[128]]:
              stor10[uint256(stor7[caller])][mem[128]] = 1
              playerAddr[uint256(stor7[caller])].field_768++
              plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                uint256 amountPaid=caller,
                uint256 timeStamp=mem[128])
      else:
          if mem[128] == _affCode:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if pIDxName_[_affCode] != playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = pIDxName_[_affCode]
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not pIDxName_[_affCode]:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=pIDxName_[_affCode],
                    bytes32 playerName=playerAddr[stor8[_affCode]].field_0,
                    bool isNewPlayer=playerAddr[stor8[_affCode]].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
  else:
      stor6++
      uint256(pIDxAddr_[caller]) = stor6 + 1
      playerAddr[stor6 + 1].field_0 = caller
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          playerAddr[uint256(stor7[caller])].field_512 = 2
          if not stor10[uint256(stor7[caller])][mem[128]]:
              stor10[uint256(stor7[caller])][mem[128]] = 1
              playerAddr[uint256(stor7[caller])].field_768++
              plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=1,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                uint256 amountPaid=caller,
                uint256 timeStamp=mem[128])
      else:
          if mem[128] == _affCode:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if pIDxName_[_affCode] != playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = pIDxName_[_affCode]
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not pIDxName_[_affCode]:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=pIDxName_[_affCode],
                    bytes32 playerName=playerAddr[stor8[_affCode]].field_0,
                    bool isNewPlayer=playerAddr[stor8[_affCode]].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])


# hash = 0x6c52660d
# getter = None
# const = None
# payable = False
def checkIfNameValid(string _nameStr): # not payable
  mem[64] = ceil32(_nameStr.length) + 128
  mem[96] = _nameStr.length
  mem[128 len _nameStr.length] = _nameStr[all]
  if _nameStr.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _nameStr.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _nameStr.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _nameStr.length - 1 < _nameStr.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[_nameStr.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < _nameStr.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _nameStr.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _nameStr.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _nameStr.length:
      require [94midx < _nameStr.length
      require [94midx < _nameStr.length
      require [94midx < _nameStr.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _nameStr.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _nameStr.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _nameStr.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _nameStr.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _nameStr.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _nameStr.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if pIDxName_[mem[128]]:
      return 0
  return 1


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  require caller == stor0
  stor0 = _newAdmin


# hash = 0x745ea0c1
# getter = None
# const = None
# payable = True
def registerNameXnameFromDapp(address _addr, bytes32 _name, bytes32 _affCode, bool _all) payable: 
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  if call.value < nameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(pIDxAddr_[addr(_addr)]):
      if not _affCode:
          if pIDxName_[_name]:
              if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
          pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
          if not stor10[uint256(stor7[addr(_addr)])][_name]:
              stor10[uint256(stor7[addr(_addr)])][_name] = 1
              playerAddr[uint256(stor7[addr(_addr)])].field_768++
              plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
                uint256 amountPaid=_addr,
                uint256 timeStamp=_name)
          return 0
      if _name == _affCode:
          if pIDxName_[_name]:
              if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
          pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
          if not stor10[uint256(stor7[addr(_addr)])][_name]:
              stor10[uint256(stor7[addr(_addr)])][_name] = 1
              playerAddr[uint256(stor7[addr(_addr)])].field_768++
              plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
                uint256 amountPaid=_addr,
                uint256 timeStamp=_name)
          return 0
      if pIDxName_[_affCode] != playerAddr[uint256(stor7[addr(_addr)])].field_512:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = pIDxName_[_affCode]
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      else:
          if not pIDxName_[_affCode]:
              playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=0,
            address playerAddress=pIDxName_[_affCode],
            bytes32 playerName=playerAddr[stor8[_affCode]].field_0,
            bool isNewPlayer=playerAddr[stor8[_affCode]].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 0, pIDxName_[_affCode]
  stor6++
  uint256(pIDxAddr_[addr(_addr)]) = stor6 + 1
  playerAddr[stor6 + 1].field_0 = _addr
  if not _affCode:
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=1,
            address playerAddress=0,
            bytes32 playerName=playerAddr[0].field_0,
            bool isNewPlayer=playerAddr[0].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 1, 0
  if _name == _affCode:
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=1,
            address playerAddress=0,
            bytes32 playerName=playerAddr[0].field_0,
            bool isNewPlayer=playerAddr[0].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 1, 0
  if pIDxName_[_affCode] != playerAddr[uint256(stor7[addr(_addr)])].field_512:
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = pIDxName_[_affCode]
  if pIDxName_[_name]:
      if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
          revert with 0, 'sorry that names already taken'
  playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
  pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
  if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  else:
      if not pIDxName_[_affCode]:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  if not stor10[uint256(stor7[addr(_addr)])][_name]:
      stor10[uint256(stor7[addr(_addr)])][_name] = 1
      playerAddr[uint256(stor7[addr(_addr)])].field_768++
      plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if unknown2a46f2c5Address:
      require ext_code.size(stor2)
      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  log onNewName(
        uint256 playerID=1,
        address playerAddress=pIDxName_[_affCode],
        bytes32 playerName=playerAddr[stor8[_affCode]].field_0,
        bool isNewPlayer=playerAddr[stor8[_affCode]].field_256,
        uint256 affiliateID=call.value,
        address affiliateAddress=block.timestamp,
        bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
        uint256 amountPaid=_addr,
        uint256 timeStamp=_name)
  return 1, pIDxName_[_affCode]


# hash = 0x82e37b2c
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 9]]]]
# const = None
# payable = False
def getPlayerName(uint256 _pID): # not payable
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  return playerAddr[_pID].field_256


# hash = 0x8ed85e51
# getter = None
# const = None
# payable = False
def unknown8ed85e51(addr _param1): # not payable
  require caller == stor0
  unknown2a46f2c5Address = _param1
  stor2 = _param1


# hash = 0x921dec21
# getter = None
# const = None
# payable = True
def registerNameXID(string _nameString, uint256 _affCode, bool _all) payable: 
  mem[64] = ceil32(_nameString.length) + 128
  mem[96] = _nameString.length
  mem[128 len _nameString.length] = _nameString[all]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < nameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if _nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _nameString.length - 1 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < _nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _nameString.length:
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(pIDxAddr_[caller]):
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          if _affCode == uint256(pIDxAddr_[caller]):
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not _affCode:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=0,
                    address playerAddress=_affCode,
                    bytes32 playerName=playerAddr[_affCode].field_0,
                    bool isNewPlayer=playerAddr[_affCode].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
      else:
          if _affCode == playerAddr[uint256(stor7[caller])].field_512:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if _affCode == uint256(pIDxAddr_[caller]):
                  playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=0,
                        address playerAddress=0,
                        bytes32 playerName=playerAddr[0].field_0,
                        bool isNewPlayer=playerAddr[0].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
              else:
                  if not playerAddr[uint256(stor7[caller])].field_512:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
                  else:
                      if not _affCode:
                          playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=0,
                        address playerAddress=_affCode,
                        bytes32 playerName=playerAddr[_affCode].field_0,
                        bool isNewPlayer=playerAddr[_affCode].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
          else:
              if _affCode == uint256(pIDxAddr_[caller]):
                  if pIDxName_[mem[128]]:
                      if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                          revert with 0, 'sorry that names already taken'
                  playerAddr[uint256(stor7[caller])].field_256 = mem[128]
                  pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
                  playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=0,
                        address playerAddress=0,
                        bytes32 playerName=playerAddr[0].field_0,
                        bool isNewPlayer=playerAddr[0].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
              else:
                  playerAddr[uint256(stor7[caller])].field_512 = _affCode
                  if pIDxName_[mem[128]]:
                      if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                          revert with 0, 'sorry that names already taken'
                  playerAddr[uint256(stor7[caller])].field_256 = mem[128]
                  pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
                  if not playerAddr[uint256(stor7[caller])].field_512:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
                  else:
                      if not _affCode:
                          playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=0,
                        address playerAddress=_affCode,
                        bytes32 playerName=playerAddr[_affCode].field_0,
                        bool isNewPlayer=playerAddr[_affCode].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
  else:
      stor6++
      uint256(pIDxAddr_[caller]) = stor6 + 1
      playerAddr[stor6 + 1].field_0 = caller
      if not _affCode:
          if pIDxName_[mem[128]]:
              if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[caller])].field_256 = mem[128]
          pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
          if _affCode == uint256(pIDxAddr_[caller]):
              playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=0,
                    bytes32 playerName=playerAddr[0].field_0,
                    bool isNewPlayer=playerAddr[0].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
          else:
              if not playerAddr[uint256(stor7[caller])].field_512:
                  playerAddr[uint256(stor7[caller])].field_512 = 2
              else:
                  if not _affCode:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
              if not stor10[uint256(stor7[caller])][mem[128]]:
                  stor10[uint256(stor7[caller])][mem[128]] = 1
                  playerAddr[uint256(stor7[caller])].field_768++
                  plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
              call stor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown2a46f2c5Address:
                  require ext_code.size(stor2)
                  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              log onNewName(
                    uint256 playerID=1,
                    address playerAddress=_affCode,
                    bytes32 playerName=playerAddr[_affCode].field_0,
                    bool isNewPlayer=playerAddr[_affCode].field_256,
                    uint256 affiliateID=call.value,
                    address affiliateAddress=block.timestamp,
                    bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                    uint256 amountPaid=caller,
                    uint256 timeStamp=mem[128])
      else:
          if _affCode == playerAddr[uint256(stor7[caller])].field_512:
              if pIDxName_[mem[128]]:
                  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                      revert with 0, 'sorry that names already taken'
              playerAddr[uint256(stor7[caller])].field_256 = mem[128]
              pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
              if _affCode == uint256(pIDxAddr_[caller]):
                  playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=1,
                        address playerAddress=0,
                        bytes32 playerName=playerAddr[0].field_0,
                        bool isNewPlayer=playerAddr[0].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
              else:
                  if not playerAddr[uint256(stor7[caller])].field_512:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
                  else:
                      if not _affCode:
                          playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=1,
                        address playerAddress=_affCode,
                        bytes32 playerName=playerAddr[_affCode].field_0,
                        bool isNewPlayer=playerAddr[_affCode].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
          else:
              if _affCode == uint256(pIDxAddr_[caller]):
                  if pIDxName_[mem[128]]:
                      if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                          revert with 0, 'sorry that names already taken'
                  playerAddr[uint256(stor7[caller])].field_256 = mem[128]
                  pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
                  playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=1,
                        address playerAddress=0,
                        bytes32 playerName=playerAddr[0].field_0,
                        bool isNewPlayer=playerAddr[0].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])
              else:
                  playerAddr[uint256(stor7[caller])].field_512 = _affCode
                  if pIDxName_[mem[128]]:
                      if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
                          revert with 0, 'sorry that names already taken'
                  playerAddr[uint256(stor7[caller])].field_256 = mem[128]
                  pIDxName_[mem[128]] = uint256(pIDxAddr_[caller])
                  if not playerAddr[uint256(stor7[caller])].field_512:
                      playerAddr[uint256(stor7[caller])].field_512 = 2
                  else:
                      if not _affCode:
                          playerAddr[uint256(stor7[caller])].field_512 = 2
                  if not stor10[uint256(stor7[caller])][mem[128]]:
                      stor10[uint256(stor7[caller])][mem[128]] = 1
                      playerAddr[uint256(stor7[caller])].field_768++
                      plyrNameList_[uint256(stor7[caller])][stor9[uint256(stor7[caller])].field_768 + 1] = mem[128]
                  call stor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown2a46f2c5Address:
                      require ext_code.size(stor2)
                      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(pIDxAddr_[caller]), caller, playerAddr[uint256(stor7[caller])].field_256, playerAddr[uint256(stor7[caller])].field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  log onNewName(
                        uint256 playerID=1,
                        address playerAddress=_affCode,
                        bytes32 playerName=playerAddr[_affCode].field_0,
                        bool isNewPlayer=playerAddr[_affCode].field_256,
                        uint256 affiliateID=call.value,
                        address affiliateAddress=block.timestamp,
                        bytes32 affiliateName=uint256(pIDxAddr_[caller]),
                        uint256 amountPaid=caller,
                        uint256 timeStamp=mem[128])


# hash = 0xa448ed4b
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 11]]]]]
# const = None
# payable = False
def plyrNameList_(uint256 _param1, uint256 _param2): # not payable
  return plyrNameList_[_param1][_param2]


# hash = 0xaa4d490b
# getter = None
# const = None
# payable = True
def registerNameXaddrFromDapp(address _addr, bytes32 _name, address _affCode, bool _all) payable: 
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  if call.value < nameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(pIDxAddr_[addr(_addr)]):
      if not _affCode:
          if pIDxName_[_name]:
              if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
          pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
          if not stor10[uint256(stor7[addr(_addr)])][_name]:
              stor10[uint256(stor7[addr(_addr)])][_name] = 1
              playerAddr[uint256(stor7[addr(_addr)])].field_768++
              plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
                uint256 amountPaid=_addr,
                uint256 timeStamp=_name)
          return 0
      if _affCode == _addr:
          if pIDxName_[_name]:
              if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
          pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
          if not stor10[uint256(stor7[addr(_addr)])][_name]:
              stor10[uint256(stor7[addr(_addr)])][_name] = 1
              playerAddr[uint256(stor7[addr(_addr)])].field_768++
              plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
                uint256 amountPaid=_addr,
                uint256 timeStamp=_name)
          return 0
      if uint256(pIDxAddr_[addr(_affCode)]) != playerAddr[uint256(stor7[addr(_addr)])].field_512:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = uint256(pIDxAddr_[addr(_affCode)])
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      else:
          if not uint256(pIDxAddr_[addr(_affCode)]):
              playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=0,
            address playerAddress=uint256(pIDxAddr_[addr(_affCode)]),
            bytes32 playerName=playerAddr[uint256(stor7[addr(_affCode)])].field_0,
            bool isNewPlayer=playerAddr[uint256(stor7[addr(_affCode)])].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 0, uint256(pIDxAddr_[addr(_affCode)])
  stor6++
  uint256(pIDxAddr_[addr(_addr)]) = stor6 + 1
  playerAddr[stor6 + 1].field_0 = _addr
  if not _affCode:
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=1,
            address playerAddress=0,
            bytes32 playerName=playerAddr[0].field_0,
            bool isNewPlayer=playerAddr[0].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 1, 0
  if _affCode == _addr:
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=1,
            address playerAddress=0,
            bytes32 playerName=playerAddr[0].field_0,
            bool isNewPlayer=playerAddr[0].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 1, 0
  if uint256(pIDxAddr_[addr(_affCode)]) != playerAddr[uint256(stor7[addr(_addr)])].field_512:
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = uint256(pIDxAddr_[addr(_affCode)])
  if pIDxName_[_name]:
      if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
          revert with 0, 'sorry that names already taken'
  playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
  pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
  if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  else:
      if not uint256(pIDxAddr_[addr(_affCode)]):
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  if not stor10[uint256(stor7[addr(_addr)])][_name]:
      stor10[uint256(stor7[addr(_addr)])][_name] = 1
      playerAddr[uint256(stor7[addr(_addr)])].field_768++
      plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if unknown2a46f2c5Address:
      require ext_code.size(stor2)
      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  log onNewName(
        uint256 playerID=1,
        address playerAddress=uint256(pIDxAddr_[addr(_affCode)]),
        bytes32 playerName=playerAddr[uint256(stor7[addr(_affCode)])].field_0,
        bool isNewPlayer=playerAddr[uint256(stor7[addr(_affCode)])].field_256,
        uint256 affiliateID=call.value,
        address affiliateAddress=block.timestamp,
        bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
        uint256 amountPaid=_addr,
        uint256 timeStamp=_name)
  return 1, uint256(pIDxAddr_[addr(_affCode)])


# hash = 0xb9291296
# getter = None
# const = None
# payable = False
def useMyOldName(string _nameString): # not payable
  mem[64] = ceil32(_nameString.length) + 128
  mem[96] = _nameString.length
  mem[128 len _nameString.length] = _nameString[all]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if _nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _nameString.length - 1 < _nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < _nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _nameString.length:
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      require [94midx < _nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if bool(stor10[uint256(stor7[caller])][mem[128]]) != 1:
      revert with 0, 'umm... thats not a name you own'
  playerAddr[uint256(stor7[caller])].field_256 = mem[128]


# hash = 0xc0942dfd
# getter = None
# const = None
# payable = True
def registerNameXIDFromDapp(address _addr, bytes32 _name, uint256 _affCode, bool _all) payable: 
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  if call.value < nameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(pIDxAddr_[addr(_addr)]):
      if _affCode == uint256(pIDxAddr_[addr(_addr)]):
          if pIDxName_[_name]:
              if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
                  revert with 0, 'sorry that names already taken'
          playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
          pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
          if not stor10[uint256(stor7[addr(_addr)])][_name]:
              stor10[uint256(stor7[addr(_addr)])][_name] = 1
              playerAddr[uint256(stor7[addr(_addr)])].field_768++
              plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
          call stor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if unknown2a46f2c5Address:
              require ext_code.size(stor2)
              call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          log onNewName(
                uint256 playerID=0,
                address playerAddress=0,
                bytes32 playerName=playerAddr[0].field_0,
                bool isNewPlayer=playerAddr[0].field_256,
                uint256 affiliateID=call.value,
                address affiliateAddress=block.timestamp,
                bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
                uint256 amountPaid=_addr,
                uint256 timeStamp=_name)
          return 0
      if not _affCode:
      else:
          if _affCode == playerAddr[uint256(stor7[addr(_addr)])].field_512:
          else:
              playerAddr[uint256(stor7[addr(_addr)])].field_512 = _affCode
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      else:
          if not _affCode:
              playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=0,
            address playerAddress=_affCode,
            bytes32 playerName=playerAddr[_affCode].field_0,
            bool isNewPlayer=playerAddr[_affCode].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 0, _affCode
  stor6++
  uint256(pIDxAddr_[addr(_addr)]) = stor6 + 1
  playerAddr[stor6 + 1].field_0 = _addr
  if _affCode == uint256(pIDxAddr_[addr(_addr)]):
      if pIDxName_[_name]:
          if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
              revert with 0, 'sorry that names already taken'
      playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
      pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
      if not stor10[uint256(stor7[addr(_addr)])][_name]:
          stor10[uint256(stor7[addr(_addr)])][_name] = 1
          playerAddr[uint256(stor7[addr(_addr)])].field_768++
          plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
      call stor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if unknown2a46f2c5Address:
          require ext_code.size(stor2)
          call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      log onNewName(
            uint256 playerID=1,
            address playerAddress=0,
            bytes32 playerName=playerAddr[0].field_0,
            bool isNewPlayer=playerAddr[0].field_256,
            uint256 affiliateID=call.value,
            address affiliateAddress=block.timestamp,
            bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
            uint256 amountPaid=_addr,
            uint256 timeStamp=_name)
      return 1, 0
  if not _affCode:
  else:
      if _affCode == playerAddr[uint256(stor7[addr(_addr)])].field_512:
      else:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = _affCode
  if pIDxName_[_name]:
      if bool(stor10[uint256(stor7[addr(_addr)])][_name]) != 1:
          revert with 0, 'sorry that names already taken'
  playerAddr[uint256(stor7[addr(_addr)])].field_256 = _name
  pIDxName_[_name] = uint256(pIDxAddr_[addr(_addr)])
  if not playerAddr[uint256(stor7[addr(_addr)])].field_512:
      playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  else:
      if not _affCode:
          playerAddr[uint256(stor7[addr(_addr)])].field_512 = 2
  if not stor10[uint256(stor7[addr(_addr)])][_name]:
      stor10[uint256(stor7[addr(_addr)])][_name] = 1
      playerAddr[uint256(stor7[addr(_addr)])].field_768++
      plyrNameList_[uint256(stor7[addr(_addr)])][stor9[uint256(stor7[addr(_addr)])].field_768 + 1] = _name
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if unknown2a46f2c5Address:
      require ext_code.size(stor2)
      call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  log onNewName(
        uint256 playerID=1,
        address playerAddress=_affCode,
        bytes32 playerName=playerAddr[_affCode].field_0,
        bool isNewPlayer=playerAddr[_affCode].field_256,
        uint256 affiliateID=call.value,
        address affiliateAddress=block.timestamp,
        bytes32 affiliateName=uint256(pIDxAddr_[addr(_addr)]),
        uint256 amountPaid=_addr,
        uint256 timeStamp=_name)
  return 1, _affCode


# hash = 0xc320c727
# getter = None
# const = None
# payable = False
def setRegistrationFee(uint256 _fee): # not payable
  require caller == stor0
  nameFee = _fee


# hash = 0xdbbcaa97
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def gameIDs_(address _param1): # not payable
  return gameIDs_[_param1]


# hash = 0xde7874f3
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def plyr_(uint256 _param1): # not payable
  return playerAddr[_param1].field_0, 
         playerAddr[_param1].field_256,
         playerAddr[_param1].field_512,
         playerAddr[_param1].field_768


# hash = 0xe3c08adf
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 9]]]]
# const = None
# payable = False
def getPlayerLAff(uint256 _pID): # not payable
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  return playerAddr[_pID].field_512


# hash = 0xe56556a9
# getter = None
# const = None
# payable = False
def getPlayerID(address _addr): # not payable
  if not gameIDs_[caller]:
      revert with 0, 'agame not registered'
  if not uint256(pIDxAddr_[addr(_addr)]):
      stor6++
      uint256(pIDxAddr_[addr(_addr)]) = stor6 + 1
      playerAddr[stor6 + 1].field_0 = _addr
  if not unknown2a46f2c5Address:
      return uint256(pIDxAddr_[addr(_addr)])
  require ext_code.size(stor2)
  call stor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
       gas gas_remaining wei
      args 0, uint32(pIDxAddr_[addr(_addr)]), addr(_addr), playerAddr[uint256(stor7[addr(_addr)])].field_256, playerAddr[uint256(stor7[addr(_addr)])].field_512
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


