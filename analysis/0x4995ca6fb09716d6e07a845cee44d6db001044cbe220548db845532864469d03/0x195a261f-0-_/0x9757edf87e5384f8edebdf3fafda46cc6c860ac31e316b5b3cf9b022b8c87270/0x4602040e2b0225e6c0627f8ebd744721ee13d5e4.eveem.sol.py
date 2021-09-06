# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4602040e2b0225E6c0627f8EBD744721Ee13d5e4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xb73515eb': 'unknownb73515eb(?)'} 

# storage definitions
def storage:
    # storage address 0
    authorityAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    stor2
    # storage address 3
    unknown9624e83eAddress # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    unknownd3240bd2Address # mask: a s
    # storage address 6
    unknownab3dbf3bAddress # mask: a s
    # storage address 7
    sharesAddress # mask: a s
    # storage address 8
    tradingAddress # mask: a s
    # storage address 9
    vaultAddress # mask: a s
    # storage address 10
    unknown20531bc9Address # mask: a s
    # storage address 11
    registryAddress # mask: a s
    # storage address 12
    versionAddress # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    managerAddress # mask: a s
    # storage address 16
    creatorAddress # mask: a s
    # storage address 17
    name
    # storage address 18
    unknown42143c2a # mask: a s
    # storage address 18
    unknownd1599d92 # mask: a s
    # storage address 18
    isShutDown # mask: a s
    # storage address 18
    unknown433f5e60 # mask: a s
    # storage address 19
    creationTime # mask: a s
    # storage address 20
    stor20
    # storage address 25650552922148892519344032483236097322509251582074379366566173648062335731131
    stor25650552922148892519344032483236097322509251582074379366566173648062335731131
    # storage address 32556593370438695430030356523483399124461889696563987552370384290271767317911
    stor32556593370438695430030356523483399124461889696563987552370384290271767317911
    # storage address 110427618500584310386934646482157803069831868813143861061298555264591081543926
    storF423 # mask: a s
# hash = 0x02d05d3f
# getter = ['storage', 160, 0, 16]
# const = None
# payable = False
def creator(): # not payable
  return mcreatorAddress


# hash = 0x03314efa
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def shares(): # not payable
  return msharesAddress


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


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


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return munknown20531bc9Address


# hash = 0x2bc3217d
# getter = None
# const = None
# payable = False
def forbid(address m_src, address m_dst, bytes32 m_sig): # not payable
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
  mstor2m[addr(m_src)m]m[addr(m_dst)m]m[m_sigm] = 0
  log LogForbid(
        bytes32 src=addr(_src),
        bytes32 dst=addr(_dst),
        bytes32 sig=_sig)


