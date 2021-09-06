# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF01FE1A15673A5209C94121C45E2121FE2903416 
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
# payable = True
def balances(address m_param1) payable: 
  return mbalancesm[m_param1m]


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = True
def withdrawBalance() payable: 
  call caller with:
     value mbalancesm[callerm] wei
       gas gas_remaining - 34050 wei
  require ext_call.success
  mbalancesm[callerm] = 0


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  mbalancesm[callerm] += 10^17


# hash = 0xf8b2cb4f
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = True
def getBalance(address m_addressToCheck) payable: 
  return mbalancesm[addr(m_addressToCheck)m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


