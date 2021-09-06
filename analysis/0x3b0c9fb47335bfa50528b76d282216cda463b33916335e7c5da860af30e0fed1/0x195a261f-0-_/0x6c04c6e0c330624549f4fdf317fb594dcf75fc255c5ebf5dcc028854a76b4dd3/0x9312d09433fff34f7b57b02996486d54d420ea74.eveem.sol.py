# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x9312D09433fFF34f7b57b02996486d54D420eA74 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x61346679': 'unknown61346679(?)', '0x79705be7': 'unknown79705be7(?)', '0xe51be6e8': 'unknowne51be6e8(?)'} 

# storage definitions
def storage:
# hash = 0xd7d1c4d5
# getter = None
# const = None
# payable = False
def unknownd7d1c4d5(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >=′ 96
  require ext_code.size(caller)
  call caller.0x2e62efbb with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 96
  require ext_code.size(caller)
  call caller.0xec7dd7bb with:
       gas gas_remaining wei
      args ext_call.return_data[64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  require ext_code.size(_param1)
  call _param1.filled(bytes32 hash) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(_param1)
  call _param1.cancelled(bytes32 param1) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if ext_call.return_data[0]:
      return addr(_param2), addr(ext_call.return_data[32]), 0, 0
  if ext_call.return_data[96] - ext_call.return_data[0] > ext_call.return_data[96]:
      revert with 0, 'ds-math-sub-underflow'
  if not ext_call.return_data[96] - ext_call.return_data[0]:
      return addr(_param2), addr(ext_call.return_data[32]), 0, 0
  if ext_call.return_data[96] - ext_call.return_data[0] > ext_call.return_data[96]:
      revert with 0, 'ds-math-sub-underflow'
  return addr(_param2), 
         addr(ext_call.return_data[32]),
         ext_call.return_data[64],
         ext_call.return_data[96] - ext_call.return_data[0]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


