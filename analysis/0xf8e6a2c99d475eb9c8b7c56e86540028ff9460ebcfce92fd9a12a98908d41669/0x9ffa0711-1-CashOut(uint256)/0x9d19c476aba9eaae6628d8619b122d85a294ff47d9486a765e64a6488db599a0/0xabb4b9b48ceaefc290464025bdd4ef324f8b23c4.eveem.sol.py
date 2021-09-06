# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAbb4B9B48CEaEFC290464025bdd4ef324F8B23C4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 1
    unknownf85f97ddAddress # mask: a s
    # storage address 2
    stor2
    # storage address 3
    unknowneb5c3a36 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    unknown4fe6f55fAddress # mask: a s
# hash = 0x1190a88a
# getter = None
# const = None
# payable = True
def unknown1190a88a(uint256 m_param1) payable: 
  require caller == munknown89977cdfAddress
  mstor3 = 0
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value m_param1 wei
       gas gas_remaining - 34710 wei
  mstor3 = 1
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args m_param1
  call munknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args eth.balance(munknown4fe6f55fAddress)
  require eth.balance(this.address) >= eth.balance(this.address)


# hash = 0x2fac8979
# getter = None
# const = None
# payable = False
def unknown2fac8979(): # not payable
  if caller == munknownf85f97ddAddress:
      munknown89977cdfAddress = munknownf85f97ddAddress


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
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown4fe6f55f(): # not payable
  return munknown4fe6f55fAddress


# hash = 0x529334a1
# getter = None
# const = None
# payable = False
def unknown529334a1(addr m_param1): # not payable
  require caller == munknown89977cdfAddress
  munknown4fe6f55fAddress = m_param1


# hash = 0x89977cdf
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return munknown89977cdfAddress


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


# hash = 0x90a68455
# getter = None
# const = None
# payable = False
def unknown90a68455(addr m_param1): # not payable
  require caller == munknown89977cdfAddress
  munknownf85f97ddAddress = m_param1


# hash = 0xbe9474bb
# getter = None
# const = None
# payable = False
def unknownbe9474bb(addr m_param1, bool m_param2): # not payable
  require caller == munknown89977cdfAddress
  mstor2m[addr(m_param1)m] = uint8(m_param2)


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
# getter = ['bool', ['storage', 8, 160, 3]]
# const = None
# payable = False
def unknowneb5c3a36(): # not payable
  return bool(munknowneb5c3a36)


# hash = 0xedbbdf2e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 2]]]]
# const = None
# payable = False
def Managers(address m_param1): # not payable
  return bool(mstor2m[m_param1m])


# hash = 0xf85f97dd
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknownf85f97dd(): # not payable
  return munknownf85f97ddAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if bool(munknowneb5c3a36) == 1:
      mstor3 = 0
      call munknown4fe6f55fAddress with:
         funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
           gas gas_remaining - 25710 wei
          args 1


