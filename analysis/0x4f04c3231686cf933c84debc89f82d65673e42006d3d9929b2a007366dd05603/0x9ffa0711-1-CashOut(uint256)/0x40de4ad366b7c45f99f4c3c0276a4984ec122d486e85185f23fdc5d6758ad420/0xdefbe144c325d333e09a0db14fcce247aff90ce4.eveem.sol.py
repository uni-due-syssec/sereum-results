# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xdefBE144C325d333E09a0DB14FcCe247Aff90ce4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown89977cdfAddress # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    unknown4fe6f55fAddress # mask: a s
# hash = 0x3d79d1c8
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const bal = eth.balance(this.address)


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
           gas gas_remaining - 34710 wei
          args mem[ceil32(_param3.length) + 132 len _param3.length - 4]
  else:
      mem[floor32(_param3.length) + ceil32(_param3.length) + 128] = mem[floor32(_param3.length) + ceil32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32]
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining - 34710 wei
          args mem[ceil32(_param3.length) + 132 len floor32(_param3.length) + 28]
  require ext_call.success


# hash = 0x4fe6f55f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown4fe6f55f(): # not payable
  return unknown4fe6f55fAddress


# hash = 0x529334a1
# getter = None
# const = None
# payable = False
def unknown529334a1(addr _param1): # not payable
  unknown4fe6f55fAddress = _param1


# hash = 0x89977cdf
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown89977cdf(): # not payable
  return unknown89977cdfAddress


# hash = 0x8a7cf7f5
# getter = None
# const = None
# payable = True
def unknown8a7cf7f5() payable: 
  Mask(96, 0, stor1.field_160) = 0
  call unknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('Deposit()')) >> 224
     value 10^18 wei
       gas gas_remaining - 34710 wei
  Mask(96, 0, stor1.field_160) = 1
  call unknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args 10^18
  call unknown4fe6f55fAddress with:
     funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
       gas gas_remaining - 25710 wei
      args eth.balance(unknown4fe6f55fAddress)
  require eth.balance(this.address) >= eth.balance(this.address)


# hash = 0x9003e39a
# getter = None
# const = None
# payable = True
def unknown9003e39a(addr _param1, array _param2) payable: 
  mem[128 len _param2.length] = _param2[all]
  require caller == unknown89977cdfAddress
  mem[ceil32(_param2.length) + 128 len ceil32(_param2.length)] = _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]
  if not _param2.length % 32:
      [93mdelegate _param1.mem[ceil32(_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(_param2.length) + 132 len _param2.length - 4]
  else:
      mem[floor32(_param2.length) + ceil32(_param2.length) + 128] = mem[floor32(_param2.length) + ceil32(_param2.length) + -(_param2.length % 32) + 160 len _param2.length % 32]
      [93mdelegate _param1.mem[ceil32(_param2.length) + 128 len 4] with:
           gas gas_remaining - 25710 wei
          args mem[ceil32(_param2.length) + 132 len floor32(_param2.length) + 28]
  require delegate.return_code


# hash = 0xc144811f
# getter = None
# const = None
# payable = True
def unknownc144811f() payable: 
  require caller == unknown89977cdfAddress
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xeb5c3a36
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = False
def unknowneb5c3a36(): # not payable
  return bool(uint8(stor1.field_160))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if bool(uint8(stor1.field_160)) == 1:
      Mask(96, 0, stor1.field_160) = 0
      call unknown4fe6f55fAddress with:
         funct Mask(32, 224, sha3('CashOut(uint256)')) >> 224
           gas gas_remaining - 25710 wei
          args 1


