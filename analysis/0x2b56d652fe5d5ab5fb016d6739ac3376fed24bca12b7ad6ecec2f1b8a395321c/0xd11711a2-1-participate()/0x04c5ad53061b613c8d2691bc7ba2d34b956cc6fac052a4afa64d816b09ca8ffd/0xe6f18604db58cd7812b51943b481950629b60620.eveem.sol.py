# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xE6f18604Db58Cd7812b51943b481950629B60620 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 19
    depositOf
    # storage address 15
    stor15 # mask: a s
    # storage address 1
    version
    # storage address 18
    wallets
    # storage address 14
    stor14
    # storage address 20
    gamesLog
    # storage address 7
    wallet_2Address # mask: a s
    # storage address 8
    finishTime # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 6
    wallet_1Address # mask: a s
    # storage address 4
    minPayment # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 64284843162247381215979476806684916065743510587729232560922368151854080304818
    stor8E1F # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 16
    stor16 # mask: a s
    # storage address 2
    secureAddress # mask: a s
    # storage address 3
    games # mask: a s
    # storage address 5
    wallet_0Address # mask: a s
    # storage address 9
    roundDuration # mask: a s
# hash = 0x23e3fbd5
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 19]]]
# const = None
# payable = False
def depositOf(address m_payee): # not payable
  require calldata.size - 4 >= 32
  return mdepositOfm[addr(m_payee)m]


# hash = 0x2e276499
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def minPayment(): # not payable
  return mminPayment


# hash = 0x36c92c3f
# getter = None
# const = None
# payable = False
def setRoundDuration(uint256 m_a): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  mroundDuration = m_a
  return 1


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  mdepositOfm[callerm] = 0
  call caller with:
     value mdepositOfm[callerm] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log Withdrawn(
        address payee=depositOf[caller],
        uint256 weiAmount=caller)


# hash = 0x4d9b3735
# getter = None
# const = None
# payable = True
def getFunds() payable: 
  if mwallet_0Address != caller:
      if mwallet_1Address != caller:
          require caller == mwallet_2Address


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x56084664
# getter = ['struct', ['loc', 20]]
# const = None
# payable = False
def gamesLog(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return mgamesLogm[m_param1m]m.field_0, 
         mgamesLogm[m_param1m]m.field_256,
         mgamesLogm[m_param1m]m.field_512,
         mgamesLogm[m_param1m]m.field_768,
         mgamesLogm[m_param1m]m.field_1024


# hash = 0x5958611e
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def finishTime(): # not payable
  return mfinishTime


# hash = 0x63b4b112
# getter = None
# const = None
# payable = False
def setSecure(address m_address): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  msecureAddress = m_address
  return 1


# hash = 0x6d427fa3
# getter = None
# const = None
# payable = False
def setMinPayment(uint256 m_value): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  mminPayment = m_value


# hash = 0x7024dc2e
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def wallet_2(): # not payable
  return mwallet_2Address


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x7ad71f72
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 18]]]
# const = None
# payable = False
def wallets(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return mwalletsm[m_param1m]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == mowner)


# hash = 0x955a015b
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def games(): # not payable
  return mgames


# hash = 0xb69fcd5d
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def secure(): # not payable
  return msecureAddress


# hash = 0xb82b245e
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def wallet_1(): # not payable
  return mwallet_1Address


