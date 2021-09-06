# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x59752433DbE28f5aa59B479958689D353B3dee08 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    userBalances
# hash = 0x26224c64
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def userBalances(address m_param1): # not payable
  return muserBalancesm[m_param1m]


# hash = 0xccd6e5b6
# getter = None
# const = None
# payable = True
def unknownccd6e5b6(uint256 m_param1, addr m_param2) payable: 
  if m_param1 > muserBalancesm[callerm]:
      log Transfer(
            string name=Array(len=30, data='Amount greater than balance...'),
            address from=caller,
            address to=addr(_param2),
            uint256 amount=_param1)
  else:
      call m_param2 with:
         value m_param1 wei
           gas gas_remaining - 34050 wei
      if not ext_call.success:
          log Transfer(
                string name=Array(len=24, data='Call.value went wrong...'),
                address from=caller,
                address to=addr(_param2),
                uint256 amount=_param1)
      else:
          muserBalancesm[callerm] -= m_param1
          log Transfer(
                string name=Array(len=17, data='Payment executed.'),
                address from=caller,
                address to=addr(_param2),
                uint256 amount=_param1)


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  log Deposit(
        address sender=caller,
        uint256 value=call.value)
  muserBalancesm[callerm] += call.value


# hash = 0xf8b2cb4f
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def getBalance(address m_addressToCheck): # not payable
  return muserBalancesm[addr(m_addressToCheck)m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


