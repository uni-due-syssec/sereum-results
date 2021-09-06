# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x032bFe294ef20d3272B1e5ac960f9b84cE1690d5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    tokenAddress # mask: a s
    # storage address 2
    startTime # mask: a s
    # storage address 3
    endTime # mask: a s
    # storage address 4
    walletAddress # mask: a s
    # storage address 5
    rate # mask: a s
    # storage address 6
    weiRaised # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    maxPurchase # mask: a s
    # storage address 9
    minPurchase # mask: a s
    # storage address 10
    unknowneef9d905 # mask: a s
# hash = 0x1d412dcb
# getter = None
# const = None
# payable = False
def unknown1d412dcb(uint256 _param1): # not payable
  require owner == caller
  require _param1 > endTime
  endTime = _param1


# hash = 0x2c4e722e
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def rate(): # not payable
  return rate


# hash = 0x3197cbb6
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def endTime(): # not payable
  return endTime


# hash = 0x33b5b62e
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def minPurchase(): # not payable
  return minPurchase


# hash = 0x4042b66f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def weiRaised(): # not payable
  return weiRaised


# hash = 0x40582f13
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def getWeiRaised(): # not payable
  return weiRaised


# hash = 0x521eb273
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def wallet(): # not payable
  return walletAddress


# hash = 0x78e97925
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def startTime(): # not payable
  return startTime


# hash = 0x83408d73
# getter = None
# const = None
# payable = False
def burnRemainingTokens(): # not payable
  require owner == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.burnAll() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x977b055b
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def maxPurchase(): # not payable
  return maxPurchase


# hash = 0xc0ee0b8a
# getter = None
# const = ['return', 1]
# payable = False
const tokenFallback(address _from, uint256 _value, bytes _param3) = 1


# hash = 0xc2507ac1
# getter = None
# const = None
# payable = False
def getTokenAmount(uint256 _amount): # not payable
  if _amount:
      require rate * _amount / _amount == rate
      if _amount >= 10 * 10^18:
          if _amount >= 25 * 10^18:
              if _amount >= 100 * 10^18:
                  require (rate * _amount / 5) + (rate * _amount) >= rate * _amount
                  return ((rate * _amount / 5) + (rate * _amount))
              else:
                  if rate * _amount:
                      require 15 * rate * _amount / rate * _amount == 15
                      require (15 * rate * _amount / 100) + (rate * _amount) >= rate * _amount
                      return ((15 * rate * _amount / 100) + (rate * _amount))
                  else:
                      require rate * _amount >= rate * _amount
                      return (rate * _amount)
          else:
              if unknowneef9d905:
                  require rate * _amount >= rate * _amount
                  return (rate * _amount)
              else:
                  require (rate * _amount / 10) + (rate * _amount) >= rate * _amount
                  return ((rate * _amount / 10) + (rate * _amount))
      else:
          require rate * _amount >= rate * _amount
          return (rate * _amount)
  else:
      if _amount >= 10 * 10^18:
          if _amount >= 25 * 10^18:
              if _amount >= 100 * 10^18:
                  return 0
              else:
                  return 0
          else:
              if unknowneef9d905:
                  return 0
              else:
                  return 0
      else:
          return 0


