# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x308115e30d6faA1a707A8461aCf9BB41EFb23109 
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
# hash = 0x20740e9a
# getter = None
# const = None
# payable = True
def unknown20740e9a() payable: 
  call mstor0.deposit() with:
       gas gas_remaining - 25050 wei
  require ext_call.success


# hash = 0xa1c51915
# getter = None
# const = None
# payable = True
def getB() payable: 
  call mstor0.getBalance(address addressToCheck) with:
       gas gas_remaining - 25050 wei
      args this.address
  require ext_call.success
  return ext_call.return_data[0]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mstor1 > 5:
      mstor1 = 0
  else:
      if not mstor2:
          mstor1 = 0
      else:
          mstor1++
          call mstor0.withdrawBalance() with:
               gas gas_remaining - 25050 wei
          require ext_call.success


