# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xaE32A0e6EceCFcA06aE2045f0d01C7d8AaD183B9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 0
    stor0 # mask: a s
# hash = 0x87f14e6f
# getter = None
# const = None
# payable = False
def unknown87f14e6f(): # not payable
  require mowner == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0xacec338a
# getter = None
# const = None
# payable = False
def setActive(bool m_active): # not payable
  require mowner == caller
  Mask(96, 0, mstor0m.field_160) = Mask(96, 0, m_active)


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  stop


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require mowner == caller
  require m_newOwner
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if not uint8(mstor0m.field_160):
      require mowner == tx.origin


