# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xE4AF0EEDb8312d812b0Ad2F2390391923F181D64 
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
    stor3
    # storage address 4
    stor4
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
# hash = 0x21a7a6f0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown21a7a6f0(addr m_param1): # not payable
  return bool(mstor4m[m_param1m])


# hash = 0x2fac8979
# getter = None
# const = None
# payable = False
def unknown2fac8979(): # not payable
  if caller == munknownf85f97ddAddress:
      munknown89977cdfAddress = munknownf85f97ddAddress


# hash = 0x3d79d1c8
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const bal = eth.balance(this.address)


# hash = 0x474dacce
# getter = None
# const = None
# payable = False
def unknown474dacce(addr m_param1, bool m_param2): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  mstor3m[addr(m_param1)m] = uint8(m_param2)


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


# hash = 0x4c2f04a4
# getter = None
# const = None
# payable = False
def AddMessage(address m_adr, uint256 m_val, string m_data): # not payable
  mem[128 len m_data.length] = m_data[allm]
  if not mstor3m[addr(m_adr)m]:
      mstor6 = m_adr
      mstor9 = block.timestamp
      mstor8 = m_val
      uint256(mstor7m[m]) = Array(len=m_data.length, data=m_data[allm])
      mhistorym.length++
      if not mhistorym.length <= mhistorym.length + 1:
          mem[0] = 5
          [94midx = 4 * mhistorym.length + 1
          mwhile sha3(5) + (4 * mhistorym.length) > [94midx + sha3(mem[0])m:
              addr(mstor[[94midx + sha3(mem[0])m]) = 0
              uint256(mstor[[94midx + sha3(mem[0]) + 1m]) = 0
              if 31 < mstor[[94midx + sha3(mem[0]) + 1m]m.length:
                  mem[0] = [94midx + sha3(mem[0]) + 1
                  [94ms = sha3([94midx + sha3(mem[0]) + 1)
                  mwhile sha3([94midx + sha3(mem[0]) + 1) + (mstor[[94midx + sha3(mem[0]) + 1m]m.length + 31 / 32) > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
              uint256(mstor[[94midx + sha3(mem[0]) + 2m]) = 0
              uint256(mstor[[94midx + sha3(mem[0]) + 3m]) = 0
              [94midx = [94midx + 4
              mcontinue 
      addr(mhistorym[mhistorym.lengthm]m.field_0) = mstor6
      if 31 >= mstor7m.length:
          uint256(mhistorym[mhistorym.lengthm]m.field_256) = mstor7m.length
          [94midx = 0
          mwhile mstor[(4 * mhistorym.length) + ('name', 'history', 5) + 1m]m.length + 31 / 32 > [94midxm:
              uint256(mstor[[94midx + sha3((4 * mhistorym.length) + ('name', 'history', 5) + 1)m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          uint256(mhistorym[mhistorym.lengthm]m.field_256) = Mask(255, 1, (256 * not bool(mstor7m.length)) - 1 and mstor7m.length) + 1
          if not Mask(255, 1, (256 * not bool(mstor7m.length)) - 1 and mstor7m.length):
              [94midx = 0
              mwhile mstor[(4 * mhistorym.length) + ('name', 'history', 5) + 1m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((4 * mhistorym.length) + ('name', 'history', 5) + 1)m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              [94ms = 0
              [94midx = 0
              mwhile mstor7m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94ms + sha3((4 * mhistorym.length) + ('name', 'history', 5) + 1)m]m.field_0) = uint256(mstor7m[[94midxm])
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  mcontinue 
              [94midx = mstor7m.length + 31 / 32
              mwhile mstor[(4 * mhistorym.length) + ('name', 'history', 5) + 1m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((4 * mhistorym.length) + ('name', 'history', 5) + 1)m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
      uint256(mhistorym[mhistorym.lengthm]m.field_512) = mstor8
      uint256(mhistorym[mhistorym.lengthm]m.field_768) = mstor9
      if mstor4m[callerm]:
          require 0 < m_data.length
          if Mask(8, 248, mem[128]) == 'C':
              require m_val <= 0


# hash = 0x6cb3d1ad
# getter = None
# const = None
# payable = False
def unknown6cb3d1ad(addr m_param1, bool m_param2): # not payable
  if munknown89977cdfAddress != caller:
      require mstor2m[callerm]
  mstor4m[addr(m_param1)m] = uint8(m_param2)


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
  require caller == munknown89977cdfAddress
  munknownf85f97ddAddress = m_param1


# hash = 0x930339be
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknown930339be(addr m_param1): # not payable
  return bool(mstor3m[m_param1m])


# hash = 0xa21f0368
# getter = ['struct', ['loc', 5]]
# const = None
# payable = False
def History(uint256 m_param1): # not payable
  require m_param1 < mhistorym.length
  mem[256] = uint256(mstor[sha3((4 * m_param1) + ('name', 'history', 5) + 1)m]m.field_0)
  [94midx = 256
  [94ms = 0
  mwhile mstor[(4 * m_param1) + ('name', 'history', 5) + 1m]m.length + 256 > [94midx + 32m:
      mem[[94midx + 32] = uint256(mstor[[94ms + sha3((4 * m_param1) + ('name', 'history', 5) + 1)m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return addr(mhistorym[m_param1m]m.field_0), 
         Array(len=mstor[(4 * m_param1) + ('name', 'history', 5) + 1m]m.length, data=mem[256 len mstor[(4 * m_param1) + ('name', 'history', 5) + 1m]m.length + (floor32(mstor[(4 * m_param1) + ('name', 'history', 5) + 1m]m.length - 1) + -mstor[(4 * m_param1) + ('name', 'history', 5) + 1m]m.length + 32 % 32)]),
         uint256(mhistorym[m_param1m]m.field_512),
         uint256(mhistorym[m_param1m]m.field_768)


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
  require caller == munknown89977cdfAddress
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


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
  stop


