# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2ba9D006C1D72E67A70b5526Fc6b4b0C0fd6D334 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    unknownee0e7a7d # mask: a s
    # storage address 1
    unknown371fa854 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    unknown99b24e0aAddress # mask: a s
    # storage address 3
    unknown8c062e4eAddress # mask: a s
    # storage address 4
    times # mask: a s
    # storage address 5
    startCalled # mask: a s
    # storage address 5
    unknown3500f91e # mask: a s
    # storage address 6
    unknown592cdadd # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    libAddress # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 8
    unknown355e937dAddress # mask: a s
# hash = 0x21ee999c
# getter = None
# const = None
# payable = True
def unknown21ee999c(uint128 _param1) payable: 
  require owner == caller
  stor0 = Mask(96, 0, _param1)


# hash = 0x3372033c
# getter = None
# const = None
# payable = True
def unknown3372033c(uint256 _param1) payable: 
  require owner == caller
  uint256(stor8) = _param1 or Mask(96, 160, uint256(stor8))


# hash = 0x3500f91e
# getter = ['storage', 8, 8, 5]
# const = None
# payable = True
def unknown3500f91e() payable: 
  return unknown3500f91e


# hash = 0x355e937d
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def unknown355e937d() payable: 
  return addr(unknown355e937dAddress)


# hash = 0x371fa854
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def unknown371fa854() payable: 
  return unknown371fa854


# hash = 0x592cdadd
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def unknown592cdadd() payable: 
  return unknown592cdadd


# hash = 0x632a9a52
# getter = None
# const = None
# payable = True
def vote() payable: 
  require owner == caller
  unknown3500f91e = 1
  call unknown8c062e4eAddress.vote(uint256 proposalNumber, bool supportsProposal) with:
       gas gas_remaining - 25050 wei
      args unknown371fa854, 1
  require ext_call.success


# hash = 0x8c062e4e
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def unknown8c062e4e() payable: 
  return unknown8c062e4eAddress


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x92801230
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def lib() payable: 
  return addr(libAddress)


# hash = 0x99b24e0a
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def unknown99b24e0a() payable: 
  return addr(unknown99b24e0aAddress)


# hash = 0x9e3b34bf
# getter = ['storage', 256, 0, 4]
# const = None
# payable = True
def times() payable: 
  return times


# hash = 0xa04a0908
# getter = None
# const = None
# payable = True
def unknowna04a0908(addr _param1, array _param2, uint256 _param3) payable: 
  mem[128 len _param2.length] = _param2[all]
  require caller == owner
  mem[ceil32(_param2.length) + 128 len _param2.length] = _param2[all]
  if not _param2.length % 32:
      call _param1 with:
         value _param3 wei
           gas gas_remaining - 34050 wei
          args _param2[all]
  else:
      mem[floor32(_param2.length) + ceil32(_param2.length) + 128] = mem[floor32(_param2.length) + ceil32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32]
      call _param1.mem[ceil32(_param2.length) + 128 len 4] with:
         value _param3 wei
           gas gas_remaining - 34050 wei
          args mem[ceil32(_param2.length) + 132 len floor32(_param2.length) + 28]


# hash = 0xb6b98c5d
# getter = None
# const = None
# payable = True
def executeDelegate(address _delegate, bytes _functionCall) payable: 
  mem[128 len _functionCall.length] = _functionCall[all]
  require caller == owner
  mem[ceil32(_functionCall.length) + 128 len _functionCall.length] = _functionCall[all]
  if not _functionCall.length % 32:
      [93mdelegate _delegate with:
           gas gas_remaining - 50 wei
          args _functionCall[all]
  else:
      mem[floor32(_functionCall.length) + ceil32(_functionCall.length) + 128] = mem[floor32(_functionCall.length) + ceil32(_functionCall.length) + -(_functionCall.length % 32) + 160 len _functionCall.length % 32]
      [93mdelegate _delegate.mem[ceil32(_functionCall.length) + 128 len 4] with:
           gas gas_remaining - 50 wei
          args mem[ceil32(_functionCall.length) + 132 len floor32(_functionCall.length) + 28]
  require delegate.return_code


# hash = 0xbe9a6555
# getter = None
# const = None
# payable = True
def start() payable: 
  require owner == caller
  startCalled = 1
  call unknown8c062e4eAddress.splitDAO(uint256 proposalID, address newCurator) with:
       gas gas_remaining - 25050 wei
      args unknown371fa854, addr(unknown99b24e0aAddress)
  require ext_call.success


# hash = 0xc240e65a
# getter = None
# const = None
# payable = True
def unknownc240e65a(uint256 _param1) payable: 
  require owner == caller
  uint256(stor7) = _param1 or Mask(96, 160, uint256(stor7))


# hash = 0xcea941fc
# getter = ['storage', 8, 0, 5]
# const = None
# payable = True
def startCalled() payable: 
  return startCalled


# hash = 0xe90956cf
# getter = None
# const = None
# payable = True
def setCurator(address _newCurator) payable: 
  require owner == caller
  uint256(stor2) = _newCurator or Mask(96, 160, uint256(stor2))


# hash = 0xee0e7a7d
# getter = ['storage', 8, 160, 0]
# const = None
# payable = True
def unknownee0e7a7d() payable: 
  return unknownee0e7a7d


# hash = 0xfb91de56
# getter = None
# const = None
# payable = True
def unknownfb91de56(uint256 _param1) payable: 
  require owner == caller
  unknown371fa854 = _param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if addr(libAddress) != 0:
      [93mdelegate addr(libAddress) with:
           gas gas_remaining - 50 wei
          args 
      require delegate.return_code
  else:
      call unknown8c062e4eAddress.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      if not unknownee0e7a7d:
          call unknown8c062e4eAddress.transfer(address to, uint256 value) with:
               gas gas_remaining - 25050 wei
              args addr(unknown355e937dAddress), ext_call.return_data[0]
      else:
          if gas_remaining <= 200000:
              call unknown8c062e4eAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining - 25050 wei
                  args addr(unknown355e937dAddress), ext_call.return_data[0]
          else:
              if eth.balance(unknown8c062e4eAddress) > ext_call.return_data[0]:
                  call unknown8c062e4eAddress.splitDAO(uint256 proposalID, address newCurator) with:
                       gas gas_remaining - 25050 wei
                      args unknown371fa854, addr(unknown99b24e0aAddress)
                  require ext_call.success
              else:
                  call unknown8c062e4eAddress.balanceOf(address owner) with:
                       gas gas_remaining - 25050 wei
                      args this.address
                  require ext_call.success
                  call unknown8c062e4eAddress.transfer(address to, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args addr(unknown355e937dAddress), ext_call.return_data[0]


