# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4a12FdF03040e87C242CA446E13622BB89E068c8 
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
    tokenAddress # mask: a s
# hash = 0x2f54bf6e
# getter = None
# const = None
# payable = False
def isOwner(address m_addr): # not payable
  return (mstor258m[addr(m_addr)m] > 0)


# hash = 0x4123cb6b
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def m_numOwners(): # not payable
  return mm_numOwners


# hash = 0x45c4db40
# getter = None
# const = None
# payable = False
def unknown45c4db40(addr m_param1): # not payable
  require mstor258m[callerm] > 0
  if 512 == mstor260m.length:
      require mstor258m[callerm] > 0
      [94midx = 0
      mwhile [94midx < mstor260m.lengthm:
          mem[0] = 260
          if mstor260m[[94midxm]:
              require [94midx < mstor260m.length
              mem[0] = mstor260m[[94midxm]
              mem[32] = 259
              mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
          [94midx = [94midx + 1
          mcontinue 
      mstor260m.length = 0
      [94midx = 0
      mwhile mstor260m.length > [94midxm:
          mstor260m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  if not mstor259m[call.data[0 len calldata.size]m]m.field_0:
      mstor259m[call.data[0 len calldata.size]m]m.field_0 = mm_multiOwnedRequired
      mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
      mstor260m.length++
      if not mstor260m.length <= mstor260m.length + 1:
          [94midx = mstor260m.length + 1
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor259m[call.data[0 len calldata.size]m]m.field_512 = mstor260m.length
      require mstor260m.length < mstor260m.length
      mstor260m[mstor260m.lengthm] = sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0
      require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
      require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
  require mstor258m[callerm]
  require mstor258m[callerm] <= 250
  if 0 == mstor259m[call.data[0 len calldata.size]m]m.field_256 and 2^mstor258m[callerm]:
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 > 0
      if mstor259m[call.data[0 len calldata.size]m]m.field_0 != 1:
          mstor259m[call.data[0 len calldata.size]m]m.field_0--
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 2^mstor258m[callerm] or mstor259m[call.data[0 len calldata.size]m]m.field_256
          require mstor259m[call.data[0 len calldata.size]m]m.field_0
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
          require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_0 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          require ext_code.size(mtokenAddress)
          call mtokenAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          require ext_call.success
          require ext_code.size(mtokenAddress)
          call mtokenAddress.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_param1), ext_call.return_data[0]
          require ext_call.success
      return 0
  else:
      return 0


# hash = 0x4e4ab830
# getter = None
# const = None
# payable = False
def amIOwner(): # not payable
  require mstor258m[callerm] > 0
  return 1


# hash = 0x7065cb48
# getter = None
# const = None
# payable = False
def addOwner(address m_owner): # not payable
  require mstor258m[addr(m_owner)m] <= 0
  require mm_numOwners + 1 > 0
  require mm_numOwners + 1 <= 250
  require mstor258m[callerm] > 0
  if 512 == mstor260m.length:
      require mstor258m[callerm] > 0
      [94midx = 0
      mwhile [94midx < mstor260m.lengthm:
          mem[0] = 260
          if mstor260m[[94midxm]:
              require [94midx < mstor260m.length
              mem[0] = mstor260m[[94midxm]
              mem[32] = 259
              mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
          [94midx = [94midx + 1
          mcontinue 
      mstor260m.length = 0
      [94midx = 0
      mwhile mstor260m.length > [94midxm:
          mstor260m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  if not mstor259m[call.data[0 len calldata.size]m]m.field_0:
      mstor259m[call.data[0 len calldata.size]m]m.field_0 = mm_multiOwnedRequired
      mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
      mstor260m.length++
      if not mstor260m.length <= mstor260m.length + 1:
          [94midx = mstor260m.length + 1
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor259m[call.data[0 len calldata.size]m]m.field_512 = mstor260m.length
      require mstor260m.length < mstor260m.length
      mstor260m[mstor260m.lengthm] = sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0
      require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
      require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
  require mstor258m[callerm]
  require mstor258m[callerm] <= 250
  if 0 == mstor259m[call.data[0 len calldata.size]m]m.field_256 and 2^mstor258m[callerm]:
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 > 0
      if mstor259m[call.data[0 len calldata.size]m]m.field_0 != 1:
          mstor259m[call.data[0 len calldata.size]m]m.field_0--
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 2^mstor258m[callerm] or mstor259m[call.data[0 len calldata.size]m]m.field_256
          require mstor259m[call.data[0 len calldata.size]m]m.field_0
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
          require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_0 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          require mm_numOwners > 0
          require mm_numOwners <= 250
          require not mstor2m.length
          require mm_multiOwnedRequired
          require mm_multiOwnedRequired <= mm_numOwners
          require mstor258m[callerm] > 0
          [94midx = 0
          mwhile [94midx < mstor260m.lengthm:
              mem[0] = 260
              if mstor260m[[94midxm]:
                  require [94midx < mstor260m.length
                  mem[0] = mstor260m[[94midxm]
                  mem[32] = 259
                  mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor260m.length = 0
          [94midx = 0
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
          mm_numOwners++
          require mm_numOwners + 1 < 256
          mownerm[mstor1m] = m_owner
          require mm_numOwners
          require mm_numOwners <= 250
          mstor258m[addr(m_owner)m] = mm_numOwners
          require mm_numOwners > 0
          require mm_numOwners <= 250
          require not mstor2m.length
          require mm_multiOwnedRequired
          require mm_multiOwnedRequired <= mm_numOwners
          log OwnerAdded(address newOwner=_owner)


# hash = 0x787d64e4
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def m_multiOwnedRequired(): # not payable
  return mm_multiOwnedRequired


# hash = 0xa0e67e2b
# getter = None
# const = None
# payable = False
def getOwners(): # not payable
  [94midx = 0
  mwhile [94midx < mm_numOwnersm:
      require [94midx + 1 < 256
      require [94midx < mm_numOwners
      mem[(32 * [94midx) + 192] = mownerm[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * mm_numOwners) + 192] = 32
  mem[(32 * mm_numOwners) + 224] = mm_numOwners
  [94ms = 0
  mwhile mm_numOwners < 32 * mm_numOwnersm:
      mem[(34 * mm_numOwners) + 256] = mem[mm_numOwners + 192]
      [94ms = mm_numOwners + 32
      mcontinue 
  return memory
    from (32 * mm_numOwners) + 192
     [93mlen (96 * mm_numOwners) + 64


# hash = 0xb75c7dc6
# getter = None
# const = None
# payable = False
def revoke(bytes32 m_digest): # not payable
  require mstor259m[m_digestm]m.field_0
  require mstor258m[callerm] > 0
  require mstor258m[callerm]
  require mstor258m[callerm] <= 250
  require 2^mstor258m[callerm] and mstor259m[m_digestm]m.field_256 > 0
  require mstor259m[m_digestm]m.field_0
  require mstor259m[m_digestm]m.field_512 < mstor260m.length
  require mstor260m[mstor259m[m_digestm]m.field_512m] == m_digest
  require mstor259m[m_digestm]m.field_0 <= mm_multiOwnedRequired
  mstor259m[m_digestm]m.field_0++
  mstor259m[m_digestm]m.field_256 -= 2^mstor258m[callerm]
  require mstor259m[m_digestm]m.field_0
  require mstor259m[m_digestm]m.field_512 < mstor260m.length
  require mstor260m[mstor259m[m_digestm]m.field_512m] == m_digest
  require mstor259m[m_digestm]m.field_0 <= mm_multiOwnedRequired
  log Revoke(
        address owner=caller,
        bytes32 operation=_digest)


# hash = 0xba51a6df
# getter = None
# const = None
# payable = False
def changeRequirement(uint256 m_required): # not payable
  require m_required > 0
  require m_required <= mm_numOwners
  require mstor258m[callerm] > 0
  if 512 == mstor260m.length:
      require mstor258m[callerm] > 0
      [94midx = 0
      mwhile [94midx < mstor260m.lengthm:
          mem[0] = 260
          if mstor260m[[94midxm]:
              require [94midx < mstor260m.length
              mem[0] = mstor260m[[94midxm]
              mem[32] = 259
              mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
          [94midx = [94midx + 1
          mcontinue 
      mstor260m.length = 0
      [94midx = 0
      mwhile mstor260m.length > [94midxm:
          mstor260m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  if not mstor259m[call.data[0 len calldata.size]m]m.field_0:
      mstor259m[call.data[0 len calldata.size]m]m.field_0 = mm_multiOwnedRequired
      mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
      mstor260m.length++
      if not mstor260m.length <= mstor260m.length + 1:
          [94midx = mstor260m.length + 1
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor259m[call.data[0 len calldata.size]m]m.field_512 = mstor260m.length
      require mstor260m.length < mstor260m.length
      mstor260m[mstor260m.lengthm] = sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0
      require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
      require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
  require mstor258m[callerm]
  require mstor258m[callerm] <= 250
  if 0 == mstor259m[call.data[0 len calldata.size]m]m.field_256 and 2^mstor258m[callerm]:
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 > 0
      if mstor259m[call.data[0 len calldata.size]m]m.field_0 != 1:
          mstor259m[call.data[0 len calldata.size]m]m.field_0--
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 2^mstor258m[callerm] or mstor259m[call.data[0 len calldata.size]m]m.field_256
          require mstor259m[call.data[0 len calldata.size]m]m.field_0
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
          require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_0 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          mm_multiOwnedRequired = m_required
          require mstor258m[callerm] > 0
          [94midx = 0
          mwhile [94midx < mstor260m.lengthm:
              mem[0] = 260
              if mstor260m[[94midxm]:
                  require [94midx < mstor260m.length
                  mem[0] = mstor260m[[94midxm]
                  mem[32] = 259
                  mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor260m.length = 0
          [94midx = 0
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
          log RequirementChanged(uint256 newRequirement=_required)


# hash = 0xc0ee0b8a
# getter = None
# const = ['return', 1]
# payable = False
const tokenFallback(address m_from, uint256 m_value, bytes m_param3) = 1


# hash = 0xc2cf7326
# getter = None
# const = None
# payable = False
def hasConfirmed(bytes32 m_operation, address m_owner): # not payable
  require mstor259m[m_operationm]m.field_0
  require mstor258m[addr(m_owner)m] > 0
  require mstor258m[addr(m_owner)m]
  require mstor258m[addr(m_owner)m] <= 250
  return bool(mstor259m[m_operationm]m.field_256 and 2^mstor258m[addr(m_owner)m])


# hash = 0xc41a360a
# getter = ['storage', 160, 0, ['add', 3, ['cd', 4]]]
# const = None
# payable = False
def getOwner(uint256 m_id): # not payable
  require m_id + 1 < 256
  return mownerm[m_idm]


# hash = 0xf00d4b5d
# getter = None
# const = None
# payable = False
def changeOwner(address m_previousOwner, address m_newOwner): # not payable
  require mstor258m[addr(m_previousOwner)m] > 0
  require mstor258m[addr(m_newOwner)m] <= 0
  require mstor258m[callerm] > 0
  if 512 == mstor260m.length:
      require mstor258m[callerm] > 0
      [94midx = 0
      mwhile [94midx < mstor260m.lengthm:
          mem[0] = 260
          if mstor260m[[94midxm]:
              require [94midx < mstor260m.length
              mem[0] = mstor260m[[94midxm]
              mem[32] = 259
              mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
              mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
          [94midx = [94midx + 1
          mcontinue 
      mstor260m.length = 0
      [94midx = 0
      mwhile mstor260m.length > [94midxm:
          mstor260m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  if not mstor259m[call.data[0 len calldata.size]m]m.field_0:
      mstor259m[call.data[0 len calldata.size]m]m.field_0 = mm_multiOwnedRequired
      mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
      mstor260m.length++
      if not mstor260m.length <= mstor260m.length + 1:
          [94midx = mstor260m.length + 1
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor259m[call.data[0 len calldata.size]m]m.field_512 = mstor260m.length
      require mstor260m.length < mstor260m.length
      mstor260m[mstor260m.lengthm] = sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0
      require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
      require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
  require mstor258m[callerm]
  require mstor258m[callerm] <= 250
  if 0 == mstor259m[call.data[0 len calldata.size]m]m.field_256 and 2^mstor258m[callerm]:
      require mstor259m[call.data[0 len calldata.size]m]m.field_0 > 0
      if mstor259m[call.data[0 len calldata.size]m]m.field_0 != 1:
          mstor259m[call.data[0 len calldata.size]m]m.field_0--
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 2^mstor258m[callerm] or mstor259m[call.data[0 len calldata.size]m]m.field_256
          require mstor259m[call.data[0 len calldata.size]m]m.field_0
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          require mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] == sha3(call.data[0 len calldata.size])
          require mstor259m[call.data[0 len calldata.size]m]m.field_0 <= mm_multiOwnedRequired
          log Confirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
      else:
          require mstor259m[call.data[0 len calldata.size]m]m.field_512 < mstor260m.length
          mstor260m[mstor259m[call.data[0 len calldata.size]m]m.field_512m] = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_0 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_256 = 0
          mstor259m[call.data[0 len calldata.size]m]m.field_512 = 0
          log FinalConfirmation(
                address owner=caller,
                bytes32 operation=sha3(call.data[0 len calldata.size]))
          require mm_numOwners > 0
          require mm_numOwners <= 250
          require not mstor2m.length
          require mm_multiOwnedRequired
          require mm_multiOwnedRequired <= mm_numOwners
          require mstor258m[callerm] > 0
          [94midx = 0
          mwhile [94midx < mstor260m.lengthm:
              mem[0] = 260
              if mstor260m[[94midxm]:
                  require [94midx < mstor260m.length
                  mem[0] = mstor260m[[94midxm]
                  mem[32] = 259
                  mstor259m[mstor260m[[94midxm]m]m.field_0 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_256 = 0
                  mstor259m[mstor260m[[94midxm]m]m.field_512 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor260m.length = 0
          [94midx = 0
          mwhile mstor260m.length > [94midxm:
              mstor260m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
          require mstor258m[addr(m_previousOwner)m]
          require mstor258m[addr(m_previousOwner)m] <= 250
          require mstor258m[addr(m_previousOwner)m] < 256
          mstor2m[mstor258m[addr(m_previousOwner)m]m] = m_newOwner
          mstor258m[addr(m_previousOwner)m] = 0
          mstor258m[m_newOwnerm] = mstor258m[addr(m_previousOwner)m]
          require mm_numOwners > 0
          require mm_numOwners <= 250
          require not mstor2m.length
          require mm_multiOwnedRequired
          require mm_multiOwnedRequired <= mm_numOwners
          log OwnerChanged(
                address oldOwner=addr(_previousOwner),
                address newOwner=_newOwner)


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 261]
# const = None
# payable = False
def token(): # not payable
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


