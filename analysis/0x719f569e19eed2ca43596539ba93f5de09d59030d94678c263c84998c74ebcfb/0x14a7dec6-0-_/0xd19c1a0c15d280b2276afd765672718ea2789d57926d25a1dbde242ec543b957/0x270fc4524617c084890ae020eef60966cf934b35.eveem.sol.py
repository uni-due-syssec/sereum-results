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
  if mstor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address m_newAdmin): # not payable
  if mstor0 == caller:
      mstor0 = m_newAdmin


# hash = 0xbb34534c
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def addressOf(bytes32 m_name): # not payable
  return maddressOfm[m_namem]


# hash = 0xe1fa8e84
# getter = None
# const = None
# payable = False
def register(bytes32 m_name): # not payable
  if mstor0 == tx.origin:
      if mnameOfm[callerm]:
          maddressOfm[mstor1m[callerm]m] = 0
      mnameOfm[callerm] = m_name
      maddressOfm[m_namem] = caller
      log 0xb2899cb2: caller


# hash = 0xe79a198f
# getter = None
# const = None
# payable = False
def unregister(): # not payable
  if mstor0 == tx.origin:
      if mnameOfm[callerm]:
          log 0xe4519776: addressOf[stor1[caller]]
          mnameOfm[callerm] = 0
          maddressOfm[mstor1m[callerm]m] = 0


# hash = 0xf5c57382
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]
# const = None
# payable = False
def nameOf(address m_param1): # not payable
  return mnameOfm[addr(m_param1)m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


