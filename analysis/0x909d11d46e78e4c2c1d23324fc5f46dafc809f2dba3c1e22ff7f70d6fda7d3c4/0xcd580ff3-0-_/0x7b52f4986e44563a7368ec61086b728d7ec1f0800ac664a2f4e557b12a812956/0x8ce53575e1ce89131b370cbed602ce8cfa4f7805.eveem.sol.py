# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8ce53575E1ce89131b370CbeD602ce8cFA4F7805 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    balances
# hash = 0x27e235e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def balances(address _param1): # not payable
  return balances[_param1]


# hash = 0x2b68b9c6
# getter = None
# const = None
# payable = False
def destruct(): # not payable
  require caller == owner
  [93mselfdestruct([91mowner[93m)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xc68d81e0
# getter = None
# const = None
# payable = True
def unknownc68d81e0(addr _param1) payable: 
  balances[addr(_param1)] += call.value


# hash = 0xcd580ff3
# getter = None
# const = None
# payable = False
def unknowncd580ff3(uint256 _param1): # not payable
  if _param1 <= balances[caller]:
      call caller with:
         value _param1 wei
           gas gas_remaining wei
      balances[caller] -= _param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


