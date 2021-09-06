# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0Cba8d8E41BE400952c14afDb9c0b3f92544d8bE 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    resolverAddress # mask: a s
    # storage address 1
    key # mask: a s
    # storage address 2
    CONTRACT_ADDRESS # mask: a s
# hash = 0x04f3bcec
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def resolver(): # not payable
  return resolverAddress


# hash = 0x18836994
# getter = None
# const = None
# payable = False
def unknown18836994(addr _param1, addr _param2): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x5aad90f8 with:
       gas gas_remaining - 710 wei
      args addr(_param1), _param2
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x1e279a37
# getter = None
# const = None
# payable = False
def get_balance(address _query_address): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'sv:tdemurrage'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x76cab952 with:
       gas gas_remaining - 710 wei
      args _query_address
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x3943380c
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def key(): # not payable
  return key


# hash = 0x3f83acff
# getter = None
# const = None
# payable = False
def get_contract(bytes32 _key): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args _key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.locked() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require not ext_call.return_data[0]
  require ext_code.size(resolverAddress)
  call resolverAddress.owner() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(resolverAddress)
  call resolverAddress.0xc8b56bda with:
       gas gas_remaining - 710 wei
      args key
  require ext_call.success
  require ext_call.return_data[0]
  [93mselfdestruct([91maddr(ext_call.return_data[0])[93m)


# hash = 0xdb4ecbc1
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def CONTRACT_ADDRESS(): # not payable
  return CONTRACT_ADDRESS


# hash = 0xf923058c
# getter = None
# const = None
# payable = False
def unknownf923058c(): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x57e7946f with:
       gas gas_remaining - 710 wei
  require ext_call.success
  return ext_call.return_data[0]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


