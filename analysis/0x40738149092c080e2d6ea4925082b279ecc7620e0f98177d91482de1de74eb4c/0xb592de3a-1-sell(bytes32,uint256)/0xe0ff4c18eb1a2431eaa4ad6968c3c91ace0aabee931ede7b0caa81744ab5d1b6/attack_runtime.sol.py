#
#  Panoramix 17 Feb 2020
#

const transferFrom(address _from, address _to, uint256 _value) = 1

def storage:
  stor0 is uint256 at storage 0
  stor1 is uint256 at storage 1

#
#  Regular functions
#

def unknown34196683(uint256 _param1, uint256 _param2) payable:
  stor0 = _param1
  stor1 = _param2
  require ext_code.size(0x72f60eca0db6811274215694129661151f97982e)
  call 0x72f60eca0db6811274215694129661151f97982e.sell(bytes32 id, uint256 amount) with:
       gas gas_remaining wei
      args _param1, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  selfdestruct(caller)

def _fallback() payable: # default function
  stop

def transfer(address _to, uint256 _value) payable:
  if eth.balance(0x72f60eca0db6811274215694129661151f97982e) >= stor1:
      require ext_code.size(0x72f60eca0db6811274215694129661151f97982e)
      call 0x72f60eca0db6811274215694129661151f97982e.sell(bytes32 id, uint256 amount) with:
           gas gas_remaining wei
          args stor0, 1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  return 1
