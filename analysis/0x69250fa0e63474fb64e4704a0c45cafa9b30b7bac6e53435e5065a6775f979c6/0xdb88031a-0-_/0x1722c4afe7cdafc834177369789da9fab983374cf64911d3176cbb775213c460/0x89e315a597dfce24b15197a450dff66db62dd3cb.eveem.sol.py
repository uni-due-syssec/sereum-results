# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x89e315a597dFcE24b15197A450DfF66db62dd3cb 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
# hash = 0x1b9265b8
# getter = None
# const = None
# payable = True
def pay() payable: 
  stop


# hash = 0x40c82671
# getter = None
# const = None
# payable = False
def unknown40c82671(uint256 m_param1): # not payable
  call mstor0 with:
     value m_param1 wei
       gas gas_remaining - 34710 wei
  require ext_code.size(mstor0)
  call mstor0.0xdb88031a with:
       gas gas_remaining - 710 wei
  require ext_call.success


# hash = 0x63bd1d4a
# getter = None
# const = None
# payable = False
def payout(): # not payable
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei


# hash = 0xd1d80fdf
# getter = None
# const = None
# payable = False
def setAddr(address m_addr): # not payable
  mstor0 = m_addr


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require ext_code.size(mstor0)
  call mstor0.0xdb88031a with:
       gas gas_remaining - 710 wei
  require ext_call.success


