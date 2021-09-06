# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x10AC721a0CC85C7Fa4664E358c2e6E683C50F73f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
# hash = 0x090d23b9
# getter = None
# const = None
# payable = False
def setBank(address m_bank): # not payable
  require caller == mstor0
  mstor2 = m_bank


# hash = 0x2e64cec1
# getter = None
# const = None
# payable = False
def unknown2e64cec1(): # not payable
  require caller == mstor0
  [93mselfdestruct([91mstor0[93m)


# hash = 0x98e1b410
# getter = None
# const = None
# payable = False
def getMoney(): # not payable
  require caller == mstor0
  require ext_code.size(mstor2)
  call mstor2.Deposit() with:
     value 10^18 wei
       gas gas_remaining - 9710 wei
  require ext_call.success
  mstor1 = 2
  require ext_code.size(mstor2)
  call mstor2.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args 10^18
  require ext_call.success
  require eth.balance(this.address) >= eth.balance(this.address)


# hash = 0xcca955a0
# getter = None
# const = None
# payable = True
def unknowncca955a0() payable: 
  stop


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mstor1 > 0:
      mstor1--
      require ext_code.size(mstor2)
      call mstor2.balances(address param1) with:
           gas gas_remaining - 710 wei
          args this.address
      require ext_call.success
      require ext_code.size(mstor2)
      call mstor2.CashOut(uint256 amount) with:
           gas gas_remaining - 710 wei
          args ext_call.return_data[0]
      require ext_call.success


