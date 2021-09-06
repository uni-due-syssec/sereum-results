# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x270fC4524617c084890ae020eEF60966CF934b35 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    nameOf
    # storage address 2
    addressOf
# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if stor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  if stor0 == caller:
      stor0 = _newAdmin


# hash = 0xbb34534c
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def addressOf(bytes32 _name): # not payable
  return addressOf[_name]


# hash = 0xe1fa8e84
# getter = None
# const = None
# payable = False
def register(bytes32 _name): # not payable
  if stor0 == tx.origin:
      if nameOf[caller]:
          addressOf[stor1[caller]] = 0
      nameOf[caller] = _name
      addressOf[_name] = caller
      log 0xb2899cb2: caller


# hash = 0xe79a198f
# getter = None
# const = None
# payable = False
def unregister(): # not payable
  if stor0 == tx.origin:
      if nameOf[caller]:
          log 0xe4519776: addressOf[stor1[caller]]
          nameOf[caller] = 0
          addressOf[stor1[caller]] = 0


# hash = 0xf5c57382
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]
# const = None
# payable = False
def nameOf(address _param1): # not payable
  return nameOf[addr(_param1)]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


