# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x893cE40A9405d1a1cfD36efaA1f81992dD2a106C 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x8060830a': 'unknown8060830a(?)'} 

# storage definitions
def storage:
    # storage address 2
    stor2
    # storage address 4
    stor4
    # storage address 1
    stor1
    # storage address 29102676481673041902632991033461445430619272659676223336789171408008386403024
    stor29102676481673041902632991033461445430619272659676223336789171408008386403024
    # storage address 29102676481673041902632991033461445430619272659676223336789171408008386403023
    stor29102676481673041902632991033461445430619272659676223336789171408008386403023
    # storage address 5
    stor5
    # storage address 1546678032441257452667456735582814959992782782816731922691272282333561699759
    stor1546678032441257452667456735582814959992782782816731922691272282333561699759
    # storage address 0
    multiAccessRecipientAddress # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 3
    multiAccessRequired # mask: a s
# hash = 0x24f1ec37
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def multiAccessRecipient() payable: 
  return addr(mmultiAccessRecipientAddress)


# hash = 0x446294ad
# getter = None
# const = None
# payable = True
def multiAccessGetOwners() payable: 
  mem[160] = mstor5m.length - 1
  [94midx = 1
  mwhile [94midx < mstor5m.lengthm:
      mem[0] = 5
      require [94midx - 1 < mem[160]
      mem[(32 * [94midx - 1) + 192] = addr(mstor[[94midx + code.data[4730 len 32]m])
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * mstor5m.length - 1) + 192] = 32
  mem[(32 * mstor5m.length - 1) + 224] = mem[160]
  mem[(32 * mstor5m.length - 1) + 256 len 32 * mem[160]] = mem[192 len 32 * mem[160]]
  return 32, mem[(32 * mstor5m.length - 1) + 224 len (32 * mem[160]) + 32]


# hash = 0x4f60f334
# getter = None
# const = None
# payable = True
def multiAccessAddOwner(address m_owner) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mstor1m[call.data[0 len calldata.size]m] = 0
  if uint256(mstor4m[addr(m_owner)m]m.field_0) > 0:
      return 0
  mstor5m.length++
  if not mstor5m.length <= mstor5m.length + 1:
      [94midx = mstor5m.length + 1
      mwhile mstor5m.length > [94midxm:
          mstor5m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  require mstor5m.length < mstor5m.length
  uint256(mstor[mstor5m.length + code.data[4730 len 32]m]) = m_owner or Mask(96, 160, uint256(mstor[mstor5m.length + code.data[4730 len 32]m]))
  uint256(mstor4m[addr(m_owner)m]m.field_0) = mstor5m.length
  log OwnerAdded(address newOwner=_owner)
  return 1


# hash = 0x62891b5d
# getter = None
# const = None
# payable = True
def multiAccessChangeRequirement(uint256 m_newRequired) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mem[0] = sha3(call.data[0 len calldata.size])
  mstor1m[call.data[0 len calldata.size]m] = 0
  if 0 == m_newRequired:
      return 0
  if m_newRequired > mstor5m.length - 1:
      return 0
  mmultiAccessRequired = m_newRequired
  [94midx = mstor2m.length - 1
  mwhile [94midx > 0m:
      require [94midx < mstor2m.length
      mem[0] = uint256(mstor2m[[94midxm]m.field_512)
      mem[32] = 1
      mstor1m[uint256(mstor2m[[94midxm]m.field_512)m] = 0
      mstor2m.length--
      if not mstor2m.length <= mstor2m.length - 1:
          mem[0] = 2
          [94ms = sha3(mem[0]) + (3 * mstor2m.length) - 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94msm:
              uint256(mstor[[94msm]) = 0
              mem[0] = [94ms
              [94mt = sha3([94mt)
              mwhile sha3([94mt) + (uint256(mstor[[94mtm]) + 31 / 32) > [94mtm:
                  uint256(mstor[[94mtm]) = 0
                  [94mt = [94mt + 1
                  mcontinue 
              mstor1m[[94mtm] = 0
              uint256(mstor2m[[94mtm]m.field_0) = 0
              [94mt = [94mt + 3
              mcontinue 
      [94midx = [94midx - 1
      mcontinue 
  log RequirementChanged(uint256 newRequirement=_newRequired)
  return 1


# hash = 0x69a5e902
# getter = None
# const = None
# payable = True
def multiAccessCall(address m_to, uint256 m_value, bytes m_data) payable: 
  mem[128 len m_data.length] = m_data[allm]
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  mem[ceil32(m_data.length) + 128 len calldata.size] = call.data[0 len calldata.size]
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
      mem[ceil32(m_data.length) + 128] = 1
      log Confirmation(
            address owner=1,
            bytes32 operation=caller,
            bool completed=sha3(call.data[0 len calldata.size]))
      if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
          require mstor2m.length - 1 < mstor2m.length
          require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
              [94midx = 0
              mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                  uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              [94ms = 0
              [94midx = 0
              mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                  uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  mcontinue 
              [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
              mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                  uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
      mstor2m.length--
      if not mstor2m.length > mstor2m.length - 1:
          mstor1m[call.data[0 len calldata.size]m] = 0
          mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
          if not m_data.length % 32:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args m_data[allm]
          else:
              mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
              call m_to.mem[ceil32(m_data.length) + 128 len 4] with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]
      else:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) - 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
          mstor1m[call.data[0 len calldata.size]m] = 0
          mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
          if not m_data.length % 32:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args mem[ceil32(m_data.length) + 132 len m_data.length - 4]
          else:
              mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]
  else:
      mstor2m.length++
      if not mstor2m.length > mstor2m.length + 1:
          require mstor2m.length < mstor2m.length
          mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
          mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
          mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
          if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
              log Confirmation(
                    address owner=0,
                    bytes32 operation=caller,
                    bool completed=sha3(call.data[0 len calldata.size]))
              uint256(mstor2m[mstor2m.lengthm]m.field_256)--
              if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
                  uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
                  if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                      [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                      mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                          uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                          [94midx = [94midx + 1
                          mcontinue 
                  require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
              uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
              return 0
          mem[ceil32(m_data.length) + 128] = 1
          log Confirmation(
                address owner=1,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
              require mstor2m.length - 1 < mstor2m.length
              require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
                  [94midx = 0
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  [94ms = 0
                  [94midx = 0
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
                      [94ms = [94ms + 1
                      [94midx = [94midx + 1
                      mcontinue 
                  [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
          mstor2m.length--
          if not mstor2m.length > mstor2m.length - 1:
              mstor1m[call.data[0 len calldata.size]m] = 0
              mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
              if not m_data.length % 32:
                  call m_to with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args m_data[allm]
              else:
                  mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
                  call m_to.mem[ceil32(m_data.length) + 128 len 4] with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]
          else:
              mem[0] = 2
              [94midx = (3 * mstor2m.length) - 3
              mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
                  uint256(mstor[[94midx + sha3(mem[0])m]) = 0
                  mem[0] = [94midx + sha3(mem[0])
                  [94ms = sha3([94ms + sha3(mem[0]))
                  mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                      uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
                  uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
                  [94ms = [94ms + 3
                  mcontinue 
              mstor1m[call.data[0 len calldata.size]m] = 0
              mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
              if not m_data.length % 32:
                  call m_to with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args mem[ceil32(m_data.length) + 132 len m_data.length - 4]
              else:
                  mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
                  call m_to with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]
      else:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
          require mstor2m.length < mstor2m.length
          mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
          mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
          mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
          if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
              log Confirmation(
                    address owner=0,
                    bytes32 operation=caller,
                    bool completed=sha3(call.data[0 len calldata.size]))
              uint256(mstor2m[mstor2m.lengthm]m.field_256)--
              if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
                  uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
                  if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                      [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                      mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                          uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                          [94midx = [94midx + 1
                          mcontinue 
                  require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
              uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
              return 0
          mem[ceil32(m_data.length) + 128] = 1
          log Confirmation(
                address owner=1,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
              require mstor2m.length - 1 < mstor2m.length
              require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
                  [94midx = 0
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  [94ms = 0
                  [94midx = 0
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
                      [94ms = [94ms + 1
                      [94midx = [94midx + 1
                      mcontinue 
                  [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
              mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
          mstor2m.length--
          if not mstor2m.length <= mstor2m.length - 1:
              mem[0] = 2
              [94midx = (3 * mstor2m.length) - 3
              mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
                  uint256(mstor[[94midx + sha3(mem[0])m]) = 0
                  mem[0] = [94midx + sha3(mem[0])
                  [94ms = sha3([94ms + sha3(mem[0]))
                  mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                      uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
                  uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
                  [94ms = [94ms + 3
                  mcontinue 
          mstor1m[call.data[0 len calldata.size]m] = 0
          mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
          if not m_data.length % 32:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args mem[ceil32(m_data.length) + 132 len m_data.length - 4]
          else:
              mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]
  return bool(ext_call.success)


# hash = 0x73f310df
# getter = None
# const = None
# payable = True
def multiAccessRemoveOwner(address m_owner) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mstor1m[call.data[0 len calldata.size]m] = 0
  if not uint256(mstor4m[addr(m_owner)m]m.field_0):
      return 0
  if mmultiAccessRequired >= mstor5m.length - 1:
      return 0
  if uint256(mstor4m[addr(m_owner)m]m.field_0) < mstor5m.length - 1:
      require mstor5m.length - 1 < mstor5m.length
      require uint256(mstor4m[addr(m_owner)m]m.field_0) < mstor5m.length
      addr(mstor[uint256(mstor4m[addr(m_owner)m]m.field_0) + code.data[4730 len 32]m]) = mstor36B6m[mstor5m.lengthm]
      uint256(mstor4m[mstor36B6m[mstor5m.lengthm]m]m.field_0) = uint256(mstor4m[addr(m_owner)m]m.field_0)
  mstor5m.length--
  if not mstor5m.length <= mstor5m.length - 1:
      [94midx = mstor5m.length - 1
      mwhile mstor5m.length > [94midxm:
          mstor5m[[94midxm] = 0
          [94midx = [94midx + 1
          mcontinue 
  mem[0] = m_owner
  uint256(mstor4m[addr(m_owner)m]m.field_0) = 0
  [94midx = mstor2m.length - 1
  mwhile [94midx > 0m:
      require [94midx < mstor2m.length
      mem[0] = uint256(mstor2m[[94midxm]m.field_512)
      mem[32] = 1
      mstor1m[uint256(mstor2m[[94midxm]m.field_512)m] = 0
      mstor2m.length--
      if not mstor2m.length <= mstor2m.length - 1:
          mem[0] = 2
          [94ms = sha3(mem[0]) + (3 * mstor2m.length) - 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94msm:
              uint256(mstor[[94msm]) = 0
              mem[0] = [94ms
              [94mt = sha3([94mt)
              mwhile sha3([94mt) + (uint256(mstor[[94mtm]) + 31 / 32) > [94mtm:
                  uint256(mstor[[94mtm]) = 0
                  [94mt = [94mt + 1
                  mcontinue 
              mstor1m[[94mtm] = 0
              uint256(mstor2m[[94mtm]m.field_0) = 0
              [94mt = [94mt + 3
              mcontinue 
      [94midx = [94midx - 1
      mcontinue 
  log OwnerRemoved(address oldOwner=_owner)
  return 1


# hash = 0x7ed19af9
# getter = None
# const = None
# payable = True
def multiAccessRevoke(bytes32 m_operation) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if 0 == mstor1m[m_operationm]:
      return 0
  require mstor1m[m_operationm] < mstor2m.length
  if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[m_operationm]m]m.field_0):
      return 0
  if not mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('param', '_operation'), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
      return 0
  require mstor1m[m_operationm] < mstor2m.length
  require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[m_operationm]m]m.field_0)
  uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('param', '_operation'), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('param', '_operation'), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) and !(255 * 256^mstor4m[callerm]m.field_0 % 32)
  mstor4057m[mstor1m[m_operationm]m]++
  if mmultiAccessRequired == mstor4057m[mstor1m[m_operationm]m] + 1:
      if mstor1m[m_operationm] < mstor2m.length - 1:
          require mstor2m.length - 1 < mstor2m.length
          require mstor1m[m_operationm] < mstor2m.length
          uint256(mstor2m[mstor1m[m_operationm]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
              [94midx = 0
              mwhile uint256(mstor2m[mstor1m[m_operationm]m]m.field_0) + 31 / 32 > [94midxm:
                  uint8(mstor2m[(3 * mstor1m[m_operationm]) + [94midxm]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              [94ms = 0
              [94midx = 0
              mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                  uint256(mstor2m[(3 * mstor1m[m_operationm]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  mcontinue 
              [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
              mwhile uint256(mstor2m[mstor1m[m_operationm]m]m.field_0) + 31 / 32 > [94midxm:
                  uint8(mstor2m[(3 * mstor1m[m_operationm]) + [94midxm]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          uint256(mstor2m[mstor1m[m_operationm]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor2m[mstor1m[m_operationm]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
          mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[m_operationm]
      mstor2m.length--
      if not mstor2m.length <= mstor2m.length - 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) - 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      mstor1m[m_operationm] = 0
  log Revoke(
        address owner=caller,
        bytes32 operation=_operation)
  return 1


# hash = 0x9bd99195
# getter = None
# const = None
# payable = True
def multiAccessChangeOwner(address m_from, address m_to) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mstor1m[call.data[0 len calldata.size]m] = 0
  if uint256(mstor4m[addr(m_to)m]m.field_0) > 0:
      return 0
  mem[0] = m_from
  if not uint256(mstor4m[addr(m_from)m]m.field_0):
      return 0
  [94midx = mstor2m.length - 1
  mwhile [94midx > 0m:
      require [94midx < mstor2m.length
      mem[0] = uint256(mstor2m[[94midxm]m.field_512)
      mem[32] = 1
      mstor1m[uint256(mstor2m[[94midxm]m.field_512)m] = 0
      mstor2m.length--
      if not mstor2m.length <= mstor2m.length - 1:
          mem[0] = 2
          [94ms = sha3(mem[0]) + (3 * mstor2m.length) - 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94msm:
              uint256(mstor[[94msm]) = 0
              mem[0] = [94ms
              [94mt = sha3([94mt)
              mwhile sha3([94mt) + (uint256(mstor[[94mtm]) + 31 / 32) > [94mtm:
                  uint256(mstor[[94mtm]) = 0
                  [94mt = [94mt + 1
                  mcontinue 
              mstor1m[[94mtm] = 0
              uint256(mstor2m[[94mtm]m.field_0) = 0
              [94mt = [94mt + 3
              mcontinue 
      [94midx = [94midx - 1
      mcontinue 
  require uint256(mstor4m[addr(m_from)m]m.field_0) < mstor5m.length
  uint256(mstor[uint256(mstor4m[addr(m_from)m]m.field_0) + code.data[4730 len 32]m]) = m_to or Mask(96, 160, uint256(mstor[uint256(mstor4m[addr(m_from)m]m.field_0) + code.data[4730 len 32]m]))
  uint256(mstor4m[addr(m_from)m]m.field_0) = 0
  uint256(mstor4m[m_tom]m.field_0) = uint256(mstor4m[addr(m_from)m]m.field_0)
  log OwnerChanged(
        address oldOwner=addr(_from),
        address newOwner=_to)
  return 1


# hash = 0xb87c03c2
# getter = ['storage', 160, 0, ['add', ['code.data', 4730, 32], ['cd', 4]]]
# const = None
# payable = True
def multiAccessOwners(uint256 m_param1) payable: 
  require m_param1 < mstor5m.length
  return addr(mstor[code.data[4730 len 32] + m_param1m])


# hash = 0xc23693e0
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def multiAccessRequired() payable: 
  return mmultiAccessRequired


# hash = 0xd1cf113e
# getter = None
# const = None
# payable = True
def multiAccessSetRecipient(address m_address) payable: 
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mstor1m[call.data[0 len calldata.size]m] = 0
  uint256(mstor0) = m_address or Mask(96, 160, uint256(mstor0))
  return 1


# hash = 0xe419f189
# getter = None
# const = None
# payable = True
def multiAccessIsOwner(address m_addr) payable: 
  return (uint256(mstor4m[addr(m_addr)m]m.field_0) > 0)


# hash = 0xeb7402f5
# getter = None
# const = None
# payable = True
def multiAccessHasConfirmed(bytes32 m_operation, address m_owner) payable: 
  if mstor1m[m_operationm] != 0:
      require mstor1m[m_operationm] < mstor2m.length
      if uint256(mstor4m[addr(m_owner)m]m.field_0) < uint256(mstor2m[mstor1m[m_operationm]m]m.field_0):
          return bool(mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, ('param', '_owner')), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('param', '_operation'), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[addr(m_owner)m]m.field_0 % 32m])
      else:
          return 0
  else:
      return 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if uint256(mstor4m[callerm]m.field_0) <= 0:
      return 0
  if mstor1m[call.data[0 len calldata.size]m] != 0:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
          if mstor(floor32(stor[('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor4', 4))]) + ('array', ('mul', 3, ('stor', 256, 0, ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2)))m[mstor4m[callerm]m.field_0 % 32m]:
              return 0
  if mstor1m[call.data[0 len calldata.size]m]:
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      if uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0):
              uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('map', ('data', ('call.data', 0, 'calldatasize')), ('name', 'stor1', 1)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  else:
      mstor2m.length++
      if not mstor2m.length <= mstor2m.length + 1:
          mem[0] = 2
          [94midx = (3 * mstor2m.length) + 3
          mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
              uint256(mstor[[94midx + sha3(mem[0])m]) = 0
              mem[0] = [94midx + sha3(mem[0])
              [94ms = sha3([94ms + sha3(mem[0]))
              mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
                  uint256(mstor[[94ms + sha3(mem[0])m]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
              uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
              uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
              [94ms = [94ms + 3
              mcontinue 
      require mstor2m.length < mstor2m.length
      mstor4057m[mstor2m.lengthm] = mmultiAccessRequired
      mstor4057m[mstor2m.lengthm] = sha3(call.data[0 len calldata.size])
      mstor1m[call.data[0 len calldata.size]m] = mstor2m.length
      if uint256(mstor2m[mstor2m.lengthm]m.field_256) > 1:
          log Confirmation(
                address owner=0,
                bytes32 operation=caller,
                bool completed=sha3(call.data[0 len calldata.size]))
          uint256(mstor2m[mstor2m.lengthm]m.field_256)--
          if uint256(mstor4m[callerm]m.field_0) >= uint256(mstor2m[mstor2m.lengthm]m.field_0):
              uint256(mstor2m[mstor2m.lengthm]m.field_0) = uint256(mstor4m[callerm]m.field_0) + 1
              if not uint256(mstor2m[mstor2m.lengthm]m.field_0) <= uint256(mstor4m[callerm]m.field_0) + 1:
                  [94midx = uint256(mstor4m[callerm]m.field_0) + 32 / 32
                  mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
                      uint256(mstor2m[(3 * mstor2m.length) + [94midxm]m.field_0) = 0
                      [94midx = [94midx + 1
                      mcontinue 
              require uint256(mstor4m[callerm]m.field_0) < uint256(mstor2m[mstor2m.lengthm]m.field_0)
          uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0) = 256^mstor4m[callerm]m.field_0 % 32 or !(255 * 256^mstor4m[callerm]m.field_0 % 32) and uint256(mstor[Mask(251, 0, mstor4m[callerm]m.field_5) + ('array', ('mul', 3, ('stor', ('length', ('name', 'stor2', 2)))), ('name', 'stor2', 2))m]m.field_0)
          return 0
  log Confirmation(
        address owner=1,
        bytes32 operation=caller,
        bool completed=sha3(call.data[0 len calldata.size]))
  if mstor1m[call.data[0 len calldata.size]m] < mstor2m.length - 1:
      require mstor2m.length - 1 < mstor2m.length
      require mstor1m[call.data[0 len calldata.size]m] < mstor2m.length
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      if not uint256(mstor2m[mstor2m.lengthm]m.field_0):
          [94midx = 0
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32 > [94midxm:
              uint256(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94msm]m.field_0) = uint256(mstor[[94midx + sha3((3 * mstor2m.length) + ('name', 'stor2', 2) - 3)m]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = uint256(mstor2m[mstor2m.lengthm]m.field_0) + 31 / 32
          mwhile uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_0) + 31 / 32 > [94midxm:
              uint8(mstor2m[(3 * mstor1m[call.data[0 len calldata.size]m]) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_256) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      uint256(mstor2m[mstor1m[call.data[0 len calldata.size]m]m]m.field_512) = uint256(mstor2m[mstor2m.lengthm]m.field_0)
      mstor1m[uint256(mstor2m[mstor2m.lengthm]m.field_0)m] = mstor1m[call.data[0 len calldata.size]m]
  mstor2m.length--
  if not mstor2m.length <= mstor2m.length - 1:
      mem[0] = 2
      [94midx = (3 * mstor2m.length) - 3
      mwhile sha3(2) + (3 * mstor2m.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          mem[0] = [94midx + sha3(mem[0])
          [94ms = sha3([94ms + sha3(mem[0]))
          mwhile sha3([94ms + sha3(mem[0])) + (uint256(mstor[[94ms + sha3(mem[0])m]) + 31 / 32) > [94ms + sha3(mem[0])m:
              uint256(mstor[[94ms + sha3(mem[0])m]) = 0
              [94ms = [94ms + 1
              mcontinue 
          uint256(mstor[[94ms + sha3(mem[0]) + 1m]) = 0
          uint256(mstor[[94ms + sha3(mem[0]) + 2m]) = 0
          [94ms = [94ms + 3
          mcontinue 
  mstor1m[call.data[0 len calldata.size]m] = 0
  if calldata.size <= 0:
      return 0
  call addr(mmultiAccessRecipientAddress) with:
     funct call.data[0 len 4]
       gas gas_remaining - 25050 wei
      args call.data[4 len calldata.size - 4]
  return bool(ext_call.success)


