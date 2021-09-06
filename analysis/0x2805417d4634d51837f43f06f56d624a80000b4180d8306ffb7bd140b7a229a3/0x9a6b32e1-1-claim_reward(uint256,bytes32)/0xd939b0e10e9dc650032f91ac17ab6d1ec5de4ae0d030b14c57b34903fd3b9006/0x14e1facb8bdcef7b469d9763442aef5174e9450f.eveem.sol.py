# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x14e1FAcB8bDceF7b469D9763442aEf5174E9450F 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
# hash = 0x45bcc288
# getter = None
# const = None
# payable = True
def unknown45bcc288(addr _param1) payable: 
  stor0 = _param1
  require ext_code.size(_param1)
  call _param1.get_parameters() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  stor1 = ext_call.return_data[0]
  require ext_code.size(stor0)
  call stor0.register(bytes32 name) with:
     value stor1 wei
       gas gas_remaining - 9710 wei
      args 0x6100000000000000000000000000000000000000000000000000000000000000
  require ext_call.success
  stor2 = ext_call.return_data[0]
  stor3 = ext_call.return_data[0] + 2
  require ext_call.return_data[0] + 2 < 30
  require ext_code.size(stor0)
  call stor0.claim_reward(uint256 uid, bytes32 passcode) with:
     value stor1 wei
       gas gas_remaining - 9710 wei
      args stor2, 0x6100000000000000000000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(stor0)
  call stor0.register(bytes32 name) with:
     value stor1 wei
       gas gas_remaining - 9710 wei
      args 0x6100000000000000000000000000000000000000000000000000000000000000
  require ext_call.success
  stor3 = 0
  require ext_code.size(stor0)
  call stor0.claim_reward(uint256 uid, bytes32 passcode) with:
     value stor1 wei
       gas gas_remaining - 9710 wei
      args (-77194726158210796949047323339125271902179989777093709359638389338608753093291 * sha3(0)) - 0x5555555555555555555555555555555555555555555555555555555555555556, 0
  require ext_call.success
  [93mselfdestruct([91mcaller[93m)


# hash = 0x77028d93
# getter = None
# const = None
# payable = False
def unknown77028d93(uint256 _param1): # not payable
  return ((0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab * _param1) - (0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab * sha3(0)))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if stor0 == caller:
      if stor3:
          stor3--
          require ext_code.size(stor0)
          call stor0.claim_reward(uint256 uid, bytes32 passcode) with:
             value stor1 wei
               gas gas_remaining - 9710 wei
              args stor2, 0x6100000000000000000000000000000000000000000000000000000000000000
          require ext_call.success


