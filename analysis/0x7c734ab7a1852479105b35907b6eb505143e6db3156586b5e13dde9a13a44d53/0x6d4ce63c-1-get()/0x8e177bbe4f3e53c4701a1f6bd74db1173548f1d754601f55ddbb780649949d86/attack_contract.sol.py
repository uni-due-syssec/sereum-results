#
#  Panoramix 17 Feb 2020
#

def storage:
  stor0 is uint8 at storage 0

def go() payable:
  require ext_code.size(0xeb68f34efa0086e4136bca51fc4d0696580643e)
  call 0x0eb68f34efa0086e4136bca51fc4d0696580643e.0x549262ba with:
     value call.value wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0xeb68f34efa0086e4136bca51fc4d0696580643e)
  call 0x0eb68f34efa0086e4136bca51fc4d0696580643e.get() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require eth.balance(this.address) < eth.balance(this.address)
  selfdestruct(tx.origin)

def _fallback() payable: # default function
  if not stor0:
      stor0 = 1
      require ext_code.size(0xeb68f34efa0086e4136bca51fc4d0696580643e)
      call 0x0eb68f34efa0086e4136bca51fc4d0696580643e.get() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
