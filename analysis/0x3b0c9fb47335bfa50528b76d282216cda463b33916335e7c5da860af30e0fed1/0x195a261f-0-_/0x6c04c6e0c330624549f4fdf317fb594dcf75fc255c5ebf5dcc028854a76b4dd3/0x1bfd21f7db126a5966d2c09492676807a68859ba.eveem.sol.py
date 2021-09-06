# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1Bfd21f7db126a5966d2C09492676807a68859Ba 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x316a750e': 'unknown316a750e(?)', '0xe9804c2b': 'assetInformation(address _param1)', '0xf34ada68': 'unknownf34ada68(?)'} 

# storage definitions
def storage:
    # storage address 0
    authorityAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    name
    # storage address 3
    registeredAssets
    # storage address 4
    unknown6e1a19e3
    # storage address 5
    unknown8d56e43c
    # storage address 6
    unknown697c5364
    # storage address 7
    unknown40fd0d19
    # storage address 8
    stor8
    # storage address 9
    unknownd2b048ab
    # storage address 10
    stor10
    # storage address 11
    unknown32b34f99
    # storage address 12
    unknown1d4632ac # mask: a s
    # storage address 13
    unknown20531bc9Address # mask: a s
    # storage address 14
    unknown8a471df9Address # mask: a s
    # storage address 15
    unknown74d32ad4Address # mask: a s
    # storage address 16
    unknownc9d4623fAddress # mask: a s
    # storage address 17
    unknown5769fc33Address # mask: a s
    # storage address 18
    unknownaa8862baAddress # mask: a s
    # storage address 1546678032441257452667456735582814959992782782816731922691272282333561699760
    stor1546678032441257452667456735582814959992782782816731922691272282333561699760
# hash = 0x0129df11
# getter = None
# const = None
# payable = False
def unknown0129df11(uint256 _param1): # not payable
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
  unknown1d4632ac = _param1
  log 0x4d934cb6: _param1


