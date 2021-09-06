# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5E5c3dDA30D93E64884548a7172d8e291F93Ed34 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
# hash = 0xe8b1d0f3
# getter = None
# const = None
# payable = True
def unknowne8b1d0f3(addr m_param1, uint32 m_param2, array m_param3) payable: 
  require mstor0 == caller
  mem[ceil32(m_param3.length) + 132 len m_param3.length] = m_param3[allm]
  if not m_param3.length % 32:
      call m_param1 with:
         funct m_param2
           gas gas_remaining - 25050 wei
          args m_param3[allm]
  else:
      mem[floor32(m_param3.length) + ceil32(m_param3.length) + 132] = mem[floor32(m_param3.length) + ceil32(m_param3.length) + -(m_param3.length % 32) + 164 len m_param3.length % 32]
      call m_param1 with:
         funct m_param2
           gas gas_remaining - 25050 wei
          args m_param3[allm], mem[ceil32(m_param3.length) + m_param3.length + 132 len -(m_param3.length % 32) + 32]
  return ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


