# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8767a53A9f4Ab3A4A13d6a396647C60867F21c8d 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x771602f7
# getter = None
# const = None
# payable = True
def add(uint256 _a, uint256 _b) payable: 
  require calldata.size - 4 >= 64
  require _b + _a >= _a
  return (_b + _a)


# hash = 0xa391c15b
# getter = None
# const = None
# payable = True
def div(uint256 _a, uint256 _b) payable: 
  require calldata.size - 4 >= 64
  require _b > 0
  require _b
  return (_a / _b)


# hash = 0xb67d77c5
# getter = None
# const = None
# payable = True
def sub(uint256 _a, uint256 _b) payable: 
  require calldata.size - 4 >= 64
  require _b <= _a
  return (_a - _b)


# hash = 0xc8a4ac9c
# getter = None
# const = None
# payable = True
def mul(uint256 _a, uint256 _b) payable: 
  require calldata.size - 4 >= 64
  if not _a:
      return 0
  require _b * _a / _a == _b
  return (_b * _a)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


