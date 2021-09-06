# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x22f32524A1eDf73d192737e869a8881fc95A8c15 
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


