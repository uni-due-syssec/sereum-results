# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0542b7D013ff3AFf9C897Bb98098c47E85d3B000 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown4f747cb8Address # mask: a s
    # storage address 1
    totalBets # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    totalPlayers # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    gameId # mask: a s
    # storage address 4
    unknownc5aa6e77 # mask: a s
    # storage address 5
    unknown7e0ecc00
# hash = 0x4f747cb8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown4f747cb8(): # not payable
  return munknown4f747cb8Address


# hash = 0x610be654
# getter = None
# const = None
# payable = False
def closeContract(): # not payable
  require caller == munknown4f747cb8Address
  uint8(mstor2m.field_8) = 1
  return 1


# hash = 0x7e0ecc00
# getter = ['struct', ['loc', 5]]
# const = None
# payable = False
def unknown7e0ecc00(uint8 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown7e0ecc00m[m_param1m]m.field_0, munknown7e0ecc00m[m_param1m]m.field_256


# hash = 0xbefa1e2f
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def totalBets(): # not payable
  return mtotalBets


# hash = 0xc5aa6e77
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknownc5aa6e77(): # not payable
  return munknownc5aa6e77


# hash = 0xd7c81b55
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def gameId(): # not payable
  return mgameId


# hash = 0xead3a0fe
# getter = None
# const = None
# payable = False
def unknownead3a0fe(): # not payable
  require caller == munknown4f747cb8Address
  if eth.balance(this.address) < munknownc5aa6e77:
      return 0
  require ext_code.size(munknown4f747cb8Address)
  call munknown4f747cb8Address.getFunds() with:
     value eth.balance(this.address) wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return eth.balance(this.address)


# hash = 0xf60cdcf6
# getter = ['storage', 8, 0, 2]
# const = None
# payable = False
def totalPlayers(): # not payable
  return mtotalPlayers


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require call.value >= munknownc5aa6e77
  require bool(ext_code.size(caller)) != 1
  require not uint8(mstor2m.field_8)
  require ext_code.size(0x231773551c008d9df068e8742691c52d1d86b2fe)
  [93mdelegate 0x231773551c008d9df068e8742691c52d1d86b2fe.add(uint256 a, uint256 b) with:
       gas gas_remaining wei
      args mtotalBets, call.value
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mtotalBets = delegate.return_data[0]
  require ext_code.size(0x231773551c008d9df068e8742691c52d1d86b2fe)
  [93mdelegate 0x231773551c008d9df068e8742691c52d1d86b2fe.add(uint256 a, uint256 b) with:
       gas gas_remaining wei
      args mtotalPlayers, 1
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor2m.field_0) = delegate.return_data[31 len 1] or Mask(248, 8, uint256(mstor2m.field_0))
  munknown7e0ecc00m[delegate.return_data[31 len 1]m]m.field_0 = caller
  munknown7e0ecc00m[delegate.return_data[31 len 1]m]m.field_256 = call.value
  require ext_code.size(munknown4f747cb8Address)
  call munknown4f747cb8Address.participate() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


