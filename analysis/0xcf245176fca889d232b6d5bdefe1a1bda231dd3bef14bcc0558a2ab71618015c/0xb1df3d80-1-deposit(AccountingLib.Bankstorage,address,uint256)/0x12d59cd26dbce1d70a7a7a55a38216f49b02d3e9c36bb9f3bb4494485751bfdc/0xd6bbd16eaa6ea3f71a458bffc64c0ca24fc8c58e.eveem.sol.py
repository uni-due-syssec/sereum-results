# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD6BBD16eAa6ea3f71A458BfFC64C0ca24fC8c58E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x317c152d': 'unknown317c152d(?)', '0x5748147e': 'unknown5748147e(?)'} 

# storage definitions
def storage:
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
# hash = 0x068e3ef1
# getter = None
# const = None
# payable = True
def unknown068e3ef1(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  require uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) + m_param3 >= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) += m_param3


# hash = 0x079ed96f
# getter = None
# const = None
# payable = True
def unknown079ed96f(uint256 m_param1, addr m_param2) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if callcode.return_data[0] != 0:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if callcode.return_data[0] != 0:
          if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
              mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
              [94midx = 320
              [94ms = 0
              mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
          [94midx = 0
          mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
              require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
              if mem[(32 * [94midx) + 332 len 20] != m_param2:
                  [94midx = [94midx + 1
                  mcontinue 
              return 1
  else:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if callcode.return_data[0]:
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if callcode.return_data[0] != 0:
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = 320
                  [94ms = 0
                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  return 1
  return 0


# hash = 0x332a06ac
# getter = None
# const = None
# payable = True
def unknown332a06ac(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3


# hash = 0x3458e13e
# getter = None
# const = None
# payable = True
def unknown3458e13e(uint256 m_param1, uint256 m_param2, addr m_param3) payable: 
  [94midx = 0
  mwhile [94midx < mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m]m:
      mem[0] = sha3(m_param2, m_param1 + 8) + 3
      if addr(mstor[m_param1 + 8m]m[m_param2m]m[[94midx + 3m]) != m_param3:
          [94midx = [94midx + 1
          mcontinue 
      require mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] - 1 < mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m]
      require [94midx < mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m]
      addr(mstor[m_param1 + 8m]m[m_param2m]m[[94midx + 3m]) = addr(mstor[mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))) - 1m])
      mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m]--
      if not mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] <= mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] - 1:
          [94midx = sha3(sha3(m_param2, m_param1 + 8) + 3) + mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] - 1
          mwhile sha3(sha3(m_param2, m_param1 + 8) + 3) + mstor3m[('map', ('param', '_param2'), ('add', 8, ('param', '_param1')))m] > [94midxm:
              uint256(mstor[[94midxm]) = 0
              [94midx = [94midx + 1
              mcontinue 
      return 1
  return 0


# hash = 0x38f4c9eb
# getter = None
# const = None
# payable = True
def unknown38f4c9eb(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, m_param2
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 6, '>=', m_param3
      require callcode.return_code
      if not callcode.return_data[0]:
          return 0
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
          [94midx = 384
          [94ms = 0
          mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
      if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
          return 0
      if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
          if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
              return 0
  else:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
          if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 6, '>=', m_param3
              require callcode.return_code
              if not callcode.return_data[0]:
                  return 0
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              require callcode.return_code
              if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                  else:
                      if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] >= m_param3:
                          mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                      else:
                          if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                          else:
                              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                  return memory
                    from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                     [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
              [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
              [94ms = 0
              mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
              if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                  return 0
              if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                  if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                      return 0
          else:
              if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                  if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 6, '>=', m_param3
                      require callcode.return_code
                      if not callcode.return_data[0]:
                          return 0
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                          else:
                              if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] >= m_param3:
                                  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                              else:
                                  if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                                      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                                  else:
                                      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                          return memory
                            from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                             [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                      [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                      [94ms = 0
                      mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          mcontinue 
                      if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                          return 0
                      if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                          if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                              return 0
      else:
          [94midx = 384
          [94ms = 0
          mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
          if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 6, '>=', m_param3
              require callcode.return_code
              if not callcode.return_data[0]:
                  return 0
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              require callcode.return_code
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                  [94ms = 0
                  mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
              if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                  return 0
              if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                  if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                      return 0
          else:
              if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                  if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 6, '>=', m_param3
                      require callcode.return_code
                      if not callcode.return_data[0]:
                          return 0
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                          [94ms = 0
                          mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              mcontinue 
                      if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) > m_param2:
                          return 0
                      if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] < m_param3:
                          if mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m] != 0:
                              return 0
  return uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])


# hash = 0x54e37911
# getter = None
# const = None
# payable = True
def unknown54e37911(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) < m_param3:
      return 0
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if not callcode.return_data[0]:
          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
               gas gas_remaining - 50 wei
              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
          require callcode.return_code
          if callcode.return_data[0] != 0:
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                      mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                      [94midx = 384
                      [94ms = 0
                      mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          mcontinue 
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 396 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      else:
                          return 0
          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
               gas gas_remaining - 50 wei
              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
          require callcode.return_code
          if 0 == callcode.return_data[0]:
              return 1
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if not callcode.return_data[0]:
              return 1
          if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
              return 1
          else:
              return 0
  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
       gas gas_remaining - 50 wei
      args callcode.return_data[0]
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if callcode.return_data[0] != 0:
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if callcode.return_data[0] != 0:
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = 384
                  [94ms = 0
                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 396 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  else:
                      return 0
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          return 1
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not callcode.return_data[0]:
          return 1
      if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
          return 1
      else:
          return 0
  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
      mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
      [94midx = 320
      [94ms = 0
      mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
          if mem[(32 * [94midx) + 332 len 20] != m_param2:
              [94midx = [94midx + 1
              mcontinue 
          else:
              return 0
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if callcode.return_data[0] != 0:
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if callcode.return_data[0] != 0:
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                  [94ms = 0
                  mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  else:
                      return 0
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          return 1
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not callcode.return_data[0]:
          return 1
      if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
          return 1
      return 0
  [94midx = 0
  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
      if mem[(32 * [94midx) + 332 len 20] != m_param2:
          [94midx = [94midx + 1
          mcontinue 
      else:
          return 0
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          return 1
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not callcode.return_data[0]:
          return 1
      if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
          return 1
      else:
          return 0
  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
       gas gas_remaining - 50 wei
      args callcode.return_data[0]
  require callcode.return_code
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 320] = 0
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352] = 0
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          return 1
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not callcode.return_data[0]:
          return 1
      if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
          return 1
      else:
          return 0
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 384] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 416] = uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m])
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 448] = mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512] = mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
      [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
      [94ms = 0
      mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
          if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
              [94midx = [94midx + 1
              mcontinue 
          else:
              return 0
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          return 1
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if not callcode.return_data[0]:
          return 1
      if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
          return 1
      return 0
  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 480] = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512
  [94midx = 0
  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
      if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
          [94midx = [94midx + 1
          mcontinue 
      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
      return memory
        from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
         [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 548] = m_param1 + 4
  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 580] = 0x3e00000000000000000000000000000000000000000000000000000000000000
  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 612] = block.number
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 548 len (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 96]
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
  else:
      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 548] = callcode.return_data[0]
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 548 len (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32]
      require callcode.return_code
      if not callcode.return_data[0]:
          mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
      else:
          if block.number + mstor2m[m_param1m] < uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]):
              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
          else:
              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
  return memory
    from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
     [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32


# hash = 0x67f146ce
# getter = None
# const = None
# payable = True
def unknown67f146ce(uint256 m_param1, addr m_param2) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if callcode.return_data[0] != 0:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if 0 == callcode.return_data[0]:
          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
               gas gas_remaining - 50 wei
              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
          require callcode.return_code
          if callcode.return_data[0] != 0:
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                      mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                      [94midx = 384
                      [94ms = 0
                      mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          mcontinue 
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 396 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      return 1
      else:
          if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
              mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
              [94midx = 320
              [94ms = 0
              mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  return 1
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                       gas gas_remaining - 50 wei
                      args callcode.return_data[0]
                  require callcode.return_code
                  if callcode.return_data[0] != 0:
                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                          [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                          [94ms = 0
                          mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              mcontinue 
                      [94midx = 0
                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                              [94midx = [94midx + 1
                              mcontinue 
                          return 1
          else:
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  return 1
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                       gas gas_remaining - 50 wei
                      args callcode.return_data[0]
                  require callcode.return_code
                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 320] = 0
                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352] = 0
                  if callcode.return_data[0] != 0:
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 384] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 416] = uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m])
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 448] = mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512] = mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 480] = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512
                          [94midx = 0
                          mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                              require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                              if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                  [94midx = [94midx + 1
                                  mcontinue 
                              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
                              return memory
                                from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                 [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                          mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                          return memory
                            from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                             [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                      [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                      [94ms = 0
                      mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          mcontinue 
                      [94midx = 0
                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                              [94midx = [94midx + 1
                              mcontinue 
                          return 1
  else:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if not callcode.return_data[0]:
          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
               gas gas_remaining - 50 wei
              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
          require callcode.return_code
          if callcode.return_data[0] != 0:
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                      mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                      [94midx = 384
                      [94ms = 0
                      mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                          mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          mcontinue 
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 396 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      return 1
      else:
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if 0 == callcode.return_data[0]:
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              require callcode.return_code
              if callcode.return_data[0] != 0:
                  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                       gas gas_remaining - 50 wei
                      args callcode.return_data[0]
                  require callcode.return_code
                  if callcode.return_data[0] != 0:
                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                          [94midx = 384
                          [94ms = 0
                          mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              mcontinue 
                      [94midx = 0
                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          if mem[(32 * [94midx) + 396 len 20] != m_param2:
                              [94midx = [94midx + 1
                              mcontinue 
                          return 1
          else:
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = 320
                  [94ms = 0
                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 332 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      return 1
                  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                       gas gas_remaining - 50 wei
                      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                  require callcode.return_code
                  if callcode.return_data[0] != 0:
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      if callcode.return_data[0] != 0:
                          if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                              [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                              [94ms = 0
                              mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  mcontinue 
                          [94midx = 0
                          mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                              require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                              if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                  [94midx = [94midx + 1
                                  mcontinue 
                              return 1
              else:
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 332 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      return 1
                  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                       gas gas_remaining - 50 wei
                      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                  require callcode.return_code
                  if callcode.return_data[0] != 0:
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 320] = 0
                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352] = 0
                      if callcode.return_data[0] != 0:
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 384] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 416] = uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m])
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 448] = mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512] = mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 480] = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
                                  return memory
                                    from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                     [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                              mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                              return memory
                                from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                 [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                          [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                          [94ms = 0
                          mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              mcontinue 
                          [94midx = 0
                          mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                              require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                              if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                  [94midx = [94midx + 1
                                  mcontinue 
                              return 1
  return 0


# hash = 0x6a704d7b
# getter = None
# const = None
# payable = True
def unknown6a704d7b(addr m_param1, uint256 m_param2) payable: 
  log 0x4327115b: _param1, _param2


# hash = 0x83973eb3
# getter = None
# const = None
# payable = True
def unknown83973eb3(uint256 m_param1, addr m_param2) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if callcode.return_data[0] != 0:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if callcode.return_data[0] != 0:
          if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
              mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
              [94midx = 320
              [94ms = 0
              mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
          [94midx = 0
          mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
              require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
              if mem[(32 * [94midx) + 332 len 20] != m_param2:
                  [94midx = [94midx + 1
                  mcontinue 
              return 1
          return 0
      else:
          return 0
  else:
      return 0


# hash = 0x8f00e61a
# getter = None
# const = None
# payable = True
def unknown8f00e61a(uint256 m_param1) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      return 0
  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
       gas gas_remaining - 50 wei
      args callcode.return_data[0]
  require callcode.return_code
  return callcode.return_data[0]


# hash = 0x968f7720
# getter = None
# const = None
# payable = True
def unknown968f7720(uint256 m_param1, addr m_param2) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if callcode.return_data[0] != 0:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      require callcode.return_code
      if callcode.return_data[0] != 0:
          if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                       gas gas_remaining - 50 wei
                      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                  require callcode.return_code
                  if 0 == callcode.return_data[0]:
                      return 1
                  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                       gas gas_remaining - 50 wei
                      args callcode.return_data[0]
                  require callcode.return_code
                  if 0 == callcode.return_data[0]:
                      return 1
                  if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) - mstor2m[m_param1m] > block.number:
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      require callcode.return_code
                      if callcode.return_data[0] != 0:
                          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                               gas gas_remaining - 50 wei
                              args callcode.return_data[0]
                          require callcode.return_code
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 320] = 0
                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352] = 0
                          if callcode.return_data[0] != 0:
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 384] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 416] = uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m])
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 448] = mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512] = mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                              if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 480] = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512
                                  [94midx = 0
                                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                      if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
                                      return memory
                                        from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                         [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                                  mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                                  return memory
                                    from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                     [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                              [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                              [94ms = sha3(sha3(callcode.return_data[0], m_param1 + 8) + 3)
                              mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                  mem[[94midx + 32] = addr(mstor1m[[94msm])
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  mcontinue 
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  return 1
                              return 0
                          else:
                              return 0
                      else:
                          return 0
                  else:
                      return 0
          else:
              mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
              [94midx = 320
              [94ms = 0
              mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                  mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                       gas gas_remaining - 50 wei
                      args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                  require callcode.return_code
                  if 0 == callcode.return_data[0]:
                      return 1
                  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                       gas gas_remaining - 50 wei
                      args callcode.return_data[0]
                  require callcode.return_code
                  if 0 == callcode.return_data[0]:
                      return 1
                  if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) - mstor2m[m_param1m] > block.number:
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      require callcode.return_code
                      if callcode.return_data[0] != 0:
                          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                               gas gas_remaining - 50 wei
                              args callcode.return_data[0]
                          require callcode.return_code
                          if callcode.return_data[0] != 0:
                              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                  [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                  [94ms = sha3(sha3(callcode.return_data[0], m_param1 + 8) + 3)
                                  mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                      mem[[94midx + 32] = addr(mstor1m[[94msm])
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      mcontinue 
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  return 1
                              return 0
                          else:
                              return 0
                      else:
                          return 0
                  else:
                      return 0
  else:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if callcode.return_data[0]:
          [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
               gas gas_remaining - 50 wei
              args callcode.return_data[0]
          require callcode.return_code
          if callcode.return_data[0] != 0:
              if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 332 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      require callcode.return_code
                      if 0 == callcode.return_data[0]:
                          return 1
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      if 0 == callcode.return_data[0]:
                          return 1
                      if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) - mstor2m[m_param1m] > block.number:
                          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                               gas gas_remaining - 50 wei
                              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                          require callcode.return_code
                          if callcode.return_data[0] != 0:
                              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                                   gas gas_remaining - 50 wei
                                  args callcode.return_data[0]
                              require callcode.return_code
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 320] = 0
                              mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352] = 0
                              if callcode.return_data[0] != 0:
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 384] = uint256(mstor[m_param1 + 8m]m[callcode.return_data[0]m])
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 416] = uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m])
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 448] = mstor2m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512] = mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if not mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 480] = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512
                                      [94midx = 0
                                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                          if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                              [94midx = [94midx + 1
                                              mcontinue 
                                          mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 1
                                          return memory
                                            from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                             [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                                      mem[(64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = 0
                                      return memory
                                        from (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                         [93mlen (127 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 32
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                  [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                  [94ms = sha3(sha3(callcode.return_data[0], m_param1 + 8) + 3)
                                  mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                      mem[[94midx + 32] = addr(mstor1m[[94msm])
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      mcontinue 
                                  [94midx = 0
                                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                      if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                      return 1
                                  return 0
                              else:
                                  return 0
                          else:
                              return 0
                      else:
                          return 0
              else:
                  mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = 320
                  [94ms = 0
                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
                  [94midx = 0
                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                      if mem[(32 * [94midx) + 332 len 20] != m_param2:
                          [94midx = [94midx + 1
                          mcontinue 
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      require callcode.return_code
                      if 0 == callcode.return_data[0]:
                          return 1
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      require callcode.return_code
                      if 0 == callcode.return_data[0]:
                          return 1
                      if uint256(mstor1m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) - mstor2m[m_param1m] > block.number:
                          [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                               gas gas_remaining - 50 wei
                              args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                          require callcode.return_code
                          if callcode.return_data[0] != 0:
                              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                                   gas gas_remaining - 50 wei
                                  args callcode.return_data[0]
                              require callcode.return_code
                              if callcode.return_data[0] != 0:
                                  if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                      mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                      [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                      [94ms = sha3(sha3(callcode.return_data[0], m_param1 + 8) + 3)
                                      mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                          mem[[94midx + 32] = addr(mstor1m[[94msm])
                                          [94midx = [94midx + 32
                                          [94ms = [94ms + 1
                                          mcontinue 
                                  [94midx = 0
                                  mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                      require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                      if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                          [94midx = [94midx + 1
                                          mcontinue 
                                      return 1
                                  return 0
                              else:
                                  return 0
                          else:
                              return 0
                      else:
                          return 0
  return 0


# hash = 0xa163a325
# getter = None
# const = None
# payable = True
def unknowna163a325(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  if m_param3 != 0:
      if mstor3m[('map', ('param', '_param3'), ('add', 8, ('param', '_param1')))m]:
          mem[320] = addr(mstor[m_param1 + 8m]m[m_param3m]m[3m])
          [94midx = 320
          [94ms = 0
          mwhile (32 * mstor3m[('map', ('param', '_param3'), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('param', '_param3'), ('add', 8, ('param', '_param1')))) + 1m])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
      [94midx = 0
      mwhile [94midx < mstor3m[('map', ('param', '_param3'), ('add', 8, ('param', '_param1')))m]m:
          require [94midx < mstor3m[('map', ('param', '_param3'), ('add', 8, ('param', '_param1')))m]
          if mem[(32 * [94midx) + 332 len 20] != m_param2:
              [94midx = [94midx + 1
              mcontinue 
          return 1
      return 0
  else:
      return 0


# hash = 0xb6cbfdb2
# getter = None
# const = None
# payable = True
def unknownb6cbfdb2(uint256 m_param1) payable: 
  mem[96] = 0
  mem[32] = m_param1 + 8
  mstor3m[m_param1m]++
  mem[0] = mstor3m[m_param1m] + 1
  uint256(mstor[m_param1 + 8m]m[mstor3m[m_param1m] + 1m]) = mstor3m[m_param1m] + 1
  uint256(mstor1m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) = block.number + mstor2m[m_param1m] + uint256(mstor[m_param1m])
  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.uintToBytes(uint256 i) with:
       gas gas_remaining - 50 wei
      args (mstor3m[m_param1m] + 1)
  require callcode.return_code
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.insert(GroveLib.Index storage index, bytes32 id, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 4, callcode.return_data[0], uint256(mstor1m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m])
  if uint256(mstor[m_param1 + 8m]m[mstor3m[m_param1m]m]) != 0:
      mstor2m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m] = uint256(mstor1m[m_param1m]) + uint256(mstor[m_param1m]) + block.number + mstor2m[m_param1m]
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.uintToBytes(uint256 i) with:
           gas gas_remaining - 50 wei
          args uint256(mstor[m_param1 + 8m]m[mstor3m[m_param1m]m])
      require callcode.return_code
      mem[132] = m_param1 + 6
      mem[164] = callcode.return_data[0]
      mem[196] = mstor2m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.insert(GroveLib.Index storage index, bytes32 id, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 6, callcode.return_data[0], mstor2m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]
      mem[64] = (32 * mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]) + 160
      mem[128] = mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]
      if not mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]:
          [94ms = 0
          [94midx = 0
          mwhile [94midx < mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]m:
              [94m_43 = mem[128]
              mem[mem[64]] = block.hash(block.number)
              mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]++
              if not mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] > mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + 1:
                  require sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
                  [94m_50 = mem[(32 * sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160]
                  require mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] - 1 < mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]) = [94m_50 or Mask(96, 160, uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]))
              else:
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  [94ms = mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + sha3(sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3) + 1
                  mwhile sha3(sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3) + mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  require sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
                  [94m_69 = mem[(32 * sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160]
                  require mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] - 1 < mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]) = [94m_69 or Mask(96, 160, uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]))
              require mem[128] - 1 < mem[128]
              require sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
              mem[(32 * sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160] = mem[(32 * mem[128] - 1) + 172 len 20]
              [94ms = sha3(block.hash(block.number)) % [94m_43 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[0] = sha3(mstor3m[m_param1m], m_param1 + 8) + 3
          mem[160] = addr(mstor[m_param1 + 8m]m[mstor3m[m_param1m]m]m[3m])
          [94midx = 160
          [94ms = 0
          mwhile (32 * mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]) + 128 > [94midxm:
              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))) + 1m])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
          [94ms = 0
          [94midx = 0
          mwhile [94midx < mstor3m[('map', ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3))), ('add', 8, ('param', '_param1')))m]m:
              [94m_94 = mem[128]
              mem[mem[64]] = block.hash(block.number)
              mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]++
              if not mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] > mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + 1:
                  require sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
                  [94m_101 = mem[(32 * sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160]
                  require mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] - 1 < mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]) = [94m_101 or Mask(96, 160, uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]))
              else:
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  [94ms = mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + sha3(sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3) + 1
                  mwhile sha3(sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3) + mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  require sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
                  [94m_115 = mem[(32 * sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160]
                  require mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] - 1 < mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
                  mem[0] = sha3(mstor3m[m_param1m] + 1, m_param1 + 8) + 3
                  uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]) = [94m_115 or Mask(96, 160, uint256(mstor[mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] + ('array', 3, ('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))) - 1m]))
              require mem[128] - 1 < mem[128]
              require sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m] < mem[128]
              mem[(32 * sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]) + 160] = mem[(32 * mem[128] - 1) + 172 len 20]
              [94ms = sha3(block.hash(block.number)) % [94m_94 - mstor3m[('map', ('add', 1, ('stor', ('array', ('param', '_param1'), ('name', 'stor3', 3)))), ('add', 8, ('param', '_param1')))m]
              [94midx = [94midx + 1
              mcontinue 
  return uint256(mstor[m_param1 + 8m]m[mstor3m[m_param1m] + 1m])


# hash = 0xc75e8f88
# getter = None
# const = None
# payable = True
def unknownc75e8f88(uint256 m_param1) payable: 
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if 0 == callcode.return_data[0]:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      require callcode.return_code
      if not callcode.return_data[0]:
          return 0
  [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
       gas gas_remaining - 50 wei
      args callcode.return_data[0]
  require callcode.return_code
  return callcode.return_data[0]


# hash = 0xdd8abb6c
# getter = None
# const = None
# payable = True
def unknowndd8abb6c(uint256 m_param1, addr m_param2, uint256 m_param3, uint256 m_param4) payable: 
  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
  [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
       gas gas_remaining - 50 wei
      args m_param1 + 6, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
  require callcode.return_code
  if callcode.return_data[0] != 0:
      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
           gas gas_remaining - 50 wei
          args callcode.return_data[0]
      if callcode.return_code:
          if 0 == callcode.return_data[0]:
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              if callcode.return_code:
                  if 0 == callcode.return_data[0]:
                      if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                          call m_param2 with:
                             value m_param3 wei
                               gas 0 wei
                          if ext_call.success:
                              stop
                          call m_param2 with:
                             value m_param3 wei
                               gas gas_remaining wei
                  else:
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      if callcode.return_code:
                          if callcode.return_data[0] != 0:
                              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                  mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                  [94midx = 384
                                  [94ms = 0
                                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      mcontinue 
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + 396 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                                      stop
                                  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas 0 wei
                                  if ext_call.success:
                                      stop
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas gas_remaining wei
                                  revert 
                          if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                              uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                              call m_param2 with:
                                 value m_param3 wei
                                   gas 0 wei
                              if ext_call.success:
                                  stop
                              call m_param2 with:
                                 value m_param3 wei
                                   gas gas_remaining wei
          else:
              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                  mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                  [94midx = 320
                  [94ms = 0
                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
              [94midx = 0
              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                  if mem[(32 * [94midx) + 332 len 20] != m_param2:
                      [94midx = [94midx + 1
                      mcontinue 
                  if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                      stop
                  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                  call m_param2 with:
                     value m_param3 wei
                       gas 0 wei
                  if ext_call.success:
                      stop
                  call m_param2 with:
                     value m_param3 wei
                       gas gas_remaining wei
                  revert 
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              if callcode.return_code:
                  if 0 == callcode.return_data[0]:
                      if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                          call m_param2 with:
                             value m_param3 wei
                               gas 0 wei
                          if ext_call.success:
                              stop
                          call m_param2 with:
                             value m_param3 wei
                               gas gas_remaining wei
                  else:
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      if callcode.return_code:
                          if callcode.return_data[0] != 0:
                              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                  mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                  [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                  [94ms = 0
                                  mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      mcontinue 
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                                      stop
                                  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas 0 wei
                                  if ext_call.success:
                                      stop
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas gas_remaining wei
                                  revert 
                          if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                              uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                              call m_param2 with:
                                 value m_param3 wei
                                   gas 0 wei
                              if ext_call.success:
                                  stop
                              call m_param2 with:
                                 value m_param3 wei
                                   gas gas_remaining wei
  else:
      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
           gas gas_remaining - 50 wei
          args m_param1 + 4, 0x3c3d000000000000000000000000000000000000000000000000000000000000, block.number
      if callcode.return_code:
          if not callcode.return_data[0]:
              [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                   gas gas_remaining - 50 wei
                  args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
              if callcode.return_code:
                  if 0 == callcode.return_data[0]:
                      if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                          call m_param2 with:
                             value m_param3 wei
                               gas 0 wei
                          if ext_call.success:
                              stop
                          call m_param2 with:
                             value m_param3 wei
                               gas gas_remaining wei
                  else:
                      [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                           gas gas_remaining - 50 wei
                          args callcode.return_data[0]
                      if callcode.return_code:
                          if callcode.return_data[0] != 0:
                              if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                  mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                  [94midx = 384
                                  [94ms = 0
                                  mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                                      mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      mcontinue 
                              [94midx = 0
                              mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                  require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                  if mem[(32 * [94midx) + 396 len 20] != m_param2:
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                                      stop
                                  require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas 0 wei
                                  if ext_call.success:
                                      stop
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas gas_remaining wei
                                  revert 
                          if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                              uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                              call m_param2 with:
                                 value m_param3 wei
                                   gas 0 wei
                              if ext_call.success:
                                  stop
                              call m_param2 with:
                                 value m_param3 wei
                                   gas gas_remaining wei
          else:
              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                   gas gas_remaining - 50 wei
                  args callcode.return_data[0]
              if callcode.return_code:
                  if 0 == callcode.return_data[0]:
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      if callcode.return_code:
                          if 0 == callcode.return_data[0]:
                              if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas 0 wei
                                  if ext_call.success:
                                      stop
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas gas_remaining wei
                          else:
                              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                                   gas gas_remaining - 50 wei
                                  args callcode.return_data[0]
                              if callcode.return_code:
                                  if callcode.return_data[0] != 0:
                                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                          mem[384] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                          [94midx = 384
                                          [94ms = 0
                                          mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 352 > [94midxm:
                                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      [94midx = 0
                                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                          if mem[(32 * [94midx) + 396 len 20] != m_param2:
                                              [94midx = [94midx + 1
                                              mcontinue 
                                          if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                                              stop
                                          require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                          call m_param2 with:
                                             value m_param3 wei
                                               gas 0 wei
                                          if ext_call.success:
                                              stop
                                          call m_param2 with:
                                             value m_param3 wei
                                               gas gas_remaining wei
                                          revert 
                                  if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                                      uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                      call m_param2 with:
                                         value m_param3 wei
                                           gas 0 wei
                                      if ext_call.success:
                                          stop
                                      call m_param2 with:
                                         value m_param3 wei
                                           gas gas_remaining wei
                  else:
                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                          mem[320] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                          [94midx = 320
                          [94ms = 0
                          mwhile (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 288 > [94midxm:
                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              mcontinue 
                      [94midx = 0
                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                          if mem[(32 * [94midx) + 332 len 20] != m_param2:
                              [94midx = [94midx + 1
                              mcontinue 
                          if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                              stop
                          require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                          call m_param2 with:
                             value m_param3 wei
                               gas 0 wei
                          if ext_call.success:
                              stop
                          call m_param2 with:
                             value m_param3 wei
                               gas gas_remaining wei
                          revert 
                      [93mcodecall 0x920c890a90db8fba7604864b0cf38ee667331323.query(GroveLib.Index storage index, bytes2 operator, int256 value) with:
                           gas gas_remaining - 50 wei
                          args m_param1 + 4, 0x3e00000000000000000000000000000000000000000000000000000000000000, block.number
                      if callcode.return_code:
                          if 0 == callcode.return_data[0]:
                              if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                                  uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas 0 wei
                                  if ext_call.success:
                                      stop
                                  call m_param2 with:
                                     value m_param3 wei
                                       gas gas_remaining wei
                          else:
                              [93mcodecall 0x443b53559d337277373171280ec57029718203fb.bytesToUInt(bytes32 v) with:
                                   gas gas_remaining - 50 wei
                                  args callcode.return_data[0]
                              if callcode.return_code:
                                  if callcode.return_data[0] != 0:
                                      if mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]:
                                          mem[(32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544] = addr(mstor[m_param1 + 8m]m[callcode.return_data[0]m]m[3m])
                                          [94midx = (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 544
                                          [94ms = 0
                                          mwhile (64 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 512 > [94midxm:
                                              mem[[94midx + 32] = addr(mstor[[94ms + ('array', 3, ('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))) + 1m])
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              mcontinue 
                                      [94midx = 0
                                      mwhile [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]m:
                                          require [94midx < mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]
                                          if mem[(32 * [94midx) + (32 * mstor3m[('map', ('callcode.return_data', 0, 32), ('add', 8, ('param', '_param1')))m]) + 556 len 20] != m_param2:
                                              [94midx = [94midx + 1
                                              mcontinue 
                                          if uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) - m_param3 < m_param4:
                                              stop
                                          require m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m])
                                          uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                          call m_param2 with:
                                             value m_param3 wei
                                               gas 0 wei
                                          if ext_call.success:
                                              stop
                                          call m_param2 with:
                                             value m_param3 wei
                                               gas gas_remaining wei
                                          revert 
                                  if m_param3 <= uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]):
                                      uint256(mstor[m_param1 + 9m]m[addr(m_param2)m]) -= m_param3
                                      call m_param2 with:
                                         value m_param3 wei
                                           gas 0 wei
                                      if ext_call.success:
                                          stop
                                      call m_param2 with:
                                         value m_param3 wei
                                           gas gas_remaining wei
  revert 


# hash = 0xf1173928
# getter = None
# const = None
# payable = True
def unknownf1173928(addr m_param1, uint256 m_param2) payable: 
  log 0xd6940c8c: _param1, _param2


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


