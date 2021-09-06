# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xFa16ce2c9136d37Ea7630e6A83f8C844Af314AC0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    multiplier # mask: a s
    # storage address 1
    baseRate # mask: a s
# hash = 0x15f24053
# getter = None
# const = None
# payable = True
def unknown15f24053(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 96
  if not m_param2:
      if mbaseRate + (0 / 10^18) < 0 / 10^18:
          return 4, 0
      return 0, mbaseRate / 584 * 3600
  if m_param2 + m_param1 < m_param1:
      return 1, 0
  if not m_param2:
      if not m_param2 + m_param1:
          return 2, 0
      if not 0 / m_param2 + m_param1:
          if mbaseRate + (0 / 10^18) < 0 / 10^18:
              return 4, 0
          return 0, mbaseRate / 584 * 3600
      if mmultiplier * 0 / m_param2 + m_param1 / 0 / m_param2 + m_param1 != mmultiplier:
          return 3, 0
      if mbaseRate + (mmultiplier * 0 / m_param2 + m_param1 / 10^18) < mmultiplier * 0 / m_param2 + m_param1 / 10^18:
          return 4, 0
      return 0, mbaseRate + (mmultiplier * 0 / m_param2 + m_param1 / 10^18) / 584 * 3600
  if 10^18 * m_param2 / m_param2 != 10^18:
      return 2, 0
  if not m_param2 + m_param1:
      return 2, 0
  if not 10^18 * m_param2 / m_param2 + m_param1:
      if mbaseRate + (0 / 10^18) < 0 / 10^18:
          return 4, 0
      return 0, mbaseRate / 584 * 3600
  if mmultiplier * 10^18 * m_param2 / m_param2 + m_param1 / 10^18 * m_param2 / m_param2 + m_param1 != mmultiplier:
      return 3, 0
  if mbaseRate + (mmultiplier * 10^18 * m_param2 / m_param2 + m_param1 / 10^18) < mmultiplier * 10^18 * m_param2 / m_param2 + m_param1 / 10^18:
      return 4, 0
  return 0, mbaseRate + (mmultiplier * 10^18 * m_param2 / m_param2 + m_param1 / 10^18) / 584 * 3600


# hash = 0x1b3ed722
# getter = ['storage', 256, 0, 0]
# const = None
# payable = True
def multiplier() payable: 
  return mmultiplier


# hash = 0x1f68f20a
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def baseRate() payable: 
  return mbaseRate


# hash = 0x2191f92a
# getter = None
# const = ['return', 1]
# payable = True
const unknown2191f92a = 1


# hash = 0xa385fb96
# getter = None
# const = ['return', 2102400]
# payable = True
const unknowna385fb96 = (584 * 3600)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


