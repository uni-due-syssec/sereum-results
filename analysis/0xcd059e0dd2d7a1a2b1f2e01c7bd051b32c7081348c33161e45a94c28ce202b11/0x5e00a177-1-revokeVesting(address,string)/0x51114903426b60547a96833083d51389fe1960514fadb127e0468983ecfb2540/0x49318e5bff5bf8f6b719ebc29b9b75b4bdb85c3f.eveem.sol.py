# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x49318e5bFF5bF8f6b719eBc29B9b75b4BDb85c3f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    newOwner # mask: a s
    # storage address 2
    beneficiaryAddress # mask: a s
    # storage address 3
    tokenAddress # mask: a s
    # storage address 4
    startTime # mask: a s
    # storage address 5
    unknown37dafa5b # mask: a s
    # storage address 6
    unknown69a89b85 # mask: a s
    # storage address 7
    version # mask: a s
    # storage address 8
    revocable # mask: a s
    # storage address 9
    unknownb888c479 # mask: a s
    # storage address 10
    revoked # mask: a s
    # storage address 11
    internalBalance # mask: a s
# hash = 0x03991aea
# getter = None
# const = None
# payable = False
def unknown03991aea(): # not payable
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if startTime >= block.timestamp:
      return 0
  require startTime <= block.timestamp
  require unknown37dafa5b
  require unknownb888c479 <= block.timestamp - startTime / unknown37dafa5b * unknown69a89b85
  if (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479 <= ext_call.return_data[0]:
      return ((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479)
  return ext_call.return_data[0]


# hash = 0x21b8092e
# getter = None
# const = None
# payable = False
def setWithdrawalAddress(address _newWithdrawalAddress): # not payable
  require owner == caller
  beneficiaryAddress = _newWithdrawalAddress
  log 0x66bd5edd: _newWithdrawalAddress


# hash = 0x26000ba2
# getter = None
# const = None
# payable = False
def unknown26000ba2(uint256 _param1): # not payable
  require owner == caller
  require _param1 + internalBalance >= internalBalance
  internalBalance += _param1
  log 0xb9a94bb3: _param1


# hash = 0x2e6245c6
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def internalBalance(): # not payable
  return internalBalance


# hash = 0x37dafa5b
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown37dafa5b(): # not payable
  return unknown37dafa5b


# hash = 0x38af3eed
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def beneficiary(): # not payable
  return beneficiaryAddress


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def version(): # not payable
  return version


# hash = 0x63d256ce
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def revoked(): # not payable
  return bool(revoked)


# hash = 0x65b2a863
# getter = None
# const = None
# payable = False
def unknown65b2a863(array _param1): # not payable
  require owner == caller
  require revocable
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if not ext_call.return_data[0]:
      require ext_code.size(tokenAddress)
      call tokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args beneficiaryAddress, 0
      require ext_call.success
      require ext_code.size(owner)
      call owner.substractLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args 0
  else:
      if startTime >= block.timestamp:
          require ext_code.size(tokenAddress)
          call tokenAddress.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args beneficiaryAddress, 0
          require ext_call.success
          require ext_code.size(owner)
          call owner.substractLockedAmount(uint256 amount) with:
               gas gas_remaining wei
              args 0
      else:
          require startTime <= block.timestamp
          require unknown37dafa5b
          require unknownb888c479 <= block.timestamp - startTime / unknown37dafa5b * unknown69a89b85
          require ext_code.size(tokenAddress)
          if (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479 <= ext_call.return_data[0]:
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args beneficiaryAddress, (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479
              require ext_call.success
              require ext_code.size(owner)
              call owner.substractLockedAmount(uint256 amount) with:
                   gas gas_remaining wei
                  args ((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479)
          else:
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args beneficiaryAddress, ext_call.return_data[0]
              require ext_call.success
              require ext_code.size(owner)
              call owner.substractLockedAmount(uint256 amount) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_code.size(owner)
  call owner.addInternalBalance(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args owner, ext_call.return_data[0]
  require ext_call.success
  log 0x2983ef16: Array(len=_param1.length, data=_param1[all])
  [93mselfdestruct([91mowner[93m)


# hash = 0x69a89b85
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown69a89b85(): # not payable
  return unknown69a89b85


# hash = 0x78e97925
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def startTime(): # not payable
  return startTime


# hash = 0x79ba5097
# getter = None
# const = None
# payable = False
def acceptOwnership(): # not payable
  require newOwner == caller
  log OwnerUpdate(
        address prevOwner=owner,
        address newOwner=newOwner)
  owner = newOwner
  newOwner = 0


# hash = 0x7b24343e
# getter = None
# const = None
# payable = False
def unknown7b24343e(addr _param1, addr _param2, uint256 _param3): # not payable
  require owner == caller
  require tokenAddress != _param1
  require ext_code.size(_param1)
  call _param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), _param3
  require ext_call.success


# hash = 0x82b2e257
# getter = None
# const = None
# payable = False
def getTokenBalance(): # not payable
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x86d1a69f
# getter = None
# const = None
# payable = False
def release(): # not payable
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if ext_call.return_data[0] != internalBalance:
      require ext_code.size(tokenAddress)
      call tokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      require internalBalance <= ext_call.return_data[0]
      require ext_code.size(tokenAddress)
      call tokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      internalBalance = ext_call.return_data[0]
      require ext_code.size(owner)
      call owner.addLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data[0] - internalBalance)
      require ext_call.success
      log TokensReceivedSinceLastCheck(uint256 amount=(ext_call.return_data[0] - internalBalance))
  require beneficiaryAddress == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_call.return_data[0]
  require startTime < block.timestamp
  require startTime <= block.timestamp
  require unknown37dafa5b
  require unknownb888c479 <= block.timestamp - startTime / unknown37dafa5b * unknown69a89b85
  if (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479 <= ext_call.return_data[0]:
      require (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479 > 0
      require block.timestamp - startTime / unknown37dafa5b * unknown69a89b85 >= unknownb888c479
      unknownb888c479 = block.timestamp - startTime / unknown37dafa5b * unknown69a89b85
      require (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479 <= internalBalance
      internalBalance = internalBalance - (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) + unknownb888c479
      require ext_code.size(owner)
      call owner.substractLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args ((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479)
      require ext_call.success
      require ext_code.size(tokenAddress)
      call tokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args beneficiaryAddress, (block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479
      require ext_call.success
      log Released(uint256 amount=((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479))
      return ((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479)
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0] + unknownb888c479 >= unknownb888c479
  unknownb888c479 += ext_call.return_data[0]
  require ext_call.return_data[0] <= internalBalance
  internalBalance -= ext_call.return_data[0]
  require ext_code.size(owner)
  call owner.substractLockedAmount(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args beneficiaryAddress, ext_call.return_data[0]
  require ext_call.success
  log Released(uint256 amount=ext_call.return_data[0])
  return ext_call.return_data[0]


# hash = 0x872a7810
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def revocable(): # not payable
  return bool(revocable)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9d76ea58
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def tokenAddress(): # not payable
  return tokenAddress


# hash = 0xb888c479
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknownb888c479(): # not payable
  return unknownb888c479


# hash = 0xd4ee1d90
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def newOwner(): # not payable
  return newOwner


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require owner == caller
  require owner != _newOwner
  newOwner = _newOwner


# hash = 0xf61ac3a4
# getter = None
# const = None
# payable = False
def checkForReceivedTokens(): # not payable
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if ext_call.return_data[0] != internalBalance:
      require ext_code.size(tokenAddress)
      call tokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      require internalBalance <= ext_call.return_data[0]
      require ext_code.size(tokenAddress)
      call tokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      internalBalance = ext_call.return_data[0]
      require ext_code.size(owner)
      call owner.addLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data[0] - internalBalance)
      require ext_call.success
      log TokensReceivedSinceLastCheck(uint256 amount=(ext_call.return_data[0] - internalBalance))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


