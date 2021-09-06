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
def unknown0129df11(uint256 m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknown1d4632ac = m_param1
  log 0x4d934cb6: _param1


# hash = 0x03e45bbf
# getter = None
# const = None
# payable = False
def unknown03e45bbf(addr m_param1, addr m_param2, array m_param3): # not payable
  mem[0] = caller
  mem[32] = 6
  if not uint8(munknown697c5364m[callerm]m.field_0):
      revert with 0, 'Only a Version can do this'
  mem[64] = ceil32(m_param3.length) + 128
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[ceil32(m_param3.length) + 128 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[ceil32(m_param3.length) + floor32(m_param3.length) + -(m_param3.length % 32) + 160 len m_param3.length % 32] = mem[floor32(m_param3.length) + -(m_param3.length % 32) + 160 len m_param3.length % 32]
  if m_param3.length > 66:
      revert with 0, 'Fund name cannot be used'
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m_param3.lengthm:
      require [94midx < m_param3.length
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
      mcontinue 
  if munknown32b34f99m[call.data[m_param3 + 36 len floor32(m_param3.length)]m][mem[ceil32(m_param3.length) + floor32(m_param3.length) + 128 len m_param3.length % 32]m]:
      if munknown32b34f99m[call.data[m_param3 + 36 len floor32(m_param3.length)]m][mem[ceil32(m_param3.length) + floor32(m_param3.length) + 128 len m_param3.length % 32]m] != m_param2:
          revert with 0, 'Fund name cannot be used'
  munknownd2b048abm[addr(m_param1)m] = caller


# hash = 0x0e830e49
# getter = None
# const = None
# payable = False
def unknown0e830e49(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknownc9d4623fAddress = m_param1
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
def setOwner(address m_newOwner): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mowner = m_newOwner
  log LogSetOwner(address owner=_newOwner)


# hash = 0x18e467f7
# getter = None
# const = None
# payable = False
def unknown18e467f7(addr m_param1, uint256 m_param2): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if uint8(munknown697c5364m[addr(m_param1)m]m.field_0):
      revert with 0, 'Version already exists'
  if mstor10m[m_param2m]:
      revert with 0, 'Version name already exists'
  uint8(munknown697c5364m[addr(m_param1)m]m.field_0) = 1
  mstor10m[m_param2m] = 1
  munknown697c5364m[addr(m_param1)m]m.field_256 = m_param2
  munknown40fd0d19m.length++
  addr(munknown40fd0d19m[munknown40fd0d19m.lengthm]m.field_0) = m_param1
  log 0xcd234f73: _param1


# hash = 0x1d4632ac
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown1d4632ac(): # not payable
  return munknown1d4632ac


# hash = 0x1e663d02
# getter = None
# const = None
# payable = False
def unknown1e663d02(addr m_param1, array m_param2): # not payable
  mem[64] = ceil32(m_param2.length) + 128
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[ceil32(m_param2.length) + 128 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[ceil32(m_param2.length) + floor32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32] = mem[floor32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32]
  if m_param2.length > 66:
      return 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'A':
          if Mask(8, 248, mem[[94midx + 128]) <= 'Z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'a':
          if Mask(8, 248, mem[[94midx + 128]) <= 'z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == ' ':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '-':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '.':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '_':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '*':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      else:
          return 0
  if munknown32b34f99m[call.data[m_param2 + 36 len floor32(m_param2.length)]m][mem[ceil32(m_param2.length) + floor32(m_param2.length) + 128 len m_param2.length % 32]m]:
      return (munknown32b34f99m[call.data[m_param2 + 36 len floor32(m_param2.length)]m][mem[ceil32(m_param2.length) + floor32(m_param2.length) + 128 len m_param2.length % 32]m] == m_param1)
  mem[ceil32(m_param2.length) + 128] = not bool(munknown32b34f99m[call.data[m_param2 + 36 len floor32(m_param2.length)]m][mem[ceil32(m_param2.length) + floor32(m_param2.length) + 128 len m_param2.length % 32]m])
  return memory
    from ceil32(m_param2.length) + 128
     [93mlen 32


# hash = 0x1f8d99a9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def assetIsRegistered(address m_ofAsset): # not payable
  return bool(uint8(mnamem[addr(m_ofAsset)m]m.field_0))


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return munknown20531bc9Address


# hash = 0x2317ef67
# getter = None
# const = None
# payable = False
def removeAsset(address m_ofAsset, uint256 m_assetIndex): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  require uint8(mnamem[addr(m_ofAsset)m]m.field_0)
  require m_assetIndex < mregisteredAssetsm.length
  require addr(mregisteredAssetsm[m_assetIndexm]m.field_0) == m_ofAsset
  uint8(mnamem[addr(m_ofAsset)m]m.field_0) = 0
  mnamem[addr(m_ofAsset)m]m.field_256 = 0
  if 31 < mnamem[addr(m_ofAsset)m]m[1m]m.length:
      [94midx = 0
      mwhile mnamem[addr(m_ofAsset)m]m[1m]m.length + 31 / 32 > [94midxm:
          mnamem[addr(m_ofAsset)m]m[[94midx + 1m]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mnamem[addr(m_ofAsset)m]m.field_512 = 0
  if 31 < mnamem[addr(m_ofAsset)m]m[2m]m.length:
      [94midx = 0
      mwhile mnamem[addr(m_ofAsset)m]m[2m]m.length + 31 / 32 > [94midxm:
          mnamem[addr(m_ofAsset)m]m[[94midx + 2m]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mnamem[addr(m_ofAsset)m]m.field_768 = 0
  mnamem[addr(m_ofAsset)m]m.field_1024 = 0
  if 31 < mnamem[addr(m_ofAsset)m]m[4m]m.length:
      [94midx = 0
      mwhile mnamem[addr(m_ofAsset)m]m[4m]m.length + 31 / 32 > [94midxm:
          mnamem[addr(m_ofAsset)m]m[[94midx + 4m]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mnamem[addr(m_ofAsset)m]m.field_1280 = 0
  mnamem[addr(m_ofAsset)m]m.field_1536 = 0
  [94midx = 0
  mwhile mnamem[addr(m_ofAsset)m]m.field_1536 > [94midxm:
      mnamem[addr(m_ofAsset)m]m[[94midx + 6m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  mnamem[addr(m_ofAsset)m]m.field_1792 = 0
  [94midx = 0
  mwhile mnamem[addr(m_ofAsset)m]m.field_1792 + 7 / 8 > [94midxm:
      mnamem[addr(m_ofAsset)m]m[[94midx + 7m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  require m_assetIndex < mregisteredAssetsm.length
  addr(mregisteredAssetsm[m_assetIndexm]m.field_0) = 0
  [94midx = m_assetIndex
  mwhile [94midx < mregisteredAssetsm.length - 1m:
      require [94midx + 1 < mregisteredAssetsm.length
      require [94midx < mregisteredAssetsm.length
      mem[0] = 3
      addr(mregisteredAssetsm[[94midxm]m.field_0) = addr(mregisteredAssetsm[[94midxm]m.field_256)
      [94midx = [94midx + 1
      mcontinue 
  mregisteredAssetsm.length--
  if mregisteredAssetsm.length > mregisteredAssetsm.length - 1:
      [94midx = mregisteredAssetsm.length - 1
      mwhile mregisteredAssetsm.length > [94midxm:
          mregisteredAssetsm[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  log 0x78c7527d: _ofAsset


# hash = 0x24da4f19
# getter = None
# const = None
# payable = False
def unknown24da4f19(): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 8
      mstor8m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 1
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x32b34f99
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 11]]]
# const = None
# payable = False
def unknown32b34f99(uint256 m_param1): # not payable
  return munknown32b34f99m[m_param1m]


# hash = 0x33394ca8
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]]
# const = None
# payable = False
def unknown33394ca8(addr m_param1): # not payable
  return bool(uint8(munknown6e1a19e3m[addr(m_param1)m]m.field_0))


# hash = 0x336790fa
# getter = None
# const = None
# payable = False
def unknown336790fa(addr m_param1, addr m_param2, bool m_param3, array m_param4): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[100] = caller
          mem[132] = this.address
          mem[164] = mcall.func_hash
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if uint8(munknown6e1a19e3m[addr(m_param2)m]m.field_0):
      revert with 0, 'Adapter already exists'
  uint8(munknown6e1a19e3m[addr(m_param2)m]m.field_0) = 1
  if 20 <= munknown8d56e43cm.length:
      revert with 0, 'Exchange limit reached'
  munknown8d56e43cm.length++
  mstor36B6m[mstor5m.lengthm] = m_param2
  mem[128 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[(32 * m_param4.length) + 196] = mcall.func_hash
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          mem[(32 * m_param4.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not uint8(munknown6e1a19e3m[addr(m_param2)m]m.field_0):
      revert with 0, 'Exchange with adapter doesn't exist'
  addr(munknown6e1a19e3m[addr(m_param2)m]m.field_8) = m_param1
  Mask(88, 0, munknown6e1a19e3m[addr(m_param2)m]m.field_168) = Mask(88, 0, m_param3)
  Mask(80, 0, munknown6e1a19e3m[addr(m_param2)m]m.field_176) = 0
  munknown6e1a19e3m[addr(m_param2)m]m.field_256 = m_param4.length
  if not m_param4.length:
      [94midx = 0
      mwhile munknown6e1a19e3m[addr(m_param2)m]m.field_256 + 7 / 8 > [94midxm:
          uint32(munknown6e1a19e3m[addr(m_param2)m]m[[94midx + 1m]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param4.length) + 128 > [94midxm:
          munknown6e1a19e3m[addr(m_param2)m]m[1m]m.field_0 = mem[[94midx len 4] * 256^[94ms or !(4294967295 * 256^[94ms) and munknown6e1a19e3m[addr(m_param2)m]m[1m]m.field_0
          [94ms = [94ms + (4 * -[94ms + 7 / 32) + (-1 * [94ms * [94ms + 7 / 32) + 4
          [94midx = [94midx + 32
          mcontinue 
      [94midx = floor32(m_param4.length) >> 3
      [94ms = sha3(sha3(addr(m_param2), 4) + 1)
      mwhile [94midxm:
          mstor[[94msm] = !(4294967295 * 256^[94midx) and mstor[[94msm]
          [94midx = [94midx + (4 * -[94midx + 7 / 32) + (-1 * [94midx * [94midx + 7 / 32) + 4
          [94ms = ([94midx + 7 / 32) + [94ms
          mcontinue 
      [94midx = (floor32(m_param4.length) >> 3) + Mask(252, 2, None + -(floor32(m_param4.length) >> 3) + 5) + 7 / 32 * Mask(254, 0, None + -(floor32(m_param4.length) >> 3) + 5) >> 2
      mwhile munknown6e1a19e3m[addr(m_param2)m]m.field_256 + 7 / 8 > [94midxm:
          uint32(munknown6e1a19e3m[addr(m_param2)m]m[[94midx + 1m]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  mem[(32 * m_param4.length) + 224 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  log 0x4d38780a: _param3, Array(len=_param4.length, data=call.data[_param4 + 36 len floor32(_param4.length)], mem[(32 * _param4.length) + floor32(_param4.length) + 224 len (32 * _param4.length) - floor32(_param4.length)]), _param1, _param2


# hash = 0x37401e97
# getter = None
# const = None
# payable = False
def unknown37401e97(addr m_param1): # not payable
  if not munknown6e1a19e3m[addr(m_param1)m]m.field_256:
      mem[(32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 128] = 32
      mem[(32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 160] = munknown6e1a19e3m[addr(m_param1)m]m.field_256
      mem[(32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 192 len floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)] = mem[128 len floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)]
      return memory
        from (32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 128
         [93mlen (96 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 64
  mem[128] = munknown6e1a19e3m[addr(m_param1)m]m[1m]m.field_0 / 256^0 << 224
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 96 > [94midxm:
      mem[[94midx + 32] = munknown6e1a19e3m[addr(m_param1)m]m[1m]m.field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
      [94midx = [94midx + 32
      [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
      mcontinue 
  mem[(32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 192 len floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)] = mem[128 len floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)]
  return Array(len=munknown6e1a19e3m[addr(m_param1)m]m.field_256, data=mem[128 len floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)], mem[(32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 192 len (32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) - floor32(munknown6e1a19e3m[addr(m_param1)m]m.field_256)]), 


# hash = 0x38f68e91
# getter = None
# const = None
# payable = False
def unknown38f68e91(addr m_param1, addr m_param2, bool m_param3, array m_param4): # not payable
  mem[128 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          mem[(32 * m_param4.length) + 196] = mcall.func_hash
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          mem[(32 * m_param4.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not uint8(munknown6e1a19e3m[addr(m_param2)m]m.field_0):
      revert with 0, 'Exchange with adapter doesn't exist'
  addr(munknown6e1a19e3m[addr(m_param2)m]m.field_8) = m_param1
  Mask(88, 0, munknown6e1a19e3m[addr(m_param2)m]m.field_168) = Mask(88, 0, m_param3)
  Mask(80, 0, munknown6e1a19e3m[addr(m_param2)m]m.field_176) = 0
  munknown6e1a19e3m[addr(m_param2)m]m.field_256 = m_param4.length
  if not m_param4.length:
      [94midx = 0
      mwhile munknown6e1a19e3m[addr(m_param2)m]m.field_256 + 7 / 8 > [94midxm:
          uint32(munknown6e1a19e3m[addr(m_param2)m]m[[94midx + 1m]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param4.length) + 128 > [94midxm:
          munknown6e1a19e3m[addr(m_param2)m]m[1m]m.field_0 = mem[[94midx len 4] * 256^[94ms or !(4294967295 * 256^[94ms) and munknown6e1a19e3m[addr(m_param2)m]m[1m]m.field_0
          [94ms = [94ms + (4 * -[94ms + 7 / 32) + (-1 * [94ms * [94ms + 7 / 32) + 4
          [94midx = [94midx + 32
          mcontinue 
      [94midx = floor32(m_param4.length) >> 3
      [94ms = sha3(sha3(addr(m_param2), 4) + 1)
      mwhile [94midxm:
          mstor[[94msm] = !(4294967295 * 256^[94midx) and mstor[[94msm]
          [94midx = [94midx + (4 * -[94midx + 7 / 32) + (-1 * [94midx * [94midx + 7 / 32) + 4
          [94ms = ([94midx + 7 / 32) + [94ms
          mcontinue 
      [94midx = (floor32(m_param4.length) >> 3) + Mask(252, 2, None + -(floor32(m_param4.length) >> 3) + 5) + 7 / 32 * Mask(254, 0, None + -(floor32(m_param4.length) >> 3) + 5) >> 2
      mwhile munknown6e1a19e3m[addr(m_param2)m]m.field_256 + 7 / 8 > [94midxm:
          uint32(munknown6e1a19e3m[addr(m_param2)m]m[[94midx + 1m]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  mem[(32 * m_param4.length) + 224 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  log 0x4d38780a: _param3, Array(len=_param4.length, data=call.data[_param4 + 36 len floor32(_param4.length)], mem[(32 * _param4.length) + floor32(_param4.length) + 224 len (32 * _param4.length) - floor32(_param4.length)]), _param1, _param2


# hash = 0x40fd0d19
# getter = ['storage', 160, 0, ['add', ['sha3', 7], ['cd', 4]]]
# const = None
# payable = False
def unknown40fd0d19(uint256 m_param1): # not payable
  require m_param1 < munknown40fd0d19m.length
  return addr(munknown40fd0d19m[m_param1m]m.field_0)


# hash = 0x41b80b0e
# getter = None
# const = None
# payable = False
def unknown41b80b0e(): # not payable
  if not munknown8d56e43cm.length:
      mem[(32 * munknown8d56e43cm.length) + 128] = 32
      mem[(32 * munknown8d56e43cm.length) + 160] = munknown8d56e43cm.length
      mem[(32 * munknown8d56e43cm.length) + 192 len floor32(munknown8d56e43cm.length)] = mem[128 len floor32(munknown8d56e43cm.length)]
      return memory
        from (32 * munknown8d56e43cm.length) + 128
         [93mlen (96 * munknown8d56e43cm.length) + 64
  mem[128] = addr(munknown8d56e43cm.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown8d56e43cm.length) + 96 > [94midxm:
      mem[[94midx + 32] = addr(munknown8d56e43cm[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown8d56e43cm.length) + 192 len floor32(munknown8d56e43cm.length)] = mem[128 len floor32(munknown8d56e43cm.length)]
  return Array(len=munknown8d56e43cm.length, data=mem[128 len floor32(munknown8d56e43cm.length)], mem[(32 * munknown8d56e43cm.length) + floor32(munknown8d56e43cm.length) + 192 len (32 * munknown8d56e43cm.length) - floor32(munknown8d56e43cm.length)]), 


# hash = 0x56701d46
# getter = None
# const = None
# payable = False
def unknown56701d46(array m_param1): # not payable
  mem[64] = ceil32(m_param1.length) + 128
  mem[96] = m_param1.length
  mem[128 len m_param1.length] = m_param1[allm]
  if m_param1.length > 66:
      return 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'A':
          if Mask(8, 248, mem[[94midx + 128]) <= 'Z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) >= 'a':
          if Mask(8, 248, mem[[94midx + 128]) <= 'z':
              [94ms = Mask(8, 248, mem[[94midx + 128])
              [94midx = [94midx + 1
              mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == ' ':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '-':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '.':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '_':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      if Mask(8, 248, mem[[94midx + 128]) == '*':
          [94ms = Mask(8, 248, mem[[94midx + 128])
          [94midx = [94midx + 1
          mcontinue 
      else:
          return 0
  return 1


# hash = 0x5769fc33
# getter = ['storage', 160, 0, 17]
# const = None
# payable = False
def unknown5769fc33(): # not payable
  return munknown5769fc33Address


# hash = 0x5fd4b08a
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 1, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]], ['add', 1, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def getName(address m_address): # not payable
  return mnamem[addr(m_address)m]m[1m]m[0 len mnamem[addr(m_address)m]m[1m]m.lengthm]m.field_0


# hash = 0x63a65847
# getter = None
# const = None
# payable = False
def unknown63a65847(): # not payable
  if munknown40fd0d19m.length:
      mem[128] = addr(munknown40fd0d19m.field_0)
      if (32 * munknown40fd0d19m.length) + 32 > 64:
          mem[160] = addr(munknown40fd0d19m.field_256)
          [94midx = 160
          [94ms = 1
          mwhile (32 * munknown40fd0d19m.length) + 96 > [94midxm:
              mem[[94midx + 32] = addr(munknown40fd0d19m[[94msm]m.field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * munknown40fd0d19m.length) + 128] = 32
  mem[(32 * munknown40fd0d19m.length) + 160] = munknown40fd0d19m.length
  mem[(32 * munknown40fd0d19m.length) + 192 len floor32(munknown40fd0d19m.length)] = mem[128 len floor32(munknown40fd0d19m.length)]
  return memory
    from (32 * munknown40fd0d19m.length) + 128
     [93mlen (96 * munknown40fd0d19m.length) + 64


# hash = 0x671521e8
# getter = None
# const = None
# payable = False
def unknown671521e8(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknown74d32ad4Address = m_param1
  log 0x2c58ddee: _param1


# hash = 0x68171516
# getter = None
# const = None
# payable = False
def assetMethodIsAllowed(address m_ofAsset, bytes4 m_querySignature): # not payable
  if mnamem[addr(m_ofAsset)m]m.field_1792:
      mem[128] = mnamem[addr(m_ofAsset)m]m[7m]m.field_0 / 256^0 << 224
      [94midx = 128
      [94ms = 0
      mwhile (32 * mnamem[addr(m_ofAsset)m]m.field_1792) + 96 > [94midxm:
          mem[[94midx + 32] = mnamem[addr(m_ofAsset)m]m[7m]m.field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
          [94midx = [94midx + 32
          [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
          mcontinue 
  [94midx = 0
  mwhile [94midx < mnamem[addr(m_ofAsset)m]m.field_1792m:
      require [94midx < mnamem[addr(m_ofAsset)m]m.field_1792
      if Mask(32, 224, mem[(32 * [94midx) + 128]) != Mask(32, 224, m_querySignature):
          [94midx = [94midx + 1
          mcontinue 
      return 1
  return 0


# hash = 0x697c5364
# getter = ['struct', ['loc', 6]]
# const = None
# payable = False
def unknown697c5364(addr m_param1): # not payable
  return bool(uint8(munknown697c5364m[m_param1m]m.field_0)), munknown697c5364m[m_param1m]m.field_256


# hash = 0x6e1a19e3
# getter = ['storage', 160, 8, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]
# const = None
# payable = False
def unknown6e1a19e3(addr m_param1): # not payable
  return addr(munknown6e1a19e3m[addr(m_param1)m]m.field_8)


# hash = 0x6ff76de1
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 8]]]]
# const = None
# payable = False
def unknown6ff76de1(addr m_param1): # not payable
  return bool(mstor8m[m_param1m])


# hash = 0x74d32ad4
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def unknown74d32ad4(): # not payable
  return munknown74d32ad4Address


# hash = 0x7a9e5e4b
# getter = None
# const = None
# payable = False
def setAuthority(address m_authority): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mauthorityAddress = m_authority_
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
  return munknown8a471df9Address


# hash = 0x8b522db9
# getter = None
# const = None
# payable = False
def unknown8b522db9(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknown5769fc33Address = m_param1
  log 0x80f7a2a1: _param1


# hash = 0x8d56e43c
# getter = ['storage', 160, 0, ['add', ['sha3', 5], ['cd', 4]]]
# const = None
# payable = False
def unknown8d56e43c(uint256 m_param1): # not payable
  require m_param1 < munknown8d56e43cm.length
  return addr(munknown8d56e43cm[m_param1m]m.field_0)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9b8ce78f
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]]
# const = None
# payable = False
def unknown9b8ce78f(addr m_param1): # not payable
  return bool(uint8(munknown697c5364m[addr(m_param1)m]m.field_0))


# hash = 0x9e0a4570
# getter = None
# const = None
# payable = False
def unknown9e0a4570(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknown8a471df9Address = m_param1
  log 0x46adb525: _param1


# hash = 0xa083bd3c
# getter = ['storage', 160, 0, ['add', ['sha3', 3], ['cd', 4]]]
# const = None
# payable = False
def registeredAssets(uint256 m_param1): # not payable
  require m_param1 < mregisteredAssetsm.length
  return addr(mregisteredAssetsm[m_param1m]m.field_0)


# hash = 0xa419c615
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def exchangeInformation(address m_param1): # not payable
  return bool(uint8(munknown6e1a19e3m[m_param1m]m.field_0)), 
         addr(munknown6e1a19e3m[m_param1m]m.field_0),
         bool(uint8(munknown6e1a19e3m[m_param1m]m.field_168))


# hash = 0xaa8862ba
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def unknownaa8862ba(): # not payable
  return munknownaa8862baAddress


# hash = 0xbda53107
# getter = None
# const = None
# payable = False
def unknownbda53107(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknown20531bc9Address = m_param1
  log 0xbe4a9fa8: _param1


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return mauthorityAddress


# hash = 0xc35d8621
# getter = None
# const = None
# payable = False
def unknownc35d8621(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  munknownaa8862baAddress = m_param1
  log 0x7bab9795: _param1


# hash = 0xc7153b89
# getter = None
# const = None
# payable = False
def unknownc7153b89(addr m_param1): # not payable
  if munknownd2b048abm[addr(m_param1)m]:
      return 1
  require ext_code.size(m_param1)
  call m_param1.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x3957a225 with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Call from either a spoke or hub'
  return bool(munknownd2b048abm[addr(ext_call.return_data[0])m])


# hash = 0xc9b2e522
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]], ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def getSymbol(address m_ofAsset): # not payable
  return mnamem[addr(m_ofAsset)m]m[2m]m[0 len mnamem[addr(m_ofAsset)m]m[2m]m.lengthm]m.field_0


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 16]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return munknownc9d4623fAddress


# hash = 0xcf54aaa0
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def getDecimals(address m_token): # not payable
  return mnamem[addr(m_token)m]m.field_768


# hash = 0xcf5cb132
# getter = None
# const = None
# payable = False
def getRegisteredAssets(): # not payable
  if mregisteredAssetsm.length:
      mem[128] = addr(mregisteredAssetsm.field_0)
      if (32 * mregisteredAssetsm.length) + 32 > 64:
          mem[160] = addr(mregisteredAssetsm.field_256)
          [94midx = 160
          [94ms = 1
          mwhile (32 * mregisteredAssetsm.length) + 96 > [94midxm:
              mem[[94midx + 32] = addr(mregisteredAssetsm[[94msm]m.field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * mregisteredAssetsm.length) + 128] = 32
  mem[(32 * mregisteredAssetsm.length) + 160] = mregisteredAssetsm.length
  mem[(32 * mregisteredAssetsm.length) + 192 len floor32(mregisteredAssetsm.length)] = mem[128 len floor32(mregisteredAssetsm.length)]
  return memory
    from (32 * mregisteredAssetsm.length) + 128
     [93mlen (96 * mregisteredAssetsm.length) + 64


# hash = 0xd2b048ab
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknownd2b048ab(addr m_param1): # not payable
  return munknownd2b048abm[m_param1m]


# hash = 0xd6abbf0a
# getter = None
# const = None
# payable = False
def unknownd6abbf0a(addr m_param1, array m_param2): # not payable
  mem[0] = caller
  mem[32] = 6
  if not uint8(munknown697c5364m[callerm]m.field_0):
      revert with 0, 'Only a Version can do this'
  mem[64] = ceil32(m_param2.length) + 128
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[ceil32(m_param2.length) + 128 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[ceil32(m_param2.length) + floor32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32] = mem[floor32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32]
  if m_param2.length > 66:
      revert with 0, 'Fund name cannot be used'
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
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
      mcontinue 
  if munknown32b34f99m[call.data[m_param2 + 36 len floor32(m_param2.length)]m][mem[ceil32(m_param2.length) + floor32(m_param2.length) + 128 len m_param2.length % 32]m]:
      if munknown32b34f99m[call.data[m_param2 + 36 len floor32(m_param2.length)]m][mem[ceil32(m_param2.length) + floor32(m_param2.length) + 128 len m_param2.length % 32]m] != m_param1:
          revert with 0, 'Fund name cannot be used'
  munknown32b34f99m[m_param2[allm]m] = m_param1


# hash = 0xd737c4b9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 10]]]]
# const = None
# payable = False
def unknownd737c4b9(uint256 m_param1): # not payable
  return bool(mstor10m[m_param1m])


# hash = 0xe2a1b398
# getter = None
# const = None
# payable = False
def unknowne2a1b398(): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 8
      mstor8m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xe46c871c
# getter = None
# const = None
# payable = False
def unknowne46c871c(addr m_param1, uint32 m_param2): # not payable
  if munknown6e1a19e3m[addr(m_param1)m]m.field_256:
      mem[128] = munknown6e1a19e3m[addr(m_param1)m]m[1m]m.field_0 / 256^0 << 224
      [94midx = 128
      [94ms = 0
      mwhile (32 * munknown6e1a19e3m[addr(m_param1)m]m.field_256) + 96 > [94midxm:
          mem[[94midx + 32] = munknown6e1a19e3m[addr(m_param1)m]m[1m]m.field_0 / 256^((4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)) << 224
          [94midx = [94midx + 32
          [94ms = (4 * -([94ms + 7 / 32) + 1) + [94ms - ([94ms + 7 / 32 * [94ms)
          mcontinue 
  [94midx = 0
  mwhile [94midx < munknown6e1a19e3m[addr(m_param1)m]m.field_256m:
      require [94midx < munknown6e1a19e3m[addr(m_param1)m]m.field_256
      if Mask(32, 224, mem[(32 * [94midx) + 128]) != Mask(32, 224, m_param2):
          [94midx = [94midx + 1
          mcontinue 
      return 1
  return 0


# hash = 0xf31507df
# getter = None
# const = None
# payable = False
def unknownf31507df(addr m_param1, uint256 m_param2): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not uint8(munknown6e1a19e3m[addr(m_param1)m]m.field_0):
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Exchange with adapter doesn't exist'
  require m_param2 < munknown8d56e43cm.length
  if addr(munknown8d56e43cm[m_param2m]m.field_0) != m_param1:
      revert with 0, 'Incorrect adapter index'
  Mask(176, 0, munknown6e1a19e3m[addr(m_param1)m]m.field_0) = 0
  munknown6e1a19e3m[addr(m_param1)m]m.field_256 = 0
  [94midx = 0
  mwhile munknown6e1a19e3m[addr(m_param1)m]m.field_256 + 7 / 8 > [94midxm:
      munknown6e1a19e3m[addr(m_param1)m]m[[94midx + 1m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  require m_param2 < munknown8d56e43cm.length
  addr(munknown8d56e43cm[m_param2m]m.field_0) = 0
  [94midx = m_param2
  mwhile [94midx < munknown8d56e43cm.length - 1m:
      require [94midx + 1 < munknown8d56e43cm.length
      require [94midx < munknown8d56e43cm.length
      mem[0] = 5
      addr(munknown8d56e43cm[[94midxm]m.field_0) = addr(munknown8d56e43cm[[94midxm]m.field_256)
      [94midx = [94midx + 1
      mcontinue 
  munknown8d56e43cm.length--
  if munknown8d56e43cm.length > munknown8d56e43cm.length - 1:
      [94midx = munknown8d56e43cm.length - 1
      mwhile munknown8d56e43cm.length > [94midxm:
          munknown8d56e43cm[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  log 0xc7e5f770: _param1


# hash = 0xf4196b63
# getter = ['storage', 256, 0, ['add', 5, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]
# const = None
# payable = False
def unknownf4196b63(addr m_param1): # not payable
  return mnamem[addr(m_param1)m]m.field_1280


# hash = 0xfe68b528
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def getExchangeInformation(address m_ofExchange): # not payable
  return addr(munknown6e1a19e3m[addr(m_ofExchange)m]m.field_0), bool(uint8(munknown6e1a19e3m[addr(m_ofExchange)m]m.field_168))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


