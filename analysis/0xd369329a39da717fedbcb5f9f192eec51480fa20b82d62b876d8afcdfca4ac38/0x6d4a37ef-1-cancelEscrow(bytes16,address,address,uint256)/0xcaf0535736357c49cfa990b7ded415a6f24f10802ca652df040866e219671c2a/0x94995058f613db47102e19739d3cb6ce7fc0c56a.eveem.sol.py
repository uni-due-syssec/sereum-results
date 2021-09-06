# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x94995058F613Db47102E19739D3CB6Ce7FC0c56a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
# hash = 0x2e01d229
# getter = None
# const = None
# payable = False
def unknown2e01d229(addr m_param1): # not payable
  require mowner == caller
  addr(mstor1m.field_0) = m_param1


# hash = 0x87f14e6f
# getter = None
# const = None
# payable = False
def unknown87f14e6f(): # not payable
  require mowner == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei


# hash = 0x88836eb5
# getter = None
# const = None
# payable = False
def unknown88836eb5(uint128 m_param1, addr m_param2, addr m_param3, uint256 m_param4): # not payable
  require mowner == caller
  mstor3 = m_param1
  mstor4 = m_param2
  mstor5 = m_param3
  mstor6 = m_param4


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9e5faafc
# getter = None
# const = None
# payable = False
def attack(): # not payable
  require mowner == caller
  uint8(mstor1m.field_160) = 0
  require ext_code.size(addr(mstor1m.field_0))
  call addr(mstor1m.field_0).cancelEscrow(bytes16 tradeID, address seller, address buyer, uint256 value) with:
       gas gas_remaining - 710 wei
      args 0, 0, mstor4, mstor5, mstor6
  require ext_call.success


# hash = 0xb0eefabe
# getter = None
# const = None
# payable = False
def setArbitrator(address m_newArbitrator): # not payable
  require mowner == caller
  require ext_code.size(addr(mstor1m.field_0))
  call addr(mstor1m.field_0).setArbitrator(address newArbitrator) with:
       gas gas_remaining - 710 wei
      args m_newArbitrator
  require ext_call.success


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  stop


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require mowner == caller
  require m_newOwner
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if not uint8(mstor1m.field_160):
      uint8(mstor1m.field_160) = 1
      require ext_code.size(0 or addr(mstor1m.field_0))
      call 0 or addr(mstor1m.field_0).cancelEscrow(bytes16 tradeID, address seller, address buyer, uint256 value) with:
           gas gas_remaining - 710 wei
          args 0, 0, mstor4, mstor5, mstor6
      require ext_call.success


