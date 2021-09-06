# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7bcD4b25419399903Ec96Fe8e1065224fEad8F3B 
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
  return mowner


# hash = 0xa6f9dae1
# getter = None
# const = None
# payable = False
def changeOwner(address m_newOwner): # not payable
  if mowner == caller:
      mowner = m_newOwner


# hash = 0xb808b43d
# getter = None
# const = None
# payable = False
def unknownb808b43d(): # not payable
  if mowner != caller:
      stop
  require block.timestamp >= mstor1
  call mowner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require block.timestamp < mstor1
  require call.value >= mstor2
  require ext_code.size(mowner)
  call mowner.0x8889218 with:
       gas gas_remaining - 50 wei
      args caller, call.value
  require ext_call.success


