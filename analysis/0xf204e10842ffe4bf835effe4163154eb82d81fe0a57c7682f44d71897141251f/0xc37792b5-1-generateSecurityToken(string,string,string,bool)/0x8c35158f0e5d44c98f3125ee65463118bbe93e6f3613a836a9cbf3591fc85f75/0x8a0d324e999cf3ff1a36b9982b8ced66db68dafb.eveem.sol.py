# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8A0D324E999CF3fF1a36b9982B8cEd66Db68daFb 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x1a83bff0': 'unknown1a83bff0(?)', '0x4ac24a9a': 'unknown4ac24a9a(?)', '0xa0632461': 'unknowna0632461(?)', '0xac90b422': 'unknownac90b422(?)', '0xad64ae4b': 'registerModule(address _moduleFactory)', '0xea393b75': 'unknownea393b75(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknown26839e53
    # storage address 1
    unknown69ba0fe9
    # storage address 2
    unknownbaed8bb1
    # storage address 3
    unknownc6cb7ab8
    # storage address 4
    stor4
    # storage address 6
    unknownb3447ac9
    # storage address 9
    stor9
# hash = 0x0818a6f0
# getter = None
# const = None
# payable = False
def unknown0818a6f0(addr _param1): # not payable
  mem[128] = 0x72657075746174696f6e000000000000000000000000000000000000000000
  mem[192 len 0] = None
  mem[202] = addr(_param1)
  mem[160] = 30
  mem[222 len 0] = None
  mem[222] = mem[252 len 2]
  mem[0] = sha3(mem[222 len 30])
  mem[32] = 9
  [94m_59 = sha3(sha3(mem[222 len 30]), 9)
  mem[64] = (32 * uint256(stor9[mem[222 len 30]])) + 254
  mem[222] = uint256(stor9[mem[222 len 30]])
  if not uint256(stor[[94m_59]):
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[222]
      [94m_64 = mem[222]
      mem[mem[64] + 64 len floor32(mem[222])] = mem[254 len floor32(mem[222])]
      return 32, mem[mem[64] + 32 len (32 * [94m_64) + 32]
  mem[0] = [94m_59
  mem[254] = addr(stor[sha3([94m_59)])
  [94midx = 254
  [94ms = 0
  while (32 * uint256(stor[[94m_59])) + 222 > [94midx:
      mem[[94midx + 32] = addr(stor[[94ms + sha3([94m_59) + 1])
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[222]
  [94m_76 = mem[222]
  mem[mem[64] + 64 len floor32(mem[222])] = mem[254 len floor32(mem[222])]
  return 32, mem[mem[64] + 32 len (32 * [94m_76) + 32]


# hash = 0x1d8acf1b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown1d8acf1b(uint256 _param1): # not payable
  return bool(stor4[_param1])


# hash = 0x26839e53
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def unknown26839e53(uint256 _param1): # not payable
  return unknown26839e53[_param1]


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  mem[198 len 0] = None
  mem[198] = mem[204 len 14], 0, mem[224 len 6]
  if not stor4[mem[198 len 6]]:
      revert with 0, 'Should not be paused'
  mem[299 len 0] = None
  mem[299] = mem[304 len 17], 'owner' % 1099511627776, mem[326 len 5]
  if unknownbaed8bb1[mem[299 len 5]] != caller:
      revert with 0, 'sender must be owner'
  mem[401 len 0] = None
  mem[401] = mem[407 len 14], 0, mem[427 len 6]
  stor4[mem[401 len 6]] = 0
  log Unpause(uint256 timestamp=block.timestamp)


# hash = 0x485cc955
# getter = None
# const = None
# payable = True
def initialize(address _addrUser, address _addrRegistry) payable: 
  mem[203 len 0] = None
  mem[203] = Mask(80, 0, 'initialised'), mem[224 len 11]
  if stor4[mem[203 len 11]]:
      revert with 0, 'already initialized'
  if not _addrRegistry:
      revert with 0, '0x address is invalid'
  if not _addrUser:
      revert with 0, '0x address is invalid'
  mem[318 len 0] = None
  mem[318] = mem[337 len 13]
  unknownbaed8bb1[mem[318 len 19]] = _addrUser
  mem[419 len 0] = None
  mem[419] = mem[424 len 17], 'owner' % 1099511627776, mem[446 len 5]
  unknownbaed8bb1[mem[419 len 5]] = _addrRegistry
  mem[521 len 0] = None
  mem[521] = mem[527 len 14], 0, mem[547 len 6]
  stor4[mem[521 len 6]] = 0
  mem[628 len 0] = None
  mem[628] = Mask(80, 0, 'initialised'), mem[649 len 11]
  stor4[mem[628 len 11]] = 1


# hash = 0x69ba0fe9
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 1]]]]], ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown69ba0fe9(uint256 _param1): # not payable
  return unknown69ba0fe9[_param1][0 len unknown69ba0fe9[_param1].length]


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  mem[198 len 0] = None
  mem[198] = mem[204 len 14], 0, mem[224 len 6]
  if stor4[mem[198 len 6]]:
      revert with 0, 'Already paused'
  mem[299 len 0] = None
  mem[299] = mem[304 len 17], 'owner' % 1099511627776, mem[326 len 5]
  if unknownbaed8bb1[mem[299 len 5]] != caller:
      revert with 0, 'sender must be owner'
  mem[401 len 0] = None
  mem[401] = mem[407 len 14], 0, mem[427 len 6]
  stor4[mem[401 len 6]] = 1
  log Pause(uint256 timestammp=block.timestamp)


# hash = 0x8905fd4f
# getter = None
# const = None
# payable = False
def reclaimERC20(address _tokenContract): # not payable
  mem[197 len 0] = None
  mem[197] = mem[202 len 17], 'owner' % 1099511627776, mem[224 len 5]
  if unknownbaed8bb1[mem[197 len 5]] != caller:
      revert with 0, 'sender must be owner'
  if not _tokenContract:
      revert with 0, '0x address is invalid'
  require ext_code.size(_tokenContract)
  call _tokenContract.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[298 len 0] = None
  mem[298] = mem[303 len 17], 'owner' % 1099511627776, mem[325 len 5]
  require ext_code.size(_tokenContract)
  call _tokenContract.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args unknownbaed8bb1[mem[298 len 5]], ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'token transfer failed'


# hash = 0x8da5cb5b
# getter = None
# const = None
# payable = False
def owner(): # not payable
  mem[197 len 0] = None
  mem[197] = mem[202 len 17], 'owner' % 1099511627776, mem[224 len 5]
  mem[197] = unknownbaed8bb1[mem[197 len 5]]
  return memory
    from 197
     [93mlen 32


# hash = 0xb187bd26
# getter = None
# const = None
# payable = False
def isPaused(): # not payable
  mem[198 len 0] = None
  mem[198] = mem[204 len 14], 0, mem[224 len 6]
  mem[198] = bool(stor4[mem[198 len 6]])
  return memory
    from 198
     [93mlen 32


# hash = 0xb3447ac9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknownb3447ac9(uint256 _param1): # not payable
  return unknownb3447ac9[_param1]


# hash = 0xbaed8bb1
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknownbaed8bb1(uint256 _param1): # not payable
  return unknownbaed8bb1[_param1]


# hash = 0xc6cb7ab8
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 3]]]]], ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknownc6cb7ab8(uint256 _param1): # not payable
  return unknownc6cb7ab8[_param1][0 len unknownc6cb7ab8[_param1].length]


# hash = 0xdc659907
# getter = None
# const = None
# payable = False
def useModule(address _moduleFactory): # not payable
  mem[96] = 21
  mem[128] = 'securityTokenRegistry'
  mem[192 len 0] = None
  mem[203 len 21] = Mask(168, 0, 'securityTokenRegistry')
  mem[160] = 21
  mem[213 len 0] = None
  mem[213] = mem[234 len 11]
  require ext_code.size(unknownbaed8bb1[mem[213 len 21]])
  call unknownbaed8bb1[mem[213 len 21]].isSecurityToken(address securityToken) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      mem[213] = 15
      mem[245] = 0x66656174757265526567697374727900000000000000000000000000000000
      mem[309 len 0] = None
      mem[277] = 15
      mem[324 len 0] = None
      mem[324] = 0, mem[341 len 15]
      mem[392] = 0x637573746f6d4d6f64756c6573416c6c6f7765640000000000000000000000
      require ext_code.size(unknownbaed8bb1[mem[324 len 15]])
      call unknownbaed8bb1[mem[324 len 15]].0x2f0019f2 with:
           gas gas_remaining wei
          args 'customModulesAllowed'
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[324] = 8
      mem[356] = 0x76657269666965640000000000000000000000000000000000000000000000
      mem[420 len 0] = None
      if not ext_call.return_data[0]:
          mem[428] = addr(_moduleFactory)
          mem[388] = 28
          mem[448 len 0] = None
          mem[448] = mem[476 len 4]
          mem[0] = sha3(mem[448 len 28])
          mem[32] = 4
          if not stor4[mem[448 len 28]]:
              revert with 0, 'ModuleFactory must be verified'
          mem[448] = 0xd8e6e2c00000000000000000000000000000000000000000000000000000000
          require ext_code.size(caller)
          call caller.getVersion() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[448 len return_data.size] = ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_6304 = mem[448]
          require mem[448] <= 4294967296
          require mem[448] + 32 <= return_data.size
          require mem[mem[448] + 448] <= 4294967296 and mem[448] + (32 * mem[mem[448] + 448]) + 32 <= return_data.size
          mem[ceil32(return_data.size) + 448] = 0x8677768f00000000000000000000000000000000000000000000000000000000
          require ext_code.size(_moduleFactory)
          call _moduleFactory.getLowerSTVersionBounds() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[ceil32(return_data.size) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (2 * ceil32(return_data.size)) + 448
          require return_data.size >= 32
          [94m_6318 = mem[ceil32(return_data.size) + 448]
          require mem[ceil32(return_data.size) + 448] <= 4294967296
          require mem[ceil32(return_data.size) + 448] + 32 <= return_data.size
          require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448] <= 4294967296 and mem[ceil32(return_data.size) + 448] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448]) + 32 <= return_data.size
          mem[(2 * ceil32(return_data.size)) + 448] = 0xf786299900000000000000000000000000000000000000000000000000000000
          require ext_code.size(_moduleFactory)
          call _moduleFactory.getUpperSTVersionBounds() with:
               gas gas_remaining wei
              args mem[(2 * ceil32(return_data.size)) + 452 len ceil32(return_data.size)]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(2 * ceil32(return_data.size)) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (4 * ceil32(return_data.size)) + 448
          require return_data.size >= 32
          require mem[(2 * ceil32(return_data.size)) + 448] <= 4294967296
          require mem[(2 * ceil32(return_data.size)) + 448] + 32 <= return_data.size
          require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 448] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]) + 32 <= return_data.size
          if mem[ceil32(return_data.size) + [94m_6318 + 448] != mem[[94m_6304 + 448]:
              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[(4 * ceil32(return_data.size)) + 452] = 32
              mem[(4 * ceil32(return_data.size)) + 484] = 21
              mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
              revert with memory
                from (4 * ceil32(return_data.size)) + 448
                 [93mlen (5 * ceil32(return_data.size)) + 100
          [94midx = 0
          [94ms = 0
          while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6318 + 448]:
              require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6318 + 448]
              if mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6318 + 511 len 1] != 0:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              [94midx = [94midx + 1
              [94ms = [94ms + 1
              continue 
          if [94ms == mem[ceil32(return_data.size) + [94m_6318 + 448]:
              if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6304 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      require uint8([94midx) < mem[[94m_6304 + 448]
                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                          require uint8([94midx) < mem[[94m_6304 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 574] = mem[(4 * ceil32(return_data.size)) + 604 len 2] or Mask(240, 16, mem[(4 * ceil32(return_data.size)) + 544])
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
          else:
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6318 + 448]:
                  require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6318 + 448]
                  require uint8([94midx) < mem[[94m_6304 + 448]
                  if mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1] <= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6318 + 511 len 1]:
                      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6318 + 448]
                      require uint8([94midx) < mem[[94m_6304 + 448]
                      if mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1] >= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6318 + 511 len 1]:
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6304 + 448]:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 21
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 100
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[[94m_6304 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                                  require uint8([94midx) < mem[[94m_6304 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 1
                                      continue 
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
                  if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6304 + 448]:
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 21
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 100
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                      [94midx = [94midx + 1
                      [94ms = [94ms + 1
                      continue 
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[[94m_6304 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                              require uint8([94midx) < mem[[94m_6304 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                                  [94midx = [94midx + 1
                                  [94ms = [94ms + 1
                                  continue 
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                          mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                          [94ms = (4 * ceil32(return_data.size)) + 480
                          [94mt = (4 * ceil32(return_data.size)) + 544
                          [94midx = 10
                          while [94midx >= 32:
                              mem[[94mt] = mem[[94ms]
                              [94ms = [94ms + 32
                              [94mt = [94mt + 32
                              [94midx = [94midx - 32
                              continue 
                          mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                          mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                          [94ms = (4 * ceil32(return_data.size)) + 544
                          [94mt = (4 * ceil32(return_data.size)) + 574
                          [94midx = (5 * ceil32(return_data.size)) + 30
                          while [94midx >= 32:
                              mem[[94mt] = mem[[94ms]
                              [94ms = [94ms + 32
                              [94mt = [94mt + 32
                              [94midx = [94midx - 32
                              continue 
                          mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                          uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                          addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                          log 0xfd0013c5: _moduleFactory, caller
                          stop
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                  mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                  [94ms = (4 * ceil32(return_data.size)) + 480
                  [94mt = (4 * ceil32(return_data.size)) + 544
                  [94midx = 10
                  while [94midx >= 32:
                      mem[[94mt] = mem[[94ms]
                      [94ms = [94ms + 32
                      [94mt = [94mt + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                  mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                  [94ms = (4 * ceil32(return_data.size)) + 544
                  [94mt = (4 * ceil32(return_data.size)) + 574
                  [94midx = (5 * ceil32(return_data.size)) + 30
                  while [94midx >= 32:
                      mem[[94mt] = mem[[94ms]
                      [94ms = [94ms + 32
                      [94mt = [94mt + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                  uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                  addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                  log 0xfd0013c5: _moduleFactory, caller
                  stop
              if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6304 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[ceil32(return_data.size) + [94m_6318 + 448] - 1:
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[[94m_6304 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                              require uint8([94midx) < mem[[94m_6304 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                                  [94midx = [94midx + 1
                                  [94ms = [94ms + 1
                                  continue 
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 48
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                  mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 132
              if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      require uint8([94midx) < mem[[94m_6304 + 448]
                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                          require uint8([94midx) < mem[[94m_6304 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6304 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = (5 * ceil32(return_data.size)) + 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
      else:
          mem[420 len 24] = 0, mem[424 len 20]
          mem[420 len 0] = 0
          mem[428] = addr(_moduleFactory)
          mem[388] = 28
          mem[448 len 0] = None
          mem[448] = mem[476 len 4]
          mem[0] = sha3(mem[448 len 28])
          mem[32] = 4
          if stor4[mem[448 len 28]]:
              mem[448] = 0xd8e6e2c00000000000000000000000000000000000000000000000000000000
              require ext_code.size(caller)
              call caller.getVersion() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_6308 = mem[448]
              require mem[448] <= 4294967296
              require mem[448] + 32 <= return_data.size
              require mem[mem[448] + 448] <= 4294967296 and mem[448] + (32 * mem[mem[448] + 448]) + 32 <= return_data.size
              mem[ceil32(return_data.size) + 448] = 0x8677768f00000000000000000000000000000000000000000000000000000000
              require ext_code.size(_moduleFactory)
              call _moduleFactory.getLowerSTVersionBounds() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[ceil32(return_data.size) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (2 * ceil32(return_data.size)) + 448
              require return_data.size >= 32
              [94m_6323 = mem[ceil32(return_data.size) + 448]
              require mem[ceil32(return_data.size) + 448] <= 4294967296
              require mem[ceil32(return_data.size) + 448] + 32 <= return_data.size
              require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448] <= 4294967296 and mem[ceil32(return_data.size) + 448] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448]) + 32 <= return_data.size
              mem[(2 * ceil32(return_data.size)) + 448] = 0xf786299900000000000000000000000000000000000000000000000000000000
              require ext_code.size(_moduleFactory)
              call _moduleFactory.getUpperSTVersionBounds() with:
                   gas gas_remaining wei
                  args mem[(2 * ceil32(return_data.size)) + 452 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(2 * ceil32(return_data.size)) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (4 * ceil32(return_data.size)) + 448
              require return_data.size >= 32
              require mem[(2 * ceil32(return_data.size)) + 448] <= 4294967296
              require mem[(2 * ceil32(return_data.size)) + 448] + 32 <= return_data.size
              require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 448] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]) + 32 <= return_data.size
              if mem[ceil32(return_data.size) + [94m_6323 + 448] != mem[[94m_6308 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6323 + 448]:
                  require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6323 + 448]
                  if mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6323 + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[ceil32(return_data.size) + [94m_6323 + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6323 + 448]:
                      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6323 + 448]
                      require uint8([94midx) < mem[[94m_6308 + 448]
                      if mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1] <= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6323 + 511 len 1]:
                          require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6323 + 448]
                          require uint8([94midx) < mem[[94m_6308 + 448]
                          if mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1] >= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6323 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6308 + 448]:
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 21
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 100
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              [94midx = 0
                              [94ms = 0
                              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                                  require uint8([94midx) < mem[[94m_6308 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                      require uint8([94midx) < mem[[94m_6308 + 448]
                                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 1
                                          continue 
                                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                                  mem[(4 * ceil32(return_data.size)) + 484] = 48
                                  mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                                  mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                                  revert with memory
                                    from (4 * ceil32(return_data.size)) + 448
                                     [93mlen (5 * ceil32(return_data.size)) + 132
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6308 + 448]:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 21
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 100
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[[94m_6308 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                  require uint8([94midx) < mem[[94m_6308 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 1
                                      continue 
                                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                                  mem[(4 * ceil32(return_data.size)) + 484] = 48
                                  mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                                  mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                                  revert with memory
                                    from (4 * ceil32(return_data.size)) + 448
                                     [93mlen (5 * ceil32(return_data.size)) + 132
                              mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                              [94ms = (4 * ceil32(return_data.size)) + 480
                              [94mt = (4 * ceil32(return_data.size)) + 544
                              [94midx = 10
                              while [94midx >= 32:
                                  mem[[94mt] = mem[[94ms]
                                  [94ms = [94ms + 32
                                  [94mt = [94mt + 32
                                  [94midx = [94midx - 32
                                  continue 
                              mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                              mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                              [94ms = (4 * ceil32(return_data.size)) + 544
                              [94mt = (4 * ceil32(return_data.size)) + 574
                              [94midx = (5 * ceil32(return_data.size)) + 30
                              while [94midx >= 32:
                                  mem[[94mt] = mem[[94ms]
                                  [94ms = [94ms + 32
                                  [94mt = [94mt + 32
                                  [94midx = [94midx - 32
                                  continue 
                              mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                              uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                              addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                              log 0xfd0013c5: _moduleFactory, caller
                              stop
                          if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = (5 * ceil32(return_data.size)) + 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[ceil32(return_data.size) + [94m_6323 + 448] - 1:
                      if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6308 + 448]:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 21
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 100
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[[94m_6308 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                  require uint8([94midx) < mem[[94m_6308 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 1
                                      continue 
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
              if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6308 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      require uint8([94midx) < mem[[94m_6308 + 448]
                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                          require uint8([94midx) < mem[[94m_6308 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6308 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = (5 * ceil32(return_data.size)) + 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
          else:
              require ext_code.size(caller)
              call caller.owner() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(_moduleFactory)
              call _moduleFactory.owner() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[12 len 20] != addr(ext_call.return_data[0]):
                  revert with 0, 'ModuleFactory must be verified or SecurityToken owner must be ModuleFactory owner'
              mem[448] = 0xd8e6e2c00000000000000000000000000000000000000000000000000000000
              require ext_code.size(caller)
              call caller.getVersion() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_6327 = mem[448]
              require mem[448] <= 4294967296
              require mem[448] + 32 <= return_data.size
              require mem[mem[448] + 448] <= 4294967296 and mem[448] + (32 * mem[mem[448] + 448]) + 32 <= return_data.size
              mem[ceil32(return_data.size) + 448] = 0x8677768f00000000000000000000000000000000000000000000000000000000
              require ext_code.size(_moduleFactory)
              call _moduleFactory.getLowerSTVersionBounds() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[ceil32(return_data.size) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (2 * ceil32(return_data.size)) + 448
              require return_data.size >= 32
              [94m_6340 = mem[ceil32(return_data.size) + 448]
              require mem[ceil32(return_data.size) + 448] <= 4294967296
              require mem[ceil32(return_data.size) + 448] + 32 <= return_data.size
              require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448] <= 4294967296 and mem[ceil32(return_data.size) + 448] + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 448] + 448]) + 32 <= return_data.size
              mem[(2 * ceil32(return_data.size)) + 448] = 0xf786299900000000000000000000000000000000000000000000000000000000
              require ext_code.size(_moduleFactory)
              call _moduleFactory.getUpperSTVersionBounds() with:
                   gas gas_remaining wei
                  args mem[(2 * ceil32(return_data.size)) + 452 len ceil32(return_data.size)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(2 * ceil32(return_data.size)) + 448 len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = (4 * ceil32(return_data.size)) + 448
              require return_data.size >= 32
              require mem[(2 * ceil32(return_data.size)) + 448] <= 4294967296
              require mem[(2 * ceil32(return_data.size)) + 448] + 32 <= return_data.size
              require mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] <= 4294967296 and mem[(2 * ceil32(return_data.size)) + 448] + (32 * mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]) + 32 <= return_data.size
              if mem[ceil32(return_data.size) + [94m_6340 + 448] != mem[[94m_6327 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6340 + 448]:
                  require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6340 + 448]
                  if mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6340 + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[ceil32(return_data.size) + [94m_6340 + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[ceil32(return_data.size) + [94m_6340 + 448]:
                      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6340 + 448]
                      require uint8([94midx) < mem[[94m_6327 + 448]
                      if mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1] <= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6340 + 511 len 1]:
                          require uint8([94midx) < mem[ceil32(return_data.size) + [94m_6340 + 448]
                          require uint8([94midx) < mem[[94m_6327 + 448]
                          if mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1] >= mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_6340 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6327 + 448]:
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 21
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 100
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              [94midx = 0
                              [94ms = 0
                              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                                  require uint8([94midx) < mem[[94m_6327 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                      require uint8([94midx) < mem[[94m_6327 + 448]
                                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 1
                                          continue 
                                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                                  mem[(4 * ceil32(return_data.size)) + 484] = 48
                                  mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                                  mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                                  revert with memory
                                    from (4 * ceil32(return_data.size)) + 448
                                     [93mlen (5 * ceil32(return_data.size)) + 132
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6327 + 448]:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 21
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 100
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[[94m_6327 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                  require uint8([94midx) < mem[[94m_6327 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 1
                                      continue 
                                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                                  mem[(4 * ceil32(return_data.size)) + 484] = 48
                                  mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                                  mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                                  revert with memory
                                    from (4 * ceil32(return_data.size)) + 448
                                     [93mlen (5 * ceil32(return_data.size)) + 132
                              mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                              [94ms = (4 * ceil32(return_data.size)) + 480
                              [94mt = (4 * ceil32(return_data.size)) + 544
                              [94midx = 10
                              while [94midx >= 32:
                                  mem[[94mt] = mem[[94ms]
                                  [94ms = [94ms + 32
                                  [94mt = [94mt + 32
                                  [94midx = [94midx - 32
                                  continue 
                              mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                              mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                              [94ms = (4 * ceil32(return_data.size)) + 544
                              [94mt = (4 * ceil32(return_data.size)) + 574
                              [94midx = (5 * ceil32(return_data.size)) + 30
                              while [94midx >= 32:
                                  mem[[94mt] = mem[[94ms]
                                  [94ms = [94ms + 32
                                  [94mt = [94mt + 32
                                  [94midx = [94midx - 32
                                  continue 
                              mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                              uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                              addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                              log 0xfd0013c5: _moduleFactory, caller
                              stop
                          if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 574] = mem[(4 * ceil32(return_data.size)) + 604 len 2] or Mask(240, 16, mem[(4 * ceil32(return_data.size)) + 544])
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[ceil32(return_data.size) + [94m_6340 + 448] - 1:
                      if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6327 + 448]:
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 21
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 100
                      [94midx = 0
                      [94ms = 0
                      while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          [94midx = [94midx + 1
                          [94ms = [94ms + 1
                          continue 
                      if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                          [94midx = 0
                          [94ms = 0
                          while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                              require uint8([94midx) < mem[[94m_6327 + 448]
                              require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                              if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                  require uint8([94midx) < mem[[94m_6327 + 448]
                                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 1
                                      continue 
                              mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                              mem[(4 * ceil32(return_data.size)) + 452] = 32
                              mem[(4 * ceil32(return_data.size)) + 484] = 48
                              mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                              mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                              revert with memory
                                from (4 * ceil32(return_data.size)) + 448
                                 [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
              if mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] != mem[[94m_6327 + 448]:
                  mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[(4 * ceil32(return_data.size)) + 452] = 32
                  mem[(4 * ceil32(return_data.size)) + 484] = 21
                  mem[(4 * ceil32(return_data.size)) + 516] = 'Input length mismatch'
                  revert with memory
                    from (4 * ceil32(return_data.size)) + 448
                     [93mlen (5 * ceil32(return_data.size)) + 100
              [94midx = 0
              [94ms = 0
              while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                  if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] != 0:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  [94midx = [94midx + 1
                  [94ms = [94ms + 1
                  continue 
              if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                  [94midx = 0
                  [94ms = 0
                  while uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]:
                      require uint8([94midx) < mem[[94m_6327 + 448]
                      require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                      if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] <= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                          require uint8([94midx) < mem[[94m_6327 + 448]
                          require uint8([94midx) < mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448]
                          if mem[(32 * uint8([94midx)) + (2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 511 len 1] >= mem[(32 * uint8([94midx)) + [94m_6327 + 511 len 1]:
                              [94midx = [94midx + 1
                              [94ms = [94ms + 1
                              continue 
                          mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                          mem[(4 * ceil32(return_data.size)) + 452] = 32
                          mem[(4 * ceil32(return_data.size)) + 484] = 48
                          mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                          mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                          revert with memory
                            from (4 * ceil32(return_data.size)) + 448
                             [93mlen (5 * ceil32(return_data.size)) + 132
                      mem[(4 * ceil32(return_data.size)) + 480] = 0x72657075746174696f6e000000000000000000000000000000000000000000
                      [94ms = (4 * ceil32(return_data.size)) + 480
                      [94mt = (4 * ceil32(return_data.size)) + 544
                      [94midx = 10
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + 544] = 0 or Mask(176, 80, mem[(4 * ceil32(return_data.size)) + 544])
                      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
                      [94ms = (4 * ceil32(return_data.size)) + 544
                      [94mt = (4 * ceil32(return_data.size)) + 574
                      [94midx = (5 * ceil32(return_data.size)) + 30
                      while [94midx >= 32:
                          mem[[94mt] = mem[[94ms]
                          [94ms = [94ms + 32
                          [94mt = [94mt + 32
                          [94midx = [94midx - 32
                          continue 
                      mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
                      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
                      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
                      log 0xfd0013c5: _moduleFactory, caller
                      stop
                  if [94ms != mem[(2 * ceil32(return_data.size)) + mem[(2 * ceil32(return_data.size)) + 448] + 448] - 1:
                      mem[(4 * ceil32(return_data.size)) + 448] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                      mem[(4 * ceil32(return_data.size)) + 452] = 32
                      mem[(4 * ceil32(return_data.size)) + 484] = 48
                      mem[(4 * ceil32(return_data.size)) + 516] = 'Version should within the compat'
                      mem[(4 * ceil32(return_data.size)) + 548] = 'ible range of ST'
                      revert with memory
                        from (4 * ceil32(return_data.size)) + 448
                         [93mlen (5 * ceil32(return_data.size)) + 132
      mem[(4 * ceil32(return_data.size)) + 544 len 0] = None
      mem[(4 * ceil32(return_data.size)) + 554] = addr(_moduleFactory)
      mem[(4 * ceil32(return_data.size)) + 574 len floor32((5 * ceil32(return_data.size)) + 30)] = mem[(4 * ceil32(return_data.size)) + 544 len floor32((5 * ceil32(return_data.size)) + 30)]
      mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] = mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 574] and 256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1 or mem[(4 * ceil32(return_data.size)) + floor32((5 * ceil32(return_data.size)) + 30) + 544] and !(256^(-((5 * ceil32(return_data.size)) + 30 % 32) + 32) - 1)
      uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])++
      addr(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]][uint256(stor9[mem[(4 * ceil32(return_data.size)) + 574 len (5 * ceil32(return_data.size)) + 30]])]) = caller
      log 0xfd0013c5: _moduleFactory, caller


# hash = 0xeac5ab43
# getter = None
# const = None
# payable = False
def verifyModule(address _moduleFactory, bool _verified): # not payable
  mem[197 len 0] = None
  mem[197] = mem[202 len 17], 'owner' % 1099511627776, mem[224 len 5]
  if unknownbaed8bb1[mem[197 len 5]] != caller:
      revert with 0, 'sender must be owner'
  mem[321 len 0] = None
  mem[321] = mem[349 len 4]
  if not unknown26839e53[mem[321 len 28]]:
      revert with 0, 'Module factory must be registered'
  mem[445 len 0] = None
  mem[445] = mem[473 len 4]
  stor4[mem[445 len 28]] = uint8(_verified)
  log 0x302d67e6: _verified, _moduleFactory


# hash = 0xf433262f
# getter = None
# const = None
# payable = False
def updateFromRegistry(): # not payable
  mem[197 len 0] = None
  mem[197] = mem[202 len 17], 'owner' % 1099511627776, mem[224 len 5]
  if unknownbaed8bb1[mem[197 len 5]] != caller:
      revert with 0, 'sender must be owner'
  mem[312 len 0] = None
  mem[312] = mem[331 len 13]
  mem[429 len 0] = None
  mem[429] = mem[450 len 11]
  require ext_code.size(unknownbaed8bb1[mem[312 len 19]])
  call unknownbaed8bb1[mem[312 len 19]].getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=21, data='SecurityTokenRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknownbaed8bb1[mem[429 len 21]] = addr(ext_call.return_data[0])
  mem[540 len 0] = None
  mem[540] = 0, mem[557 len 15]
  require ext_code.size(unknownbaed8bb1[mem[312 len 19]])
  call unknownbaed8bb1[mem[312 len 19]].getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=15, data='FeatureRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknownbaed8bb1[mem[540 len 15]] = addr(ext_call.return_data[0])
  mem[646 len 0] = None
  mem[646] = mem[656 len 2], Mask(80, 0, 'proofToken'), mem[668 len 10]
  require ext_code.size(unknownbaed8bb1[mem[312 len 19]])
  call unknownbaed8bb1[mem[312 len 19]].getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=10, data='ProofToken')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknownbaed8bb1[mem[646 len 10]] = addr(ext_call.return_data[0])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


