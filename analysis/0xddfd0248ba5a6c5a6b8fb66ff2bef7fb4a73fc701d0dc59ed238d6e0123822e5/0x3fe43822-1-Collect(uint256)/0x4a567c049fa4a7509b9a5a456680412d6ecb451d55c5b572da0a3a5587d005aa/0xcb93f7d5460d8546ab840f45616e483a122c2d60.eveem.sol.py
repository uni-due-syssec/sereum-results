# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xCb93F7d5460d8546ab840F45616E483a122c2d60 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown855a0fe3Address # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    done # mask: a s
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  require owner == caller
  [93mselfdestruct([91mowner[93m)


# hash = 0x855a0fe3
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown855a0fe3(): # not payable
  return unknown855a0fe3Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xae8421e1
# getter = ['bool', ['storage', 8, 160, 2]]
# const = None
# payable = False
def done(): # not payable
  return bool(done)


# hash = 0xbd6b6128
# getter = None
# const = None
# payable = False
def unknownbd6b6128(uint256 _param1): # not payable
  require ext_code.size(stor2)
  call stor2.Collect(uint256 am) with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success


# hash = 0xf28adc4d
# getter = None
# const = None
# payable = False
def unknownf28adc4d(): # not payable
  require ext_code.size(stor2)
  call stor2.Collect(uint256 am) with:
       gas gas_remaining - 9710 wei
      args 10^18
  require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if done:
      call owner with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
  else:
      require ext_code.size(stor2)
      call stor2.Collect(uint256 am) with:
           gas gas_remaining - 9710 wei
          args 10^18
      require ext_call.success
      done = 1
      call owner with:
         value call.value wei
           gas 2300 * is_zero(value) wei


