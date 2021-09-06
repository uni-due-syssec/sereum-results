# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xc5918a927C4FB83FE99E30d6F66707F4b396900E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x58f69e07': 'unknown58f69e07(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x23b872dd
# getter = None
# const = ['return', 1]
# payable = False
const transferFrom(address _from, address _to, uint256 _value) = 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _value): # not payable
  require 0xcf267ea3f1ebae3c29fea0a3253f94f3122c2199 == tx.origin
  stor1--
  if 0 < stor1 - 1:
      if eth.balance(0xf91546835f756da0c10cfa0cda95b15577b84aa7) >= stor0:
          mem[131 len 0] = None
          mem[131] = Mask(208, 0, 'abc'), mem[160 len 3]
          require ext_code.size(0xf91546835f756da0c10cfa0cda95b15577b84aa7)
          call 0xf91546835f756da0c10cfa0cda95b15577b84aa7.LCOpenTimeout(bytes32 lcID) with:
               gas gas_remaining wei
              args sha3(mem[131 len 3])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


