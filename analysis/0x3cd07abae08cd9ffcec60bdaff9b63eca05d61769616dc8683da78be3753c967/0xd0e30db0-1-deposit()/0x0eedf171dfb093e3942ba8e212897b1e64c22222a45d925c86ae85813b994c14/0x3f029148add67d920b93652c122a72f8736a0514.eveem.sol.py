# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3f029148adD67d920B93652c122a72F8736a0514 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x18f8cf1d
# getter = None
# const = None
# payable = True
def unknown18f8cf1d() payable: 
  mem[64] = 96
  mem[0] = caller
  mem[32] = 0
  if not stor0[caller]:
      require 0x825d5d0df3b2d59f69cc673f041ca91a296b8183 == caller
  require calldata.size >= 28
  mem[24 len calldata.size] = call.data[0 len calldata.size]
  if not mem[24 len 8] % 16:
      call 0x0 with:
         value call.value wei
           gas gas_remaining wei
          args mem[56 len calldata.size - 32]
      if not Mask(4, 4, mem[24 len 8]):
          require ext_call.success
          stop
      require Mask(4, 4, mem[24 len 8]) == 16
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require mem[24 len 8] % 16 == 1
      [93mdelegate 0x0.0x0 with:
           gas gas_remaining wei
          args mem[56 len calldata.size - 32]
      if not Mask(4, 4, mem[24 len 8]):
          require delegate.return_code
          stop
      require Mask(4, 4, mem[24 len 8]) == 16
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  if not stor0[caller]:
      require 0x825d5d0df3b2d59f69cc673f041ca91a296b8183 == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa5b4e966
# getter = None
# const = None
# payable = False
def unknowna5b4e966(addr _param1, bool _param2): # not payable
  if not stor0[caller]:
      require 0x825d5d0df3b2d59f69cc673f041ca91a296b8183 == caller
  addr(stor1.field_0) = _param1
  Mask(96, 0, stor1.field_160) = Mask(96, 0, _param2)


# hash = 0xadf48490
# getter = None
# const = None
# payable = False
def unknownadf48490(addr _param1, bool _param2): # not payable
  if not stor0[caller]:
      require 0x825d5d0df3b2d59f69cc673f041ca91a296b8183 == caller
  stor0[addr(_param1)] = uint8(_param2)


# hash = 0xb88a802f
# getter = None
# const = None
# payable = False
def claimReward(): # not payable
  if not stor0[caller]:
      require 0x825d5d0df3b2d59f69cc673f041ca91a296b8183 == caller
  Mask(168, 0, stor1.field_0) = 0
  call 0x9ae601435c8daa915ea8123e9b51a067f9966929 with:
       gas gas_remaining wei
  require ext_call.success
  uint8(stor1.field_160) = 1
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  Mask(168, 0, stor1.field_0) = 0
  call 0x9ae601435c8daa915ea8123e9b51a067f9966929 with:
     value 10^16 wei
       gas gas_remaining wei
  require ext_call.success
  uint8(stor1.field_160) = 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if not addr(stor1.field_0):
      require not uint256(stor1.field_0)
      stop
  [93mdelegate addr(stor1.field_0) with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


