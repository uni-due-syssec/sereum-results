# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xcac115B0E6876fe3b13aE16d5CE27F717C88Fb21 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknownd0e0b167Address # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x78018bb7
# getter = None
# const = None
# payable = True
def unknown78018bb7() payable: 
  call munknownd0e0b167Address with:
     value call.value wei
       gas 200000 wei


# hash = 0x8e72f3d9
# getter = None
# const = None
# payable = True
def unknown8e72f3d9() payable: 
  call mstor1 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xd0e0b167
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknownd0e0b167(): # not payable
  return munknownd0e0b167Address


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  call munknownd0e0b167Address with:
       gas 200000 wei


