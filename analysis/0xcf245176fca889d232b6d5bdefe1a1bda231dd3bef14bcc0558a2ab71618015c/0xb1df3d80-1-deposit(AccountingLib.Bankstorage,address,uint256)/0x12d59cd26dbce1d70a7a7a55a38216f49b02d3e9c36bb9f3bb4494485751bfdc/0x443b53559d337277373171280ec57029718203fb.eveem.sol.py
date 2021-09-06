# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x443b53559d337277373171280Ec57029718203Fb 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x81a33a6f
# getter = None
# const = None
# payable = True
def bytesToUInt(bytes32 _v) payable: 
  require _v != 0
  [94midx = 0
  [94ms = 0
  [94ms = 0
  while [94midx < 32:
      if not uint8(_v / 2^(8 * -[94midx + 31)):
          return [94ms
      require uint8(_v / 2^(8 * -[94midx + 31)) >= 48
      require uint8(_v / 2^(8 * -[94midx + 31)) <= 57
      [94midx = [94midx + 1
      [94ms = uint8(_v / 2^(8 * -[94midx + 31))
      [94ms = uint8(_v / 2^(8 * -[94midx + 31)) + (10 * [94ms) - 48
      continue 
  return -1536


# hash = 0x94e8767d
# getter = None
# const = None
# payable = True
def uintToBytes(uint256 _i) payable: 
  if 0 == _i:
      return '0'
  [94ms = 0
  [94midx = _i
  while [94midx > 0:
      [94ms = [94ms / 256 or ([94midx % 10) + 48 << 248
      [94midx = [94midx / 10
      continue 
  return [94ms


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


