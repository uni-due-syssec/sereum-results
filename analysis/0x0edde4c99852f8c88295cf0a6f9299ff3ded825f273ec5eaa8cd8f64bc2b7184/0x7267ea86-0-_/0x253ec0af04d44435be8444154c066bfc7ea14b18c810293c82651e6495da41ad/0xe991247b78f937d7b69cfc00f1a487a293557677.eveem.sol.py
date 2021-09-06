# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xE991247b78F937D7B69cFC00f1A487A293557677 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    controllerAddress # mask: a s
    # storage address 1
    controllerLookupName # mask: a s
# hash = 0x3018205f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getController(): # not payable
  return mcontrollerAddress


# hash = 0x92eefe9b
# getter = None
# const = None
# payable = False
def setController(address m_c): # not payable
  require mcontrollerAddress == caller
  mcontrollerAddress = m_c
  return 1


# hash = 0xbef72fa2
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def controllerLookupName(): # not payable
  return mcontrollerLookupName


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if not mcontrollerLookupName:
      stop
  require ext_code.size(mcontrollerAddress)
  call mcontrollerAddress.lookup(bytes32 param1) with:
       gas gas_remaining - 710 wei
      args mcontrollerLookupName
  require ext_call.success
  [93mdelegate ext_call.return_data[0] with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  require delegate.return_code
  return ext_call.return_data[0 len return_data.size]


