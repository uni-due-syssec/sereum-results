# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xcFc448d29f342273fEb6653d2769dDb1a530cbb1 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
# hash = 0x1b9265b8
# getter = None
# const = None
# payable = True
def pay() payable: 
  stop


# hash = 0x40c82671
# getter = None
# const = None
# payable = False
def unknown40c82671(uint256 _param1): # not payable
  call stor0 with:
     value _param1 wei
       gas gas_remaining - 34710 wei
  require ext_code.size(stor0)
  call stor0.0xdb88031a with:
       gas gas_remaining - 710 wei
  require ext_call.success


# hash = 0xd1d80fdf
# getter = None
# const = None
# payable = False
def setAddr(address _addr): # not payable
  stor0 = _addr


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require ext_code.size(stor0)
  call stor0.0xdb88031a with:
       gas gas_remaining - 710 wei
  require ext_call.success


