# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xbD0Ef4D900fa6b5CCefFecd81550c84A530bdf52 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x173825d9': 'removeOwner(address _owner)'} 

# storage definitions
def storage:
    # storage address 0
    m_multiOwnedRequired # mask: a s
    # storage address 1
    m_numOwners # mask: a s
    # storage address 2
    stor2
    # storage address 3
    owner
    # storage address 258
    stor258
    # storage address 259
    stor259
    # storage address 260
    stor260
    # storage address 261
    stor261 # mask: a s
    # storage address 261
    escrowAddress # mask: a s
# hash = 0x0d5defa4
# getter = ['storage', 160, 0, 261]
# const = None
# payable = False
def escrowAddress(): # not payable
  return escrowAddress


# hash = 0x2f54bf6e
# getter = None
# const = None
# payable = False
def isOwner(address _addr): # not payable
  return (stor258[addr(_addr)] > 0)


# hash = 0x38d5630b
# getter = None
# const = None
# payable = False
def unknown38d5630b(addr _param1): # not payable
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller] != 0:
      return 0
  require stor259[call.data[0 len calldata.size]].field_0 > 0
  if stor259[call.data[0 len calldata.size]].field_0 != 1:
      stor259[call.data[0 len calldata.size]].field_0--
      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
      log Confirmation(
            address owner=caller,
            bytes32 operation=sha3(call.data[0 len calldata.size]))
      return 0
  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
  stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
  stor259[call.data[0 len calldata.size]].field_0 = 0
  stor259[call.data[0 len calldata.size]].field_256 = 0
  stor259[call.data[0 len calldata.size]].field_512 = 0
  log FinalConfirmation(
        address owner=caller,
        bytes32 operation=sha3(call.data[0 len calldata.size]))
  escrowAddress = _param1
  return 1


# hash = 0x3e6494db
# getter = None
# const = None
# payable = False
def unknown3e6494db(): # not payable
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller] != 0:
      return 0
  require stor259[call.data[0 len calldata.size]].field_0 > 0
  if stor259[call.data[0 len calldata.size]].field_0 != 1:
      stor259[call.data[0 len calldata.size]].field_0--
      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
      log Confirmation(
            address owner=caller,
            bytes32 operation=sha3(call.data[0 len calldata.size]))
      return 0
  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
  stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
  stor259[call.data[0 len calldata.size]].field_0 = 0
  stor259[call.data[0 len calldata.size]].field_256 = 0
  stor259[call.data[0 len calldata.size]].field_512 = 0
  log FinalConfirmation(
        address owner=caller,
        bytes32 operation=sha3(call.data[0 len calldata.size]))
  require stor261
  call escrowAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success
  return 1


# hash = 0x4123cb6b
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def m_numOwners(): # not payable
  return m_numOwners


# hash = 0x4e4ab830
# getter = None
# const = None
# payable = False
def amIOwner(): # not payable
  require stor258[caller] > 0
  return 1


