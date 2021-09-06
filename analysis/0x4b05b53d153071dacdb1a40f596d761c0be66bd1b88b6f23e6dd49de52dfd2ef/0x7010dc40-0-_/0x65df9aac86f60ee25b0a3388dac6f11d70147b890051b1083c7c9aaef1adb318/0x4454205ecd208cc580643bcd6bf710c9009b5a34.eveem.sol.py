# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4454205ECd208CC580643Bcd6bF710C9009B5a34 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x1b5ac4b5
# getter = None
# const = None
# payable = True
def abs(int256 _val) payable: 
  if _val <=′ 0:
      return -_val
  return _val


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


