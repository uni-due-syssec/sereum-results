# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xe6aD144FF2b68B3d890EF6D5B6bB080c3A2da3bD 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    adminAddress # mask: a s
    # storage address 1
    pendingAdminAddress # mask: a s
    # storage address 2
    unknownbb82aa5eAddress # mask: a s
    # storage address 3
    unknowndcfbc0c7Address # mask: a s
# hash = 0x26782247
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def pendingAdmin(): # not payable
  return mpendingAdminAddress


# hash = 0xb71d1a0c
# getter = None
# const = None
# payable = False
def _setPendingAdmin(address m_newPendingAdmin): # not payable
  require calldata.size - 4 >= 32
  if madminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=14,
            uint256 detail=0)
      return 1
  mpendingAdminAddress = m_newPendingAdmin
  log NewPendingAdmin(
        address oldPendingAdmin=pendingAdminAddress,
        address newPendingAdmin=_newPendingAdmin)
  return 0


# hash = 0xbb82aa5e
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownbb82aa5e(): # not payable
  return munknownbb82aa5eAddress


# hash = 0xc1e80334
# getter = None
# const = None
# payable = False
def unknownc1e80334(): # not payable
  if munknowndcfbc0c7Address != caller:
      log Failure(
            uint256 error=1,
            uint256 info=1,
            uint256 detail=0)
      return 1
  if not munknowndcfbc0c7Address:
      log Failure(
            uint256 error=1,
            uint256 info=1,
            uint256 detail=0)
      return 1
  munknownbb82aa5eAddress = munknowndcfbc0c7Address
  munknowndcfbc0c7Address = 0
  log 0xd604de94: unknownbb82aa5eAddress, unknowndcfbc0c7Address
  log 0xe945ccee: unknowndcfbc0c7Address, unknowndcfbc0c7Address
  return 0


# hash = 0xdcfbc0c7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknowndcfbc0c7(): # not payable
  return munknowndcfbc0c7Address


# hash = 0xe992a041
# getter = None
# const = None
# payable = False
def unknowne992a041(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if madminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=15,
            uint256 detail=0)
      return 1
  munknowndcfbc0c7Address = m_param1
  log 0xe945ccee: unknowndcfbc0c7Address, _param1
  return 0


# hash = 0xe9c714f2
# getter = None
# const = None
# payable = False
def _acceptAdmin(): # not payable
  if mpendingAdminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=0,
            uint256 detail=0)
      return 1
  if not caller:
      log Failure(
            uint256 error=1,
            uint256 info=0,
            uint256 detail=0)
      return 1
  madminAddress = mpendingAdminAddress
  mpendingAdminAddress = 0
  log NewAdmin(
        address oldAdmin=adminAddress,
        address newAdmin=pendingAdminAddress)
  log NewPendingAdmin(
        address oldPendingAdmin=pendingAdminAddress,
        address newPendingAdmin=pendingAdminAddress)
  return 0


# hash = 0xf851a440
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def admin(): # not payable
  return madminAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate munknownbb82aa5eAddress with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


