# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa81aBc1C22F0c3faBd55Ae850aae563341C939D8 
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
def unknown1d412dcb(uint256 m_param1): # not payable
  require mowner == caller
  require m_param1 > mendTime
  mendTime = m_param1


# hash = 0x2c4e722e
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def rate(): # not payable
  return mrate


# hash = 0x3197cbb6
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def endTime(): # not payable
  return mendTime


# hash = 0x33b5b62e
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def minPurchase(): # not payable
  return mminPurchase


# hash = 0x4042b66f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def weiRaised(): # not payable
  return mweiRaised


# hash = 0x40582f13
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def getWeiRaised(): # not payable
  return mweiRaised


# hash = 0x521eb273
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def wallet(): # not payable
  return mwalletAddress


# hash = 0x78e97925
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def startTime(): # not payable
  return mstartTime


# hash = 0x83408d73
# getter = None
# const = None
# payable = False
def burnRemainingTokens(): # not payable
  require mowner == caller
  require ext_code.size(mtokenAddress)
  call mtokenAddress.burnAll() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x977b055b
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def maxPurchase(): # not payable
  return mmaxPurchase


# hash = 0xc0ee0b8a
# getter = None
# const = ['return', 1]
# payable = False
const tokenFallback(address m_from, uint256 m_value, bytes m_param3) = 1


# hash = 0xc2507ac1
# getter = None
# const = None
# payable = False
def getTokenAmount(uint256 m_amount): # not payable
  if m_amount:
      require mrate * m_amount / m_amount == mrate
      if m_amount >= 10 * 10^18:
          if m_amount >= 25 * 10^18:
              if m_amount >= 100 * 10^18:
                  require (mrate * m_amount / 5) + (mrate * m_amount) >= mrate * m_amount
                  return ((mrate * m_amount / 5) + (mrate * m_amount))
              else:
                  if mrate * m_amount:
                      require 15 * mrate * m_amount / mrate * m_amount == 15
                      require (15 * mrate * m_amount / 100) + (mrate * m_amount) >= mrate * m_amount
                      return ((15 * mrate * m_amount / 100) + (mrate * m_amount))
                  else:
                      require mrate * m_amount >= mrate * m_amount
                      return (mrate * m_amount)
          else:
              if munknowneef9d905:
                  require mrate * m_amount >= mrate * m_amount
                  return (mrate * m_amount)
              else:
                  require (mrate * m_amount / 10) + (mrate * m_amount) >= mrate * m_amount
                  return ((mrate * m_amount / 10) + (mrate * m_amount))
      else:
          require mrate * m_amount >= mrate * m_amount
          return (mrate * m_amount)
  else:
      if m_amount >= 10 * 10^18:
          if m_amount >= 25 * 10^18:
              if m_amount >= 100 * 10^18:
                  return 0
              else:
                  return 0
          else:
              if munknowneef9d905:
                  return 0
              else:
                  return 0
      else:
          return 0


# hash = 0xec8ac4d8
# getter = None
# const = None
# payable = True
def buyTokens(address m_beneficiary) payable: 
  require m_beneficiary
  if block.timestamp < mstartTime:
      require ext_code.size(mstor7)
      call mstor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args m_beneficiary
      require ext_call.success
      require block.timestamp >= mstartTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= mmaxPurchase
      require call.value >= mminPurchase
      if call.value:
          require mrate * call.value / call.value == mrate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (mrate * call.value / 5) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 5) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), (mrate * call.value / 5) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if mrate * call.value:
                          require 15 * mrate * call.value / mrate * call.value == 15
                          require (15 * mrate * call.value / 100) + (mrate * call.value) >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * mrate * call.value / 100) + (mrate * call.value) <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_beneficiary), (15 * mrate * call.value / 100) + (mrate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require mrate * call.value >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require mrate * call.value <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_beneficiary), mrate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if munknowneef9d905:
                      require mrate * call.value >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require mrate * call.value <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), mrate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (mrate * call.value / 10) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 10) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), (mrate * call.value / 10) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require mrate * call.value >= mrate * call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require mrate * call.value <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_beneficiary), mrate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if munknowneef9d905:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_beneficiary), 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
  else:
      require ext_code.size(mstor7)
      call mstor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args m_beneficiary
      require ext_call.success
      require block.timestamp <= mendTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= mmaxPurchase
      require call.value >= mminPurchase
      if call.value:
          require mrate * call.value / call.value == mrate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (mrate * call.value / 5) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 5) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), (mrate * call.value / 5) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if mrate * call.value:
                          require 15 * mrate * call.value / mrate * call.value == 15
                          require (15 * mrate * call.value / 100) + (mrate * call.value) >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * mrate * call.value / 100) + (mrate * call.value) <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_beneficiary), (15 * mrate * call.value / 100) + (mrate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require mrate * call.value >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require mrate * call.value <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_beneficiary), mrate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=_beneficiary)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if munknowneef9d905:
                      require mrate * call.value >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require mrate * call.value <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), mrate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (mrate * call.value / 10) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 10) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), (mrate * call.value / 10) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require mrate * call.value >= mrate * call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require mrate * call.value <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_beneficiary), mrate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if munknowneef9d905:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_beneficiary), 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=_beneficiary)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_beneficiary), 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=_beneficiary)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop


# hash = 0xecb70fb7
# getter = None
# const = None
# payable = False
def hasEnded(): # not payable
  return (block.timestamp > mendTime)