# hash = 0x03e45bbf
# getter = None
# const = None
# payable = False
def unknown03e45bbf(addr _param1, addr _param2, array _param3): # not payable
  mem[0] = caller
  mem[32] = 6
  if not uint8(unknown697c5364[caller].field_0):
      revert with 0, 'Only a Version can do this'
  mem[64] = ceil32(_param3.length) + 128
  mem[96] = _param3.length
  mem[128 len _param3.length] = _param3[all]
  mem[ceil32(_param3.length) + 128 len floor32(_param3.length)] = call.data[_param3 + 36 len floor32(_param3.length)]
  mem[ceil32(_param3.length) + floor32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32] = mem[floor32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32]
  if _param3.length > 66:
      revert with 0, 'Fund name cannot be used'
  [94ms = 0
  [94midx = 0
  while [94midx < _param3.length:
      require [94midx < _param3.length
      if Mask(8, 248, mem[[94midx + 128]) < '0':
          if Mask(8, 248, mem[[94midx + 128]) < 'A':
              if Mask(8, 248, mem[[94midx + 128]) < 'a':
                  if Mask(8, 248, mem[[94midx + 128]) != ' ':
                      if Mask(8, 248, mem[[94midx + 128]) != '-':
                          if Mask(8, 248, mem[[94midx + 128]) != '.':
                              if Mask(8, 248, mem[[94midx + 128]) != '_':
                                  if Mask(8, 248, mem[[94midx + 128]) != '*':
                                      revert with 0, 'Fund name cannot be used'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) > 'z':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
          else:
              if Mask(8, 248, mem[[94midx + 128]) > 'Z':
                  if Mask(8, 248, mem[[94midx + 128]) < 'a':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) > 'z':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
      else:
          if Mask(8, 248, mem[[94midx + 128]) > '9':
              if Mask(8, 248, mem[[94midx + 128]) < 'A':
                  if Mask(8, 248, mem[[94midx + 128]) < 'a':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) > 'z':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) > 'Z':
                      if Mask(8, 248, mem[[94midx + 128]) < 'a':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) > 'z':
                              if Mask(8, 248, mem[[94midx + 128]) != ' ':
                                  if Mask(8, 248, mem[[94midx + 128]) != '-':
                                      if Mask(8, 248, mem[[94midx + 128]) != '.':
                                          if Mask(8, 248, mem[[94midx + 128]) != '_':
                                              if Mask(8, 248, mem[[94midx + 128]) != '*':
                                                  revert with 0, 'Fund name cannot be used'
      [94ms = Mask(8, 248, mem[[94midx + 128])
      [94midx = [94midx + 1
      continue 
  if unknown32b34f99[call.data[_param3 + 36 len floor32(_param3.length)]][mem[ceil32(_param3.length) + floor32(_param3.length) + 128 len _param3.length % 32]]:
      if unknown32b34f99[call.data[_param3 + 36 len floor32(_param3.length)]][mem[ceil32(_param3.length) + floor32(_param3.length) + 128 len _param3.length % 32]] != _param2:
          revert with 0, 'Fund name cannot be used'
  unknownd2b048ab[addr(_param1)] = caller


# hash = 0x0e830e49
# getter = None
# const = None
# payable = False
def unknown0e830e49(addr _param1): # not payable
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
  unknownc9d4623fAddress = _param1
  log 0x24a2ad1b: _param1


# hash = 0x1104ca92
# getter = None
# const = ['return', 20]
# payable = False
const unknown1104ca92 = 20


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


# hash = 0x18e467f7
# getter = None
# const = None
# payable = False
def unknown18e467f7(addr _param1, uint256 _param2): # not payable
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
  if uint8(unknown697c5364[addr(_param1)].field_0):
      revert with 0, 'Version already exists'
  if stor10[_param2]:
      revert with 0, 'Version name already exists'
  uint8(unknown697c5364[addr(_param1)].field_0) = 1
  stor10[_param2] = 1
  unknown697c5364[addr(_param1)].field_256 = _param2
  unknown40fd0d19.length++
  addr(unknown40fd0d19[unknown40fd0d19.length].field_0) = _param1
  log 0xcd234f73: _param1


# hash = 0x1d4632ac
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown1d4632ac(): # not payable
  return unknown1d4632ac


# hash = 0x1e663d02
# getter = None
# const = None
# payable = False
def unknown1e663d02(addr _param1, array _param2): # not payable
  mem[64] = ceil32(_param2.length) + 128
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  mem[ceil32(_param2.length) + 128 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
  mem[ceil32(_param2.length) + floor32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32] = mem[floor32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32]
  if _param2.length > 66:
      return 0
  [94ms = 0
  [94midx = 0
  while [94midx < _param2.length:
      require [94midx < _param2.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'A':
          if Mask(8, 248, mem[[94midx + 128]) <= 'Z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'a':
          if Mask(8, 248, mem[[94midx + 128]) <= 'z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) == ' ':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '-':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '.':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '_':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '*':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      else:
          return 0
  if unknown32b34f99[call.data[_param2 + 36 len floor32(_param2.length)]][mem[ceil32(_param2.length) + floor32(_param2.length) + 128 len _param2.length % 32]]:
      return (unknown32b34f99[call.data[_param2 + 36 len floor32(_param2.length)]][mem[ceil32(_param2.length) + floor32(_param2.length) + 128 len _param2.length % 32]] == _param1)
  mem[ceil32(_param2.length) + 128] = not bool(unknown32b34f99[call.data[_param2 + 36 len floor32(_param2.length)]][mem[ceil32(_param2.length) + floor32(_param2.length) + 128 len _param2.length % 32]])
  return memory
    from ceil32(_param2.length) + 128
     [93mlen 32


# hash = 0x1f8d99a9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def assetIsRegistered(address _ofAsset): # not payable
  return bool(uint8(name[addr(_ofAsset)].field_0))


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return unknown20531bc9Address


# hash = 0x2317ef67
# getter = None
# const = None
# payable = False
def removeAsset(address _ofAsset, uint256 _assetIndex): # not payable
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
  require uint8(name[addr(_ofAsset)].field_0)
  require _assetIndex < registeredAssets.length
  require addr(registeredAssets[_assetIndex].field_0) == _ofAsset
  uint8(name[addr(_ofAsset)].field_0) = 0
  name[addr(_ofAsset)].field_256 = 0
  if 31 < name[addr(_ofAsset)][1].length:
      [94midx = 0
      while name[addr(_ofAsset)][1].length + 31 / 32 > [94midx:
          name[addr(_ofAsset)][[94midx + 1].field_0 = 0
          [94midx = [94midx + 1
          continue 
  name[addr(_ofAsset)].field_512 = 0
  if 31 < name[addr(_ofAsset)][2].length:
      [94midx = 0
      while name[addr(_ofAsset)][2].length + 31 / 32 > [94midx:
          name[addr(_ofAsset)][[94midx + 2].field_0 = 0
          [94midx = [94midx + 1
          continue 
  name[addr(_ofAsset)].field_768 = 0
  name[addr(_ofAsset)].field_1024 = 0
  if 31 < name[addr(_ofAsset)][4].length:
      [94midx = 0
      while name[addr(_ofAsset)][4].length + 31 / 32 > [94midx:
          name[addr(_ofAsset)][[94midx + 4].field_0 = 0
          [94midx = [94midx + 1
          continue 
  name[addr(_ofAsset)].field_1280 = 0
  name[addr(_ofAsset)].field_1536 = 0
  [94midx = 0
  while name[addr(_ofAsset)].field_1536 > [94midx:
      name[addr(_ofAsset)][[94midx + 6].field_0 = 0
      [94midx = [94midx + 1
      continue 
  name[addr(_ofAsset)].field_1792 = 0
  [94midx = 0
  while name[addr(_ofAsset)].field_1792 + 7 / 8 > [94midx:
      name[addr(_ofAsset)][[94midx + 7].field_0 = 0
      [94midx = [94midx + 1
      continue 
  require _assetIndex < registeredAssets.length
  addr(registeredAssets[_assetIndex].field_0) = 0
  [94midx = _assetIndex
  while [94midx < registeredAssets.length - 1:
      require [94midx + 1 < registeredAssets.length
      require [94midx < registeredAssets.length
      mem[0] = 3
      addr(registeredAssets[[94midx].field_0) = addr(registeredAssets[[94midx].field_256)
      [94midx = [94midx + 1
      continue 
  registeredAssets.length--
  if registeredAssets.length > registeredAssets.length - 1:
      [94midx = registeredAssets.length - 1
      while registeredAssets.length > [94midx:
          registeredAssets[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  log 0x78c7527d: _ofAsset


# hash = 0x24da4f19
# getter = None
# const = None
# payable = False
def unknown24da4f19(): # not payable
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
  [94midx = 0
  while [94midx < ('cd', 4).length:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 8
      stor8[addr(cd[((32 * [94midx) + cd[4] + 36)])] = 1
      [94midx = [94midx + 1
      continue 


# hash = 0x32b34f99
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 11]]]
# const = None
# payable = False
def unknown32b34f99(uint256 _param1): # not payable
  return unknown32b34f99[_param1]


# hash = 0x33394ca8
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]]
# const = None
# payable = False
def unknown33394ca8(addr _param1): # not payable
  return bool(uint8(unknown6e1a19e3[addr(_param1)].field_0))


# hash = 0x336790fa
# getter = None
# const = None
# payable = False
def unknown336790fa(addr _param1, addr _param2, bool _param3, array _param4): # not payable
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[100] = caller
          mem[132] = this.address
          mem[164] = call.func_hash
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if uint8(unknown6e1a19e3[addr(_param2)].field_0):
      revert with 0, 'Adapter already exists'
  uint8(unknown6e1a19e3[addr(_param2)].field_0) = 1
  if 20 <= unknown8d56e43c.length:
      revert with 0, 'Exchange limit reached'
  unknown8d56e43c.length++
  stor36B6[stor5.length] = _param2
  mem[128 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[(32 * _param4.length) + 196] = call.func_hash
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          mem[(32 * _param4.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not uint8(unknown6e1a19e3[addr(_param2)].field_0):
      revert with 0, 'Exchange with adapter doesn't exist'
  addr(unknown6e1a19e3[addr(_param2)].field_8) = _param1
  Mask(88, 0, unknown6e1a19e3[addr(_param2)].field_168) = Mask(88, 0, _param3)
  Mask(80, 0, unknown6e1a19e3[addr(_param2)].field_176) = 0
  unknown6e1a19e3[addr(_param2)].field_256 = _param4.length
  if not _param4.length:
      [94midx = 0
      while unknown6e1a19e3[addr(_param2)].field_256 + 7 / 8 > [94midx:
          uint32(unknown6e1a19e3[addr(_param2)][[94midx + 1].field_0) = 0
          [94midx = [94midx + 1
          continue 
  else:
      [94ms = 0
      [94midx = 128
      while (32 * _param4.length) + 128 > [94midx:
          unknown6e1a19e3[addr(_param2)][1].field_0 = mem[[94midx len 4] * 256^[94ms or !(4294967295 * 256^[94ms) and unknown6e1a19e3[addr(_param2)][1].field_0
          [94ms = [94ms + (4 * -[94ms + 7 / 32) + (-1 * [94ms * [94ms + 7 / 32) + 4
          [94midx = [94midx + 32
          continue 
      [94midx = floor32(_param4.length) >> 3
      [94ms = sha3(sha3(addr(_param2), 4) + 1)
      while [94midx:
          stor[[94ms] = !(4294967295 * 256^[94midx) and stor[[94ms]
          [94midx = [94midx + (4 * -[94midx + 7 / 32) + (-1 * [94midx * [94midx + 7 / 32) + 4
          [94ms = ([94midx + 7 / 32) + [94ms
          continue 
      [94midx = (floor32(_param4.length) >> 3) + Mask(252, 2, None + -(floor32(_param4.length) >> 3) + 5) + 7 / 32 * Mask(254, 0, None + -(floor32(_param4.length) >> 3) + 5) >> 2
      while unknown6e1a19e3[addr(_param2)].field_256 + 7 / 8 > [94midx:
          uint32(unknown6e1a19e3[addr(_param2)][[94midx + 1].field_0) = 0
          [94midx = [94midx + 1
          continue 
  mem[(32 * _param4.length) + 224 len floor32(_param4.length)] = call.data[_param4 + 36 len floor32(_param4.length)]
  log 0x4d38780a: _param3, Array(len=_param4.length, data=call.data[_param4 + 36 len floor32(_param4.length)], mem[(32 * _param4.length) + floor32(_param4.length) + 224 len (32 * _param4.length) - floor32(_param4.length)]), _param1, _param2


# hash = 0x37401e97
# getter = None
# const = None
# payable = False
def unknown37401e97(addr _param1): # not payable
  if not unknown6e1a19e3[addr(_param1)].field_256:
      mem[(32 * unknown6e1a19e3[addr(_param1)].field_256) + 128] = 32
      mem[(32 * unknown6e1a19e3[addr(_param1)].field_256) + 160] = unknown6e1a19e3[addr(_param1)].field_256
      mem[(32 * unknown6e1a19e3[addr(_param1)].field_256) + 192 len floor32(unknown6e1a19e3[addr(_param1)].field_256)] = mem[128 len floor32(unknown6e1a19e3[addr(_param1)].field_256)]
      return memory
        from (32 * unknown6e1a19e3[addr(_param1)].field_256) + 128
         [93mlen (96 * unknown6e1a19e3[addr(_param1)].field_256) + 64
  mem[128] = unknown6e1a19e3[addr(_param1)][1].field_0 / 256^0 << 224
  [94midx = 128
  [94ms = 0
  while (32 * unknown6e1a19e3[addr(_param1)].field_256) + 96 > [94midx:
      mem[[94midx + 32] = unknown6e1a19e3[addr(_param1)][1].field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
      [94midx = [94midx + 32
      [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
      continue 
  mem[(32 * unknown6e1a19e3[addr(_param1)].field_256) + 192 len floor32(unknown6e1a19e3[addr(_param1)].field_256)] = mem[128 len floor32(unknown6e1a19e3[addr(_param1)].field_256)]
  return Array(len=unknown6e1a19e3[addr(_param1)].field_256, data=mem[128 len floor32(unknown6e1a19e3[addr(_param1)].field_256)], mem[(32 * unknown6e1a19e3[addr(_param1)].field_256) + floor32(unknown6e1a19e3[addr(_param1)].field_256) + 192 len (32 * unknown6e1a19e3[addr(_param1)].field_256) - floor32(unknown6e1a19e3[addr(_param1)].field_256)]), 


# hash = 0x38f68e91
# getter = None
# const = None
# payable = False
def unknown38f68e91(addr _param1, addr _param2, bool _param3, array _param4): # not payable
  mem[128 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[(32 * _param4.length) + 196] = call.func_hash
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, call.func_hash
          mem[(32 * _param4.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not uint8(unknown6e1a19e3[addr(_param2)].field_0):
      revert with 0, 'Exchange with adapter doesn't exist'
  addr(unknown6e1a19e3[addr(_param2)].field_8) = _param1
  Mask(88, 0, unknown6e1a19e3[addr(_param2)].field_168) = Mask(88, 0, _param3)
  Mask(80, 0, unknown6e1a19e3[addr(_param2)].field_176) = 0
  unknown6e1a19e3[addr(_param2)].field_256 = _param4.length
  if not _param4.length:
      [94midx = 0
      while unknown6e1a19e3[addr(_param2)].field_256 + 7 / 8 > [94midx:
          uint32(unknown6e1a19e3[addr(_param2)][[94midx + 1].field_0) = 0
          [94midx = [94midx + 1
          continue 
  else:
      [94ms = 0
      [94midx = 128
      while (32 * _param4.length) + 128 > [94midx:
          unknown6e1a19e3[addr(_param2)][1].field_0 = mem[[94midx len 4] * 256^[94ms or !(4294967295 * 256^[94ms) and unknown6e1a19e3[addr(_param2)][1].field_0
          [94ms = [94ms + (4 * -[94ms + 7 / 32) + (-1 * [94ms * [94ms + 7 / 32) + 4
          [94midx = [94midx + 32
          continue 
      [94midx = floor32(_param4.length) >> 3
      [94ms = sha3(sha3(addr(_param2), 4) + 1)
      while [94midx:
          stor[[94ms] = !(4294967295 * 256^[94midx) and stor[[94ms]
          [94midx = [94midx + (4 * -[94midx + 7 / 32) + (-1 * [94midx * [94midx + 7 / 32) + 4
          [94ms = ([94midx + 7 / 32) + [94ms
          continue 
      [94midx = (floor32(_param4.length) >> 3) + Mask(252, 2, None + -(floor32(_param4.length) >> 3) + 5) + 7 / 32 * Mask(254, 0, None + -(floor32(_param4.length) >> 3) + 5) >> 2
      while unknown6e1a19e3[addr(_param2)].field_256 + 7 / 8 > [94midx:
          uint32(unknown6e1a19e3[addr(_param2)][[94midx + 1].field_0) = 0
          [94midx = [94midx + 1
          continue 
  mem[(32 * _param4.length) + 224 len floor32(_param4.length)] = call.data[_param4 + 36 len floor32(_param4.length)]
  log 0x4d38780a: _param3, Array(len=_param4.length, data=call.data[_param4 + 36 len floor32(_param4.length)], mem[(32 * _param4.length) + floor32(_param4.length) + 224 len (32 * _param4.length) - floor32(_param4.length)]), _param1, _param2


# hash = 0x40fd0d19
# getter = ['storage', 160, 0, ['add', ['sha3', 7], ['cd', 4]]]
# const = None
# payable = False
def unknown40fd0d19(uint256 _param1): # not payable
  require _param1 < unknown40fd0d19.length
  return addr(unknown40fd0d19[_param1].field_0)


# hash = 0x41b80b0e
# getter = None
# const = None
# payable = False
def unknown41b80b0e(): # not payable
  if not unknown8d56e43c.length:
      mem[(32 * unknown8d56e43c.length) + 128] = 32
      mem[(32 * unknown8d56e43c.length) + 160] = unknown8d56e43c.length
      mem[(32 * unknown8d56e43c.length) + 192 len floor32(unknown8d56e43c.length)] = mem[128 len floor32(unknown8d56e43c.length)]
      return memory
        from (32 * unknown8d56e43c.length) + 128
         [93mlen (96 * unknown8d56e43c.length) + 64
  mem[128] = addr(unknown8d56e43c.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknown8d56e43c.length) + 96 > [94midx:
      mem[[94midx + 32] = addr(unknown8d56e43c[[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown8d56e43c.length) + 192 len floor32(unknown8d56e43c.length)] = mem[128 len floor32(unknown8d56e43c.length)]
  return Array(len=unknown8d56e43c.length, data=mem[128 len floor32(unknown8d56e43c.length)], mem[(32 * unknown8d56e43c.length) + floor32(unknown8d56e43c.length) + 192 len (32 * unknown8d56e43c.length) - floor32(unknown8d56e43c.length)]), 


# hash = 0x56701d46
# getter = None
# const = None
# payable = False
def unknown56701d46(array _param1): # not payable
  mem[64] = ceil32(_param1.length) + 128
  mem[96] = _param1.length
  mem[128 len _param1.length] = _param1[all]
  if _param1.length > 66:
      return 0
  [94ms = 0
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'A':
          if Mask(8, 248, mem[[94midx + 128]) <= 'Z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'a':
          if Mask(8, 248, mem[[94midx + 128]) <= 'z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              continue 
      if Mask(8, 248, mem[[94midx + 128]) == ' ':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '-':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '.':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '_':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) == '*':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          continue 
      else:
          return 0
  return 1


# hash = 0x5769fc33
# getter = ['storage', 160, 0, 17]
# const = None
# payable = False
def unknown5769fc33(): # not payable
  return unknown5769fc33Address


# hash = 0x5fd4b08a
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 1, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]], ['add', 1, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def getName(address _address): # not payable
  return name[addr(_address)][1][0 len name[addr(_address)][1].length].field_0


# hash = 0x63a65847
# getter = None
# const = None
# payable = False
def unknown63a65847(): # not payable
  if unknown40fd0d19.length:
      mem[128] = addr(unknown40fd0d19.field_0)
      if (32 * unknown40fd0d19.length) + 32 > 64:
          mem[160] = addr(unknown40fd0d19.field_256)
          [94midx = 160
          [94ms = 1
          while (32 * unknown40fd0d19.length) + 96 > [94midx:
              mem[[94midx + 32] = addr(unknown40fd0d19[[94ms].field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  mem[(32 * unknown40fd0d19.length) + 128] = 32
  mem[(32 * unknown40fd0d19.length) + 160] = unknown40fd0d19.length
  mem[(32 * unknown40fd0d19.length) + 192 len floor32(unknown40fd0d19.length)] = mem[128 len floor32(unknown40fd0d19.length)]
  return memory
    from (32 * unknown40fd0d19.length) + 128
     [93mlen (96 * unknown40fd0d19.length) + 64


# hash = 0x671521e8
# getter = None
# const = None
# payable = False
def unknown671521e8(addr _param1): # not payable
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
  unknown74d32ad4Address = _param1
  log 0x2c58ddee: _param1


# hash = 0x68171516
# getter = None
# const = None
# payable = False
def assetMethodIsAllowed(address _ofAsset, bytes4 _querySignature): # not payable
  if name[addr(_ofAsset)].field_1792:
      mem[128] = name[addr(_ofAsset)][7].field_0 / 256^0 << 224
      [94midx = 128
      [94ms = 0
      while (32 * name[addr(_ofAsset)].field_1792) + 96 > [94midx:
          mem[[94midx + 32] = name[addr(_ofAsset)][7].field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
          [94midx = [94midx + 32
          [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
          continue 
  [94midx = 0
  while [94midx < name[addr(_ofAsset)].field_1792:
      require [94midx < name[addr(_ofAsset)].field_1792
      if Mask(32, 224, mem[(32 * [94midx) + 128]) != Mask(32, 224, _querySignature):
          [94midx = [94midx + 1
          continue 
      return 1
  return 0


# hash = 0x697c5364
# getter = ['struct', ['loc', 6]]
# const = None
# payable = False
def unknown697c5364(addr _param1): # not payable
  return bool(uint8(unknown697c5364[_param1].field_0)), unknown697c5364[_param1].field_256


# hash = 0x6e1a19e3
# getter = ['storage', 160, 8, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]
# const = None
# payable = False
def unknown6e1a19e3(addr _param1): # not payable
  return addr(unknown6e1a19e3[addr(_param1)].field_8)


# hash = 0x6ff76de1
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 8]]]]
# const = None
# payable = False
def unknown6ff76de1(addr _param1): # not payable
  return bool(stor8[_param1])


# hash = 0x74d32ad4
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def unknown74d32ad4(): # not payable
  return unknown74d32ad4Address


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


# hash = 0x7f2309ba
# getter = None
# const = ['return', 66]
# payable = False
const unknown7f2309ba = 66


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return unknown8a471df9Address


# hash = 0x8b522db9
# getter = None
# const = None
# payable = False
def unknown8b522db9(addr _param1): # not payable
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
  unknown5769fc33Address = _param1
  log 0x80f7a2a1: _param1


# hash = 0x8d56e43c
# getter = ['storage', 160, 0, ['add', ['sha3', 5], ['cd', 4]]]
# const = None
# payable = False
def unknown8d56e43c(uint256 _param1): # not payable
  require _param1 < unknown8d56e43c.length
  return addr(unknown8d56e43c[_param1].field_0)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9b8ce78f
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]]
# const = None
# payable = False
def unknown9b8ce78f(addr _param1): # not payable
  return bool(uint8(unknown697c5364[addr(_param1)].field_0))


# hash = 0x9e0a4570
# getter = None
# const = None
# payable = False
def unknown9e0a4570(addr _param1): # not payable
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
  unknown8a471df9Address = _param1
  log 0x46adb525: _param1


# hash = 0xa083bd3c
# getter = ['storage', 160, 0, ['add', ['sha3', 3], ['cd', 4]]]
# const = None
# payable = False
def registeredAssets(uint256 _param1): # not payable
  require _param1 < registeredAssets.length
  return addr(registeredAssets[_param1].field_0)


# hash = 0xa419c615
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def exchangeInformation(address _param1): # not payable
  return bool(uint8(unknown6e1a19e3[_param1].field_0)), 
         addr(unknown6e1a19e3[_param1].field_0),
         bool(uint8(unknown6e1a19e3[_param1].field_168))


# hash = 0xaa8862ba
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def unknownaa8862ba(): # not payable
  return unknownaa8862baAddress


# hash = 0xbda53107
# getter = None
# const = None
# payable = False
def unknownbda53107(addr _param1): # not payable
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
  unknown20531bc9Address = _param1
  log 0xbe4a9fa8: _param1


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return authorityAddress


# hash = 0xc35d8621
# getter = None
# const = None
# payable = False
def unknownc35d8621(addr _param1): # not payable
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
  unknownaa8862baAddress = _param1
  log 0x7bab9795: _param1


# hash = 0xc7153b89
# getter = None
# const = None
# payable = False
def unknownc7153b89(addr _param1): # not payable
  if unknownd2b048ab[addr(_param1)]:
      return 1
  require ext_code.size(_param1)
  call _param1.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x3957a225 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Call from either a spoke or hub'
  return bool(unknownd2b048ab[addr(ext_call.return_data[0])])


# hash = 0xc9b2e522
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]], ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def getSymbol(address _ofAsset): # not payable
  return name[addr(_ofAsset)][2][0 len name[addr(_ofAsset)][2].length].field_0


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 16]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return unknownc9d4623fAddress


# hash = 0xcf54aaa0
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def getDecimals(address _token): # not payable
  return name[addr(_token)].field_768


# hash = 0xcf5cb132
# getter = None
# const = None
# payable = False
def getRegisteredAssets(): # not payable
  if registeredAssets.length:
      mem[128] = addr(registeredAssets.field_0)
      if (32 * registeredAssets.length) + 32 > 64:
          mem[160] = addr(registeredAssets.field_256)
          [94midx = 160
          [94ms = 1
          while (32 * registeredAssets.length) + 96 > [94midx:
              mem[[94midx + 32] = addr(registeredAssets[[94ms].field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  mem[(32 * registeredAssets.length) + 128] = 32
  mem[(32 * registeredAssets.length) + 160] = registeredAssets.length
  mem[(32 * registeredAssets.length) + 192 len floor32(registeredAssets.length)] = mem[128 len floor32(registeredAssets.length)]
  return memory
    from (32 * registeredAssets.length) + 128
     [93mlen (96 * registeredAssets.length) + 64


# hash = 0xd2b048ab
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknownd2b048ab(addr _param1): # not payable
  return unknownd2b048ab[_param1]


# hash = 0xd6abbf0a
# getter = None
# const = None
# payable = False
def unknownd6abbf0a(addr _param1, array _param2): # not payable
  mem[0] = caller
  mem[32] = 6
  if not uint8(unknown697c5364[caller].field_0):
      revert with 0, 'Only a Version can do this'
  mem[64] = ceil32(_param2.length) + 128
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  mem[ceil32(_param2.length) + 128 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
  mem[ceil32(_param2.length) + floor32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32] = mem[floor32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32]
  if _param2.length > 66:
      revert with 0, 'Fund name cannot be used'
  [94ms = 0
  [94midx = 0
  while [94midx < _param2.length:
      require [94midx < _param2.length
      if Mask(8, 248, mem[[94midx + 128]) < '0':
          if Mask(8, 248, mem[[94midx + 128]) < 'A':
              if Mask(8, 248, mem[[94midx + 128]) < 'a':
                  if Mask(8, 248, mem[[94midx + 128]) != ' ':
                      if Mask(8, 248, mem[[94midx + 128]) != '-':
                          if Mask(8, 248, mem[[94midx + 128]) != '.':
                              if Mask(8, 248, mem[[94midx + 128]) != '_':
                                  if Mask(8, 248, mem[[94midx + 128]) != '*':
                                      revert with 0, 'Fund name cannot be used'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) > 'z':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
          else:
              if Mask(8, 248, mem[[94midx + 128]) > 'Z':
                  if Mask(8, 248, mem[[94midx + 128]) < 'a':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) > 'z':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
      else:
          if Mask(8, 248, mem[[94midx + 128]) > '9':
              if Mask(8, 248, mem[[94midx + 128]) < 'A':
                  if Mask(8, 248, mem[[94midx + 128]) < 'a':
                      if Mask(8, 248, mem[[94midx + 128]) != ' ':
                          if Mask(8, 248, mem[[94midx + 128]) != '-':
                              if Mask(8, 248, mem[[94midx + 128]) != '.':
                                  if Mask(8, 248, mem[[94midx + 128]) != '_':
                                      if Mask(8, 248, mem[[94midx + 128]) != '*':
                                          revert with 0, 'Fund name cannot be used'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) > 'z':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) > 'Z':
                      if Mask(8, 248, mem[[94midx + 128]) < 'a':
                          if Mask(8, 248, mem[[94midx + 128]) != ' ':
                              if Mask(8, 248, mem[[94midx + 128]) != '-':
                                  if Mask(8, 248, mem[[94midx + 128]) != '.':
                                      if Mask(8, 248, mem[[94midx + 128]) != '_':
                                          if Mask(8, 248, mem[[94midx + 128]) != '*':
                                              revert with 0, 'Fund name cannot be used'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) > 'z':
                              if Mask(8, 248, mem[[94midx + 128]) != ' ':
                                  if Mask(8, 248, mem[[94midx + 128]) != '-':
                                      if Mask(8, 248, mem[[94midx + 128]) != '.':
                                          if Mask(8, 248, mem[[94midx + 128]) != '_':
                                              if Mask(8, 248, mem[[94midx + 128]) != '*':
                                                  revert with 0, 'Fund name cannot be used'
      [94ms = Mask(8, 248, mem[[94midx + 128])
      [94midx = [94midx + 1
      continue 
  if unknown32b34f99[call.data[_param2 + 36 len floor32(_param2.length)]][mem[ceil32(_param2.length) + floor32(_param2.length) + 128 len _param2.length % 32]]:
      if unknown32b34f99[call.data[_param2 + 36 len floor32(_param2.length)]][mem[ceil32(_param2.length) + floor32(_param2.length) + 128 len _param2.length % 32]] != _param1:
          revert with 0, 'Fund name cannot be used'
  unknown32b34f99[_param2[all]] = _param1


# hash = 0xd737c4b9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 10]]]]
# const = None
# payable = False
def unknownd737c4b9(uint256 _param1): # not payable
  return bool(stor10[_param1])


# hash = 0xe2a1b398
# getter = None
# const = None
# payable = False
def unknowne2a1b398(): # not payable
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
  [94midx = 0
  while [94midx < ('cd', 4).length:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 8
      stor8[addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
      [94midx = [94midx + 1
      continue 


# hash = 0xe46c871c
# getter = None
# const = None
# payable = False
def unknowne46c871c(addr _param1, uint32 _param2): # not payable
  if unknown6e1a19e3[addr(_param1)].field_256:
      mem[128] = unknown6e1a19e3[addr(_param1)][1].field_0 / 256^0 << 224
      [94midx = 128
      [94ms = 0
      while (32 * unknown6e1a19e3[addr(_param1)].field_256) + 96 > [94midx:
          mem[[94midx + 32] = unknown6e1a19e3[addr(_param1)][1].field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
          [94midx = [94midx + 32
          [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
          continue 
  [94midx = 0
  while [94midx < unknown6e1a19e3[addr(_param1)].field_256:
      require [94midx < unknown6e1a19e3[addr(_param1)].field_256
      if Mask(32, 224, mem[(32 * [94midx) + 128]) != Mask(32, 224, _param2):
          [94midx = [94midx + 1
          continue 
      return 1
  return 0


# hash = 0xf31507df
# getter = None
# const = None
# payable = False
def unknownf31507df(addr _param1, uint256 _param2): # not payable
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
  if not uint8(unknown6e1a19e3[addr(_param1)].field_0):
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Exchange with adapter doesn't exist'
  require _param2 < unknown8d56e43c.length
  if addr(unknown8d56e43c[_param2].field_0) != _param1:
      revert with 0, 'Incorrect adapter index'
  Mask(176, 0, unknown6e1a19e3[addr(_param1)].field_0) = 0
  unknown6e1a19e3[addr(_param1)].field_256 = 0
  [94midx = 0
  while unknown6e1a19e3[addr(_param1)].field_256 + 7 / 8 > [94midx:
      unknown6e1a19e3[addr(_param1)][[94midx + 1].field_0 = 0
      [94midx = [94midx + 1
      continue 
  require _param2 < unknown8d56e43c.length
  addr(unknown8d56e43c[_param2].field_0) = 0
  [94midx = _param2
  while [94midx < unknown8d56e43c.length - 1:
      require [94midx + 1 < unknown8d56e43c.length
      require [94midx < unknown8d56e43c.length
      mem[0] = 5
      addr(unknown8d56e43c[[94midx].field_0) = addr(unknown8d56e43c[[94midx].field_256)
      [94midx = [94midx + 1
      continue 
  unknown8d56e43c.length--
  if unknown8d56e43c.length > unknown8d56e43c.length - 1:
      [94midx = unknown8d56e43c.length - 1
      while unknown8d56e43c.length > [94midx:
          unknown8d56e43c[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  log 0xc7e5f770: _param1


# hash = 0xf4196b63
# getter = ['storage', 256, 0, ['add', 5, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def unknownf4196b63(addr _param1): # not payable
  return name[addr(_param1)].field_1280


# hash = 0xfe68b528
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def getExchangeInformation(address _ofExchange): # not payable
  return addr(unknown6e1a19e3[addr(_ofExchange)].field_0), bool(uint8(unknown6e1a19e3[addr(_ofExchange)].field_168))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


