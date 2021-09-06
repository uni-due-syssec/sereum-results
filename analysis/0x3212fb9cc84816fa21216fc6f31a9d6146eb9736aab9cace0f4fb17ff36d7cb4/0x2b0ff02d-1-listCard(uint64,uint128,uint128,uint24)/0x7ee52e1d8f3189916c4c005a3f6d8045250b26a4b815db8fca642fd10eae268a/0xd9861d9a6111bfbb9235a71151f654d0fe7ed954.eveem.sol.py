# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD9861D9a6111bfBB9235a71151f654D0Fe7Ed954 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
# hash = 0x24fd0a5c
# getter = None
# const = None
# payable = False
def unknown24fd0a5c(uint64 _param1): # not payable
  require ext_code.size(stor0)
  call stor0.0xa9014b0f with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success
  return not bool(ext_call.return_data[0])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


