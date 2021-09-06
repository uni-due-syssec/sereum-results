# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x157c2746BF3697457888aB63526D951C79e1b507 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    adminAddress # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    auctionAddress # mask: a s
    # storage address 6
    unknown22d3a2e2Address # mask: a s
# hash = 0x06481cda
# getter = None
# const = None
# payable = False
def unknown06481cda(): # not payable
  require ext_code.size(auctionAddress)
  call auctionAddress.0xf5366a6f with:
       gas gas_remaining wei
      args unknown22d3a2e2Address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(auctionAddress)
  call auctionAddress.0xc44e6640 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= 0:
      return 3
  require ext_code.size(auctionAddress)
  call auctionAddress.0xc44e6640 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if 100 * ext_call.return_data[0] / ext_call.return_data[0] >= stor3:
      return 2
  return 1


# hash = 0x221d1301
# getter = None
# const = None
# payable = False
def unknown221d1301(): # not payable
  require ext_code.size(auctionAddress)
  call auctionAddress.0xf5366a6f with:
       gas gas_remaining wei
      args unknown22d3a2e2Address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (stor2 > ext_call.return_data[0])


# hash = 0x22d3a2e2
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown22d3a2e2(): # not payable
  return unknown22d3a2e2Address


# hash = 0x4d19d515
# getter = None
# const = None
# payable = False
def unknown4d19d515(): # not payable
  require ext_code.size(auctionAddress)
  call auctionAddress.0xf5366a6f with:
       gas gas_remaining wei
      args unknown22d3a2e2Address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(auctionAddress)
  call auctionAddress.0xc44e6640 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] >= stor2:
      if ext_call.return_data[0]:
          if 100 * ext_call.return_data[0] / ext_call.return_data[0] >= stor3:
              return 0
          [94ms = 0
          [94midx = 0
          [94ms = 0
          while [94midx < ext_call.return_data[0]:
              mem[132] = [94midx
              require ext_code.size(auctionAddress)
              call auctionAddress.0x1c0c78bc with:
                   gas gas_remaining wei
                  args unknown22d3a2e2Address, [94midx
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(auctionAddress)
              call auctionAddress.0x974c28b2 with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  [94ms = ext_call.return_data[0]
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94ms = [94ms + 1
              continue 
          require ext_call.return_data[0]
          if 100 * [94ms / ext_call.return_data[0] >= stor4:
              return 0
  return 2


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  require caller == owner
  require _newAdmin
  log OwnershipTransferred(
        address previousOwner=adminAddress,
        address newOwner=_newAdmin)
  adminAddress = _newAdmin


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x7d9f6db5
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def auction(): # not payable
  return auctionAddress


# hash = 0x83129800
# getter = None
# const = None
# payable = False
def unknown83129800(): # not payable
  require ext_code.size(auctionAddress)
  call auctionAddress.0xf5366a6f with:
       gas gas_remaining wei
      args unknown22d3a2e2Address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94ms = 0
  [94midx = 0
  [94ms = 0
  while [94midx < ext_call.return_data[0]:
      mem[132] = [94midx
      require ext_code.size(auctionAddress)
      call auctionAddress.0x1c0c78bc with:
           gas gas_remaining wei
          args unknown22d3a2e2Address, [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = ext_call.return_data[0]
      require ext_code.size(auctionAddress)
      call auctionAddress.0x974c28b2 with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94ms = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if ext_call.return_data[0]:
      if 100 * [94ms / ext_call.return_data[0] >= stor4:
          return 0
  return 1


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require caller == owner
  [93mselfdestruct([91mowner[93m)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xa8b0db17
# getter = None
# const = None
# payable = False
def unknowna8b0db17(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  require caller == adminAddress
  stor2 = _param1
  stor3 = _param2
  stor4 = _param3


# hash = 0xd4df0c6d
# getter = None
# const = None
# payable = False
def unknownd4df0c6d(addr _param1, addr _param2): # not payable
  require caller == owner
  require ext_code.size(_param1)
  call _param1.0xd7648949 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'is not ERC721'
  auctionAddress = _param1
  unknown22d3a2e2Address = _param2


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  if not _newOwner:
      revert with 0, 'new owner must be valid'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf5074f41
# getter = None
# const = None
# payable = False
def destroyAndSend(address _recipient): # not payable
  require caller == owner
  [93mselfdestruct([91m_recipient[93m)


# hash = 0xf851a440
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def admin(): # not payable
  return adminAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


