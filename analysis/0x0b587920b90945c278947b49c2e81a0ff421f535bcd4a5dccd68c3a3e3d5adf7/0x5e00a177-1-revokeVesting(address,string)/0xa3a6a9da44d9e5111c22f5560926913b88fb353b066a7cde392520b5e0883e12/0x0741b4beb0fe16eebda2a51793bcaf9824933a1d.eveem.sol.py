# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0741b4bEB0FE16EebDA2a51793Bcaf9824933A1d 
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
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if mstartTime >= block.timestamp:
      return 0
  require mstartTime <= block.timestamp
  require munknown37dafa5b
  require munknownb888c479 <= block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85
  if (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479 <= ext_call.return_data[0]:
      return ((block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479)
  return ext_call.return_data[0]


# hash = 0x21b8092e
# getter = None
# const = None
# payable = False
def setWithdrawalAddress(address m_newWithdrawalAddress): # not payable
  require mowner == caller
  mbeneficiaryAddress = m_newWithdrawalAddress
  log 0x66bd5edd: _newWithdrawalAddress


# hash = 0x26000ba2
# getter = None
# const = None
# payable = False
def unknown26000ba2(uint256 m_param1): # not payable
  require mowner == caller
  require m_param1 + minternalBalance >= minternalBalance
  minternalBalance += m_param1
  log 0xb9a94bb3: _param1


# hash = 0x2e6245c6
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def internalBalance(): # not payable
  return minternalBalance


# hash = 0x37dafa5b
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown37dafa5b(): # not payable
  return munknown37dafa5b


# hash = 0x38af3eed
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def beneficiary(): # not payable
  return mbeneficiaryAddress


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def version(): # not payable
  return mversion


# hash = 0x63d256ce
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def revoked(): # not payable
  return bool(mrevoked)


# hash = 0x65b2a863
# getter = None
# const = None
# payable = False
def unknown65b2a863(array m_param1): # not payable
  require mowner == caller
  require mrevocable
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if not ext_call.return_data[0]:
      require ext_code.size(mtokenAddress)
      call mtokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mbeneficiaryAddress, 0
      require ext_call.success
      require ext_code.size(mowner)
      call mowner.substractLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args 0
  else:
      if mstartTime >= block.timestamp:
          require ext_code.size(mtokenAddress)
          call mtokenAddress.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mbeneficiaryAddress, 0
          require ext_call.success
          require ext_code.size(mowner)
          call mowner.substractLockedAmount(uint256 amount) with:
               gas gas_remaining wei
              args 0
      else:
          require mstartTime <= block.timestamp
          require munknown37dafa5b
          require munknownb888c479 <= block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85
          require ext_code.size(mtokenAddress)
          if (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479 <= ext_call.return_data[0]:
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args mbeneficiaryAddress, (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479
              require ext_call.success
              require ext_code.size(mowner)
              call mowner.substractLockedAmount(uint256 amount) with:
                   gas gas_remaining wei
                  args ((block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479)
          else:
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args mbeneficiaryAddress, ext_call.return_data[0]
              require ext_call.success
              require ext_code.size(mowner)
              call mowner.substractLockedAmount(uint256 amount) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_code.size(mowner)
  call mowner.addInternalBalance(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mowner, ext_call.return_data[0]
  require ext_call.success
  log 0x2983ef16: Array(len=_param1.length, data=_param1[all])
  [93mselfdestruct([91mowner[93m)


# hash = 0x69a89b85
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown69a89b85(): # not payable
  return munknown69a89b85


# hash = 0x78e97925
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def startTime(): # not payable
  return mstartTime


# hash = 0x79ba5097
# getter = None
# const = None
# payable = False
def acceptOwnership(): # not payable
  require mnewOwner == caller
  log OwnerUpdate(
        address prevOwner=owner,
        address newOwner=newOwner)
  mowner = mnewOwner
  mnewOwner = 0


# hash = 0x7b24343e
# getter = None
# const = None
# payable = False
def unknown7b24343e(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require mowner == caller
  require mtokenAddress != m_param1
  require ext_code.size(m_param1)
  call m_param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param2), m_param3
  require ext_call.success


# hash = 0x82b2e257
# getter = None
# const = None
# payable = False
def getTokenBalance(): # not payable
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x86d1a69f
# getter = None
# const = None
# payable = False
def release(): # not payable
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if ext_call.return_data[0] != minternalBalance:
      require ext_code.size(mtokenAddress)
      call mtokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      require minternalBalance <= ext_call.return_data[0]
      require ext_code.size(mtokenAddress)
      call mtokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      minternalBalance = ext_call.return_data[0]
      require ext_code.size(mowner)
      call mowner.addLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data[0] - minternalBalance)
      require ext_call.success
      log TokensReceivedSinceLastCheck(uint256 amount=(ext_call.return_data[0] - internalBalance))
  require mbeneficiaryAddress == caller
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require ext_call.return_data[0]
  require mstartTime < block.timestamp
  require mstartTime <= block.timestamp
  require munknown37dafa5b
  require munknownb888c479 <= block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85
  if (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479 <= ext_call.return_data[0]:
      require (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479 > 0
      require block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85 >= munknownb888c479
      munknownb888c479 = block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85
      require (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479 <= minternalBalance
      minternalBalance = minternalBalance - (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) + munknownb888c479
      require ext_code.size(mowner)
      call mowner.substractLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args ((block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479)
      require ext_call.success
      require ext_code.size(mtokenAddress)
      call mtokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mbeneficiaryAddress, (block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479
      require ext_call.success
      log Released(uint256 amount=((block.timestamp - startTime / unknown37dafa5b * unknown69a89b85) - unknownb888c479))
      return ((block.timestamp - mstartTime / munknown37dafa5b * munknown69a89b85) - munknownb888c479)
  require ext_call.return_data[0] > 0
  require ext_call.return_data[0] + munknownb888c479 >= munknownb888c479
  munknownb888c479 += ext_call.return_data[0]
  require ext_call.return_data[0] <= minternalBalance
  minternalBalance -= ext_call.return_data[0]
  require ext_code.size(mowner)
  call mowner.substractLockedAmount(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  require ext_call.success
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mbeneficiaryAddress, ext_call.return_data[0]
  require ext_call.success
  log Released(uint256 amount=ext_call.return_data[0])
  return ext_call.return_data[0]


# hash = 0x872a7810
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def revocable(): # not payable
  return bool(mrevocable)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9d76ea58
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def tokenAddress(): # not payable
  return mtokenAddress


# hash = 0xb888c479
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknownb888c479(): # not payable
  return munknownb888c479


# hash = 0xd4ee1d90
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def newOwner(): # not payable
  return mnewOwner


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require mowner == caller
  require mowner != m_newOwner
  mnewOwner = m_newOwner


# hash = 0xf61ac3a4
# getter = None
# const = None
# payable = False
def checkForReceivedTokens(): # not payable
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  if ext_call.return_data[0] != minternalBalance:
      require ext_code.size(mtokenAddress)
      call mtokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      require minternalBalance <= ext_call.return_data[0]
      require ext_code.size(mtokenAddress)
      call mtokenAddress.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      require ext_call.success
      minternalBalance = ext_call.return_data[0]
      require ext_code.size(mowner)
      call mowner.addLockedAmount(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data[0] - minternalBalance)
      require ext_call.success
      log TokensReceivedSinceLastCheck(uint256 amount=(ext_call.return_data[0] - internalBalance))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


