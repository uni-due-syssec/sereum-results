# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x231773551c008D9DF068E8742691C52d1D86b2FE 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x771602f7
# getter = None
# const = None
# payable = True
def add(uint256 m_a, uint256 m_b) payable: 
  require calldata.size - 4 >= 64
  require m_b + m_a >= m_a
  return (m_b + m_a)


# hash = 0xa391c15b
# getter = None
# const = None
# payable = True
def div(uint256 m_a, uint256 m_b) payable: 
  require calldata.size - 4 >= 64
  require m_b > 0
  require m_b
  return (m_a / m_b)


# hash = 0xb67d77c5
# getter = None
# const = None
# payable = True
def sub(uint256 m_a, uint256 m_b) payable: 
  require calldata.size - 4 >= 64
  require m_b <= m_a
  return (m_a - m_b)


# hash = 0xc8a4ac9c
# getter = None
# const = None
# payable = True
def mul(uint256 m_a, uint256 m_b) payable: 
  require calldata.size - 4 >= 64
  if not m_a:
      return 0
  require m_b * m_a / m_a == m_b
  return (m_b * m_a)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


