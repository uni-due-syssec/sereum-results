# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x87F53784494C693d1Ea80aAfFfaF53b547B87df5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    tokenAddress # mask: a s
# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0xaf7d6ca3
# getter = None
# const = None
# payable = False
def spend(address m_key, uint256 m_amount): # not payable
  require caller == mowner
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_key), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Token transfer could not be executed.'


# hash = 0xdf8de3e7
# getter = None
# const = None
# payable = False
def claimTokens(address m_token): # not payable
  require caller == mowner
  if m_token:
      require ext_code.size(m_token)
      call m_token.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(m_token)
          call m_token.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mowner, ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Token transfer could not be executed.'
              else:
                  log ClaimedTokens(
                        address token=ext_call.return_data[0],
                        address controller=_token,
                        uint256 amount=owner)
                  stop
  else:
      call mowner with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          stop


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
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
  revert


