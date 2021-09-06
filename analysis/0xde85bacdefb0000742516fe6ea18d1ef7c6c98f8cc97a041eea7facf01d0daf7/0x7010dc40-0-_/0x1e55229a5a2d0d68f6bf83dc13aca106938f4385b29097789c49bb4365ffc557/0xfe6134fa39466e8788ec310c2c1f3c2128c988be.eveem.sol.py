# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xfE6134fa39466E8788eC310C2c1F3C2128C988BE 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x1b5ac4b5
# getter = None
# const = None
# payable = True
def abs(int256 m_val) payable: 
  if m_val <=′ 0:
      return -m_val
  return m_val


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


