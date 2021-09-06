# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x82F1Be1e1dE456c101f5d7eaE87bf69dA216c3Cb 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknownef89aff3Address # mask: a s
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  [93mselfdestruct([91mcaller[93m)


# hash = 0xe5225381
# getter = None
# const = None
# payable = True
def collect() payable: 
  require ext_code.size(unknownef89aff3Address)
  call unknownef89aff3Address.put() with:
     value call.value wei
       gas gas_remaining - 9050 wei
  require ext_call.success
  require ext_code.size(unknownef89aff3Address)
  call unknownef89aff3Address.get() with:
       gas gas_remaining - 50 wei
  require ext_call.success


# hash = 0xef89aff3
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknownef89aff3(): # not payable
  return unknownef89aff3Address


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if eth.balance(unknownef89aff3Address) >= call.value:
      require ext_code.size(unknownef89aff3Address)
      call unknownef89aff3Address.get() with:
           gas gas_remaining - 50 wei
      require ext_call.success


