# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x26b8aF052895080148dabBC1007b3045f023916E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    balances
# hash = 0x27e235e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def balances(address _param1): # not payable
  return balances[_param1]


# hash = 0x46d6c084
# getter = None
# const = None
# payable = True
def unknown46d6c084() payable: 
  stop


# hash = 0x549262ba
# getter = None
# const = None
# payable = True
def put() payable: 
  balances[caller] = call.value


# hash = 0x6d4ce63c
# getter = None
# const = None
# payable = False
def get(): # not payable
  call caller with:
     value balances[caller] wei
       gas gas_remaining - 34050 wei
  require ext_call.success
  balances[caller] = 0


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  revert 


