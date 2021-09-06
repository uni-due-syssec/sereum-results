# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xE752B7D837A6969A5986467B0109bdF052e45bdB 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x10639ea0
# getter = None
# const = None
# payable = False
def cancelMigration(): # not payable
  if mstor0 != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'Forwarder cancelMigration failed - msg.sender must be current corp bank'
  addr(mstor1m.field_0) = 0
  return 1


# hash = 0x200d2ed2
# getter = None
# const = None
# payable = False
def status(): # not payable
  return mstor0, addr(mstor1m.field_0), bool(uint8(mstor1m.field_160))


# hash = 0x66d38203
# getter = None
# const = None
# payable = False
def setup(address m_xrt): # not payable
  if bool(uint8(mstor1m.field_160)) != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'Forwarder setup failed - corp bank already registered'
  mstor0 = m_xrt
  uint8(mstor1m.field_160) = 0


# hash = 0x88d761f2
# getter = None
# const = None
# payable = False
def finishMigration(): # not payable
  if addr(mstor1m.field_0) != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'Forwarder finishMigration failed - msg.sender must be new corp bank'
  mstor0 = addr(mstor1m.field_0)
  addr(mstor1m.field_0) = 0
  return 1


# hash = 0xa0f52da0
# getter = None
# const = None
# payable = False
def startMigration(address m_newCorpBank): # not payable
  if mstor0 != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'Forwarder startMigration failed - msg.sender must be current corp bank'
  require ext_code.size(m_newCorpBank)
  call m_newCorpBank.migrationReceiver_setup() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      return 0
  addr(mstor1m.field_0) = m_newCorpBank
  return 1


# hash = 0xd021bff5
# getter = None
# const = None
# payable = False
def unknownd021bff5(): # not payable
  require caller == 0xd3049b671c9818e0896f34ec4ad0bb58fe1248e5
  [93mselfdestruct([91mcaller[93m)


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  if 0 >= call.value:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'Forwarder Deposit failed - zero deposits not allowed'
  if uint8(mstor1m.field_160):
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Forwarder Deposit failed - no registered bank'
  require ext_code.size(mstor0)
  call mstor0.deposit(address payee) with:
     value call.value wei
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      return 0
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require ext_code.size(mstor0)
  call mstor0.deposit(address payee) with:
     value eth.balance(this.address) wei
       gas gas_remaining wei
      args mstor0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