# hash = 0x30ed7255
# getter = None
# const = None
# payable = False
def unknown30ed7255(): # not payable
  if mcreatorAddress != caller:
      revert with 0, 'Only creator can do this'
  if munknown42143c2a:
      revert with 0, 'Spokes already set'
  [94midx = 0
  mwhile [94midx < 12m:
      mem[0] = addr(cd[((32 * [94midx) + 4)])
      mem[32] = 20
      mstor20m[addr(cd[((32 * [94midx) + 4)])m] = 1
      [94midx = [94midx + 1
      mcontinue 
  munknown9624e83eAddress = addr(cd[4])
  mstor4 = addr(cd[36])
  munknownd3240bd2Address = addr(cd[68])
  munknownab3dbf3bAddress = addr(cd[100])
  msharesAddress = addr(cd[132])
  mtradingAddress = addr(cd[164])
  mvaultAddress = addr(cd[196])
  munknown20531bc9Address = addr(cd[228])
  mregistryAddress = addr(cd[260])
  mversionAddress = addr(cd[292])
  mstor13 = addr(cd[324])
  mstor14 = addr(cd[356])
  munknown42143c2a = 1


# hash = 0x3957a225
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 20]]]]
# const = None
# payable = False
def unknown3957a225(addr m_param1): # not payable
  return bool(mstor20m[m_param1m])


# hash = 0x42143c2a
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def unknown42143c2a(): # not payable
  return bool(munknown42143c2a)


# hash = 0x433f5e60
# getter = ['bool', ['storage', 8, 24, 18]]
# const = None
# payable = False
def unknown433f5e60(): # not payable
  return bool(munknown433f5e60)


# hash = 0x481c6a75
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def manager(): # not payable
  return mmanagerAddress


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return mversionAddress


# hash = 0x79d88d87
# getter = None
# const = None
# payable = False
def forbid(bytes32 m_src, bytes32 m_dst, bytes32 m_sig): # not payable
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
  mstor2m[m_srcm]m[m_dstm]m[m_sigm] = 0
  log LogForbid(
        bytes32 src=_src,
        bytes32 dst=_dst,
        bytes32 sig=_sig)


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


# hash = 0x7b103999
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def registry(): # not payable
  return mregistryAddress


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9624e83e
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown9624e83e(): # not payable
  return munknown9624e83eAddress


# hash = 0xa8542f66
# getter = None
# const = ['return', -1]
# payable = False
const ANY = -1


# hash = 0xab3dbf3b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknownab3dbf3b(): # not payable
  return munknownab3dbf3bAddress


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return munknown9624e83eAddress, 
         mstor4,
         munknownd3240bd2Address,
         munknownab3dbf3bAddress,
         msharesAddress,
         mtradingAddress,
         mvaultAddress,
         munknown20531bc9Address,
         mregistryAddress,
         mversionAddress,
         mstor13,
         mstor14


# hash = 0xb7009613
# getter = None
# const = None
# payable = False
def canCall(address m_caller, address m_code, bytes4 m_sig): # not payable
  if mstor2m[addr(m_caller)m]m[addr(m_code)m]m[Mask(32, 224, m_sig)m]:
      return bool(mstor2m[addr(m_caller)m]m[addr(m_code)m]m[Mask(32, 224, m_sig)m])
  if mstor2m[addr(m_caller)m]m[addr(m_code)m]m[-1m]:
      return bool(mstor2m[addr(m_caller)m]m[addr(m_code)m]m[-1m])
  if mstor2m[addr(m_caller)m]m[-1m]m[Mask(32, 224, m_sig)m]:
      return bool(mstor2m[addr(m_caller)m]m[-1m]m[Mask(32, 224, m_sig)m])
  if mstor2m[addr(m_caller)m]m[-1m]m[-1m]:
      return bool(mstor2m[addr(m_caller)m]m[-1m]m[-1m])
  if mstor38B5m[addr(m_code)m]m[Mask(32, 224, m_sig)m]:
      return bool(mstor38B5m[addr(m_code)m]m[Mask(32, 224, m_sig)m])
  if mstor38B5m[addr(m_code)m]m[-1m]:
      return bool(mstor38B5m[addr(m_code)m]m[-1m])
  if mstor47FAm[Mask(32, 224, m_sig)m]:
      return bool(mstor47FAm[Mask(32, 224, m_sig)m])
  return bool(mstorF423)


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return mauthorityAddress


# hash = 0xc8d70559
# getter = None
# const = None
# payable = False
def unknownc8d70559(): # not payable
  require caller == mversionAddress
  misShutDown = 1
  log 0x3b5df664 


# hash = 0xcbeea68c
# getter = None
# const = None
# payable = False
def permit(address m_src, address m_dst, bytes32 m_sig): # not payable
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
  mstor2m[addr(m_src)m]m[addr(m_dst)m]m[m_sigm] = 1
  log LogPermit(
        bytes32 src=addr(_src),
        bytes32 dst=addr(_dst),
        bytes32 sig=_sig)


# hash = 0xd1599d92
# getter = ['bool', ['storage', 8, 16, 18]]
# const = None
# payable = False
def unknownd1599d92(): # not payable
  return bool(munknownd1599d92)


# hash = 0xd3240bd2
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknownd3240bd2(): # not payable
  return munknownd3240bd2Address


# hash = 0xd8270dce
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def creationTime(): # not payable
  return mcreationTime


# hash = 0xec44acf2
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def trading(): # not payable
  return mtradingAddress


# hash = 0xf0217ce5
# getter = None
# const = None
# payable = False
def permit(bytes32 m_src, bytes32 m_dst, bytes32 m_sig): # not payable
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
  mstor2m[m_srcm]m[m_dstm]m[m_sigm] = 1
  log LogPermit(
        bytes32 src=_src,
        bytes32 dst=_dst,
        bytes32 sig=_sig)


# hash = 0xf1a07269
# getter = None
# const = None
# payable = False
def unknownf1a07269(): # not payable
  if mcreatorAddress != caller:
      revert with 0, 'Only creator can do this'
  if not munknown42143c2a:
      revert with 0, 'Spokes must be set'
  if munknownd1599d92:
      revert with 0, 'Routing already set'
  require ext_code.size(munknown9624e83eAddress)
  call munknown9624e83eAddress.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(mstor4)
  call mstor4.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknownd3240bd2Address)
  call munknownd3240bd2Address.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknownab3dbf3bAddress)
  call munknownab3dbf3bAddress.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(msharesAddress)
  call msharesAddress.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(mtradingAddress)
  call mtradingAddress.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(mvaultAddress)
  call mvaultAddress.0x83259ed9 with:
       gas gas_remaining wei
      args munknown9624e83eAddress, mstor4, munknownd3240bd2Address, munknownab3dbf3bAddress, msharesAddress, mtradingAddress, mvaultAddress, munknown20531bc9Address, mregistryAddress, mversionAddress, mstor13, mstor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  munknownd1599d92 = 1


# hash = 0xfbfa77cf
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def vault(): # not payable
  return mvaultAddress


# hash = 0xff947525
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def isShutDown(): # not payable
  return bool(misShutDown)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


