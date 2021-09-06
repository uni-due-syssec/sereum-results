# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x268D0F0f11776ea094de4f24da6B3Bcfb2743085 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x4c33fe94
# getter = None
# const = None
# payable = False
def cancel(address m_tag): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xe0c703dc with:
       gas gas_remaining - 710 wei
      args 0, m_tag
  require delegate.return_code


# hash = 0x5a0cf9f3
# getter = None
# const = None
# payable = True
def unknown5a0cf9f3(addr m_param1) payable: 
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0x29f2e907 with:
       gas gas_remaining - 710 wei
      args 0, addr(m_param1), 0
  require delegate.return_code
  return bool(delegate.return_data[0])


# hash = 0x79599f96
# getter = None
# const = None
# payable = False
def unknown79599f96(): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xd30d447d with:
       gas gas_remaining - 710 wei
      args 0
  require delegate.return_code


# hash = 0x7e102b2a
# getter = None
# const = None
# payable = False
def unknown7e102b2a(bool m_param1): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xf5471307 with:
       gas gas_remaining - 710 wei
      args 0, m_param1
  require delegate.return_code


# hash = 0xb82a0978
# getter = None
# const = None
# payable = False
def unknownb82a0978(addr m_param1, uint256 m_param2): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xfe7a0fb9 with:
       gas gas_remaining - 710 wei
      args 0, 0, addr(m_param1), m_param2, 0
  require delegate.return_code


# hash = 0xd9214ed5
# getter = None
# const = None
# payable = True
def unknownd9214ed5(addr m_param1) payable: 
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0x29f2e907 with:
       gas gas_remaining - 710 wei
      args 0, addr(m_param1), 1
  require delegate.return_code
  return bool(delegate.return_data[0])


# hash = 0xd9a96852
# getter = None
# const = None
# payable = False
def unknownd9a96852(addr m_param1, uint32 m_param2): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xa8b7983 with:
       gas gas_remaining - 710 wei
      args 0, addr(m_param1), m_param2
  require delegate.return_code


# hash = 0xdf9b8fff
# getter = None
# const = None
# payable = False
def unknowndf9b8fff(addr m_param1, uint256 m_param2): # not payable
  require ext_code.size(0xa52d005b0488f23f756a72591a82e259d2d5acae)
  [93mdelegate 0xa52d005b0488f23f756a72591a82e259d2d5acae.0xfe7a0fb9 with:
       gas gas_remaining - 710 wei
      args 0, 0, addr(m_param1), m_param2, 1
  require delegate.return_code


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  revert


