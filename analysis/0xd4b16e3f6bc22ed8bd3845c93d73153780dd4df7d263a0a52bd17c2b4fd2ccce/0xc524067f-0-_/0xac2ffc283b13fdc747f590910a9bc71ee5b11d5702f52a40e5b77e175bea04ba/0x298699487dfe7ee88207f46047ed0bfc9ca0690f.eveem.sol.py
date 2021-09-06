# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x298699487dFE7EE88207F46047ED0BFC9cA0690f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0xd4b83992
# getter = None
# const = ['return', 834372416802631139485793267967982352710663660933]
# payable = False
const target = 0x92268d9c15657f14c9b0d551b97e260467dbe585


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require ext_code.size(0x92268d9c15657f14c9b0d551b97e260467dbe585) > 0
  [93mdelegate 0x92268d9c15657f14c9b0d551b97e260467dbe585 with:
     funct call.data[0 len 4]
       gas gas_remaining - 10000 wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


