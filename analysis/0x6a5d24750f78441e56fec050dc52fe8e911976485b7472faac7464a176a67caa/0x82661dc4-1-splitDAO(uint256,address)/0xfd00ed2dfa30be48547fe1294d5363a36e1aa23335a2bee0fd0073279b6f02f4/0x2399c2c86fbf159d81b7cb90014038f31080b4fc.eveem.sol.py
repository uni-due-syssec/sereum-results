# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2399c2C86FBF159d81b7cb90014038f31080B4FC 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    totalSupply # mask: a s
    # storage address 1
    unknown449c847c # mask: a s
    # storage address 2
    unknowne71bffd0 # mask: a s
    # storage address 3
    unknown238aa42a # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    unknownbcb0447d # mask: a s
    # storage address 6
    unknown3b0c03b1Address # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
# hash = 0x01238171
# getter = None
# const = None
# payable = True
def unknown01238171() payable: 
  if addr(munknown3b0c03b1Address) != caller:
      stop
  else:
      call mstor4.getNewDAOAddress(uint256 proposalID) with:
           gas gas_remaining - 25050 wei
          args munknownbcb0447d
      require ext_call.success
      if ext_call.return_data[12 len 20]:
          if ext_call.return_data[12 len 20] != 0:
              stop
          else:
              if mtotalSupply:
                  stop
              else:
                  call mstor4.totalSupply() with:
                       gas gas_remaining - 25050 wei
                  require ext_call.success
                  munknowne71bffd0 = ext_call.return_data[0]
                  stop
      else:
          if munknown449c847c != 0:
              if ext_call.return_data[12 len 20] != 0:
                  stop
              else:
                  if mtotalSupply:
                      stop
                  else:
                      call mstor4.totalSupply() with:
                           gas gas_remaining - 25050 wei
                      require ext_call.success
                      munknowne71bffd0 = ext_call.return_data[0]
                      stop
          else:
              call mstor4.actualBalance() with:
                   gas gas_remaining - 25050 wei
              require ext_call.success
              munknown238aa42a = ext_call.return_data[0]
              if addr(ext_call.return_data[0]) != 0:
                  stop
              else:
                  if mtotalSupply:
                      stop
                  else:
                      call mstor4.totalSupply() with:
                           gas gas_remaining - 25050 wei
                      require ext_call.success
                      munknowne71bffd0 = ext_call.return_data[0]
                      stop


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 0]
# const = None
# payable = True
def totalSupply() payable: 
  return mtotalSupply


# hash = 0x238aa42a
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def unknown238aa42a() payable: 
  return munknown238aa42a


# hash = 0x3a1f074f
# getter = None
# const = None
# payable = True
def unknown3a1f074f() payable: 
  call mstor4.getNewDAOAddress(uint256 proposalID) with:
       gas gas_remaining - 25050 wei
      args munknownbcb0447d
  require ext_call.success
  if ext_call.return_data[12 len 20] != 0:
      if munknown449c847c != 0:
          return munknown449c847c
  return munknown238aa42a


# hash = 0x3b0c03b1
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def unknown3b0c03b1() payable: 
  return addr(munknown3b0c03b1Address)


# hash = 0x449c847c
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def unknown449c847c() payable: 
  return munknown449c847c


# hash = 0x632a9a52
# getter = None
# const = None
# payable = True
def vote() payable: 
  if addr(munknown3b0c03b1Address) == caller:
      call mstor4.vote(uint256 proposalNumber, bool supportsProposal) with:
           gas gas_remaining - 25050 wei
          args munknownbcb0447d, 1
      require ext_call.success
      call mstor4.actualBalance() with:
           gas gas_remaining - 25050 wei
      munknown238aa42a = ext_call.return_data[0]
      call mstor4.totalSupply() with:
           gas gas_remaining - 25050 wei
      munknowne71bffd0 = ext_call.return_data[0]


# hash = 0x76eb6ade
# getter = None
# const = None
# payable = True
def unknown76eb6ade(uint256 m_param1, uint256 m_param2) payable: 
  if addr(munknown3b0c03b1Address) == caller:
      mtotalSupply = m_param1
      munknown449c847c = m_param2


# hash = 0x8fdf8b8e
# getter = None
# const = None
# payable = True
def unknown8fdf8b8e(uint256 m_param1) payable: 
  if addr(munknown3b0c03b1Address) == caller:
      uint256(mstor6) = m_param1 or Mask(96, 160, uint256(mstor6))


