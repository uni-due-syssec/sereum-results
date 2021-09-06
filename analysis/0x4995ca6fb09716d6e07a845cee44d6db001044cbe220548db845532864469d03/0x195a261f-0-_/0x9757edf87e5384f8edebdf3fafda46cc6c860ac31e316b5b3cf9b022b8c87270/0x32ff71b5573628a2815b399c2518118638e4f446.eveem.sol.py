# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x32FF71B5573628a2815b399C2518118638e4f446 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    authorityAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    unknown365a86fcAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    unknown20531bc9Address # mask: a s
    # storage address 11
    registryAddress # mask: a s
    # storage address 12
    versionAddress # mask: a s
    # storage address 13
    unknownc9d4623fAddress # mask: a s
    # storage address 14
    unknown8a471df9Address # mask: a s
    # storage address 15
    initialized # mask: a s
# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  owner = _newOwner
  log LogSetOwner(address owner=_newOwner)


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(initialized)


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return unknown20531bc9Address


# hash = 0x365a86fc
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown365a86fc(): # not payable
  return unknown365a86fcAddress


# hash = 0x4e2c75f3
# getter = None
# const = None
# payable = False
def unknown4e2c75f3(uint32 _param1): # not payable
  if stor16[Mask(32, 224, _param1)].field_0:
      mem[128 len 32 * stor16[Mask(32, 224, _param1)].field_0] = code.data[4451 len 32 * stor16[Mask(32, 224, _param1)].field_0]
  [94midx = 0
  while [94midx < stor16[Mask(32, 224, _param1)].field_0:
      mem[0] = sha3(Mask(32, 224, _param1), 16)
      require [94midx < stor16[Mask(32, 224, _param1)].field_0
      mem[(32 * [94midx) + 128] = stor16[Mask(32, 224, _param1)][[94midx].field_0
      [94midx = [94midx + 1
      continue 
  if stor16[Mask(32, 224, _param1)].field_256:
      mem[(32 * stor16[Mask(32, 224, _param1)].field_0) + 160 len 32 * stor16[Mask(32, 224, _param1)].field_256] = code.data[4451 len 32 * stor16[Mask(32, 224, _param1)].field_256]
  [94midx = 0
  while [94midx < stor16[Mask(32, 224, _param1)].field_256:
      mem[0] = sha3(Mask(32, 224, _param1), 16) + 1
      require [94midx < stor16[Mask(32, 224, _param1)].field_256
      mem[(32 * stor16[Mask(32, 224, _param1)].field_0) + (32 * [94midx) + 160] = stor16[Mask(32, 224, _param1)][[94midx + 1].field_0
      [94midx = [94midx + 1
      continue 
  mem[(32 * stor16[Mask(32, 224, _param1)].field_0) + (32 * stor16[Mask(32, 224, _param1)].field_256) + 256 len floor32(stor16[Mask(32, 224, _param1)].field_0)] = mem[128 len floor32(stor16[Mask(32, 224, _param1)].field_0)]
  mem[(64 * stor16[Mask(32, 224, _param1)].field_0) + (32 * stor16[Mask(32, 224, _param1)].field_256) + 256] = stor16[Mask(32, 224, _param1)].field_256
  mem[(64 * stor16[Mask(32, 224, _param1)].field_0) + (32 * stor16[Mask(32, 224, _param1)].field_256) + 288 len floor32(stor16[Mask(32, 224, _param1)].field_256)] = mem[(32 * stor16[Mask(32, 224, _param1)].field_0) + 160 len floor32(stor16[Mask(32, 224, _param1)].field_256)]
  return Array(len=stor16[Mask(32, 224, _param1)].field_0, data=mem[128 len floor32(stor16[Mask(32, 224, _param1)].field_0)], mem[(32 * stor16[Mask(32, 224, _param1)].field_0) + (32 * stor16[Mask(32, 224, _param1)].field_256) + floor32(stor16[Mask(32, 224, _param1)].field_0) + 256 len (32 * stor16[Mask(32, 224, _param1)].field_0) + (32 * stor16[Mask(32, 224, _param1)].field_256) + -floor32(stor16[Mask(32, 224, _param1)].field_0) + 32]), 
         (32 * stor16[Mask(32, 224, _param1)].field_0) + 96


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return versionAddress


# hash = 0x7a9e5e4b
# getter = None
# const = None
# payable = False
def setAuthority(address _authority): # not payable
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  authorityAddress = _authority_
  log LogSetAuthority(address authority=_authority_)


# hash = 0x7b103999
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def registry(): # not payable
  return registryAddress


# hash = 0x83259ed9
# getter = None
# const = None
# payable = False
def unknown83259ed9(addr _param1, addr _param2, addr _param3, addr _param4, addr _param5, addr _param6, addr _param7, addr _param8, addr _param9, addr _param10, addr _param11, addr _param12): # not payable
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  require caller == unknown365a86fcAddress
  if initialized:
      revert with 0, 'Already initialized'
  stor3 = _param1
  stor4 = _param2
  stor5 = _param3
  stor6 = _param4
  stor7 = _param5
  stor8 = _param6
  stor9 = _param7
  unknown20531bc9Address = _param8
  registryAddress = _param9
  versionAddress = _param10
  unknownc9d4623fAddress = _param11
  unknown8a471df9Address = _param12
  initialized = 1
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  owner = 0
  log LogSetOwner(address owner)
  log 0x0 


# hash = 0x8665f0ac
# getter = None
# const = None
# payable = False
def unknown8665f0ac(array _param1, array _param2): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  if this.address == caller:
      if _param1.length != _param2.length:
          revert with 0, 'Arrays lengths unequal'
      [94midx = 0
      while [94midx < _param1.length:
          require [94midx < _param1.length
          [94m_214 = mem[(32 * [94midx) + 128]
          require [94midx < _param2.length
          [94m_218 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
          if caller != this.address:
              if owner != caller:
                  if not authorityAddress:
                      revert with 0, 'ds-auth-unauthorized'
                  else:
                      mem[(32 * _param2.length) + (32 * _param1.length) + 164] = caller
                      mem[(32 * _param2.length) + (32 * _param1.length) + 196] = this.address
                      mem[(32 * _param2.length) + (32 * _param1.length) + 228] = call.func_hash
                      require ext_code.size(authorityAddress)
                      call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
                           gas gas_remaining wei
                          args caller, this.address, call.func_hash
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'ds-auth-unauthorized'
                          else:
                              require ext_code.size(addr([94m_218))
                              call addr([94m_218).0x9218e91 with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 1
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0] <= 1
                                      if ext_call.return_data[0] != 1:
                                          revert with 0, 'Only pre and post allowed'
                                      else:
                                          mem[32] = 16
                                          stor16[Mask(32, 224, [94m_214)].field_256++
                                          mem[0] = sha3(Mask(32, 224, [94m_214), 16) + 1
                                          stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('var', '_214')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, [94m_214)].field_256].field_0 = addr([94m_218)
                                          require ext_call.return_data[0] <= 1
                                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                                          [94midx = [94midx + 1
                                          continue 
                                  else:
                                      mem[32] = 16
                                      stor16[Mask(32, 224, [94m_214)].field_0++
                                      mem[0] = sha3(Mask(32, 224, [94m_214), 16)
                                      stor16[Mask(32, 224, [94m_214)][stor16[Mask(32, 224, [94m_214)].field_0].field_0 = addr([94m_218)
                                      require ext_call.return_data[0] <= 1
                                      mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                      log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                                      [94midx = [94midx + 1
                                      continue 
              else:
                  require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
                  call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 1
                      if ext_call.return_data[0]:
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0] != 1:
                              revert with 0, 'Only pre and post allowed'
                          else:
                              mem[32] = 16
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                              mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                              stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                              require ext_call.return_data[0] <= 1
                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[32] = 16
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                          mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                          require ext_call.return_data[0] <= 1
                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                          [94midx = [94midx + 1
                          continue 
          else:
              require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
              call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 1
                  if ext_call.return_data[0]:
                      require ext_call.return_data[0] <= 1
                      if ext_call.return_data[0] != 1:
                          revert with 0, 'Only pre and post allowed'
                      else:
                          mem[32] = 16
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                          mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                          stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                          require ext_call.return_data[0] <= 1
                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                          [94midx = [94midx + 1
                          continue 
                  else:
                      mem[32] = 16
                      stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                      mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                      stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                      require ext_call.return_data[0] <= 1
                      mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                      log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _214), addr(_218)
                      [94midx = [94midx + 1
                      continue 
  else:
      if owner == caller:
          if _param1.length != _param2.length:
              revert with 0, 'Arrays lengths unequal'
          [94midx = 0
          while [94midx < _param1.length:
              require [94midx < _param1.length
              [94m_212 = mem[(32 * [94midx) + 128]
              require [94midx < _param2.length
              [94m_217 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
              if caller != this.address:
                  if owner != caller:
                      if not authorityAddress:
                          revert with 0, 'ds-auth-unauthorized'
                      else:
                          mem[(32 * _param2.length) + (32 * _param1.length) + 164] = caller
                          mem[(32 * _param2.length) + (32 * _param1.length) + 196] = this.address
                          mem[(32 * _param2.length) + (32 * _param1.length) + 228] = call.func_hash
                          require ext_code.size(authorityAddress)
                          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
                               gas gas_remaining wei
                              args caller, this.address, call.func_hash
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'ds-auth-unauthorized'
                              else:
                                  require ext_code.size(addr([94m_217))
                                  call addr([94m_217).0x9218e91 with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 1
                                      if ext_call.return_data[0]:
                                          require ext_call.return_data[0] <= 1
                                          if ext_call.return_data[0] != 1:
                                              revert with 0, 'Only pre and post allowed'
                                          else:
                                              mem[32] = 16
                                              stor16[Mask(32, 224, [94m_212)].field_256++
                                              mem[0] = sha3(Mask(32, 224, [94m_212), 16) + 1
                                              stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('var', '_212')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, [94m_212)].field_256].field_0 = addr([94m_217)
                                              require ext_call.return_data[0] <= 1
                                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                                              [94midx = [94midx + 1
                                              continue 
                                      else:
                                          mem[32] = 16
                                          stor16[Mask(32, 224, [94m_212)].field_0++
                                          mem[0] = sha3(Mask(32, 224, [94m_212), 16)
                                          stor16[Mask(32, 224, [94m_212)][stor16[Mask(32, 224, [94m_212)].field_0].field_0 = addr([94m_217)
                                          require ext_call.return_data[0] <= 1
                                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                                          [94midx = [94midx + 1
                                          continue 
                  else:
                      require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
                      call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0]:
                              require ext_call.return_data[0] <= 1
                              if ext_call.return_data[0] != 1:
                                  revert with 0, 'Only pre and post allowed'
                              else:
                                  mem[32] = 16
                                  stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                                  mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                                  stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                                  require ext_call.return_data[0] <= 1
                                  mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                  log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[32] = 16
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                              mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                              require ext_call.return_data[0] <= 1
                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
                  call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 1
                      if ext_call.return_data[0]:
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0] != 1:
                              revert with 0, 'Only pre and post allowed'
                          else:
                              mem[32] = 16
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                              mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                              stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                              require ext_call.return_data[0] <= 1
                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[32] = 16
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                          mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                          require ext_call.return_data[0] <= 1
                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _212), addr(_217)
                          [94midx = [94midx + 1
                          continue 
      else:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[(32 * _param2.length) + (32 * _param1.length) + 164] = caller
          mem[(32 * _param2.length) + (32 * _param1.length) + 196] = this.address
          mem[(32 * _param2.length) + (32 * _param1.length) + 228] = call.func_hash
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
          if _param1.length != _param2.length:
              revert with 0, 'Arrays lengths unequal'
          [94midx = 0
          while [94midx < _param1.length:
              require [94midx < _param1.length
              [94m_210 = mem[(32 * [94midx) + 128]
              require [94midx < _param2.length
              [94m_216 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
              if caller != this.address:
                  if owner != caller:
                      if not authorityAddress:
                          revert with 0, 'ds-auth-unauthorized'
                      else:
                          mem[(32 * _param2.length) + (32 * _param1.length) + 164] = caller
                          mem[(32 * _param2.length) + (32 * _param1.length) + 196] = this.address
                          mem[(32 * _param2.length) + (32 * _param1.length) + 228] = call.func_hash
                          require ext_code.size(authorityAddress)
                          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
                               gas gas_remaining wei
                              args caller, this.address, call.func_hash
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'ds-auth-unauthorized'
                              else:
                                  require ext_code.size(addr([94m_216))
                                  call addr([94m_216).0x9218e91 with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 1
                                      if ext_call.return_data[0]:
                                          require ext_call.return_data[0] <= 1
                                          if ext_call.return_data[0] != 1:
                                              revert with 0, 'Only pre and post allowed'
                                          else:
                                              mem[32] = 16
                                              stor16[Mask(32, 224, [94m_210)].field_256++
                                              mem[0] = sha3(Mask(32, 224, [94m_210), 16) + 1
                                              stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('var', '_210')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, [94m_210)].field_256].field_0 = addr([94m_216)
                                              require ext_call.return_data[0] <= 1
                                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                                              [94midx = [94midx + 1
                                              continue 
                                      else:
                                          mem[32] = 16
                                          stor16[Mask(32, 224, [94m_210)].field_0++
                                          mem[0] = sha3(Mask(32, 224, [94m_210), 16)
                                          stor16[Mask(32, 224, [94m_210)][stor16[Mask(32, 224, [94m_210)].field_0].field_0 = addr([94m_216)
                                          require ext_call.return_data[0] <= 1
                                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                                          [94midx = [94midx + 1
                                          continue 
                  else:
                      require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
                      call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0]:
                              require ext_call.return_data[0] <= 1
                              if ext_call.return_data[0] != 1:
                                  revert with 0, 'Only pre and post allowed'
                              else:
                                  mem[32] = 16
                                  stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                                  mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                                  stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                                  require ext_call.return_data[0] <= 1
                                  mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                                  log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[32] = 16
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                              mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                              require ext_call.return_data[0] <= 1
                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                              [94midx = [94midx + 1
                              continue 
              else:
                  require ext_code.size(mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20])
                  call mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20].0x9218e91 with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 1
                      if ext_call.return_data[0]:
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0] != 1:
                              revert with 0, 'Only pre and post allowed'
                          else:
                              mem[32] = 16
                              stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256++
                              mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16) + 1
                              stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('mem', ('range', ('add', 128, ('mul', 32, ('var', 0))), 32))), ('name', 'stor16', 16))) + stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_256].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                              require ext_call.return_data[0] <= 1
                              mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[32] = 16
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0++
                          mem[0] = sha3(Mask(32, 224, mem[(32 * [94midx) + 128]), 16)
                          stor16[Mask(32, 224, mem[(32 * [94midx) + 128])][stor16[Mask(32, 224, mem[(32 * [94midx) + 128])].field_0].field_0 = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                          require ext_call.return_data[0] <= 1
                          mem[(32 * _param2.length) + (32 * _param1.length) + 160] = uint8(ext_call.return_data[0])
                          log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _210), addr(_216)
                          [94midx = [94midx + 1
                          continue 


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return unknown8a471df9Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xa6c354b0
# getter = None
# const = None
# payable = False
def unknowna6c354b0(uint32 _param1, addr _param2): # not payable
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          else:
              require ext_code.size(authorityAddress)
              call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
                   gas gas_remaining wei
                  args caller, this.address, call.func_hash
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'ds-auth-unauthorized'
                  else:
                      require ext_code.size(_param2)
                      call _param2.0x9218e91 with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 1
                          if ext_call.return_data[0]:
                              require ext_call.return_data[0] <= 1
                              if ext_call.return_data[0] != 1:
                                  revert with 0, 'Only pre and post allowed'
                              else:
                                  stor16[Mask(32, 224, _param1)].field_256++
                                  stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('param', '_param1')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, _param1)].field_256].field_0 = _param2
                                  require ext_call.return_data[0] <= 1
                                  log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
                                  stop
                          else:
                              stor16[Mask(32, 224, _param1)].field_0++
                              stor16[Mask(32, 224, _param1)][stor16[Mask(32, 224, _param1)].field_0].field_0 = _param2
                              require ext_call.return_data[0] <= 1
                              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
                              stop
      else:
          require ext_code.size(_param2)
          call _param2.0x9218e91 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require ext_call.return_data[0] <= 1
              if ext_call.return_data[0]:
                  require ext_call.return_data[0] <= 1
                  if ext_call.return_data[0] != 1:
                      revert with 0, 'Only pre and post allowed'
                  else:
                      stor16[Mask(32, 224, _param1)].field_256++
                      stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('param', '_param1')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, _param1)].field_256].field_0 = _param2
                      require ext_call.return_data[0] <= 1
                      log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
                      stop
              else:
                  stor16[Mask(32, 224, _param1)].field_0++
                  stor16[Mask(32, 224, _param1)][stor16[Mask(32, 224, _param1)].field_0].field_0 = _param2
                  require ext_call.return_data[0] <= 1
                  log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
                  stop
  else:
      require ext_code.size(_param2)
      call _param2.0x9218e91 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_call.return_data[0] <= 1
          if ext_call.return_data[0]:
              require ext_call.return_data[0] <= 1
              if ext_call.return_data[0] != 1:
                  revert with 0, 'Only pre and post allowed'
              else:
                  stor16[Mask(32, 224, _param1)].field_256++
                  stor[('array', 1, ('map', ('mask_shl', 32, 224, 0, ('param', '_param1')), ('name', 'stor16', 16))) + stor16[Mask(32, 224, _param1)].field_256].field_0 = _param2
                  require ext_call.return_data[0] <= 1
                  log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
                  stop
          else:
              stor16[Mask(32, 224, _param1)].field_0++
              stor16[Mask(32, 224, _param1)][stor16[Mask(32, 224, _param1)].field_0].field_0 = _param2
              require ext_call.return_data[0] <= 1
              log 0xd94c45af: uint8(ext_call.return_data[0]), Mask(32, 224, _param1), _param2
              stop


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return stor3, 
         stor4,
         stor5,
         stor6,
         stor7,
         stor8,
         stor9,
         unknown20531bc9Address,
         registryAddress,
         versionAddress,
         unknownc9d4623fAddress,
         unknown8a471df9Address


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return authorityAddress


# hash = 0xc2f98e78
# getter = None
# const = None
# payable = False
def unknownc2f98e78(uint32 _param1, uint256 _param2): # not payable
  mem[96 len 160] = call.data[36 len 160]
  mem[64] = 352
  mem[256 len 96] = call.data[196 len 96]
  mem[0] = Mask(32, 224, _param1)
  mem[32] = 16
  [94midx = 0
  while [94midx < stor16[Mask(32, 224, _param1)].field_256:
      mem[0] = sha3(Mask(32, 224, _param1), 16) + 1
      [94m_16 = mem[64]
      mem[mem[64]] = 0x8a6d79000000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 4] = Mask(32, 224, _param1)
      [94ms = 0
      while [94ms < 160:
          mem[[94ms + [94m_16 + 36] = mem[[94ms + 96]
          [94ms = [94ms + 32
          continue 
      [94ms = 0
      while [94ms < 96:
          mem[[94ms + [94m_16 + 196] = mem[[94ms + 256]
          [94ms = [94ms + 32
          continue 
      mem[[94m_16 + 292] = _param2
      require ext_code.size(stor16[Mask(32, 224, _param1)][[94midx + 1].field_0)
      call stor16[Mask(32, 224, _param1)][[94midx + 1].field_0.mem[mem[64] len 4] with:
           gas gas_remaining wei
          args mem[mem[64] + 4 len [94m_16 + -mem[64] + 320]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'Rule evaluated to false'
      [94midx = [94midx + 1
      continue 


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return unknownc9d4623fAddress


# hash = 0xda6670d3
# getter = None
# const = None
# payable = False
def unknownda6670d3(uint32 _param1, uint256 _param2): # not payable
  mem[96 len 160] = call.data[36 len 160]
  mem[64] = 352
  mem[256 len 96] = call.data[196 len 96]
  mem[0] = Mask(32, 224, _param1)
  mem[32] = 16
  [94midx = 0
  while [94midx < stor16[Mask(32, 224, _param1)].field_0:
      mem[0] = sha3(Mask(32, 224, _param1), 16)
      [94m_16 = mem[64]
      mem[mem[64]] = 0x8a6d79000000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 4] = Mask(32, 224, _param1)
      [94ms = 0
      while [94ms < 160:
          mem[[94ms + [94m_16 + 36] = mem[[94ms + 96]
          [94ms = [94ms + 32
          continue 
      [94ms = 0
      while [94ms < 96:
          mem[[94ms + [94m_16 + 196] = mem[[94ms + 256]
          [94ms = [94ms + 32
          continue 
      mem[[94m_16 + 292] = _param2
      require ext_code.size(stor16[Mask(32, 224, _param1)][[94midx].field_0)
      call stor16[Mask(32, 224, _param1)][[94midx].field_0.mem[mem[64] len 4] with:
           gas gas_remaining wei
          args mem[mem[64] + 4 len [94m_16 + -mem[64] + 320]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'Rule evaluated to false'
      [94midx = [94midx + 1
      continue 


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


