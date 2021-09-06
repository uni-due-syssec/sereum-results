# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6C38917c46E605237Bbe95C5830aB15Cd0ea9d36 
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
    stor12 # mask: a s
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
    unknownd1599d92 # mask: a s
    # storage address 18
    isShutDown # mask: a s
    # storage address 18
    unknown433f5e60 # mask: a s
    # storage address 18
    unknown42143c2a # mask: a s
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
  return creatorAddress


# hash = 0x03314efa
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def shares(): # not payable
  return sharesAddress


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


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


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return unknown20531bc9Address


# hash = 0x2bc3217d
# getter = None
# const = None
# payable = False
def forbid(address _src, address _dst, bytes32 _sig): # not payable
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
  stor2[addr(_src)][addr(_dst)][_sig] = 0
  log LogForbid(
        bytes32 src=addr(_src),
        bytes32 dst=addr(_dst),
        bytes32 sig=_sig)


# hash = 0x30ed7255
# getter = None
# const = None
# payable = False
def unknown30ed7255(): # not payable
  if creatorAddress != caller:
      revert with 0, 'Only creator can do this'
  if unknown42143c2a:
      revert with 0, 'Spokes already set'
  [94midx = 0
  while [94midx < 12:
      mem[0] = addr(cd[((32 * [94midx) + 4)])
      mem[32] = 20
      stor20[addr(cd[((32 * [94midx) + 4)])] = 1
      [94midx = [94midx + 1
      continue 
  unknown9624e83eAddress = addr(cd[4])
  stor4 = addr(cd[36])
  unknownd3240bd2Address = addr(cd[68])
  unknownab3dbf3bAddress = addr(cd[100])
  sharesAddress = addr(cd[132])
  tradingAddress = addr(cd[164])
  vaultAddress = addr(cd[196])
  unknown20531bc9Address = addr(cd[228])
  registryAddress = addr(cd[260])
  stor12 = addr(cd[292])
  stor13 = addr(cd[324])
  stor14 = addr(cd[356])
  unknown42143c2a = 1


# hash = 0x3957a225
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 20]]]]
# const = None
# payable = False
def unknown3957a225(addr _param1): # not payable
  return bool(stor20[_param1])


# hash = 0x42143c2a
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def unknown42143c2a(): # not payable
  return bool(unknown42143c2a)


# hash = 0x433f5e60
# getter = ['bool', ['storage', 8, 24, 18]]
# const = None
# payable = False
def unknown433f5e60(): # not payable
  return bool(unknown433f5e60)


# hash = 0x481c6a75
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def manager(): # not payable
  return managerAddress


# hash = 0x79d88d87
# getter = None
# const = None
# payable = False
def forbid(bytes32 _src, bytes32 _dst, bytes32 _sig): # not payable
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
  stor2[_src][_dst][_sig] = 0
  log LogForbid(
        bytes32 src=_src,
        bytes32 dst=_dst,
        bytes32 sig=_sig)


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


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9624e83e
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown9624e83e(): # not payable
  return unknown9624e83eAddress


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
  return unknownab3dbf3bAddress


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return unknown9624e83eAddress, 
         stor4,
         unknownd3240bd2Address,
         unknownab3dbf3bAddress,
         sharesAddress,
         tradingAddress,
         vaultAddress,
         unknown20531bc9Address,
         registryAddress,
         stor12,
         stor13,
         stor14


# hash = 0xb7009613
# getter = None
# const = None
# payable = False
def canCall(address _caller, address _code, bytes4 _sig): # not payable
  if stor2[addr(_caller)][addr(_code)][Mask(32, 224, _sig)]:
      return bool(stor2[addr(_caller)][addr(_code)][Mask(32, 224, _sig)])
  if stor2[addr(_caller)][addr(_code)][-1]:
      return bool(stor2[addr(_caller)][addr(_code)][-1])
  if stor2[addr(_caller)][-1][Mask(32, 224, _sig)]:
      return bool(stor2[addr(_caller)][-1][Mask(32, 224, _sig)])
  if stor2[addr(_caller)][-1][-1]:
      return bool(stor2[addr(_caller)][-1][-1])
  if stor38B5[addr(_code)][Mask(32, 224, _sig)]:
      return bool(stor38B5[addr(_code)][Mask(32, 224, _sig)])
  if stor38B5[addr(_code)][-1]:
      return bool(stor38B5[addr(_code)][-1])
  if stor47FA[Mask(32, 224, _sig)]:
      return bool(stor47FA[Mask(32, 224, _sig)])
  return bool(storF423)


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return authorityAddress


# hash = 0xc8d70559
# getter = None
# const = None
# payable = False
def unknownc8d70559(): # not payable
  require caller == stor12
  isShutDown = 1
  log 0x3b5df664 


# hash = 0xcbeea68c
# getter = None
# const = None
# payable = False
def permit(address _src, address _dst, bytes32 _sig): # not payable
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
  stor2[addr(_src)][addr(_dst)][_sig] = 1
  log LogPermit(
        bytes32 src=addr(_src),
        bytes32 dst=addr(_dst),
        bytes32 sig=_sig)


# hash = 0xd1599d92
# getter = ['bool', ['storage', 8, 16, 18]]
# const = None
# payable = False
def unknownd1599d92(): # not payable
  return bool(unknownd1599d92)


# hash = 0xd3240bd2
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknownd3240bd2(): # not payable
  return unknownd3240bd2Address


# hash = 0xd8270dce
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def creationTime(): # not payable
  return creationTime


# hash = 0xec44acf2
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def trading(): # not payable
  return tradingAddress


# hash = 0xf0217ce5
# getter = None
# const = None
# payable = False
def permit(bytes32 _src, bytes32 _dst, bytes32 _sig): # not payable
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
  stor2[_src][_dst][_sig] = 1
  log LogPermit(
        bytes32 src=_src,
        bytes32 dst=_dst,
        bytes32 sig=_sig)


# hash = 0xf1a07269
# getter = None
# const = None
# payable = False
def unknownf1a07269(): # not payable
  if creatorAddress != caller:
      revert with 0, 'Only creator can do this'
  if not unknown42143c2a:
      revert with 0, 'Spokes must be set'
  if unknownd1599d92:
      revert with 0, 'Routing already set'
  require ext_code.size(unknown9624e83eAddress)
  call unknown9624e83eAddress.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(stor4)
  call stor4.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknownd3240bd2Address)
  call unknownd3240bd2Address.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknownab3dbf3bAddress)
  call unknownab3dbf3bAddress.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(sharesAddress)
  call sharesAddress.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(tradingAddress)
  call tradingAddress.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(vaultAddress)
  call vaultAddress.0x83259ed9 with:
       gas gas_remaining wei
      args unknown9624e83eAddress, stor4, unknownd3240bd2Address, unknownab3dbf3bAddress, sharesAddress, tradingAddress, vaultAddress, unknown20531bc9Address, registryAddress, stor12, stor13, stor14
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknownd1599d92 = 1


# hash = 0xfbfa77cf
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def vault(): # not payable
  return vaultAddress


# hash = 0xff947525
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def isShutDown(): # not payable
  return bool(isShutDown)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


