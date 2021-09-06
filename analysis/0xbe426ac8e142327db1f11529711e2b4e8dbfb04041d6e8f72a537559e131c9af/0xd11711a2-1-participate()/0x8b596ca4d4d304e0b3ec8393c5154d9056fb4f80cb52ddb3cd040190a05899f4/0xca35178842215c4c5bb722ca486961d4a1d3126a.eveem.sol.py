# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xCA35178842215c4C5bb722ca486961d4A1D3126A 
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
def setTrusted(address _addr): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  unknown8b8002b2Address = _addr
  log 0x1a812c8d: addr(_addr), Array(len=22, data='Trasted is configured!')


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0


# hash = 0x74550831
# getter = None
# const = None
# payable = False
def unknown74550831(uint8 _param1, uint8 _param2, uint256 _param3, uint256 _param4): # not payable
  require calldata.size - 4 >= 128
  require caller == unknown8b8002b2Address
  if _param3 < 100:
      if not _param4 + uint8(_param2^2) + _param3 + uint8(_param2 + _param1) % 3:
          if uint8(_param2^2) + _param3:
              if _param2:
                  if _param1:
                      return (sha3((block.number - 1 % uint8(_param2^2) + _param3) + _param4, (block.number - 2 % _param2) + _param4, (block.number - 3 % 3 * _param1) + _param4, (block.number - 4 % 5) + _param4^2) % _param1)
      else:
          if _param4 + uint8(_param2^2) + _param3 + uint8(_param2 + _param1) % 3 != 1:
              if uint8(_param2^2) + _param3:
                  if _param2:
                      if _param1:
                          return (sha3((block.number - 1 % uint8(_param2^2) + _param3) + _param1, (block.number - 2 % _param2) + _param1, (block.number - 3 % 3 * _param1) + _param1, (block.number - 4 % 5) + _param1^2) % _param1)
          else:
              if uint8(_param2^2) + _param3:
                  if _param2:
                      if _param1:
                          return (sha3((block.number - 1 % uint8(_param2^2) + _param3) + uint8(_param2^2) + _param3, (block.number - 2 % _param2) + uint8(_param2^2) + _param3, (block.number - 3 % 3 * _param1) + uint8(_param2^2) + _param3, (block.number - 4 % 5) + (uint8(_param2^2) + _param3)^2) % _param1)
  else:
      if _param3 <= 100:
          if _param3 - 100:
              if not _param4 + (_param3 % _param3 - 100) + uint8(_param2 + _param1) % 3:
                  if _param3 % _param3 - 100:
                      if _param2:
                          if _param1:
                              return (sha3((block.number - 1 % _param3 % _param3 - 100) + _param4, (block.number - 2 % _param2) + _param4, (block.number - 3 % 3 * _param1) + _param4, (block.number - 4 % 5) + _param4^2) % _param1)
              else:
                  if _param4 + (_param3 % _param3 - 100) + uint8(_param2 + _param1) % 3 != 1:
                      if _param3 % _param3 - 100:
                          if _param2:
                              if _param1:
                                  return (sha3((block.number - 1 % _param3 % _param3 - 100) + _param1, (block.number - 2 % _param2) + _param1, (block.number - 3 % 3 * _param1) + _param1, (block.number - 4 % 5) + _param1^2) % _param1)
                  else:
                      if _param3 % _param3 - 100:
                          if _param2:
                              if _param1:
                                  return (sha3((block.number - 1 % _param3 % _param3 - 100) + (_param3 % _param3 - 100), (block.number - 2 % _param2) + (_param3 % _param3 - 100), (block.number - 3 % 3 * _param1) + (_param3 % _param3 - 100), (block.number - 4 % 5) + (_param3 % _param3 - 100)^2) % _param1)
      else:
          if _param3 >= 300:
              if _param3 - 100:
                  if not _param4 + (_param3 % _param3 - 100) + uint8(_param2 + _param1) % 3:
                      if _param3 % _param3 - 100:
                          if _param2:
                              if _param1:
                                  return (sha3((block.number - 1 % _param3 % _param3 - 100) + _param4, (block.number - 2 % _param2) + _param4, (block.number - 3 % 3 * _param1) + _param4, (block.number - 4 % 5) + _param4^2) % _param1)
                  else:
                      if _param4 + (_param3 % _param3 - 100) + uint8(_param2 + _param1) % 3 != 1:
                          if _param3 % _param3 - 100:
                              if _param2:
                                  if _param1:
                                      return (sha3((block.number - 1 % _param3 % _param3 - 100) + _param1, (block.number - 2 % _param2) + _param1, (block.number - 3 % 3 * _param1) + _param1, (block.number - 4 % 5) + _param1^2) % _param1)
                      else:
                          if _param3 % _param3 - 100:
                              if _param2:
                                  if _param1:
                                      return (sha3((block.number - 1 % _param3 % _param3 - 100) + (_param3 % _param3 - 100), (block.number - 2 % _param2) + (_param3 % _param3 - 100), (block.number - 3 % 3 * _param1) + (_param3 % _param3 - 100), (block.number - 4 % 5) + (_param3 % _param3 - 100)^2) % _param1)
          else:
              if _param3 - 50:
                  if not _param4 + (_param3 % _param3 - 50) + uint8(_param2 + _param1) % 3:
                      if _param3 % _param3 - 50:
                          if _param2:
                              if _param1:
                                  return (sha3((block.number - 1 % _param3 % _param3 - 50) + _param4, (block.number - 2 % _param2) + _param4, (block.number - 3 % 3 * _param1) + _param4, (block.number - 4 % 5) + _param4^2) % _param1)
                  else:
                      if _param4 + (_param3 % _param3 - 50) + uint8(_param2 + _param1) % 3 != 1:
                          if _param3 % _param3 - 50:
                              if _param2:
                                  if _param1:
                                      return (sha3((block.number - 1 % _param3 % _param3 - 50) + _param1, (block.number - 2 % _param2) + _param1, (block.number - 3 % 3 * _param1) + _param1, (block.number - 4 % 5) + _param1^2) % _param1)
                      else:
                          if _param3 % _param3 - 50:
                              if _param2:
                                  if _param1:
                                      return (sha3((block.number - 1 % _param3 % _param3 - 50) + (_param3 % _param3 - 50), (block.number - 2 % _param2) + (_param3 % _param3 - 50), (block.number - 3 % 3 * _param1) + (_param3 % _param3 - 50), (block.number - 4 % 5) + (_param3 % _param3 - 50)^2) % _param1)
  revert


# hash = 0x8b8002b2
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown8b8002b2(): # not payable
  return unknown8b8002b2Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == owner)


# hash = 0xcc61681c
# getter = ['bool', ['storage', 160, 0, 1]]
# const = None
# payable = True
def unknowncc61681c() payable: 
  require caller == unknown8b8002b2Address
  return bool(unknown8b8002b2Address)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


