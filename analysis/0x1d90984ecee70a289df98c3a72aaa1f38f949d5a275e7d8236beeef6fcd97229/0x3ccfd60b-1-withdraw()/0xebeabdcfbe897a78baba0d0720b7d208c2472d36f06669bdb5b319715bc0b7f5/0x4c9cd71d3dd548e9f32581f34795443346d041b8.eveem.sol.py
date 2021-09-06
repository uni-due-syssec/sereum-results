# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4c9cD71D3dD548e9f32581F34795443346d041B8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x3c183c10
# getter = None
# const = None
# payable = True
def unknown3c183c10() payable: 
  call mstor1 with:
     value call.value wei
       gas gas_remaining wei
  require ext_code.size(mstor1)
  call mstor1.withdraw() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require eth.balance(this.address) > eth.balance(this.address)


# hash = 0x98e1b410
# getter = None
# const = None
# payable = False
def getMoney(): # not payable
  require caller == mstor0
  [93mselfdestruct([91mstor0[93m)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if eth.balance(mstor1) > 0:
      require ext_code.size(mstor1)
      call mstor1.withdraw() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


