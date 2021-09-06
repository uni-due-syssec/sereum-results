# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3E373a5C2a10Cbb8626216284A525DC5e0cE6581 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 0
    unknown1214f436 # mask: a s
    # storage address 0
    stor0 # mask: a s
# hash = 0x1214f436
# getter = ['storage', 32, 0, 0]
# const = None
# payable = False
def unknown1214f436(): # not payable
  return Mask(32, 224, munknown1214f436)


# hash = 0x4b906714
# getter = None
# const = None
# payable = True
def unknown4b906714(addr m_param1, uint256 m_param2, array m_param3) payable: 
  mem[128 len m_param3.length] = m_param3[allm]
  require caller == munknown89977cdfAddress
  mem[ceil32(m_param3.length) + 128 len ceil32(m_param3.length)] = m_param3[allm], mem[m_param3.length + 128 len ceil32(m_param3.length) - m_param3.length]
  if not m_param3.length % 32:
      call m_param1.mem[ceil32(m_param3.length) + 128 len 4] with:
         value m_param2 wei
           gas gas_remaining wei
          args mem[ceil32(m_param3.length) + 132 len m_param3.length - 4]
  else:
      mem[floor32(m_param3.length) + ceil32(m_param3.length) + 128] = mem[floor32(m_param3.length) + ceil32(m_param3.length) + -(m_param3.length % 32) + 160 len m_param3.length % 32]
      call m_param1.mem[ceil32(m_param3.length) + 128 len 4] with:
         value m_param2 wei
           gas gas_remaining wei
          args mem[ceil32(m_param3.length) + 132 len floor32(m_param3.length) + 28]
  require ext_call.success


# hash = 0x89977cdf
# getter = ['storage', 160, 40, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return munknown89977cdfAddress


# hash = 0x92f4ba65
# getter = None
# const = None
# payable = True
def unknown92f4ba65(addr m_param1, uint256 m_param2, uint32 m_param3) payable: 
  require caller == munknown89977cdfAddress
  if Mask(32, 224, m_param3):
      munknown1214f436 = m_param3
  mstor0 = 1
  call m_param1 with:
       gas gas_remaining wei
      args m_param2
  call m_param1 with:
       gas gas_remaining wei
      args eth.balance(m_param1)
  require eth.balance(this.address) < eth.balance(this.address)


# hash = 0xeb5c3a36
# getter = ['bool', ['storage', 8, 32, 0]]
# const = None
# payable = False
def unknowneb5c3a36(): # not payable
  return bool(mstor0)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if 1 == bool(mstor0):
      mstor0 = 0
      call caller with:
           gas gas_remaining wei
          args 1


