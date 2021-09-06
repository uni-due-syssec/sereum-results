# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x50D407244892244634043d65AB4388988650EEc0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    bankAddress # mask: a s
    # storage address 1
    owner # mask: a s
# hash = 0x2e1a7d4d
# getter = None
# const = None
# payable = True
def withdraw(uint256 _wdamount) payable: 
  require calldata.size - 4 >= 32
  require caller == owner
  call owner with:
     value _wdamount wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = True
def withdraw() payable: 
  require caller == owner
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  require caller == owner
  [93mselfdestruct([91mcaller[93m)


# hash = 0x76cdb03b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def bank(): # not payable
  return bankAddress


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xbe80d447
# getter = None
# const = None
# payable = True
def unknownbe80d447() payable: 
  require ext_code.size(bankAddress)
  call bankAddress.withdraw(uint256 wdamount) with:
       gas gas_remaining wei
      args 10^18
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  require call.value >= 10^18
  require ext_code.size(bankAddress)
  call bankAddress.deposit() with:
     value 10^18 wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require ext_code.size(bankAddress)
  call bankAddress.withdraw(uint256 wdamount) with:
       gas gas_remaining wei
      args 10^18
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


