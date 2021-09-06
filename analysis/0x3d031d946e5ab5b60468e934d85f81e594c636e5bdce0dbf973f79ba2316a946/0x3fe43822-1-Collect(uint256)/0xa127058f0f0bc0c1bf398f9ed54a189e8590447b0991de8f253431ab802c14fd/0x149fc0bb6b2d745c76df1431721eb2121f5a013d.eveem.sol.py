# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x149fc0BB6b2D745c76Df1431721eB2121F5a013d 
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
    unknown1214f436 # mask: a s
    # storage address 3
    logAddress # mask: a s
# hash = 0x1214f436
# getter = ['storage', 32, 0, 3]
# const = None
# payable = False
def unknown1214f436(): # not payable
  return Mask(32, 224, munknown1214f436)


# hash = 0x2d652cf9
# getter = None
# const = None
# payable = False
def unknown2d652cf9(addr m_param1): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  mlogAddress = m_param1


# hash = 0x2fac8979
# getter = None
# const = None
# payable = False
def unknown2fac8979(): # not payable
  if munknownf85f97ddAddress == caller:
      munknown89977cdfAddress = munknownf85f97ddAddress


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
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
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


# hash = 0x51973ec9
# getter = ['storage', 160, 40, 3]
# const = None
# payable = False
def log(): # not payable
  return mlogAddress


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
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
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
  require munknown89977cdfAddress == caller
  munknownf85f97ddAddress = m_param1


# hash = 0x92f4ba65
# getter = None
# const = None
# payable = True
def unknown92f4ba65(addr m_param1, uint256 m_param2, uint32 m_param3) payable: 
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  munknown1214f436 = m_param3
  munknowneb5c3a36 = 1
  call m_param1 with:
     funct 0 or m_param3
       gas gas_remaining - 25710 wei
      args m_param2
  call m_param1 with:
       gas gas_remaining - 25710 wei
      args eth.balance(m_param1)
  require eth.balance(this.address) > eth.balance(this.address)


# hash = 0xa6305edf
# getter = None
# const = None
# payable = False
def unknowna6305edf(addr m_param1): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  require ext_code.size(mlogAddress)
  call mlogAddress.0x6cb3d1ad with:
       gas gas_remaining - 710 wei
      args addr(m_param1), 1
  require ext_call.success


# hash = 0xbe9474bb
# getter = None
# const = None
# payable = False
def unknownbe9474bb(addr m_param1, bool m_param2): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  mstor2m[addr(m_param1)m] = uint8(m_param2)


# hash = 0xc144811f
# getter = None
# const = None
# payable = True
def unknownc144811f() payable: 
  require munknown89977cdfAddress == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xd1aca9f2
# getter = None
# const = None
# payable = False
def unknownd1aca9f2(addr m_param1): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  require ext_code.size(mlogAddress)
  call mlogAddress.0x474dacce with:
       gas gas_remaining - 710 wei
      args addr(m_param1), 1
  require ext_call.success


# hash = 0xeb5c3a36
# getter = ['bool', ['storage', 8, 32, 3]]
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


# hash = 0xeed27b33
# getter = None
# const = None
# payable = False
def unknowneed27b33(array m_param1): # not payable
  mem[128 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + 128 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[ceil32(m_param1.length) + floor32(m_param1.length) + -(m_param1.length % 32) + 160 len m_param1.length % 32] = mem[-(m_param1.length % 32) + floor32(m_param1.length) + 160 len m_param1.length % 32]
  mem[ceil32(m_param1.length) + 128] = Mask(32, 224, sha3(call.data[m_param1 + 36 len floor32(m_param1.length)], mem[ceil32(m_param1.length) + floor32(m_param1.length) + 128 len m_param1.length % 32]))
  return memory
    from ceil32(m_param1.length) + 128
     [93mlen 32


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
  if 1 == bool(munknowneb5c3a36):
      munknowneb5c3a36 = 0
      call caller with:
           gas gas_remaining - 25710 wei
          args 1