# hash = 0xd11711a2
# getter = None
# const = None
# payable = False
def participate(): # not payable
  if caller == mwallet_0Address:
      require msecureAddress
      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
           gas gas_remaining wei
          args mstor10, 1
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mstor10 = delegate.return_data[0]
      require ext_code.size(mwalletsm[0m])
      static call mwalletsm[0m].totalPlayers() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mwalletsm[1m])
      static call mwalletsm[1m].totalPlayers() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
           gas gas_remaining wei
          args ext_call.return_data[0] << 248, uint8(ext_call.return_data[0])
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mstor8E1F)
      static call mstor8E1F.totalPlayers() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
           gas gas_remaining wei
          args delegate.return_data[0], uint8(ext_call.return_data[0])
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mstor12) = delegate.return_data[0]
      if block.timestamp < mfinishTime:
          if uint256(mstor12) >= mstor11:
              require ext_code.size(mwallet_0Address)
              call mwallet_0Address.0xead3a0fe with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                   gas gas_remaining wei
                  args mstor15, ext_call.return_data[0]
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mstor15 = delegate.return_data[0]
              require ext_code.size(mwallet_1Address)
              call mwallet_1Address.0xead3a0fe with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                   gas gas_remaining wei
                  args delegate.return_data[0], ext_call.return_data[0]
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mstor15 = delegate.return_data[0]
              require ext_code.size(mwallet_2Address)
              call mwallet_2Address.0xead3a0fe with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                   gas gas_remaining wei
                  args delegate.return_data[0], ext_call.return_data[0]
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mstor15 = delegate.return_data[0]
              if delegate.return_data[0]:
                  [94midx = 0
                  mwhile uint8([94midx) < 3m:
                      mem[0] = uint8([94midx)
                      mem[32] = 18
                      require ext_code.size(mwalletsm[[94midx << 248m])
                      static call mwalletsm[[94midx << 248m].totalPlayers() with:
                              gas gas_remaining wei
                      mem[96] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[31 len 1] > 0:
                          mstor14m.length++
                          mem[0] = 14
                          mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                      [94midx = [94midx + 1
                      mcontinue 
                  require ext_code.size(msecureAddress)
                  static call msecureAddress.0x74550831 with:
                          gas gas_remaining wei
                         args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[31 len 1] < mstor14m.length
                  mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                  require ext_code.size(mwalletsm[mstor13m])
                  static call mwalletsm[mstor13m].totalPlayers() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  uint256(mstor12) = ext_call.return_data[31 len 1]
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, 15
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], 100
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor16 = delegate.return_data[0]
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, delegate.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor17 = delegate.return_data[0]
                  [94midx = 1
                  [94ms = 0
                  [94ms = 0
                  [94ms = 0
                  mwhile uint8([94midx) <= uint256(mstor12)m:
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].0x7e0ecc00 with:
                              gas gas_remaining wei
                             args uint8([94midx)
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 64
                      mem[128] = ext_call.return_data[32]
                      mem[96] = addr(ext_call.return_data[0])
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args ext_call.return_data[32], 10000
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].totalBets() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor17, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], 10000
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args [94ms, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                      mem[196] = delegate.return_data[0]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[0] = addr(ext_call.return_data[0])
                      mem[32] = 19
                      mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                      mem[160] = delegate.return_data[0]
                      log Deposited(
                            address payee=delegate.return_data[0],
                            uint256 weiAmount=addr(ext_call.return_data[0]))
                      [94midx = [94midx + 1
                      [94ms = delegate.return_data[0]
                      [94ms = delegate.return_data[0]
                      [94ms = delegate.return_data[0]
                      mcontinue 
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, _3370 * None
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mdepositOfm[mstor0m], delegate.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mdepositOfm[mstor0m] = delegate.return_data[0]
                  log Deposited(
                        address payee=delegate.return_data[0],
                        uint256 weiAmount=owner)
                  mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                  mgamesLogm[mstor3m]m.field_256 = block.timestamp
                  mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                  mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                  mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                  log WinnerWallet(
                        address wallet=stor15,
                        uint256 bank=wallets[stor13])
                  mstor15 = 0
                  mstor14m.length = 0
                  [94midx = 0
                  mwhile mstor14m.length + 31 / 32 > [94midxm:
                      mstor14m[[94midxm]m.field_0 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mgames, 1
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mgames = delegate.return_data[0]
                  require ext_code.size(mwalletsm[0m])
                  call mwalletsm[0m].closeContract() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(mwalletsm[1m])
                  call mwalletsm[1m].closeContract() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(mstor8E1F)
                  call mstor8E1F.closeContract() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'break on switch'
                  create contract with 0 wei
                                  code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                  if not create.new_address:
                      revert with ext_call.return_data[0 len return_data.size]
                  mwallet_0Address = addr(create.new_address)
                  mwalletsm[0m] = addr(create.new_address)
                  create contract with 0 wei
                                  code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                  mwallet_1Address = addr(create.new_address)
                  mwalletsm[1m] = addr(create.new_address)
                  create contract with 0 wei
                                  code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                  mwallet_2Address = addr(create.new_address)
                  mstor8E1F = addr(create.new_address)
      else:
          if uint256(mstor12) != 1:
              if block.timestamp >= mfinishTime:
                  require ext_code.size(mwallet_0Address)
                  call mwallet_0Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_1Address)
                  call mwallet_1Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_2Address)
                  call mwallet_2Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  if delegate.return_data[0]:
                      [94midx = 0
                      mwhile uint8([94midx) < 3m:
                          mem[0] = uint8([94midx)
                          mem[32] = 18
                          require ext_code.size(mwalletsm[[94midx << 248m])
                          static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                  gas gas_remaining wei
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if ext_call.return_data[31 len 1] > 0:
                              mstor14m.length++
                              mem[0] = 14
                              mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(msecureAddress)
                      static call msecureAddress.0x74550831 with:
                              gas gas_remaining wei
                             args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[31 len 1] < mstor14m.length
                      mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].totalPlayers() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      uint256(mstor12) = ext_call.return_data[31 len 1]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, 15
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], 100
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor16 = delegate.return_data[0]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor17 = delegate.return_data[0]
                      [94midx = 1
                      [94ms = 0
                      [94ms = 0
                      [94ms = 0
                      mwhile uint8([94midx) <= uint256(mstor12)m:
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                  gas gas_remaining wei
                                 args uint8([94midx)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          mem[128] = ext_call.return_data[32]
                          mem[96] = addr(ext_call.return_data[0])
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args ext_call.return_data[32], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalBets() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor17, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args [94ms, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                          mem[196] = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[0] = addr(ext_call.return_data[0])
                          mem[32] = 19
                          mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                          mem[160] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=addr(ext_call.return_data[0]))
                          [94midx = [94midx + 1
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, _3372 * None
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mdepositOfm[mstor0m], delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mdepositOfm[mstor0m] = delegate.return_data[0]
                      log Deposited(
                            address payee=delegate.return_data[0],
                            uint256 weiAmount=owner)
                      mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                      mgamesLogm[mstor3m]m.field_256 = block.timestamp
                      mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                      mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                      mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                      log WinnerWallet(
                            address wallet=stor15,
                            uint256 bank=wallets[stor13])
                      mstor15 = 0
                      mstor14m.length = 0
                      [94midx = 0
                      mwhile mstor14m.length + 31 / 32 > [94midxm:
                          mstor14m[[94midxm]m.field_0 = 0
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mgames, 1
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mgames = delegate.return_data[0]
                      require ext_code.size(mwalletsm[0m])
                      call mwalletsm[0m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mwalletsm[1m])
                      call mwalletsm[1m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mstor8E1F)
                      call mstor8E1F.closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'break on switch'
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      if not create.new_address:
                          revert with ext_call.return_data[0 len return_data.size]
                      mwallet_0Address = addr(create.new_address)
                      mwalletsm[0m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_1Address = addr(create.new_address)
                      mwalletsm[1m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_2Address = addr(create.new_address)
                      mstor8E1F = addr(create.new_address)
              else:
                  if uint256(mstor12) >= mstor11:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3374 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
          else:
              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                   gas gas_remaining wei
                  args block.timestamp, mroundDuration
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mfinishTime = delegate.return_data[0]
              if block.timestamp >= mfinishTime:
                  require ext_code.size(mwallet_0Address)
                  call mwallet_0Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_1Address)
                  call mwallet_1Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_2Address)
                  call mwallet_2Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  if delegate.return_data[0]:
                      [94midx = 0
                      mwhile uint8([94midx) < 3m:
                          mem[0] = uint8([94midx)
                          mem[32] = 18
                          require ext_code.size(mwalletsm[[94midx << 248m])
                          static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                  gas gas_remaining wei
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if ext_call.return_data[31 len 1] > 0:
                              mstor14m.length++
                              mem[0] = 14
                              mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(msecureAddress)
                      static call msecureAddress.0x74550831 with:
                              gas gas_remaining wei
                             args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[31 len 1] < mstor14m.length
                      mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].totalPlayers() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      uint256(mstor12) = ext_call.return_data[31 len 1]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, 15
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], 100
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor16 = delegate.return_data[0]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor17 = delegate.return_data[0]
                      [94midx = 1
                      [94ms = 0
                      [94ms = 0
                      [94ms = 0
                      mwhile uint8([94midx) <= uint256(mstor12)m:
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                  gas gas_remaining wei
                                 args uint8([94midx)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          mem[128] = ext_call.return_data[32]
                          mem[96] = addr(ext_call.return_data[0])
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args ext_call.return_data[32], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalBets() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor17, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args [94ms, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                          mem[196] = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[0] = addr(ext_call.return_data[0])
                          mem[32] = 19
                          mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                          mem[160] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=addr(ext_call.return_data[0]))
                          [94midx = [94midx + 1
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, _3376 * None
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mdepositOfm[mstor0m], delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mdepositOfm[mstor0m] = delegate.return_data[0]
                      log Deposited(
                            address payee=delegate.return_data[0],
                            uint256 weiAmount=owner)
                      mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                      mgamesLogm[mstor3m]m.field_256 = block.timestamp
                      mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                      mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                      mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                      log WinnerWallet(
                            address wallet=stor15,
                            uint256 bank=wallets[stor13])
                      mstor15 = 0
                      mstor14m.length = 0
                      [94midx = 0
                      mwhile mstor14m.length + 31 / 32 > [94midxm:
                          mstor14m[[94midxm]m.field_0 = 0
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mgames, 1
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mgames = delegate.return_data[0]
                      require ext_code.size(mwalletsm[0m])
                      call mwalletsm[0m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mwalletsm[1m])
                      call mwalletsm[1m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mstor8E1F)
                      call mstor8E1F.closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'break on switch'
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      if not create.new_address:
                          revert with ext_call.return_data[0 len return_data.size]
                      mwallet_0Address = addr(create.new_address)
                      mwalletsm[0m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_1Address = addr(create.new_address)
                      mwalletsm[1m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_2Address = addr(create.new_address)
                      mstor8E1F = addr(create.new_address)
              else:
                  if uint256(mstor12) >= mstor11:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3378 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
  else:
      if caller == mwallet_1Address:
          require msecureAddress
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args mstor10, 1
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mstor10 = delegate.return_data[0]
          require ext_code.size(mwalletsm[0m])
          static call mwalletsm[0m].totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(mwalletsm[1m])
          static call mwalletsm[1m].totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args ext_call.return_data[0] << 248, uint8(ext_call.return_data[0])
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(mstor8E1F)
          static call mstor8E1F.totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args delegate.return_data[0], uint8(ext_call.return_data[0])
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mstor12) = delegate.return_data[0]
          if block.timestamp < mfinishTime:
              if uint256(mstor12) >= mstor11:
                  require ext_code.size(mwallet_0Address)
                  call mwallet_0Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_1Address)
                  call mwallet_1Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_2Address)
                  call mwallet_2Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  if delegate.return_data[0]:
                      [94midx = 0
                      mwhile uint8([94midx) < 3m:
                          mem[0] = uint8([94midx)
                          mem[32] = 18
                          require ext_code.size(mwalletsm[[94midx << 248m])
                          static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                  gas gas_remaining wei
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if ext_call.return_data[31 len 1] > 0:
                              mstor14m.length++
                              mem[0] = 14
                              mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(msecureAddress)
                      static call msecureAddress.0x74550831 with:
                              gas gas_remaining wei
                             args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[31 len 1] < mstor14m.length
                      mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].totalPlayers() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      uint256(mstor12) = ext_call.return_data[31 len 1]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, 15
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], 100
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor16 = delegate.return_data[0]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor17 = delegate.return_data[0]
                      [94midx = 1
                      [94ms = 0
                      [94ms = 0
                      [94ms = 0
                      mwhile uint8([94midx) <= uint256(mstor12)m:
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                  gas gas_remaining wei
                                 args uint8([94midx)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          mem[128] = ext_call.return_data[32]
                          mem[96] = addr(ext_call.return_data[0])
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args ext_call.return_data[32], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalBets() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor17, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args [94ms, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                          mem[196] = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[0] = addr(ext_call.return_data[0])
                          mem[32] = 19
                          mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                          mem[160] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=addr(ext_call.return_data[0]))
                          [94midx = [94midx + 1
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, _3380 * None
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mdepositOfm[mstor0m], delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mdepositOfm[mstor0m] = delegate.return_data[0]
                      log Deposited(
                            address payee=delegate.return_data[0],
                            uint256 weiAmount=owner)
                      mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                      mgamesLogm[mstor3m]m.field_256 = block.timestamp
                      mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                      mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                      mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                      log WinnerWallet(
                            address wallet=stor15,
                            uint256 bank=wallets[stor13])
                      mstor15 = 0
                      mstor14m.length = 0
                      [94midx = 0
                      mwhile mstor14m.length + 31 / 32 > [94midxm:
                          mstor14m[[94midxm]m.field_0 = 0
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mgames, 1
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mgames = delegate.return_data[0]
                      require ext_code.size(mwalletsm[0m])
                      call mwalletsm[0m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mwalletsm[1m])
                      call mwalletsm[1m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mstor8E1F)
                      call mstor8E1F.closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'break on switch'
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      if not create.new_address:
                          revert with ext_call.return_data[0 len return_data.size]
                      mwallet_0Address = addr(create.new_address)
                      mwalletsm[0m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_1Address = addr(create.new_address)
                      mwalletsm[1m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_2Address = addr(create.new_address)
                      mstor8E1F = addr(create.new_address)
          else:
              if uint256(mstor12) != 1:
                  if block.timestamp >= mfinishTime:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3382 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
                  else:
                      if uint256(mstor12) >= mstor11:
                          require ext_code.size(mwallet_0Address)
                          call mwallet_0Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_1Address)
                          call mwallet_1Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_2Address)
                          call mwallet_2Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          if delegate.return_data[0]:
                              [94midx = 0
                              mwhile uint8([94midx) < 3m:
                                  mem[0] = uint8([94midx)
                                  mem[32] = 18
                                  require ext_code.size(mwalletsm[[94midx << 248m])
                                  static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                          gas gas_remaining wei
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if ext_call.return_data[31 len 1] > 0:
                                      mstor14m.length++
                                      mem[0] = 14
                                      mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(msecureAddress)
                              static call msecureAddress.0x74550831 with:
                                      gas gas_remaining wei
                                     args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[31 len 1] < mstor14m.length
                              mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalPlayers() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              uint256(mstor12) = ext_call.return_data[31 len 1]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, 15
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 100
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor16 = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor17 = delegate.return_data[0]
                              [94midx = 1
                              [94ms = 0
                              [94ms = 0
                              [94ms = 0
                              mwhile uint8([94midx) <= uint256(mstor12)m:
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                          gas gas_remaining wei
                                         args uint8([94midx)
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 64
                                  mem[128] = ext_call.return_data[32]
                                  mem[96] = addr(ext_call.return_data[0])
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[32], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].totalBets() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], ext_call.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mstor17, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args [94ms, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                                  mem[196] = delegate.return_data[0]
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr(ext_call.return_data[0])
                                  mem[32] = 19
                                  mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                                  mem[160] = delegate.return_data[0]
                                  log Deposited(
                                        address payee=delegate.return_data[0],
                                        uint256 weiAmount=addr(ext_call.return_data[0]))
                                  [94midx = [94midx + 1
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, _3384 * None
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[mstor0m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mdepositOfm[mstor0m] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=owner)
                              mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                              mgamesLogm[mstor3m]m.field_256 = block.timestamp
                              mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                              mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                              mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                              log WinnerWallet(
                                    address wallet=stor15,
                                    uint256 bank=wallets[stor13])
                              mstor15 = 0
                              mstor14m.length = 0
                              [94midx = 0
                              mwhile mstor14m.length + 31 / 32 > [94midxm:
                                  mstor14m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mgames, 1
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mgames = delegate.return_data[0]
                              require ext_code.size(mwalletsm[0m])
                              call mwalletsm[0m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[1m])
                              call mwalletsm[1m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mstor8E1F)
                              call mstor8E1F.closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'break on switch'
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              if not create.new_address:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mwallet_0Address = addr(create.new_address)
                              mwalletsm[0m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_1Address = addr(create.new_address)
                              mwalletsm[1m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_2Address = addr(create.new_address)
                              mstor8E1F = addr(create.new_address)
              else:
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args block.timestamp, mroundDuration
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mfinishTime = delegate.return_data[0]
                  if block.timestamp >= mfinishTime:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3386 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
                  else:
                      if uint256(mstor12) >= mstor11:
                          require ext_code.size(mwallet_0Address)
                          call mwallet_0Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_1Address)
                          call mwallet_1Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_2Address)
                          call mwallet_2Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          if delegate.return_data[0]:
                              [94midx = 0
                              mwhile uint8([94midx) < 3m:
                                  mem[0] = uint8([94midx)
                                  mem[32] = 18
                                  require ext_code.size(mwalletsm[[94midx << 248m])
                                  static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                          gas gas_remaining wei
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if ext_call.return_data[31 len 1] > 0:
                                      mstor14m.length++
                                      mem[0] = 14
                                      mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(msecureAddress)
                              static call msecureAddress.0x74550831 with:
                                      gas gas_remaining wei
                                     args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[31 len 1] < mstor14m.length
                              mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalPlayers() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              uint256(mstor12) = ext_call.return_data[31 len 1]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, 15
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 100
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor16 = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor17 = delegate.return_data[0]
                              [94midx = 1
                              [94ms = 0
                              [94ms = 0
                              [94ms = 0
                              mwhile uint8([94midx) <= uint256(mstor12)m:
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                          gas gas_remaining wei
                                         args uint8([94midx)
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 64
                                  mem[128] = ext_call.return_data[32]
                                  mem[96] = addr(ext_call.return_data[0])
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[32], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].totalBets() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], ext_call.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mstor17, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args [94ms, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                                  mem[196] = delegate.return_data[0]
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr(ext_call.return_data[0])
                                  mem[32] = 19
                                  mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                                  mem[160] = delegate.return_data[0]
                                  log Deposited(
                                        address payee=delegate.return_data[0],
                                        uint256 weiAmount=addr(ext_call.return_data[0]))
                                  [94midx = [94midx + 1
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, _3388 * None
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[mstor0m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mdepositOfm[mstor0m] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=owner)
                              mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                              mgamesLogm[mstor3m]m.field_256 = block.timestamp
                              mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                              mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                              mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                              log WinnerWallet(
                                    address wallet=stor15,
                                    uint256 bank=wallets[stor13])
                              mstor15 = 0
                              mstor14m.length = 0
                              [94midx = 0
                              mwhile mstor14m.length + 31 / 32 > [94midxm:
                                  mstor14m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mgames, 1
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mgames = delegate.return_data[0]
                              require ext_code.size(mwalletsm[0m])
                              call mwalletsm[0m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[1m])
                              call mwalletsm[1m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mstor8E1F)
                              call mstor8E1F.closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'break on switch'
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              if not create.new_address:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mwallet_0Address = addr(create.new_address)
                              mwalletsm[0m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_1Address = addr(create.new_address)
                              mwalletsm[1m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_2Address = addr(create.new_address)
                              mstor8E1F = addr(create.new_address)
      else:
          require caller == mwallet_2Address
          require msecureAddress
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args mstor10, 1
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mstor10 = delegate.return_data[0]
          require ext_code.size(mwalletsm[0m])
          static call mwalletsm[0m].totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(mwalletsm[1m])
          static call mwalletsm[1m].totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args ext_call.return_data[0] << 248, uint8(ext_call.return_data[0])
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(mstor8E1F)
          static call mstor8E1F.totalPlayers() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
               gas gas_remaining wei
              args delegate.return_data[0], uint8(ext_call.return_data[0])
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mstor12) = delegate.return_data[0]
          if block.timestamp < mfinishTime:
              if uint256(mstor12) >= mstor11:
                  require ext_code.size(mwallet_0Address)
                  call mwallet_0Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args mstor15, ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_1Address)
                  call mwallet_1Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  require ext_code.size(mwallet_2Address)
                  call mwallet_2Address.0xead3a0fe with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args delegate.return_data[0], ext_call.return_data[0]
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15 = delegate.return_data[0]
                  if delegate.return_data[0]:
                      [94midx = 0
                      mwhile uint8([94midx) < 3m:
                          mem[0] = uint8([94midx)
                          mem[32] = 18
                          require ext_code.size(mwalletsm[[94midx << 248m])
                          static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                  gas gas_remaining wei
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if ext_call.return_data[31 len 1] > 0:
                              mstor14m.length++
                              mem[0] = 14
                              mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(msecureAddress)
                      static call msecureAddress.0x74550831 with:
                              gas gas_remaining wei
                             args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[31 len 1] < mstor14m.length
                      mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                      require ext_code.size(mwalletsm[mstor13m])
                      static call mwalletsm[mstor13m].totalPlayers() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      uint256(mstor12) = ext_call.return_data[31 len 1]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, 15
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], 100
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor16 = delegate.return_data[0]
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor17 = delegate.return_data[0]
                      [94midx = 1
                      [94ms = 0
                      [94ms = 0
                      [94ms = 0
                      mwhile uint8([94midx) <= uint256(mstor12)m:
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                  gas gas_remaining wei
                                 args uint8([94midx)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          mem[128] = ext_call.return_data[32]
                          mem[96] = addr(ext_call.return_data[0])
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args ext_call.return_data[32], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalBets() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor17, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 10000
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args [94ms, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                          mem[196] = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mem[0] = addr(ext_call.return_data[0])
                          mem[32] = 19
                          mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                          mem[160] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=addr(ext_call.return_data[0]))
                          [94midx = [94midx + 1
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          [94ms = delegate.return_data[0]
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, _3390 * None
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mdepositOfm[mstor0m], delegate.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mdepositOfm[mstor0m] = delegate.return_data[0]
                      log Deposited(
                            address payee=delegate.return_data[0],
                            uint256 weiAmount=owner)
                      mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                      mgamesLogm[mstor3m]m.field_256 = block.timestamp
                      mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                      mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                      mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                      log WinnerWallet(
                            address wallet=stor15,
                            uint256 bank=wallets[stor13])
                      mstor15 = 0
                      mstor14m.length = 0
                      [94midx = 0
                      mwhile mstor14m.length + 31 / 32 > [94midxm:
                          mstor14m[[94midxm]m.field_0 = 0
                          [94midx = [94midx + 1
                          mcontinue 
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mgames, 1
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mgames = delegate.return_data[0]
                      require ext_code.size(mwalletsm[0m])
                      call mwalletsm[0m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mwalletsm[1m])
                      call mwalletsm[1m].closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(mstor8E1F)
                      call mstor8E1F.closeContract() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'break on switch'
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      if not create.new_address:
                          revert with ext_call.return_data[0 len return_data.size]
                      mwallet_0Address = addr(create.new_address)
                      mwalletsm[0m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_1Address = addr(create.new_address)
                      mwalletsm[1m] = addr(create.new_address)
                      create contract with 0 wei
                                      code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                      mwallet_2Address = addr(create.new_address)
                      mstor8E1F = addr(create.new_address)
          else:
              if uint256(mstor12) != 1:
                  if block.timestamp >= mfinishTime:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3392 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
                  else:
                      if uint256(mstor12) >= mstor11:
                          require ext_code.size(mwallet_0Address)
                          call mwallet_0Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_1Address)
                          call mwallet_1Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_2Address)
                          call mwallet_2Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          if delegate.return_data[0]:
                              [94midx = 0
                              mwhile uint8([94midx) < 3m:
                                  mem[0] = uint8([94midx)
                                  mem[32] = 18
                                  require ext_code.size(mwalletsm[[94midx << 248m])
                                  static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                          gas gas_remaining wei
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if ext_call.return_data[31 len 1] > 0:
                                      mstor14m.length++
                                      mem[0] = 14
                                      mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(msecureAddress)
                              static call msecureAddress.0x74550831 with:
                                      gas gas_remaining wei
                                     args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[31 len 1] < mstor14m.length
                              mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalPlayers() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              uint256(mstor12) = ext_call.return_data[31 len 1]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, 15
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 100
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor16 = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor17 = delegate.return_data[0]
                              [94midx = 1
                              [94ms = 0
                              [94ms = 0
                              [94ms = 0
                              mwhile uint8([94midx) <= uint256(mstor12)m:
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                          gas gas_remaining wei
                                         args uint8([94midx)
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 64
                                  mem[128] = ext_call.return_data[32]
                                  mem[96] = addr(ext_call.return_data[0])
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[32], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].totalBets() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], ext_call.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mstor17, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args [94ms, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                                  mem[196] = delegate.return_data[0]
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr(ext_call.return_data[0])
                                  mem[32] = 19
                                  mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                                  mem[160] = delegate.return_data[0]
                                  log Deposited(
                                        address payee=delegate.return_data[0],
                                        uint256 weiAmount=addr(ext_call.return_data[0]))
                                  [94midx = [94midx + 1
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, _3394 * None
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[mstor0m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mdepositOfm[mstor0m] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=owner)
                              mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                              mgamesLogm[mstor3m]m.field_256 = block.timestamp
                              mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                              mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                              mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                              log WinnerWallet(
                                    address wallet=stor15,
                                    uint256 bank=wallets[stor13])
                              mstor15 = 0
                              mstor14m.length = 0
                              [94midx = 0
                              mwhile mstor14m.length + 31 / 32 > [94midxm:
                                  mstor14m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mgames, 1
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mgames = delegate.return_data[0]
                              require ext_code.size(mwalletsm[0m])
                              call mwalletsm[0m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[1m])
                              call mwalletsm[1m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mstor8E1F)
                              call mstor8E1F.closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'break on switch'
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              if not create.new_address:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mwallet_0Address = addr(create.new_address)
                              mwalletsm[0m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_1Address = addr(create.new_address)
                              mwalletsm[1m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_2Address = addr(create.new_address)
                              mstor8E1F = addr(create.new_address)
              else:
                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                       gas gas_remaining wei
                      args block.timestamp, mroundDuration
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mfinishTime = delegate.return_data[0]
                  if block.timestamp >= mfinishTime:
                      require ext_code.size(mwallet_0Address)
                      call mwallet_0Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args mstor15, ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_1Address)
                      call mwallet_1Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      require ext_code.size(mwallet_2Address)
                      call mwallet_2Address.0xead3a0fe with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                      [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                           gas gas_remaining wei
                          args delegate.return_data[0], ext_call.return_data[0]
                      if not delegate.return_code:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mstor15 = delegate.return_data[0]
                      if delegate.return_data[0]:
                          [94midx = 0
                          mwhile uint8([94midx) < 3m:
                              mem[0] = uint8([94midx)
                              mem[32] = 18
                              require ext_code.size(mwalletsm[[94midx << 248m])
                              static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                      gas gas_remaining wei
                              mem[96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if ext_call.return_data[31 len 1] > 0:
                                  mstor14m.length++
                                  mem[0] = 14
                                  mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(msecureAddress)
                          static call msecureAddress.0x74550831 with:
                                  gas gas_remaining wei
                                 args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[31 len 1] < mstor14m.length
                          mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                          require ext_code.size(mwalletsm[mstor13m])
                          static call mwalletsm[mstor13m].totalPlayers() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          uint256(mstor12) = ext_call.return_data[31 len 1]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, 15
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], 100
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor16 = delegate.return_data[0]
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor17 = delegate.return_data[0]
                          [94midx = 1
                          [94ms = 0
                          [94ms = 0
                          [94ms = 0
                          mwhile uint8([94midx) <= uint256(mstor12)m:
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                      gas gas_remaining wei
                                     args uint8([94midx)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              mem[128] = ext_call.return_data[32]
                              mem[96] = addr(ext_call.return_data[0])
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args ext_call.return_data[32], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalBets() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], ext_call.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor17, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 10000
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args [94ms, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                              mem[196] = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mem[0] = addr(ext_call.return_data[0])
                              mem[32] = 19
                              mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                              mem[160] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=addr(ext_call.return_data[0]))
                              [94midx = [94midx + 1
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              [94ms = delegate.return_data[0]
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, _3396 * None
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mdepositOfm[mstor0m], delegate.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mdepositOfm[mstor0m] = delegate.return_data[0]
                          log Deposited(
                                address payee=delegate.return_data[0],
                                uint256 weiAmount=owner)
                          mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                          mgamesLogm[mstor3m]m.field_256 = block.timestamp
                          mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                          mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                          mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                          log WinnerWallet(
                                address wallet=stor15,
                                uint256 bank=wallets[stor13])
                          mstor15 = 0
                          mstor14m.length = 0
                          [94midx = 0
                          mwhile mstor14m.length + 31 / 32 > [94midxm:
                              mstor14m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mgames, 1
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mgames = delegate.return_data[0]
                          require ext_code.size(mwalletsm[0m])
                          call mwalletsm[0m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mwalletsm[1m])
                          call mwalletsm[1m].closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(mstor8E1F)
                          call mstor8E1F.closeContract() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'break on switch'
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          mwallet_0Address = addr(create.new_address)
                          mwalletsm[0m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_1Address = addr(create.new_address)
                          mwalletsm[1m] = addr(create.new_address)
                          create contract with 0 wei
                                          code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                          mwallet_2Address = addr(create.new_address)
                          mstor8E1F = addr(create.new_address)
                  else:
                      if uint256(mstor12) >= mstor11:
                          require ext_code.size(mwallet_0Address)
                          call mwallet_0Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args mstor15, ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_1Address)
                          call mwallet_1Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          require ext_code.size(mwallet_2Address)
                          call mwallet_2Address.0xead3a0fe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                          [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                               gas gas_remaining wei
                              args delegate.return_data[0], ext_call.return_data[0]
                          if not delegate.return_code:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          mstor15 = delegate.return_data[0]
                          if delegate.return_data[0]:
                              [94midx = 0
                              mwhile uint8([94midx) < 3m:
                                  mem[0] = uint8([94midx)
                                  mem[32] = 18
                                  require ext_code.size(mwalletsm[[94midx << 248m])
                                  static call mwalletsm[[94midx << 248m].totalPlayers() with:
                                          gas gas_remaining wei
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if ext_call.return_data[31 len 1] > 0:
                                      mstor14m.length++
                                      mem[0] = 14
                                      mstor14m[mstor14m.lengthm.field_5m]m.field_0 = !(255 * 256^mstor14m.length % 32) and mstor14m[mstor14m.lengthm.field_5m]m.field_0 or 256^mstor14m.length % 32 * uint8([94midx)
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(msecureAddress)
                              static call msecureAddress.0x74550831 with:
                                      gas gas_remaining wei
                                     args 0, uint32(mstor14m.length), uint8(mstor12), mgames, mstor10
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[31 len 1] < mstor14m.length
                              mstor13 = mstor('array', ('mask_shl', 3, 5, -5, ('ext_call.return_data', 0, 32)), ('name', 'stor14', 14))m[uint8(ext_call.return_data[0])m]
                              require ext_code.size(mwalletsm[mstor13m])
                              static call mwalletsm[mstor13m].totalPlayers() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              uint256(mstor12) = ext_call.return_data[31 len 1]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, 15
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args delegate.return_data[0], 100
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor16 = delegate.return_data[0]
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mstor17 = delegate.return_data[0]
                              [94midx = 1
                              [94ms = 0
                              [94ms = 0
                              [94ms = 0
                              mwhile uint8([94midx) <= uint256(mstor12)m:
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].0x7e0ecc00 with:
                                          gas gas_remaining wei
                                         args uint8([94midx)
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 64
                                  mem[128] = ext_call.return_data[32]
                                  mem[96] = addr(ext_call.return_data[0])
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[32], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(mwalletsm[mstor13m])
                                  static call mwalletsm[mstor13m].totalBets() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], ext_call.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.mul(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mstor17, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.div(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args delegate.return_data[0], 10000
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args [94ms, delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[164] = mdepositOfm[addr(ext_call.return_data[0])m]
                                  mem[196] = delegate.return_data[0]
                                  require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                                  [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                       gas gas_remaining wei
                                      args mdepositOfm[addr(ext_call.return_data[0])m], delegate.return_data[0]
                                  if not delegate.return_code:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr(ext_call.return_data[0])
                                  mem[32] = 19
                                  mdepositOfm[addr(ext_call.return_data[0])m] = delegate.return_data[0]
                                  mem[160] = delegate.return_data[0]
                                  log Deposited(
                                        address payee=delegate.return_data[0],
                                        uint256 weiAmount=addr(ext_call.return_data[0]))
                                  [94midx = [94midx + 1
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  [94ms = delegate.return_data[0]
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.sub(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mstor15, _3398 * None
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mdepositOfm[mstor0m], delegate.return_data[0]
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mdepositOfm[mstor0m] = delegate.return_data[0]
                              log Deposited(
                                    address payee=delegate.return_data[0],
                                    uint256 weiAmount=owner)
                              mgamesLogm[mstor3m]m.field_0 = mwalletsm[mstor13m]
                              mgamesLogm[mstor3m]m.field_256 = block.timestamp
                              mgamesLogm[mstor3m]m.field_512 = mwallet_0Address
                              mgamesLogm[mstor3m]m.field_768 = mwallet_1Address
                              mgamesLogm[mstor3m]m.field_1024 = mwallet_2Address
                              log WinnerWallet(
                                    address wallet=stor15,
                                    uint256 bank=wallets[stor13])
                              mstor15 = 0
                              mstor14m.length = 0
                              [94midx = 0
                              mwhile mstor14m.length + 31 / 32 > [94midxm:
                                  mstor14m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              require ext_code.size(0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d)
                              [93mdelegate 0x8767a53a9f4ab3a4a13d6a396647c60867f21c8d.add(uint256 a, uint256 b) with:
                                   gas gas_remaining wei
                                  args mgames, 1
                              if not delegate.return_code:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              mgames = delegate.return_data[0]
                              require ext_code.size(mwalletsm[0m])
                              call mwalletsm[0m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mwalletsm[1m])
                              call mwalletsm[1m].closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(mstor8E1F)
                              call mstor8E1F.closeContract() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'break on switch'
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              if not create.new_address:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mwallet_0Address = addr(create.new_address)
                              mwalletsm[0m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_1Address = addr(create.new_address)
                              mwalletsm[1m] = addr(create.new_address)
                              create contract with 0 wei
                                              code: 0xfe60806040526002805461ff001916905534801561001b57600080fd5b5060405160408061057e8339810180604052604081101561003b57600080fd5b508051602090910151600080546001600160a01b031916331790556003919091556004556105108061006e6000396000f3fe60806040526004361061007b5760003560e01c8063c5aa6e771161004e578063c5aa6e7714610323578063d7c81b5514610338578063ead3a0fe1461034d578063f60cdcf6146103625761007b565b80634f747cb814610252578063610be654146102835780637e0ecc00146102ac578063befa1e2f146102fc575b60045434101561008a57600080fd5b6100933361038d565b1515600114156100a257600080fd5b600254610100900460ff16156100b757600080fd5b60015460408051600160e01b63771602f7028152600481019290925234602483015251738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b15801561011557600080fd5b505af4158015610129573d6000803e3d6000fd5b505050506040513d602081101561013f57600080fd5b5051600190815560025460408051600160e01b63771602f702815260ff909216600483015260248201929092529051738767a53a9f4ab3a4a13d6a396647c60867f21c8d9163771602f7916044808301926020929190829003018186803b1580156101a957600080fd5b505af41580156101bd573d6000803e3d6000fd5b505050506040513d60208110156101d357600080fd5b50516002805460ff191660ff92831617908190556101f391163334610393565b506000805460408051600160e11b63688b88d102815290516001600160a01b039092169263d11711a29260048084019382900301818387803b15801561023857600080fd5b505af115801561024c573d6000803e3d6000fd5b50505050005b34801561025e57600080fd5b506102676103cf565b604080516001600160a01b039092168252519081900360200190f35b34801561028f57600080fd5b506102986103de565b604080519115158252519081900360200190f35b3480156102b857600080fd5b506102d9600480360360208110156102cf57600080fd5b503560ff1661040c565b604080516001600160a01b03909316835260208301919091528051918290030190f35b34801561030857600080fd5b50610311610431565b60408051918252519081900360200190f35b34801561032f57600080fd5b50610311610437565b34801561034457600080fd5b5061031161043d565b34801561035957600080fd5b50610311610443565b34801561036e57600080fd5b506103776104db565b6040805160ff9092168252519081900360200190f35b3b151590565b60ff8316600090815260056020526040902080546001600160a01b0384166001600160a01b031990911617815560019081018290559392505050565b6000546001600160a01b031681565b600080546001600160a01b031633146103f657600080fd5b506002805461ff00191661010017905560015b90565b600560205260009081526040902080546001909101546001600160a01b039091169082565b60015490565b60045481565b60035481565b600080546001600160a01b0316331461045b57600080fd5b60045430319081106104d1576000805460408051600160e01b634d9b373502815290516001600160a01b0390921692634d9b3735928592600480820193929182900301818588803b1580156104af57600080fd5b505af11580156104c3573d6000803e3d6000fd5b505050505080915050610409565b6000915050610409565b60025460ff169056fea165627a7a72305820192c2216750820ff8996d387b2cee51354d0f76c74a6b73002d8ebb42b9b562c00, games, minPayment
                              mwallet_2Address = addr(create.new_address)
                              mstor8E1F = addr(create.new_address)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf7cb789a
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def roundDuration(): # not payable
  return mroundDuration


# hash = 0xfb90f9e9
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def wallet_0(): # not payable
  return mwallet_0Address


# hash = 0xfe188184
# getter = ['storage', 160, 0, ['sha3', ['data', ['storage', 256, 0, 3], 20]]]
# const = None
# payable = False
def lastWinner(): # not payable
  return mgamesLogm[mstor3m]m.field_0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if mwallet_0Address != caller:
      if mwallet_1Address != caller:
          if mwallet_2Address != caller:
              if call.value:
                  revert with 0, 'You can't do nonzero transaction'
              if not mdepositOfm[callerm]:
                  revert with 0, 'You have zero balance'
              mdepositOfm[callerm] = 0
              call caller with:
                 value mdepositOfm[callerm] wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              log Withdrawn(
                    address payee=depositOf[caller],
                    uint256 weiAmount=caller)


