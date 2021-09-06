# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3E373a5C2a10Cbb8626216284A525DC5e0cE6581 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 0
    unknown1214f436 # mask: a s
    # storage address 0
    stor0 # mask: a s
# hash = 0x1214f436
# getter = ['storage', 32, 0, 0]
# const = None
# payable = False
def unknown1214f436(): # not payable
  return Mask(32, 224, unknown1214f436)


# hash = 0x4b906714
# getter = None
# const = None
# payable = True
def unknown4b906714(addr _param1, uint256 _param2, array _param3) payable: 
  mem[128 len _param3.length] = _param3[all]
  require caller == unknown89977cdfAddress
  mem[ceil32(_param3.length) + 128 len ceil32(_param3.length)] = _param3[all], mem[_param3.length + 128 len ceil32(_param3.length) - _param3.length]
  if not _param3.length % 32:
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining wei
          args mem[ceil32(_param3.length) + 132 len _param3.length - 4]
  else:
      mem[floor32(_param3.length) + ceil32(_param3.length) + 128] = mem[floor32(_param3.length) + ceil32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32]
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining wei
          args mem[ceil32(_param3.length) + 132 len floor32(_param3.length) + 28]
  require ext_call.success


# hash = 0x89977cdf
# getter = ['storage', 160, 40, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return unknown89977cdfAddress


# hash = 0x92f4ba65
# getter = None
# const = None
# payable = True
def unknown92f4ba65(addr _param1, uint256 _param2, uint32 _param3) payable: 
  require caller == unknown89977cdfAddress
  if Mask(32, 224, _param3):
      unknown1214f436 = _param3
  stor0 = 1
  call _param1 with:
       gas gas_remaining wei
      args _param2
  call _param1 with:
       gas gas_remaining wei
      args eth.balance(_param1)
  require eth.balance(this.address) < eth.balance(this.address)


# hash = 0xeb5c3a36
# getter = ['bool', ['storage', 8, 32, 0]]
# const = None
# payable = False
def unknowneb5c3a36(): # not payable
  return bool(stor0)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if 1 == bool(stor0):
      stor0 = 0
      call caller with:
           gas gas_remaining wei
          args 1