# hash = 0x7065cb48
# getter = None
# const = None
# payable = False
def addOwner(address _owner): # not payable
  require stor258[addr(_owner)] <= 0
  require m_numOwners + 1 > 0
  require m_numOwners + 1 <= 250
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if 0 == stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller]:
      require stor259[call.data[0 len calldata.size]].field_0 > 0
      if stor259[call.data[0 len calldata.size]].field_0 != 1:
          stor259[call.data[0 len calldata.size]].field_0--
          stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
          require stor259[call.data[0 len calldata.size]].field_0
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
          require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
          stor259[call.data[0 len calldata.size]].field_0 = 0
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor259[call.data[0 len calldata.size]].field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          require m_numOwners > 0
          require m_numOwners <= 250
          require not stor2.length
          require m_multiOwnedRequired
          require m_multiOwnedRequired <= m_numOwners
          require stor258[caller] > 0
          [94midx = 0
          while [94midx < stor260.length:
              mem[0] = 260
              if stor260[[94midx]:
                  require [94midx < stor260.length
                  mem[0] = stor260[[94midx]
                  mem[32] = 259
                  stor259[stor260[[94midx]].field_0 = 0
                  stor259[stor260[[94midx]].field_256 = 0
                  stor259[stor260[[94midx]].field_512 = 0
              [94midx = [94midx + 1
              continue 
          stor260.length = 0
          [94midx = 0
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
          m_numOwners++
          require m_numOwners + 1 < 256
          owner[stor1] = _owner
          require m_numOwners
          require m_numOwners <= 250
          stor258[addr(_owner)] = m_numOwners
          require m_numOwners > 0
          require m_numOwners <= 250
          require not stor2.length
          require m_multiOwnedRequired
          require m_multiOwnedRequired <= m_numOwners
          log OwnerAdded(address newOwner=_owner)


# hash = 0x787d64e4
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def m_multiOwnedRequired(): # not payable
  return m_multiOwnedRequired


# hash = 0xa0e67e2b
# getter = None
# const = None
# payable = False
def getOwners(): # not payable
  [94midx = 0
  while [94midx < m_numOwners:
      require [94midx + 1 < 256
      require [94midx < m_numOwners
      mem[(32 * [94midx) + 192] = owner[[94midx]
      [94midx = [94midx + 1
      continue 
  mem[(32 * m_numOwners) + 192] = 32
  mem[(32 * m_numOwners) + 224] = m_numOwners
  [94ms = 0
  while m_numOwners < 32 * m_numOwners:
      mem[(34 * m_numOwners) + 256] = mem[m_numOwners + 192]
      [94ms = m_numOwners + 32
      continue 
  return memory
    from (32 * m_numOwners) + 192
     [93mlen (96 * m_numOwners) + 64


# hash = 0xb75c7dc6
# getter = None
# const = None
# payable = False
def revoke(bytes32 _digest): # not payable
  require stor259[_digest].field_0
  require stor258[caller] > 0
  require stor258[caller]
  require stor258[caller] <= 250
  require 2^stor258[caller] and stor259[_digest].field_256 > 0
  require stor259[_digest].field_0
  require stor259[_digest].field_512 < stor260.length
  require stor260[stor259[_digest].field_512] == _digest
  require stor259[_digest].field_0 <= m_multiOwnedRequired
  stor259[_digest].field_0++
  stor259[_digest].field_256 -= 2^stor258[caller]
  require stor259[_digest].field_0
  require stor259[_digest].field_512 < stor260.length
  require stor260[stor259[_digest].field_512] == _digest
  require stor259[_digest].field_0 <= m_multiOwnedRequired
  log Revoke(
        address owner=caller,
        bytes32 operation=_digest)


# hash = 0xba51a6df
# getter = None
# const = None
# payable = False
def changeRequirement(uint256 _required): # not payable
  require _required > 0
  require _required <= m_numOwners
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if 0 == stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller]:
      require stor259[call.data[0 len calldata.size]].field_0 > 0
      if stor259[call.data[0 len calldata.size]].field_0 != 1:
          stor259[call.data[0 len calldata.size]].field_0--
          stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
          require stor259[call.data[0 len calldata.size]].field_0
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
          require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
          stor259[call.data[0 len calldata.size]].field_0 = 0
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor259[call.data[0 len calldata.size]].field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          m_multiOwnedRequired = _required
          require stor258[caller] > 0
          [94midx = 0
          while [94midx < stor260.length:
              mem[0] = 260
              if stor260[[94midx]:
                  require [94midx < stor260.length
                  mem[0] = stor260[[94midx]
                  mem[32] = 259
                  stor259[stor260[[94midx]].field_0 = 0
                  stor259[stor260[[94midx]].field_256 = 0
                  stor259[stor260[[94midx]].field_512 = 0
              [94midx = [94midx + 1
              continue 
          stor260.length = 0
          [94midx = 0
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
          log RequirementChanged(uint256 newRequirement=_required)


# hash = 0xbb8236eb
# getter = None
# const = None
# payable = False
def unknownbb8236eb(): # not payable
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller] != 0:
      return 0
  require stor259[call.data[0 len calldata.size]].field_0 > 0
  if stor259[call.data[0 len calldata.size]].field_0 != 1:
      stor259[call.data[0 len calldata.size]].field_0--
      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
      log Confirmation(
            address owner=caller,
            bytes32 operation=sha3(call.data[0 len calldata.size]))
      return 0
  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
  stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
  stor259[call.data[0 len calldata.size]].field_0 = 0
  stor259[call.data[0 len calldata.size]].field_256 = 0
  stor259[call.data[0 len calldata.size]].field_512 = 0
  log FinalConfirmation(
        address owner=caller,
        bytes32 operation=sha3(call.data[0 len calldata.size]))
  if not eth.balance(this.address):
      call escrowAddress with:
           gas 2300 wei
  else:
      require 6 * eth.balance(this.address) / eth.balance(this.address) == 6
      call escrowAddress with:
         value 6 * eth.balance(this.address) / 10 wei
           gas 2300 * is_zero(value) wei
  require ext_call.success
  stor261 = 1
  return 1


# hash = 0xc2cf7326
# getter = None
# const = None
# payable = False
def hasConfirmed(bytes32 _operation, address _owner): # not payable
  require stor259[_operation].field_0
  require stor258[addr(_owner)] > 0
  require stor258[addr(_owner)]
  require stor258[addr(_owner)] <= 250
  return bool(stor259[_operation].field_256 and 2^stor258[addr(_owner)])


# hash = 0xc41a360a
# getter = ['storage', 160, 0, ['add', 3, ['cd', 4]]]
# const = None
# payable = False
def getOwner(uint256 _id): # not payable
  require _id + 1 < 256
  return owner[_id]


# hash = 0xf00d4b5d
# getter = None
# const = None
# payable = False
def changeOwner(address _previousOwner, address _newOwner): # not payable
  require stor258[addr(_previousOwner)] > 0
  require stor258[addr(_newOwner)] <= 0
  require stor258[caller] > 0
  if 512 == stor260.length:
      require stor258[caller] > 0
      [94midx = 0
      while [94midx < stor260.length:
          mem[0] = 260
          if stor260[[94midx]:
              require [94midx < stor260.length
              mem[0] = stor260[[94midx]
              mem[32] = 259
              stor259[stor260[[94midx]].field_0 = 0
              stor259[stor260[[94midx]].field_256 = 0
              stor259[stor260[[94midx]].field_512 = 0
          [94midx = [94midx + 1
          continue 
      stor260.length = 0
      [94midx = 0
      while stor260.length > [94midx:
          stor260[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  if not stor259[call.data[0 len calldata.size]].field_0:
      stor259[call.data[0 len calldata.size]].field_0 = m_multiOwnedRequired
      stor259[call.data[0 len calldata.size]].field_256 = 0
      stor260.length++
      if not stor260.length <= stor260.length + 1:
          [94midx = stor260.length + 1
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor259[call.data[0 len calldata.size]].field_512 = stor260.length
      require stor260.length < stor260.length
      stor260[stor260.length] = sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0
      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
      require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
      require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
  require stor258[caller]
  require stor258[caller] <= 250
  if 0 == stor259[call.data[0 len calldata.size]].field_256 and 2^stor258[caller]:
      require stor259[call.data[0 len calldata.size]].field_0 > 0
      if stor259[call.data[0 len calldata.size]].field_0 != 1:
          stor259[call.data[0 len calldata.size]].field_0--
          stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
          require stor259[call.data[0 len calldata.size]].field_0
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          require stor260[stor259[call.data[0 len calldata.size]].field_512] == sha3(call.data[0 len calldata.size])
          require stor259[call.data[0 len calldata.size]].field_0 <= m_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
          stor260[stor259[call.data[0 len calldata.size]].field_512] = 0
          stor259[call.data[0 len calldata.size]].field_0 = 0
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor259[call.data[0 len calldata.size]].field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          require m_numOwners > 0
          require m_numOwners <= 250
          require not stor2.length
          require m_multiOwnedRequired
          require m_multiOwnedRequired <= m_numOwners
          require stor258[caller] > 0
          [94midx = 0
          while [94midx < stor260.length:
              mem[0] = 260
              if stor260[[94midx]:
                  require [94midx < stor260.length
                  mem[0] = stor260[[94midx]
                  mem[32] = 259
                  stor259[stor260[[94midx]].field_0 = 0
                  stor259[stor260[[94midx]].field_256 = 0
                  stor259[stor260[[94midx]].field_512 = 0
              [94midx = [94midx + 1
              continue 
          stor260.length = 0
          [94midx = 0
          while stor260.length > [94midx:
              stor260[[94midx] = 0
              [94midx = [94midx + 1
              continue 
          require stor258[addr(_previousOwner)]
          require stor258[addr(_previousOwner)] <= 250
          require stor258[addr(_previousOwner)] < 256
          stor2[stor258[addr(_previousOwner)]] = _newOwner
          stor258[addr(_previousOwner)] = 0
          stor258[_newOwner] = stor258[addr(_previousOwner)]
          require m_numOwners > 0
          require m_numOwners <= 250
          require not stor2.length
          require m_multiOwnedRequired
          require m_multiOwnedRequired <= m_numOwners
          log OwnerChanged(
                address oldOwner=addr(_previousOwner),
                address newOwner=_newOwner)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


