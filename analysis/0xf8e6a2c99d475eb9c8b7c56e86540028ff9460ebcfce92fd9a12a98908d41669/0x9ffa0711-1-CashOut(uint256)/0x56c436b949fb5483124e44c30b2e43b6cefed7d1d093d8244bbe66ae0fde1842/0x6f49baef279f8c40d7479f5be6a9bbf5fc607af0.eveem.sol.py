# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6f49BAEF279f8c40D7479f5Be6a9bBF5fc607af0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if mstor0 != caller:
      stop
  [93mselfdestruct([91mstor0[93m)


# hash = 0xb29f0835
# getter = None
# const = None
# payable = True
def unknownb29f0835() payable: 
  log 0x3984f38c: eth.balance(this.address), caller
  require ext_code.size(mstor1)
  call mstor1.Deposit() with:
     value call.value wei
       gas gas_remaining - 9710 wei
  require ext_call.success
  require ext_code.size(mstor1)
  call mstor1.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args call.value
  require ext_call.success


# hash = 0xf2a75fe4
# getter = None
# const = None
# payable = False
def empty(): # not payable
  if caller == mstor0:
      call caller with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  log 0x69f1113d: eth.balance(stor1), stor1
  if call.value <= eth.balance(mstor1):
      require ext_code.size(mstor1)
      call mstor1.CashOut(uint256 amount) with:
           gas gas_remaining - 710 wei
          args call.value
      require ext_call.success


