# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x577F79222a8787EeA6E356a7a94633b2173Fc265 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknownc215290a
    # storage address 1
    balanceOf
    # storage address 2
    tokenAddress # mask: a s
# hash = 0x3d456aa5
# getter = None
# const = None
# payable = True
def unknown3d456aa5(uint256 m_param1) payable: 
  if m_param1 > 0:
      munknownc215290am[callerm] += 24 * 3600 * m_param1
      log 0xe96f81a9: caller, _param1


# hash = 0x52ece9be
# getter = None
# const = None
# payable = True
def unknown52ece9be(uint256 m_param1) payable: 
  call mtokenAddress.allowance(address owner, address spender) with:
       gas gas_remaining - 25050 wei
      args caller, this.address
  require ext_call.success
  require ext_call.return_data[0] > 0
  require m_param1 > 0
  call mtokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining - 25050 wei
      args caller, addr(this.address), ext_call.return_data[0]
  require ext_call.success
  require ext_call.return_data[0]
  munknownc215290am[callerm] = block.timestamp + (24 * 3600 * m_param1)
  mbalanceOfm[callerm] += ext_call.return_data[0]
  log 0x7497457e: caller, _param1, ext_call.return_data[0]
  return ext_call.return_data[0]


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = True
def withdrawBalance() payable: 
  if block.timestamp <= munknownc215290am[callerm]:
      return 0
  mbalanceOfm[callerm] = 0
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining - 25050 wei
      args caller, mbalanceOfm[callerm]
  require ext_call.success
  log 0xddc398b3: caller, balanceOf[caller]
  return mbalanceOfm[callerm]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]
# const = None
# payable = True
def balanceOf(address m_owner) payable: 
  return mbalanceOfm[addr(m_owner)m]


# hash = 0xc215290a
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = True
def unknownc215290a(addr m_param1) payable: 
  return munknownc215290am[addr(m_param1)m]


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def token() payable: 
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


