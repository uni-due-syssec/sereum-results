# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x541B41fE06B8b57F1d83b13d66e281b291a10760 
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
    stor4
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
def pIDxAddr_(address m_param1): # not payable
  return uint256(mpIDxAddr_m[m_param1m])


# hash = 0x2614195f
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def getNameFee(): # not payable
  return mnameFee


# hash = 0x2660316e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 10]]]]]]
# const = None
# payable = False
def plyrNames_(uint256 m_param1, bytes32 m_param2): # not payable
  return bool(mstor10m[m_param1m]m[m_param2m])


# hash = 0x2a46f2c5
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown2a46f2c5(): # not payable
  require caller == mstor0
  return munknown2a46f2c5Address


# hash = 0x2e0e0349
# getter = None
# const = None
# payable = False
def unknown2e0e0349(addr m_param1): # not payable
  require caller == mstor0
  if mstor4m[addr(m_param1)m]:
      revert with 0, 'game already registed'
  mstor5++
  mstor4m[addr(m_param1)m] = mstor5 + 1


# hash = 0x2e19ebdc
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def pIDxName_(bytes32 m_param1): # not payable
  return mpIDxName_m[m_param1m]


# hash = 0x3ddd4698
# getter = None
# const = None
# payable = True
def registerNameXaddr(string m_nameString, address m_affCode, bool m_all) payable: 
  mem[64] = ceil32(m_nameString.length) + 128
  mem[96] = m_nameString.length
  mem[128 len m_nameString.length] = m_nameString[allm]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < mnameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if m_nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if m_nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require m_nameString.length - 1 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[m_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < m_nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < m_nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < m_nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_nameString.lengthm:
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < m_nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
      else:
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < m_nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(mpIDxAddr_m[callerm]):
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
              mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if m_affCode == caller:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if uint256(mpIDxAddr_m[addr(m_affCode)m]) != mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = uint256(mpIDxAddr_m[addr(m_affCode)m])
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not uint256(mpIDxAddr_m[addr(m_affCode)m]):
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
      mstor6++
      uint256(mpIDxAddr_m[callerm]) = mstor6 + 1
      mplayerAddrm[mstor6 + 1m]m.field_0 = caller
      mplayerAddrm[mstor6m]m.field_512 = 2
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
              mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if m_affCode == caller:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if uint256(mpIDxAddr_m[addr(m_affCode)m]) != mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = uint256(mpIDxAddr_m[addr(m_affCode)m])
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not uint256(mpIDxAddr_m[addr(m_affCode)m]):
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
def getPlayerAddr(uint256 m_pID): # not payable
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  return mplayerAddrm[m_pIDm]m.field_0


# hash = 0x685ffd83
# getter = None
# const = None
# payable = True
def registerNameXname(string m_nameString, bytes32 m_affCode, bool m_all) payable: 
  mem[64] = ceil32(m_nameString.length) + 128
  mem[96] = m_nameString.length
  mem[128 len m_nameString.length] = m_nameString[allm]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < mnameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if m_nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if m_nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require m_nameString.length - 1 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[m_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < m_nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < m_nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < m_nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_nameString.lengthm:
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < m_nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
      else:
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < m_nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(mpIDxAddr_m[callerm]):
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
              mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if mem[128] == m_affCode:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if mpIDxName_m[m_affCodem] != mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = mpIDxName_m[m_affCodem]
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not mpIDxName_m[m_affCodem]:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
      mstor6++
      uint256(mpIDxAddr_m[callerm]) = mstor6 + 1
      mplayerAddrm[mstor6 + 1m]m.field_0 = caller
      mplayerAddrm[mstor6m]m.field_512 = 2
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
              mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if mem[128] == m_affCode:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if mpIDxName_m[m_affCodem] != mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = mpIDxName_m[m_affCodem]
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not mpIDxName_m[m_affCodem]:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
def checkIfNameValid(string m_nameStr): # not payable
  mem[64] = ceil32(m_nameStr.length) + 128
  mem[96] = m_nameStr.length
  mem[128 len m_nameStr.length] = m_nameStr[allm]
  if m_nameStr.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if m_nameStr.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < m_nameStr.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require m_nameStr.length - 1 < m_nameStr.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[m_nameStr.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < m_nameStr.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < m_nameStr.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < m_nameStr.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_nameStr.lengthm:
      require [94midx < m_nameStr.length
      require [94midx < m_nameStr.length
      require [94midx < m_nameStr.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < m_nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < m_nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < m_nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < m_nameStr.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < m_nameStr.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < m_nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
      else:
          require [94midx < m_nameStr.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < m_nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameStr.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < m_nameStr.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < m_nameStr.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < m_nameStr.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
              require [94midx < m_nameStr.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < m_nameStr.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if mpIDxName_m[mem[128]m]:
      return 0
  return 1


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address m_newAdmin): # not payable
  require caller == mstor0
  mstor0 = m_newAdmin


# hash = 0x745ea0c1
# getter = None
# const = None
# payable = True
def registerNameXnameFromDapp(address m_addr, bytes32 m_name, bytes32 m_affCode, bool m_all) payable: 
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  if call.value < mnameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(mpIDxAddr_m[addr(m_addr)m]):
      if not m_affCode:
          if mpIDxName_m[m_namem]:
              if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
          mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
              mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      if m_name == m_affCode:
          if mpIDxName_m[m_namem]:
              if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
          mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
              mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      if mpIDxName_m[m_affCodem] != mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = mpIDxName_m[m_affCodem]
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      else:
          if not mpIDxName_m[m_affCodem]:
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      return 0, mpIDxName_m[m_affCodem]
  mstor6++
  uint256(mpIDxAddr_m[addr(m_addr)m]) = mstor6 + 1
  mplayerAddrm[mstor6 + 1m]m.field_0 = m_addr
  mplayerAddrm[mstor6m]m.field_512 = 2
  if not m_affCode:
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  if m_name == m_affCode:
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  if mpIDxName_m[m_affCodem] != mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = mpIDxName_m[m_affCodem]
  if mpIDxName_m[m_namem]:
      if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
          revert with 0, 'sorry that names already taken'
  mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
  mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
  if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  else:
      if not mpIDxName_m[m_affCodem]:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
      mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
      mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
  call mstor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if munknown2a46f2c5Address:
      require ext_code.size(mstor2)
      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  return 1, mpIDxName_m[m_affCodem]


# hash = 0x82e37b2c
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 9]]]]
# const = None
# payable = False
def getPlayerName(uint256 m_pID): # not payable
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  return mplayerAddrm[m_pIDm]m.field_256


# hash = 0x8ed85e51
# getter = None
# const = None
# payable = False
def unknown8ed85e51(addr m_param1): # not payable
  require caller == mstor0
  munknown2a46f2c5Address = m_param1
  mstor2 = m_param1


# hash = 0x921dec21
# getter = None
# const = None
# payable = True
def registerNameXID(string m_nameString, uint256 m_affCode, bool m_all) payable: 
  mem[64] = ceil32(m_nameString.length) + 128
  mem[96] = m_nameString.length
  mem[128 len m_nameString.length] = m_nameString[allm]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value < mnameFee:
      revert with 0, 'umm.....  you have to pay the nme fee'
  if m_nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if m_nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require m_nameString.length - 1 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[m_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < m_nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < m_nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < m_nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_nameString.lengthm:
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < m_nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
      else:
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < m_nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if uint256(mpIDxAddr_m[callerm]):
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          if m_affCode == uint256(mpIDxAddr_m[callerm]):
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not m_affCode:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if m_affCode == mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if m_affCode == uint256(mpIDxAddr_m[callerm]):
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
                  if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  else:
                      if not m_affCode:
                          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if m_affCode == uint256(mpIDxAddr_m[callerm]):
                  if mpIDxName_m[mem[128]m]:
                      if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                          revert with 0, 'sorry that names already taken'
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
                  mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = m_affCode
                  if mpIDxName_m[mem[128]m]:
                      if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                          revert with 0, 'sorry that names already taken'
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
                  mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
                  if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  else:
                      if not m_affCode:
                          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
      mstor6++
      uint256(mpIDxAddr_m[callerm]) = mstor6 + 1
      mplayerAddrm[mstor6 + 1m]m.field_0 = caller
      mplayerAddrm[mstor6m]m.field_512 = 2
      if not m_affCode:
          if mpIDxName_m[mem[128]m]:
              if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
          mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
          if m_affCode == uint256(mpIDxAddr_m[callerm]):
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              else:
                  if not m_affCode:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
              if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                  mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                  mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
              call mstor0 with:
                 value eth.balance(this.address) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if munknown2a46f2c5Address:
                  require ext_code.size(mstor2)
                  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                       gas gas_remaining wei
                      args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
          if m_affCode == mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
              if mpIDxName_m[mem[128]m]:
                  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                      revert with 0, 'sorry that names already taken'
              mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
              mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
              if m_affCode == uint256(mpIDxAddr_m[callerm]):
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
                  if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  else:
                      if not m_affCode:
                          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
              if m_affCode == uint256(mpIDxAddr_m[callerm]):
                  if mpIDxName_m[mem[128]m]:
                      if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                          revert with 0, 'sorry that names already taken'
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
                  mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = m_affCode
                  if mpIDxName_m[mem[128]m]:
                      if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
                          revert with 0, 'sorry that names already taken'
                  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]
                  mpIDxName_m[mem[128]m] = uint256(mpIDxAddr_m[callerm])
                  if not mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512:
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  else:
                      if not m_affCode:
                          mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512 = 2
                  if not mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]:
                      mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m] = 1
                      mplayerAddrm[uint256(mstor7m[callerm])m]m.field_768++
                      mplyrNameList_m[uint256(mstor7m[callerm])m]m[mstor9m[uint256(mstor7m[callerm])m]m.field_768 + 1m] = mem[128]
                  call mstor0 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if munknown2a46f2c5Address:
                      require ext_code.size(mstor2)
                      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                           gas gas_remaining wei
                          args uint256(mpIDxAddr_m[callerm]), caller, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256, mplayerAddrm[uint256(mstor7m[callerm])m]m.field_512
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
def plyrNameList_(uint256 m_param1, uint256 m_param2): # not payable
  return mplyrNameList_m[m_param1m]m[m_param2m]


# hash = 0xaa4d490b
# getter = None
# const = None
# payable = True
def registerNameXaddrFromDapp(address m_addr, bytes32 m_name, address m_affCode, bool m_all) payable: 
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  if call.value < mnameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(mpIDxAddr_m[addr(m_addr)m]):
      if not m_affCode:
          if mpIDxName_m[m_namem]:
              if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
          mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
              mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      if m_affCode == m_addr:
          if mpIDxName_m[m_namem]:
              if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
          mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
              mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      if uint256(mpIDxAddr_m[addr(m_affCode)m]) != mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = uint256(mpIDxAddr_m[addr(m_affCode)m])
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      else:
          if not uint256(mpIDxAddr_m[addr(m_affCode)m]):
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      return 0, uint256(mpIDxAddr_m[addr(m_affCode)m])
  mstor6++
  uint256(mpIDxAddr_m[addr(m_addr)m]) = mstor6 + 1
  mplayerAddrm[mstor6 + 1m]m.field_0 = m_addr
  mplayerAddrm[mstor6m]m.field_512 = 2
  if not m_affCode:
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  if m_affCode == m_addr:
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  if uint256(mpIDxAddr_m[addr(m_affCode)m]) != mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = uint256(mpIDxAddr_m[addr(m_affCode)m])
  if mpIDxName_m[m_namem]:
      if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
          revert with 0, 'sorry that names already taken'
  mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
  mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
  if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  else:
      if not uint256(mpIDxAddr_m[addr(m_affCode)m]):
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
      mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
      mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
  call mstor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if munknown2a46f2c5Address:
      require ext_code.size(mstor2)
      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  return 1, uint256(mpIDxAddr_m[addr(m_affCode)m])


# hash = 0xb9291296
# getter = None
# const = None
# payable = False
def useMyOldName(string m_nameString): # not payable
  mem[64] = ceil32(m_nameString.length) + 128
  mem[96] = m_nameString.length
  mem[128 len m_nameString.length] = m_nameString[allm]
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if m_nameString.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if m_nameString.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require m_nameString.length - 1 < m_nameString.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[m_nameString.length + 127]):
      revert with 0, 'string cannot start or end with space'
  require 0 < m_nameString.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < m_nameString.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < m_nameString.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_nameString.lengthm:
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      require [94midx < m_nameString.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < m_nameString.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
      else:
          require [94midx < m_nameString.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < m_nameString.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < m_nameString.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < m_nameString.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  mcontinue 
              require [94midx < m_nameString.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < m_nameString.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if bool(mstor10m[uint256(mstor7m[callerm])m]m[mem[128]m]) != 1:
      revert with 0, 'umm... thats not a name you own'
  mplayerAddrm[uint256(mstor7m[callerm])m]m.field_256 = mem[128]


# hash = 0xc0942dfd
# getter = None
# const = None
# payable = True
def registerNameXIDFromDapp(address m_addr, bytes32 m_name, uint256 m_affCode, bool m_all) payable: 
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  if call.value < mnameFee:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'umm.....  you have to pay the nme fee'
  if uint256(mpIDxAddr_m[addr(m_addr)m]):
      if m_affCode == uint256(mpIDxAddr_m[addr(m_addr)m]):
          if mpIDxName_m[m_namem]:
              if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
                  revert with 0, 'sorry that names already taken'
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
          mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
          if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
              mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
              mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
          call mstor0 with:
             value eth.balance(this.address) wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if munknown2a46f2c5Address:
              require ext_code.size(mstor2)
              call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
                   gas gas_remaining wei
                  args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      if not m_affCode:
      else:
          if m_affCode == mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          else:
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = m_affCode
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      else:
          if not m_affCode:
              mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
      return 0, m_affCode
  mstor6++
  uint256(mpIDxAddr_m[addr(m_addr)m]) = mstor6 + 1
  mplayerAddrm[mstor6 + 1m]m.field_0 = m_addr
  mplayerAddrm[mstor6m]m.field_512 = 2
  if m_affCode == uint256(mpIDxAddr_m[addr(m_addr)m]):
      if mpIDxName_m[m_namem]:
          if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
              revert with 0, 'sorry that names already taken'
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
      mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
      if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
          mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
          mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
      call mstor0 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if munknown2a46f2c5Address:
          require ext_code.size(mstor2)
          call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
               gas gas_remaining wei
              args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  if not m_affCode:
  else:
      if m_affCode == mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      else:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = m_affCode
  if mpIDxName_m[m_namem]:
      if bool(mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]) != 1:
          revert with 0, 'sorry that names already taken'
  mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256 = m_name
  mpIDxName_m[m_namem] = uint256(mpIDxAddr_m[addr(m_addr)m])
  if not mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512:
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  else:
      if not m_affCode:
          mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512 = 2
  if not mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem]:
      mstor10m[uint256(mstor7m[addr(m_addr)m])m]m[m_namem] = 1
      mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_768++
      mplyrNameList_m[uint256(mstor7m[addr(m_addr)m])m]m[mstor9m[uint256(mstor7m[addr(m_addr)m])m]m.field_768 + 1m] = m_name
  call mstor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if munknown2a46f2c5Address:
      require ext_code.size(mstor2)
      call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
           gas gas_remaining wei
          args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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
  return 1, m_affCode


# hash = 0xc320c727
# getter = None
# const = None
# payable = False
def setRegistrationFee(uint256 m_fee): # not payable
  require caller == mstor0
  mnameFee = m_fee


# hash = 0xde7874f3
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def plyr_(uint256 m_param1): # not payable
  return mplayerAddrm[m_param1m]m.field_0, 
         mplayerAddrm[m_param1m]m.field_256,
         mplayerAddrm[m_param1m]m.field_512,
         mplayerAddrm[m_param1m]m.field_768


# hash = 0xe3c08adf
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 9]]]]
# const = None
# payable = False
def getPlayerLAff(uint256 m_pID): # not payable
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  return mplayerAddrm[m_pIDm]m.field_512


# hash = 0xe56556a9
# getter = None
# const = None
# payable = False
def getPlayerID(address m_addr): # not payable
  if not mstor4m[callerm]:
      revert with 0, 'agame not registered'
  if not uint256(mpIDxAddr_m[addr(m_addr)m]):
      mstor6++
      uint256(mpIDxAddr_m[addr(m_addr)m]) = mstor6 + 1
      mplayerAddrm[mstor6 + 1m]m.field_0 = m_addr
      mplayerAddrm[mstor6m]m.field_512 = 2
  if not munknown2a46f2c5Address:
      return uint256(mpIDxAddr_m[addr(m_addr)m])
  require ext_code.size(mstor2)
  call mstor2.receivePlayerInfo(uint256 pID, address addr, bytes32 name, uint256 laff) with:
       gas gas_remaining wei
      args 0, uint32(mpIDxAddr_m[addr(m_addr)m]), addr(m_addr), mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_256, mplayerAddrm[uint256(mstor7m[addr(m_addr)m])m]m.field_512
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


