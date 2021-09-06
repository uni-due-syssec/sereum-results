# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xBF78025535C98f4c605FBe9EAf672999aBf19Dc1 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    balances
# hash = 0x12b58349
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getTotalBalance = eth.balance(this.address)


# hash = 0x27e235e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def balances(address _param1): # not payable
  return balances[_param1]


# hash = 0x9a166299
# getter = None
# const = ['return', 'caller']
# payable = False
const getMyAddress = caller


# hash = 0xdb88031a
# getter = None
# const = None
# payable = False
def unknowndb88031a(): # not payable
  call caller with:
     value balances[caller] wei
       gas gas_remaining - 34710 wei
  balances[caller] = 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  balances[caller] += call.value


