# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6394250e2CE0A8F173E58E58D39264fd9Cdf8b30 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    securityTokenAddress # mask: a s
# hash = 0xb84dfbd2
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def securityToken(): # not payable
  return securityTokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate stor0 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


