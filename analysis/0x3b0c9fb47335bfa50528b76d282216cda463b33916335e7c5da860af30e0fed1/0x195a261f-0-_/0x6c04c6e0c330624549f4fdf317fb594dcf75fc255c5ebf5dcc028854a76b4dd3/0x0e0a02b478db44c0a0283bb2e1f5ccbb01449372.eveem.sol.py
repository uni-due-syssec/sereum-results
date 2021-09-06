# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0e0A02b478DB44c0A0283bB2E1F5CCbb01449372 
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


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(minitialized)


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return munknown20531bc9Address


# hash = 0x365a86fc
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown365a86fc(): # not payable
  return munknown365a86fcAddress


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return mversionAddress


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


# hash = 0x83259ed9
# getter = None
# const = None
# payable = False
def unknown83259ed9(addr m_param1, addr m_param2, addr m_param3, addr m_param4, addr m_param5, addr m_param6, addr m_param7, addr m_param8, addr m_param9, addr m_param10, addr m_param11, addr m_param12): # not payable
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
  require caller == munknown365a86fcAddress
  if minitialized:
      revert with 0, 'Already initialized'
  mstor3 = m_param1
  mstor4 = m_param2
  mstor5 = m_param3
  mstor6 = m_param4
  mstor7 = m_param5
  mstor8 = m_param6
  mstor9 = m_param7
  munknown20531bc9Address = m_param8
  mregistryAddress = m_param9
  mversionAddress = m_param10
  munknownc9d4623fAddress = m_param11
  munknown8a471df9Address = m_param12
  minitialized = 1
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
  mowner = 0
  log LogSetOwner(address owner)
  log 0x0 


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return munknown8a471df9Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return mstor3, 
         mstor4,
         mstor5,
         mstor6,
         mstor7,
         mstor8,
         mstor9,
         munknown20531bc9Address,
         mregistryAddress,
         mversionAddress,
         munknownc9d4623fAddress,
         munknown8a471df9Address


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return mauthorityAddress


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return munknownc9d4623fAddress


# hash = 0xf3fef3a3
# getter = None
# const = None
# payable = False
def withdraw(address m_address, uint256 m_amount): # not payable
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
  require ext_code.size(m_address)
  call m_address.balanceOf(address owner) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_address)
  call m_address.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_address)
  call m_address.balanceOf(address owner) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] + m_amount < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if ext_call.return_data[0] + m_amount != ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Receiver did not receive tokens in transfer'


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


