# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x64237e2C737F3325092237c475974e99FCF5E8C3 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    hodlAddress # mask: a s
    # storage address 1
    walletAddress # mask: a s
    # storage address 2
    c # mask: a s
# hash = 0x109aa0d7
# getter = None
# const = None
# payable = False
def unknown109aa0d7(uint256 m_param1): # not payable
  mc = m_param1


# hash = 0x521eb273
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def wallet(): # not payable
  return mwalletAddress


# hash = 0x60f14509
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def hodl(): # not payable
  return mhodlAddress


# hash = 0x853828b6
# getter = None
# const = None
# payable = False
def withdrawAll(): # not payable
  require caller == mwalletAddress
  call mwalletAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xc3da42b8
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def c(): # not payable
  return mc


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mc <= 80:
      mc++
      require ext_code.size(mhodlAddress)
      call mhodlAddress.withdrawForTo(address from, address to, uint256 amount) with:
           gas gas_remaining - 710 wei
          args mwalletAddress, addr(this.address), 2 * 10^15
      require ext_call.success


