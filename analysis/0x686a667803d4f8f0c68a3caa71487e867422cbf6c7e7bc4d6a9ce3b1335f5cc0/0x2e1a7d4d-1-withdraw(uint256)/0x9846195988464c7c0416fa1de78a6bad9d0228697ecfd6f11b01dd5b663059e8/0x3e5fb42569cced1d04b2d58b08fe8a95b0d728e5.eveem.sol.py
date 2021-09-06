# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3E5fb42569cCEd1D04b2D58b08fE8a95b0d728e5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5
# hash = 0x10176f86
# getter = None
# const = None
# payable = True
def unknown10176f86(addr _param1, uint256 _param2, array _param3) payable: 
  require calldata.size - 4 >= 96
  require _param3 <= 4294967296
  require _param3 + 36 <= calldata.size
  require _param3.length <= 4294967296 and _param3 + _param3.length + 36 <= calldata.size
  if sha3(_param3[all]) == sha3('withdraw'):
      require _param1 == stor1
  stor3 = _param1
  stor4 = _param2
  stor5[].field_0 = Array(len=_param3.length, data=_param3[all])
  stor2.length++
  stor2[stor2.length].field_0 = stor3
  stor2[stor2.length].field_256 = stor4
  if 31 >= stor5.length:
      stor2[stor2.length].field_512 = stor5.length
      [94midx = 0
      while stor[(3 * stor2.length) + ('name', 'stor2', 2) + 2].length + 31 / 32 > [94midx:
          stor[[94midx + sha3((3 * stor2.length) + ('name', 'stor2', 2) + 2)].field_0 = 0
          [94midx = [94midx + 1
          continue 
  else:
      stor2[stor2.length].field_512 = Mask(255, 1, (256 * not bool(stor5.length)) - 1 and stor5.length) + 1
      if not Mask(255, 1, (256 * not bool(stor5.length)) - 1 and stor5.length):
          [94midx = 0
          while stor[(3 * stor2.length) + ('name', 'stor2', 2) + 2].length + 31 / 32 > [94midx:
              stor[[94midx + sha3((3 * stor2.length) + ('name', 'stor2', 2) + 2)].field_0 = 0
              [94midx = [94midx + 1
              continue 
      else:
          [94ms = 0
          [94midx = 0
          while stor5.length + 31 / 32 > [94midx:
              stor[[94ms + sha3((3 * stor2.length) + ('name', 'stor2', 2) + 2)].field_0 = stor5[[94midx].field_0
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              continue 
          [94midx = stor5.length + 31 / 32
          while stor[(3 * stor2.length) + ('name', 'stor2', 2) + 2].length + 31 / 32 > [94midx:
              stor[[94midx + sha3((3 * stor2.length) + ('name', 'stor2', 2) + 2)].field_0 = 0
              [94midx = [94midx + 1
              continue 


# hash = 0x416f5483
# getter = None
# const = None
# payable = True
def changeEthAddress(address _newAddress) payable: 
  require calldata.size - 4 >= 32
  require caller == stor0
  stor1 = _newAddress


# hash = 0xda223bc3
# getter = None
# const = None
# payable = True
def unknownda223bc3() payable: 
  mem[128] = uint256(stor5.field_0)
  [94midx = 128
  [94ms = 0
  while stor5.length + 96 > [94midx:
      mem[[94midx + 32] = stor5[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor3, stor4, Array(len=stor5.length, data=mem[128 len stor5.length])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


