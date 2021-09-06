# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x48B31F384cd6D93494740d661D96272061Fd5dd1 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x776d1a01
# getter = None
# const = None
# payable = False
def setTarget(address _target): # not payable
  require caller == owner
  stor1 = _target


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xa9e732bb
# getter = None
# const = None
# payable = True
def cashout(uint256 _amount) payable: 
  require caller == owner
  require ext_code.size(stor1)
  call stor1.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args _amount
  require ext_call.success


# hash = 0xbe9a6555
# getter = None
# const = None
# payable = True
def start() payable: 
  require caller == owner
  require stor1
  require ext_code.size(stor1)
  call stor1.Deposit() with:
     value call.value wei
       gas gas_remaining - 9710 wei
  require ext_call.success
  require ext_code.size(stor1)
  call stor1.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args call.value
  require ext_call.success


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  require caller == owner
  require ext_code.size(stor1)
  call stor1.Deposit() with:
     value call.value wei
       gas gas_remaining - 9710 wei
  require ext_call.success


# hash = 0xf2a75fe4
# getter = None
# const = None
# payable = False
def empty(): # not payable
  require caller == owner
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if 10^17 <= eth.balance(stor1):
      require ext_code.size(stor1)
      call stor1.CashOut(uint256 amount) with:
           gas gas_remaining - 710 wei
          args 10^17
      require ext_call.success


