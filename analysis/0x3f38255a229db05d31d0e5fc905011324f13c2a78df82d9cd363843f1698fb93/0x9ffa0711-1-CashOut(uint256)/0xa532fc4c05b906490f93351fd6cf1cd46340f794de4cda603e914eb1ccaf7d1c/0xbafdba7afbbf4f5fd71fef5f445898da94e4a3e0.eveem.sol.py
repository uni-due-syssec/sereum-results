# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xBAFDba7afBBF4F5FD71feF5f445898DA94E4A3E0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    targetAddress # mask: a s
    # storage address 1
    owner # mask: a s
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  require caller == owner
  [93mselfdestruct([91mowner[93m)


# hash = 0x776d1a01
# getter = None
# const = None
# payable = False
def setTarget(address _target): # not payable
  require caller == owner
  require _target
  targetAddress = _target


# hash = 0x84054d3d
# getter = None
# const = None
# payable = True
def cashout() payable: 
  require caller == owner
  call targetAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value call.value wei
       gas gas_remaining - 34710 wei
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args call.value


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9890220b
# getter = None
# const = None
# payable = False
def drain(): # not payable
  require caller == owner
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args call.value


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  require caller == owner
  call targetAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value call.value wei
       gas gas_remaining - 34710 wei


# hash = 0xd4b83992
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def target(): # not payable
  return targetAddress


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args call.value


