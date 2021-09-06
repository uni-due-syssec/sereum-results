# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa9e47658F28bFbcAd94Ef97201AC328CF7e85529 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 1
    unknownc4d68b6d
    # storage address 2
    history
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 99
    stor99
# hash = 0x222a95ee
# getter = None
# const = None
# payable = False
def unknown222a95ee(): # not payable
  mem[256] = uint256(stor4.field_0)
  [94midx = 256
  [94ms = 0
  while stor4.length + 256 > [94midx + 32:
      mem[[94midx + 32] = uint256(stor4[[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor3, 
         Array(len=stor4.length, data=mem[256 len stor4.length + (floor32(stor4.length - 1) + -stor4.length + 32 % 32)]),
         stor5,
         stor6


# hash = 0x288d47de
# getter = None
# const = None
# payable = False
def unknown288d47de(addr _param1, addr _param2): # not payable
  require caller == unknown89977cdfAddress
  unknownc4d68b6d[addr(_param1)] = _param2


# hash = 0x3d79d1c8
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const bal = eth.balance(this.address)


# hash = 0x4b906714
# getter = None
# const = None
# payable = True
def unknown4b906714(addr _param1, uint256 _param2, array _param3) payable: 
  mem[128 len _param3.length] = _param3[all]
  require caller == unknown89977cdfAddress
  mem[ceil32(_param3.length) + 128 len ceil32(_param3.length)] = _param3[all], mem[_param3.length + 128 len ceil32(_param3.length) - _param3.length]
  if not _param3.length % 32:
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining - 34710 wei
          args mem[ceil32(_param3.length) + 132 len _param3.length - 4]
  else:
      mem[floor32(_param3.length) + ceil32(_param3.length) + 128] = mem[floor32(_param3.length) + ceil32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32]
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining - 34710 wei
          args mem[ceil32(_param3.length) + 132 len floor32(_param3.length) + 28]
  require ext_call.success


# hash = 0x4c2f04a4
# getter = None
# const = None
# payable = False
def AddMessage(address _adr, uint256 _val, string _data): # not payable
  if not unknownc4d68b6d[caller]:
      stor3 = _adr
      stor6 = block.timestamp
      stor5 = _val
      uint256(stor4[].field_0) = Array(len=_data.length, data=_data[all])
      history.length++
      if not history.length <= history.length + 1:
          mem[0] = 2
          [94midx = 4 * history.length + 1
          while sha3(2) + (4 * history.length) > [94midx + sha3(mem[0]):
              addr(stor[[94midx + sha3(mem[0])]) = 0
              uint256(stor[[94midx + sha3(mem[0]) + 1]) = 0
              if 31 < stor[[94midx + sha3(mem[0]) + 1].length:
                  mem[0] = [94midx + sha3(mem[0]) + 1
                  [94ms = sha3([94midx + sha3(mem[0]) + 1)
                  while sha3([94midx + sha3(mem[0]) + 1) + (stor[[94midx + sha3(mem[0]) + 1].length + 31 / 32) > [94ms:
                      uint256(stor[[94ms]) = 0
                      [94ms = [94ms + 1
                      continue 
              uint256(stor[[94midx + sha3(mem[0]) + 2]) = 0
              uint256(stor[[94midx + sha3(mem[0]) + 3]) = 0
              [94midx = [94midx + 4
              continue 
      addr(history[history.length].field_0) = stor3
      if 31 >= stor4.length:
          uint256(history[history.length].field_256) = stor4.length
          [94midx = 0
          while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
              uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
              [94midx = [94midx + 1
              continue 
      else:
          uint256(history[history.length].field_256) = Mask(255, 1, (256 * not bool(stor4.length)) - 1 and stor4.length) + 1
          if not Mask(255, 1, (256 * not bool(stor4.length)) - 1 and stor4.length):
              [94midx = 0
              while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              [94ms = 0
              [94midx = 0
              while stor4.length + 31 / 32 > [94midx:
                  uint256(stor[[94ms + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = uint256(stor4[[94midx].field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  continue 
              [94midx = stor4.length + 31 / 32
              while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
                  [94midx = [94midx + 1
                  continue 
      uint256(history[history.length].field_512) = stor5
      uint256(history[history.length].field_768) = stor6
  else:
      if _adr != unknownc4d68b6d[caller]:
          call unknownc4d68b6d[caller] with:
             funct Mask(32, 224, sha3('GopStop()')) >> 224
               gas gas_remaining - 25710 wei
          require ext_call.success
      else:
          stor3 = _adr
          stor6 = block.timestamp
          stor5 = _val
          uint256(stor4[].field_0) = Array(len=_data.length, data=_data[all])
          history.length++
          if not history.length <= history.length + 1:
              mem[0] = 2
              [94midx = 4 * history.length + 1
              while sha3(2) + (4 * history.length) > [94midx + sha3(mem[0]):
                  addr(stor[[94midx + sha3(mem[0])]) = 0
                  uint256(stor[[94midx + sha3(mem[0]) + 1]) = 0
                  if 31 < stor[[94midx + sha3(mem[0]) + 1].length:
                      mem[0] = [94midx + sha3(mem[0]) + 1
                      [94ms = sha3([94midx + sha3(mem[0]) + 1)
                      while sha3([94midx + sha3(mem[0]) + 1) + (stor[[94midx + sha3(mem[0]) + 1].length + 31 / 32) > [94ms:
                          uint256(stor[[94ms]) = 0
                          [94ms = [94ms + 1
                          continue 
                  uint256(stor[[94midx + sha3(mem[0]) + 2]) = 0
                  uint256(stor[[94midx + sha3(mem[0]) + 3]) = 0
                  [94midx = [94midx + 4
                  continue 
          addr(history[history.length].field_0) = stor3
          if 31 >= stor4.length:
              uint256(history[history.length].field_256) = stor4.length
              [94midx = 0
              while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              uint256(history[history.length].field_256) = Mask(255, 1, (256 * not bool(stor4.length)) - 1 and stor4.length) + 1
              if not Mask(255, 1, (256 * not bool(stor4.length)) - 1 and stor4.length):
                  [94midx = 0
                  while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
                      uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
                      [94midx = [94midx + 1
                      continue 
              else:
                  [94ms = 0
                  [94midx = 0
                  while stor4.length + 31 / 32 > [94midx:
                      uint256(stor[[94ms + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = uint256(stor4[[94midx].field_0)
                      [94ms = [94ms + 1
                      [94midx = [94midx + 1
                      continue 
                  [94midx = stor4.length + 31 / 32
                  while stor[(4 * history.length) + ('name', 'history', 2) + 1].length + 31 / 32 > [94midx:
                      uint256(stor[[94midx + sha3((4 * history.length) + ('name', 'history', 2) + 1)].field_0) = 0
                      [94midx = [94midx + 1
                      continue 
          uint256(history[history.length].field_512) = stor5
          uint256(history[history.length].field_768) = stor6


# hash = 0x89977cdf
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return unknown89977cdfAddress


# hash = 0x9003e39a
# getter = None
# const = None
# payable = True
def unknown9003e39a(addr _param1, array _param2) payable: 
  mem[128 len _param2.length] = _param2[all]
  require caller == unknown89977cdfAddress
  mem[ceil32(_param2.length) + 128 len ceil32(_param2.length)] = _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]
  if not _param2.length % 32:
      [93mdelegate _param1.mem[ceil32(_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(_param2.length) + 132 len _param2.length - 4]
  else:
      mem[floor32(_param2.length) + ceil32(_param2.length) + 128] = mem[floor32(_param2.length) + ceil32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32]
      [93mdelegate _param1.mem[ceil32(_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(_param2.length) + 132 len floor32(_param2.length) + 28]
  require delegate.return_code


# hash = 0xa21f0368
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def History(uint256 _param1): # not payable
  require _param1 < history.length
  mem[256] = uint256(stor[sha3((4 * _param1) + ('name', 'history', 2) + 1)].field_0)
  [94midx = 256
  [94ms = 0
  while stor[(4 * _param1) + ('name', 'history', 2) + 1].length + 256 > [94midx + 32:
      mem[[94midx + 32] = uint256(stor[[94ms + sha3((4 * _param1) + ('name', 'history', 2) + 1)].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return addr(history[_param1].field_0), 
         Array(len=stor[(4 * _param1) + ('name', 'history', 2) + 1].length, data=mem[256 len stor[(4 * _param1) + ('name', 'history', 2) + 1].length + (floor32(stor[(4 * _param1) + ('name', 'history', 2) + 1].length - 1) + -stor[(4 * _param1) + ('name', 'history', 2) + 1].length + 32 % 32)]),
         uint256(history[_param1].field_512),
         uint256(history[_param1].field_768)


# hash = 0xc144811f
# getter = None
# const = None
# payable = True
def unknownc144811f() payable: 
  require caller == unknown89977cdfAddress
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xc4d68b6d
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def unknownc4d68b6d(addr _param1): # not payable
  return unknownc4d68b6d[_param1]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