# hash = 0x9d1a5a77
# getter = None
# const = None
# payable = True
def unknown9d1a5a77() payable: 
  if addr(munknown3b0c03b1Address) == caller:
      call mstor4.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      call mstor4.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args 0xc3214c8236d937874cf666ba3ac221c35273f82f, ext_call.return_data[0]


# hash = 0xb61d27f6
# getter = None
# const = None
# payable = True
def execute(address m_to, uint256 m_value, bytes m_data) payable: 
  mem[128 len m_data.length] = m_data[allm]
  if caller == addr(munknown3b0c03b1Address):
      mem[ceil32(m_data.length) + 128 len m_data.length] = m_data[allm]
      if not m_data.length % 32:
          call m_to with:
             value m_value wei
               gas gas_remaining - 34050 wei
              args m_data[allm]
      else:
          mem[floor32(m_data.length) + ceil32(m_data.length) + 128] = mem[floor32(m_data.length) + ceil32(m_data.length) + -(m_data.length % 32) + 160 len m_data.length % 32]
          call m_to.mem[ceil32(m_data.length) + 128 len 4] with:
             value m_value wei
               gas gas_remaining - 34050 wei
              args mem[ceil32(m_data.length) + 132 len floor32(m_data.length) + 28]


# hash = 0xbcb0447d
# getter = ['storage', 256, 0, 5]
# const = None
# payable = True
def unknownbcb0447d() payable: 
  return munknownbcb0447d


# hash = 0xc4e41b22
# getter = None
# const = None
# payable = True
def getTotalSupply() payable: 
  call mstor4.getNewDAOAddress(uint256 proposalID) with:
       gas gas_remaining - 25050 wei
      args munknownbcb0447d
  require ext_call.success
  if ext_call.return_data[12 len 20] != 0:
      if mtotalSupply != 0:
          return mtotalSupply
  return munknowne71bffd0


# hash = 0xdbceb005
# getter = None
# const = None
# payable = True
def split(uint256 m_amountToSplit) payable: 
  if addr(munknown3b0c03b1Address) != caller:
      stop
  else:
      mstor7 = m_amountToSplit
      call mstor4.proposals(uint256 param1) with:
           gas gas_remaining - 25050 wei
          args munknownbcb0447d
      require ext_call.success
      uint256(mstor8) = ext_call.return_data[0] or Mask(96, 160, uint256(mstor8))
      call mstor4.rewardAccount() with:
           gas gas_remaining - 25050 wei
      mstor9 = ext_call.return_data[0] or Mask(96, 160, mstor9)
      call mstor4.getNewDAOAddress(uint256 proposalID) with:
           gas gas_remaining - 25050 wei
          args munknownbcb0447d
      if ext_call.return_data[12 len 20]:
          call mstor4.splitDAO(uint256 proposalID, address newCurator) with:
               gas gas_remaining - 25050 wei
              args munknownbcb0447d, addr(mstor8)
          require ext_call.success
          call addr(munknown3b0c03b1Address).sendEther() with:
             value eth.balance(this.address) wei
               gas gas_remaining - 34050 wei
          stop
      else:
          call mstor4.totalSupply() with:
               gas gas_remaining - 25050 wei
          require ext_call.success
          mtotalSupply = ext_call.return_data[0]
          call mstor4.actualBalance() with:
               gas gas_remaining - 25050 wei
          munknown449c847c = ext_call.return_data[0]
          if not m_amountToSplit:
              mstor7 = 0
              call mstor4.splitDAO(uint256 proposalID, address newCurator) with:
                   gas gas_remaining - 25050 wei
                  args munknownbcb0447d, addr(mstor8)
              require ext_call.success
              call addr(munknown3b0c03b1Address).sendEther() with:
                 value eth.balance(this.address) wei
                   gas gas_remaining - 34050 wei
              stop
          else:
              mstor7 = 1
              call mstor4.splitDAO(uint256 proposalID, address newCurator) with:
                   gas gas_remaining - 25050 wei
                  args munknownbcb0447d, addr(mstor8)
              require ext_call.success
              call addr(munknown3b0c03b1Address).sendEther() with:
                 value eth.balance(this.address) wei
                   gas gas_remaining - 34050 wei
              stop


# hash = 0xe71bffd0
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def unknowne71bffd0() payable: 
  return munknowne71bffd0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mstor7 <= 0:
      call mstor4.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      call mstor4.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args addr(munknown3b0c03b1Address), ext_call.return_data[0]
  else:
      mstor7--
      call mstor4.splitDAO(uint256 proposalID, address newCurator) with:
           gas gas_remaining - 25050 wei
          args munknownbcb0447d, addr(mstor8)
      require ext_call.success
  return 1