# hash = 0xeef9d905
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def unknowneef9d905(): # not payable
  return bool(munknowneef9d905)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require mowner == caller
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def token(): # not payable
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require caller
  if block.timestamp < mstartTime:
      require ext_code.size(mstor7)
      call mstor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args caller
      require ext_call.success
      require block.timestamp >= mstartTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= mmaxPurchase
      require call.value >= mminPurchase
      if call.value:
          require mrate * call.value / call.value == mrate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (mrate * call.value / 5) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 5) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (mrate * call.value / 5) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if mrate * call.value:
                          require 15 * mrate * call.value / mrate * call.value == 15
                          require (15 * mrate * call.value / 100) + (mrate * call.value) >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * mrate * call.value / 100) + (mrate * call.value) <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, (15 * mrate * call.value / 100) + (mrate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=caller)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require mrate * call.value >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require mrate * call.value <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, mrate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=caller)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if munknowneef9d905:
                      require mrate * call.value >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require mrate * call.value <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, mrate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (mrate * call.value / 10) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 10) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (mrate * call.value / 10) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require mrate * call.value >= mrate * call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require mrate * call.value <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mrate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=caller)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if munknowneef9d905:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=caller)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
  else:
      require ext_code.size(mstor7)
      call mstor7.isAddressWhitelisted(address addr) with:
           gas gas_remaining wei
          args caller
      require ext_call.success
      require block.timestamp <= mendTime
      require call.value
      require ext_call.return_data[0]
      require call.value <= mmaxPurchase
      require call.value >= mminPurchase
      if call.value:
          require mrate * call.value / call.value == mrate
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require (mrate * call.value / 5) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 5) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (mrate * call.value / 5) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 5) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      if mrate * call.value:
                          require 15 * mrate * call.value / mrate * call.value == 15
                          require (15 * mrate * call.value / 100) + (mrate * call.value) >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require (15 * mrate * call.value / 100) + (mrate * call.value) <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, (15 * mrate * call.value / 100) + (mrate * call.value)
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=(15 * rate * call.value / 100) + (rate * call.value),
                                uint256 value=caller,
                                uint256 amount=caller)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
                      else:
                          require mrate * call.value >= mrate * call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          require ext_call.success
                          require mrate * call.value <= ext_call.return_data[0]
                          require call.value + mweiRaised >= mweiRaised
                          mweiRaised += call.value
                          require ext_code.size(mtokenAddress)
                          call mtokenAddress.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, mrate * call.value
                          require ext_call.success
                          log TokenPurchase(
                                address purchaser=call.value,
                                address beneficiary=rate * call.value,
                                uint256 value=caller,
                                uint256 amount=caller)
                          call mwalletAddress with:
                             value call.value wei
                               gas 2300 * is_zero(value) wei
                          if munknowneef9d905:
                              stop
                          else:
                              require ext_code.size(mstor7)
                              call mstor7.0x50c1bdf2 with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              require ext_call.success
                              stop
              else:
                  if munknowneef9d905:
                      require mrate * call.value >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require mrate * call.value <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, mrate * call.value
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=rate * call.value,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require (mrate * call.value / 10) + (mrate * call.value) >= mrate * call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require (mrate * call.value / 10) + (mrate * call.value) <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, (mrate * call.value / 10) + (mrate * call.value)
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=(rate * call.value / 10) + (rate * call.value),
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require mrate * call.value >= mrate * call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require mrate * call.value <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mrate * call.value
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=rate * call.value,
                    uint256 value=caller,
                    uint256 amount=caller)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop
      else:
          if call.value >= 10 * 10^18:
              if call.value >= 25 * 10^18:
                  if call.value >= 100 * 10^18:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
              else:
                  if munknowneef9d905:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
                  else:
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      require ext_call.success
                      require 0 <= ext_call.return_data[0]
                      require call.value + mweiRaised >= mweiRaised
                      mweiRaised += call.value
                      require ext_code.size(mtokenAddress)
                      call mtokenAddress.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, 0
                      require ext_call.success
                      log TokenPurchase(
                            address purchaser=call.value,
                            address beneficiary=0,
                            uint256 value=caller,
                            uint256 amount=caller)
                      call mwalletAddress with:
                         value call.value wei
                           gas 2300 * is_zero(value) wei
                      if munknowneef9d905:
                          stop
                      else:
                          require ext_code.size(mstor7)
                          call mstor7.0x50c1bdf2 with:
                               gas gas_remaining wei
                              args caller, call.value
                          require ext_call.success
                          stop
          else:
              require ext_code.size(mtokenAddress)
              call mtokenAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              require ext_call.success
              require 0 <= ext_call.return_data[0]
              require call.value + mweiRaised >= mweiRaised
              mweiRaised += call.value
              require ext_code.size(mtokenAddress)
              call mtokenAddress.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, 0
              require ext_call.success
              log TokenPurchase(
                    address purchaser=call.value,
                    address beneficiary=0,
                    uint256 value=caller,
                    uint256 amount=caller)
              call mwalletAddress with:
                 value call.value wei
                   gas 2300 * is_zero(value) wei
              if munknowneef9d905:
                  stop
              else:
                  require ext_code.size(mstor7)
                  call mstor7.0x50c1bdf2 with:
                       gas gas_remaining wei
                      args caller, call.value
                  require ext_call.success
                  stop


