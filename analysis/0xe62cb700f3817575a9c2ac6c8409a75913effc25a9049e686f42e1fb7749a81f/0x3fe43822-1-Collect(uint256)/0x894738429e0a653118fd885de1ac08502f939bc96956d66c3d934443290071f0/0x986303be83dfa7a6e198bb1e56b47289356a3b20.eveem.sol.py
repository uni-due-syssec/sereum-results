# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x986303BE83DFA7A6e198BB1E56B47289356A3b20 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 18569430475105882587588266137607568536673111973893317399460219858819262702948
    stor18569430475105882587588266137607568536673111973893317399460219858819262702948
    # storage address 18569430475105882587588266137607568536673111973893317399460219858819262702949
    stor18569430475105882587588266137607568536673111973893317399460219858819262702949
    # storage address 18569430475105882587588266137607568536673111973893317399460219858819262702950
    stor18569430475105882587588266137607568536673111973893317399460219858819262702950
# hash = 0x4b906714
# getter = None
# const = None
# payable = True
def unknown4b906714(addr m_param1, uint256 m_param2, array m_param3) payable: 
  mem[128 len m_param3.length] = m_param3[allm]
  require tx.origin == mstor7
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


# hash = 0x4c2f04a4
# getter = None
# const = None
# payable = False
def AddMessage(address m_adr, uint256 m_val, string m_data): # not payable
  mem[128 len m_data.length] = m_data[allm]
  mstor1 = m_adr
  mstor4 = block.timestamp
  mstor3 = m_val
  uint256(mstor2m[m]) = Array(len=m_data.length, data=m_data[allm])
  mstor0m.length++
  addr(mstor0m[mstor0m.lengthm]m.field_0) = mstor1
  if 31 >= mstor2m.length:
      mstor290Dm[mstor0m.lengthm] = mstor2m.length
      [94midx = 0
      mwhile mstor[(4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564m]m.length + 31 / 32 > [94midxm:
          mstor[[94midx + sha3((4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564)m] = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      mstor290Dm[mstor0m.lengthm] = Mask(255, 1, (256 * not bool(mstor2m.length)) - 1 and mstor2m.length) + 1
      if not Mask(255, 1, (256 * not bool(mstor2m.length)) - 1 and mstor2m.length):
          [94midx = 0
          mwhile mstor[(4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564m]m.length + 31 / 32 > [94midxm:
              mstor[[94midx + sha3((4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564)m] = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile mstor2m.length + 31 / 32 > [94midxm:
              mstor[[94ms + sha3((4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564)m] = uint256(mstor2m[[94midxm])
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = mstor2m.length + 31 / 32
          mwhile mstor[(4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564m]m.length + 31 / 32 > [94midxm:
              mstor[[94midx + sha3((4 * mstor0m.length) + 0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e564)m] = 0
              [94midx = [94midx + 1
              mcontinue 
  mstor290Dm[mstor0m.lengthm] = mstor3
  mstor290Dm[mstor0m.lengthm] = mstor4
  if caller == mstor5:
      if mstor7 != m_adr:
          if mstor6 != tx.origin:
              require 0 < m_data.length
              if 'C' == Mask(8, 248, mem[128]):
                  require m_val <= 0


# hash = 0xa21f0368
# getter = None
# const = None
# payable = False
def History(uint256 m_param1): # not payable
  require m_param1 < mstor0m.length
  mem[128] = mstor[sha3((4 * m_param1) + ('name', 'stor0', 0) + 1)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor[(4 * m_param1) + ('name', 'stor0', 0) + 1m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor[[94ms + sha3((4 * m_param1) + ('name', 'stor0', 0) + 1)m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return addr(mstor0m[m_param1m]m.field_0), 
         Array(len=mstor[(4 * m_param1) + ('name', 'stor0', 0) + 1m]m.length, data=mem[128 len mstor[(4 * m_param1) + ('name', 'stor0', 0) + 1m]m.length]),
         mstor0m[m_param1m]m.field_512,
         mstor0m[m_param1m]m.field_768


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


