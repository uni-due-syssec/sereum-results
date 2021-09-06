# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7F000000612813280074000600F710002BDBAa9c 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require not caller xor 0x2b13cccec913420a21e4d11b2dcd3c
  [93mselfdestruct([91m0xb3ff5753a4a0c335b2784b8d6a928ae0b4bdffc7[93m)


