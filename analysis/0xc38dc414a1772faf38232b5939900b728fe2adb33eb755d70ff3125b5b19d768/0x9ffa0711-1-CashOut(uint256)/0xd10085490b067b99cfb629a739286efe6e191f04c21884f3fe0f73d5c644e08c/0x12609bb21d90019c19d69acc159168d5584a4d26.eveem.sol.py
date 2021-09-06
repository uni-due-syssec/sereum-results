# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x12609bB21D90019C19d69aCc159168d5584A4D26 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    targetAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    unknown8993b2bc # mask: a s
# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  require caller == owner
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


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


# hash = 0x80e9071b
# getter = None
# const = None
# payable = False
def reclaim(): # not payable
  require caller == owner
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args 10^18


# hash = 0x84054d3d
# getter = None
# const = None
# payable = True
def cashout() payable: 
  require caller == owner
  require call.value >= 10^18
  call targetAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value call.value wei
       gas gas_remaining - 34710 wei
  stor1 = 1
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args call.value
  call targetAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args eth.balance(targetAddress)


# hash = 0x8993b2bc
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = False
def unknown8993b2bc(): # not payable
  return bool(unknown8993b2bc)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


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
  if unknown8993b2bc:
      stor1 = 0
      call targetAddress with:
         funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
           gas gas_remaining - 25710 wei
          args 1


