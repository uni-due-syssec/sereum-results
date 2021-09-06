# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1aF6f5bE9B2Ff68901d4e094299c8b92ED54AF51 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    count # mask: a s
# hash = 0x06661abd
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def count(): # not payable
  return mcount


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require caller == mstor0
  [93mselfdestruct([91mstor0[93m)


# hash = 0x97ec642c
# getter = None
# const = ['return', 2000000000000000]
# payable = False
const MAX_WITHDRAWAL = 2 * 10^15


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mcount < 8:
      mcount++
      require ext_code.size(caller)
      call caller.withdrawForTo(address from, address to, uint256 amount) with:
           gas gas_remaining wei
          args mstor0, addr(this.address), 2 * 10^15
      require ext_call.success