# hash = 0xec8ac4d8
# getter = None
# const = None
# payable = True
def buyTokens(address _beneficiary) payable: 
  require _beneficiary
  if block.timestamp < startTime:
      require ext_code.size(stor7)
      call stor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args _beneficiary
      require ext_call.success
      require block.timestamp >= startTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= maxPurchase
      require call.value >= minPurchase
      if call.value:
          require rate * call.value / call.value == rate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (rate * call.value / 5) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 5) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), (rate * call.value / 5) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if rate * call.value:
                          require 15 * rate * call.value / rate * call.value == 15
                          require (15 * rate * call.value / 100) + (rate * call.value) >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * rate * call.value / 100) + (rate * call.value) <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(_beneficiary), (15 * rate * call.value / 100) + (rate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require rate * call.value >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require rate * call.value <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(_beneficiary), rate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if unknowneef9d905:
                      require rate * call.value >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require rate * call.value <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), rate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (rate * call.value / 10) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 10) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), (rate * call.value / 10) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require rate * call.value >= rate * call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require rate * call.value <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_beneficiary), rate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if unknowneef9d905:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_beneficiary), 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
  else:
      require ext_code.size(stor7)
      call stor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args _beneficiary
      require ext_call.success
      require block.timestamp <= endTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= maxPurchase
      require call.value >= minPurchase
      if call.value:
          require rate * call.value / call.value == rate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (rate * call.value / 5) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 5) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), (rate * call.value / 5) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if rate * call.value:
                          require 15 * rate * call.value / rate * call.value == 15
                          require (15 * rate * call.value / 100) + (rate * call.value) >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * rate * call.value / 100) + (rate * call.value) <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(_beneficiary), (15 * rate * call.value / 100) + (rate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require rate * call.value >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require rate * call.value <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(_beneficiary), rate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if unknowneef9d905:
                      require rate * call.value >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require rate * call.value <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), rate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (rate * call.value / 10) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 10) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), (rate * call.value / 10) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require rate * call.value >= rate * call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require rate * call.value <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_beneficiary), rate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if unknowneef9d905:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_beneficiary), 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop


# hash = 0xecb70fb7
# getter = None
# const = None
# payable = False
def hasEnded(): # not payable
  return (block.timestamp > endTime)


# hash = 0xeef9d905
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def unknowneef9d905(): # not payable
  return bool(unknowneef9d905)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require owner == caller
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def token(): # not payable
  return tokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require caller
  if block.timestamp < startTime:
      require ext_code.size(stor7)
      call stor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args caller
      require ext_call.success
      require block.timestamp >= startTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= maxPurchase
      require call.value >= minPurchase
      if call.value:
          require rate * call.value / call.value == rate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (rate * call.value / 5) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 5) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (rate * call.value / 5) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if rate * call.value:
                          require 15 * rate * call.value / rate * call.value == 15
                          require (15 * rate * call.value / 100) + (rate * call.value) >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * rate * call.value / 100) + (rate * call.value) <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, (15 * rate * call.value / 100) + (rate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=caller)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require rate * call.value >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require rate * call.value <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, rate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=caller)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if unknowneef9d905:
                      require rate * call.value >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require rate * call.value <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, rate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (rate * call.value / 10) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 10) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (rate * call.value / 10) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require rate * call.value >= rate * call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require rate * call.value <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, rate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=caller)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if unknowneef9d905:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=caller)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
  else:
      require ext_code.size(stor7)
      call stor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args caller
      require ext_call.success
      require block.timestamp <= endTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= maxPurchase
      require call.value >= minPurchase
      if call.value:
          require rate * call.value / call.value == rate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (rate * call.value / 5) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 5) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (rate * call.value / 5) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if rate * call.value:
                          require 15 * rate * call.value / rate * call.value == 15
                          require (15 * rate * call.value / 100) + (rate * call.value) >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * rate * call.value / 100) + (rate * call.value) <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, (15 * rate * call.value / 100) + (rate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=caller)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require rate * call.value >= rate * call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require rate * call.value <= ext_call.return_data[0]
                          require call.value + weiRaised >= weiRaised
                          weiRaised += call.value
                          require ext_code.size(tokenAddress)
                          call tokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, rate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=caller)
                          call walletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if unknowneef9d905:
                              stop
                          else:
                              require ext_code.size(stor7)
                              call stor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if unknowneef9d905:
                      require rate * call.value >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require rate * call.value <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, rate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (rate * call.value / 10) + (rate * call.value) >= rate * call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (rate * call.value / 10) + (rate * call.value) <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (rate * call.value / 10) + (rate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require rate * call.value >= rate * call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require rate * call.value <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, rate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=caller)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if unknowneef9d905:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(tokenAddress)
                      call tokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + weiRaised >= weiRaised
                      weiRaised += call.value
                      require ext_code.size(tokenAddress)
                      call tokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call walletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if unknowneef9d905:
                          stop
                      else:
                          require ext_code.size(stor7)
                          call stor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(tokenAddress)
              call tokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + weiRaised >= weiRaised
              weiRaised += call.value
              require ext_code.size(tokenAddress)
              call tokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=caller)
              call walletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if unknowneef9d905:
                  stop
              else:
                  require ext_code.size(stor7)
                  call stor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop


