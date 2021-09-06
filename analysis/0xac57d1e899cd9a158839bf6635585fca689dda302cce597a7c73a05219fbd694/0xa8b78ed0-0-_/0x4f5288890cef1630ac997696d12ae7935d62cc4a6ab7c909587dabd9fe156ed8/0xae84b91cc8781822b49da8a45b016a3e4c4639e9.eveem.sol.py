# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAe84B91cC8781822b49Da8A45B016A3E4C4639e9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xa6f9dae1
# getter = None
# const = None
# payable = False
def changeOwner(address _newOwner): # not payable
  if owner == caller:
      owner = _newOwner


# hash = 0xb808b43d
# getter = None
# const = None
# payable = False
def unknownb808b43d(): # not payable
  if owner != caller:
      stop
  require block.timestamp >= stor1
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require block.timestamp < stor1
  require call.value >= stor2
  require ext_code.size(owner)
  call owner.0x8889218 with:
       gas gas_remaining - 50 wei
      args caller, call.value
  require ext_call.success


