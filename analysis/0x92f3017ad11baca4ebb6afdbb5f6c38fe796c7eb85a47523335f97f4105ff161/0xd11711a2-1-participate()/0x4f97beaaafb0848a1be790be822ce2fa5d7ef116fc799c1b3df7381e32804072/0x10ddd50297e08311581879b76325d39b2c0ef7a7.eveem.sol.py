# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x10DDd50297E08311581879b76325D39B2c0Ef7A7 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown8b8002b2Address # mask: a s
# hash = 0x19240661
# getter = None
# const = None
# payable = False
def setTrusted(address m_addr): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  munknown8b8002b2Address = m_addr
  log 0x1a812c8d: addr(_addr), Array(len=22, data='Trasted is configured!')


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x74550831
# getter = None
# const = None
# payable = False
def unknown74550831(uint8 m_param1, uint8 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  require calldata.size - 4 >= 128
  require munknown8b8002b2Address == caller
  if m_param3 >= 100:
      if m_param3 <= 100:
          require m_param3 - 100
          if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 100) + m_param4 % 3:
              if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 100) + m_param4 % 3 != 1:
                  require m_param3 % m_param3 - 100
                  require m_param2
                  require m_param1
                  return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + m_param1, (block.number - 2 % m_param2) + m_param1, (block.number - 3 % 3 * m_param1) + m_param1, (block.number - 4 % 5) + m_param1^2) % m_param1)
              else:
                  require m_param3 % m_param3 - 100
                  require m_param2
                  require m_param1
                  return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + (m_param3 % m_param3 - 100), (block.number - 2 % m_param2) + (m_param3 % m_param3 - 100), (block.number - 3 % 3 * m_param1) + (m_param3 % m_param3 - 100), (block.number - 4 % 5) + (m_param3 % m_param3 - 100)^2) % m_param1)
          else:
              require m_param3 % m_param3 - 100
              require m_param2
              require m_param1
              return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + m_param4, (block.number - 2 % m_param2) + m_param4, (block.number - 3 % 3 * m_param1) + m_param4, (block.number - 4 % 5) + m_param4^2) % m_param1)
      else:
          if m_param3 >= 300:
              require m_param3 - 100
              if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 100) + m_param4 % 3:
                  if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 100) + m_param4 % 3 != 1:
                      require m_param3 % m_param3 - 100
                      require m_param2
                      require m_param1
                      return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + m_param1, (block.number - 2 % m_param2) + m_param1, (block.number - 3 % 3 * m_param1) + m_param1, (block.number - 4 % 5) + m_param1^2) % m_param1)
                  else:
                      require m_param3 % m_param3 - 100
                      require m_param2
                      require m_param1
                      return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + (m_param3 % m_param3 - 100), (block.number - 2 % m_param2) + (m_param3 % m_param3 - 100), (block.number - 3 % 3 * m_param1) + (m_param3 % m_param3 - 100), (block.number - 4 % 5) + (m_param3 % m_param3 - 100)^2) % m_param1)
              else:
                  require m_param3 % m_param3 - 100
                  require m_param2
                  require m_param1
                  return (sha3((block.number - 1 % m_param3 % m_param3 - 100) + m_param4, (block.number - 2 % m_param2) + m_param4, (block.number - 3 % 3 * m_param1) + m_param4, (block.number - 4 % 5) + m_param4^2) % m_param1)
          else:
              require m_param3 - 50
              if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 50) + m_param4 % 3:
                  if uint8(m_param1 + m_param2) + (m_param3 % m_param3 - 50) + m_param4 % 3 != 1:
                      require m_param3 % m_param3 - 50
                      require m_param2
                      require m_param1
                      return (sha3((block.number - 1 % m_param3 % m_param3 - 50) + m_param1, (block.number - 2 % m_param2) + m_param1, (block.number - 3 % 3 * m_param1) + m_param1, (block.number - 4 % 5) + m_param1^2) % m_param1)
                  else:
                      require m_param3 % m_param3 - 50
                      require m_param2
                      require m_param1
                      return (sha3((block.number - 1 % m_param3 % m_param3 - 50) + (m_param3 % m_param3 - 50), (block.number - 2 % m_param2) + (m_param3 % m_param3 - 50), (block.number - 3 % 3 * m_param1) + (m_param3 % m_param3 - 50), (block.number - 4 % 5) + (m_param3 % m_param3 - 50)^2) % m_param1)
              else:
                  require m_param3 % m_param3 - 50
                  require m_param2
                  require m_param1
                  return (sha3((block.number - 1 % m_param3 % m_param3 - 50) + m_param4, (block.number - 2 % m_param2) + m_param4, (block.number - 3 % 3 * m_param1) + m_param4, (block.number - 4 % 5) + m_param4^2) % m_param1)
  else:
      if uint8(m_param1 + m_param2) + uint8(m_param2^2) + m_param3 + m_param4 % 3:
          if uint8(m_param1 + m_param2) + uint8(m_param2^2) + m_param3 + m_param4 % 3 != 1:
              require uint8(m_param2^2) + m_param3
              require m_param2
              require m_param1
              return (sha3((block.number - 1 % uint8(m_param2^2) + m_param3) + m_param1, (block.number - 2 % m_param2) + m_param1, (block.number - 3 % 3 * m_param1) + m_param1, (block.number - 4 % 5) + m_param1^2) % m_param1)
          else:
              require uint8(m_param2^2) + m_param3
              require m_param2
              require m_param1
              return (sha3((block.number - 1 % uint8(m_param2^2) + m_param3) + uint8(m_param2^2) + m_param3, (block.number - 2 % m_param2) + uint8(m_param2^2) + m_param3, (block.number - 3 % 3 * m_param1) + uint8(m_param2^2) + m_param3, (block.number - 4 % 5) + (uint8(m_param2^2) + m_param3)^2) % m_param1)
      else:
          require uint8(m_param2^2) + m_param3
          require m_param2
          require m_param1
          return (sha3((block.number - 1 % uint8(m_param2^2) + m_param3) + m_param4, (block.number - 2 % m_param2) + m_param4, (block.number - 3 % 3 * m_param1) + m_param4, (block.number - 4 % 5) + m_param4^2) % m_param1)


# hash = 0x8b8002b2
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown8b8002b2(): # not payable
  return munknown8b8002b2Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == mowner)


# hash = 0xcc61681c
# getter = None
# const = None
# payable = True
def unknowncc61681c() payable: 
  require munknown8b8002b2Address == caller
  return not not munknown8b8002b2Address


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


