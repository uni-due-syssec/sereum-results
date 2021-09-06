# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xbD4A5110B62dB3F4dc2F2dDBBC0DEB43dCCB40A8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
# hash = 0x4ddd108a
# getter = None
# const = None
# payable = False
def money(): # not payable
  require caller == stor1
  call stor1 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xb74387fc
# getter = None
# const = None
# payable = False
def unknownb74387fc(): # not payable
  require caller == stor1
  stor2 = 0
  require ext_code.size(stor0)
  call stor0.payoutPreviousRoll() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xe3295ec2
# getter = None
# const = None
# payable = True
def unknowne3295ec2() payable: 
  require caller == stor1
  require ext_code.size(stor0)
  call stor0.roll(uint8 number) with:
     value call.value wei
       gas gas_remaining wei
      args 98
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stor2++
  if gas_remaining > stor4 + (stor2 * stor3):
      require ext_code.size(stor0)
      call stor0.payoutPreviousRoll() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


