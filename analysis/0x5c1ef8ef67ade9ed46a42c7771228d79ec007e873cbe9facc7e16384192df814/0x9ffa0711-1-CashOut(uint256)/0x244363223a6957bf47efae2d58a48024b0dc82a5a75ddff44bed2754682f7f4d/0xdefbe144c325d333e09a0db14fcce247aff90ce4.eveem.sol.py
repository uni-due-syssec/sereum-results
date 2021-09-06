# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xdefBE144C325d333E09a0DB14FcCe247Aff90ce4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    unknown4fe6f55fAddress # mask: a s
# hash = 0x3d79d1c8
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const bal = eth.balance(this.address)


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
           gas gas_remaining - 34710 wei
          args mem[ceil32(m_param3.length) + 132 len m_param3.length - 4]
  else:
      mem[floor32(m_param3.length) + ceil32(m_param3.length) + 128] = mem[floor32(m_param3.length) + ceil32(m_param3.length) + -(m_param3.length % 32) + 160 len m_param3.length % 32]
      call m_param1.mem[ceil32(m_param3.length) + 128 len 4] with:
         value m_param2 wei
           gas gas_remaining - 34710 wei
          args mem[ceil32(m_param3.length) + 132 len floor32(m_param3.length) + 28]
  require ext_call.success


# hash = 0x4fe6f55f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown4fe6f55f(): # not payable
  return munknown4fe6f55fAddress


# hash = 0x529334a1
# getter = None
# const = None
# payable = False
def unknown529334a1(addr m_param1): # not payable
  munknown4fe6f55fAddress = m_param1


# hash = 0x89977cdf
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return munknown89977cdfAddress


# hash = 0x8a7cf7f5
# getter = None
# const = None
# payable = True
def unknown8a7cf7f5() payable: 
  Mask(96, 0, mstor1m.field_160) = 0
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value 10^18 wei
       gas gas_remaining - 34710 wei
  Mask(96, 0, mstor1m.field_160) = 1
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args 10^18
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args eth.balance(munknown4fe6f55fAddress)
  require eth.balance(this.address) >= eth.balance(this.address)


# hash = 0x9003e39a
# getter = None
# const = None
# payable = True
def unknown9003e39a(addr m_param1, array m_param2) payable: 
  mem[128 len m_param2.length] = m_param2[allm]
  require caller == munknown89977cdfAddress
  mem[ceil32(m_param2.length) + 128 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
  if not m_param2.length % 32:
      [93mdelegate m_param1.mem[ceil32(m_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(m_param2.length) + 132 len m_param2.length - 4]
  else:
      mem[floor32(m_param2.length) + ceil32(m_param2.length) + 128] = mem[floor32(m_param2.length) + ceil32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32]
      [93mdelegate m_param1.mem[ceil32(m_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(m_param2.length) + 132 len floor32(m_param2.length) + 28]
  require delegate.return_code


# hash = 0xc144811f
# getter = None
# const = None
# payable = True
def unknownc144811f() payable: 
  require caller == munknown89977cdfAddress
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xeb5c3a36
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = False
def unknowneb5c3a36(): # not payable
  return bool(uint8(mstor1m.field_160))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if bool(uint8(mstor1m.field_160)) == 1:
      Mask(96, 0, mstor1m.field_160) = 0
      call munknown4fe6f55fAddress with:
         funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
           gas gas_remaining - 25710 wei
          args 1


