# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4d2f5cFbA55AE412221182D8475bC85799A5644b 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate 0x2157a7894439191e520825fe9399ab8655e0f708 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  require delegate.return_code
  return delegate.return_data[0 len 4096]


