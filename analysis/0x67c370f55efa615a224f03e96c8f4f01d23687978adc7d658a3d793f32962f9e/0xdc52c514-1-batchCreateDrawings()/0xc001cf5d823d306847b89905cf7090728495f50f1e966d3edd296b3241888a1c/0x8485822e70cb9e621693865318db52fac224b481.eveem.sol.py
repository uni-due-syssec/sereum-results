# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8485822E70cb9e621693865318DB52Fac224B481 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0
# hash = 0x7497a061
# getter = None
# const = None
# payable = False
def unknown7497a061(uint256 _param1): # not payable
  if stor1.length > _param1:
      require _param1 < stor1.length
      mem[128] = stor[sha3((4 * _param1) + ('name', 'stor1', 1) + 3)].field_0
      [94midx = 128
      [94ms = 0
      while stor[(4 * _param1) + ('name', 'stor1', 1) + 3].length + 96 > [94midx:
          mem[[94midx + 32] = stor[[94ms + sha3((4 * _param1) + ('name', 'stor1', 1) + 3)].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      return stor1[_param1].field_0, 
             stor1[_param1].field_256,
             stor1[_param1].field_512,
             Array(len=stor[(4 * _param1) + ('name', 'stor1', 1) + 3].length, data=mem[128 len stor[(4 * _param1) + ('name', 'stor1', 1) + 3].length])
  mem[128] = 0
  mem[160] = 0
  mem[192] = 128
  mem[224] = '0'
  mem[256 len ceil32('0')] = mem[128 len ceil32('0')]
  if not '0' % 32:
      return '0', 0, 0, 128, '0', mem[256 len '0']
  mem[floor32('0') + 256] = mem[floor32('0') + -('0' % 32) + 288 len '0' % 32]
  return '0', 0, 0, 128, '0', mem[256 len floor32('0') + 32]


# hash = 0xdb589bbe
# getter = None
# const = None
# payable = False
def unknowndb589bbe(uint256 _param1): # not payable
  if stor0.length > _param1:
      require _param1 < stor0.length
      mem[128] = stor[sha3((5 * _param1) + ('name', 'stor0', 0) + 4)].field_0
      [94midx = 128
      [94ms = 0
      while stor[(5 * _param1) + ('name', 'stor0', 0) + 4].length + 96 > [94midx:
          mem[[94midx + 32] = stor[[94ms + sha3((5 * _param1) + ('name', 'stor0', 0) + 4)].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      return stor0[_param1].field_0, 
             stor0[_param1].field_256,
             stor0[_param1].field_512,
             stor0[_param1].field_768,
             Array(len=stor[(5 * _param1) + ('name', 'stor0', 0) + 4].length, data=mem[128 len stor[(5 * _param1) + ('name', 'stor0', 0) + 4].length])
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 160
  mem[256] = '0'
  mem[288 len ceil32('0')] = mem[128 len ceil32('0')]
  if not '0' % 32:
      return '0', 0, 0, 0, 160, '0', mem[288 len '0']
  mem[floor32('0') + 288] = mem[floor32('0') + -('0' % 32) + 320 len '0' % 32]
  return '0', 0, 0, 0, 160, '0', mem[288 len floor32('0') + 32]


# hash = 0xe6979569
# getter = None
# const = ['return', 1]
# payable = False
const unknowne6979569 = 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


