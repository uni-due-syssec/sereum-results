# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2f3f1A0f728Bf3a93EFf69a65486B758d4310989 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x4c33fe94
# getter = None
# const = None
# payable = False
def cancel(address _tag): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xe0c703dc with:
       gas gas_remaining - 710 wei
      args 0, _tag
  require delegate.return_code


# hash = 0x5a0cf9f3
# getter = None
# const = None
# payable = True
def unknown5a0cf9f3(addr _param1) payable: 
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0x29f2e907 with:
       gas gas_remaining - 710 wei
      args 0, addr(_param1), 0
  require delegate.return_code
  return bool(delegate.return_data[0])


# hash = 0x79599f96
# getter = None
# const = None
# payable = False
def unknown79599f96(): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xd30d447d with:
       gas gas_remaining - 710 wei
      args 0
  require delegate.return_code


# hash = 0x7e102b2a
# getter = None
# const = None
# payable = False
def unknown7e102b2a(bool _param1): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xf5471307 with:
       gas gas_remaining - 710 wei
      args 0, _param1
  require delegate.return_code


# hash = 0xb82a0978
# getter = None
# const = None
# payable = False
def unknownb82a0978(addr _param1, uint256 _param2): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xfe7a0fb9 with:
       gas gas_remaining - 710 wei
      args 0, 0, addr(_param1), _param2, 0
  require delegate.return_code


# hash = 0xd9214ed5
# getter = None
# const = None
# payable = True
def unknownd9214ed5(addr _param1) payable: 
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0x29f2e907 with:
       gas gas_remaining - 710 wei
      args 0, addr(_param1), 1
  require delegate.return_code
  return bool(delegate.return_data[0])


# hash = 0xd9a96852
# getter = None
# const = None
# payable = False
def unknownd9a96852(addr _param1, uint32 _param2): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xa8b7983 with:
       gas gas_remaining - 710 wei
      args 0, addr(_param1), _param2
  require delegate.return_code


# hash = 0xdf9b8fff
# getter = None
# const = None
# payable = False
def unknowndf9b8fff(addr _param1, uint256 _param2): # not payable
  require ext_code.size(0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b)
  [93mdelegate 0x41a3fae8b33a8cd99eba48b485b403c9b5d2566b.0xfe7a0fb9 with:
       gas gas_remaining - 710 wei
      args 0, 0, addr(_param1), _param2, 1
  require delegate.return_code


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  revert


