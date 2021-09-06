# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x57A9cF623BC9eaAfBC6686be57fCb7eE59102D33 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    resolverAddress # mask: a s
    # storage address 1
    key # mask: a s
    # storage address 2
    CONTRACT_ADDRESS # mask: a s
# hash = 0x04f3bcec
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def resolver(): # not payable
  return mresolverAddress


# hash = 0x38ec8116
# getter = None
# const = None
# payable = False
def unknown38ec8116(addr m_param1): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xa77af36e with:
       gas gas_remaining - 710 wei
  require ext_call.success
  mem[1696] = ext_call.return_data[108 len 20]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x9a0c130 with:
       gas gas_remaining - 710 wei
      args m_param1
  require ext_call.success
  if ext_call.return_data[32]:
      if bool(ext_call.return_data[64]) == 1:
          require ext_code.size(mresolverAddress)
          call mresolverAddress.get_contract(bytes32 key) with:
               gas gas_remaining - 710 wei
              args 's:goldtoken'
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x1326a78a with:
               gas gas_remaining - 710 wei
              args addr(m_param1), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
          require ext_call.success
          require bool(ext_call.return_data[0]) == 1
          return 1
      else:
          if uint64(m_param1) << 96 != mem[1708 len 20]:
              require block.timestamp >= ext_call.return_data[32]
              if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                  require ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600) >= ext_call.return_data[32]
                  if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                      require ext_call.return_data[32]
                      require block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= ext_call.return_data[0]
                      require ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]) >= ext_call.return_data[0]
                      require ext_code.size(mresolverAddress)
                      call mresolverAddress.get_contract(bytes32 key) with:
                           gas gas_remaining - 710 wei
                          args 's:goldtoken'
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x1326a78a with:
                           gas gas_remaining - 710 wei
                          args addr(m_param1), ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]), ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600), ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                      require ext_call.success
                      require bool(ext_call.return_data[0]) == 1
                      if block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= 0:
                          return 1
                      else:
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 'i:token'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).log_demurrage_fees(address from, address to, uint256 value) with:
                               gas gas_remaining - 710 wei
                              args addr(m_param1), addr(ext_call.return_data[108 len 20]), block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                          require ext_call.success
                          return 1
                  else:
                      require ext_code.size(mresolverAddress)
                      call mresolverAddress.get_contract(bytes32 key) with:
                           gas gas_remaining - 710 wei
                          args 's:goldtoken'
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x1326a78a with:
                           gas gas_remaining - 710 wei
                          args addr(m_param1), ext_call.return_data[0], ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600), ext_call.return_data[0]
                      require ext_call.success
                      require bool(ext_call.return_data[0]) == 1
                      return 1
              else:
                  if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                      require ext_call.return_data[32]
                      require block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= ext_call.return_data[0]
                      require ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]) >= ext_call.return_data[0]
                      require ext_code.size(mresolverAddress)
                      call mresolverAddress.get_contract(bytes32 key) with:
                           gas gas_remaining - 710 wei
                          args 's:goldtoken'
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x1326a78a with:
                           gas gas_remaining - 710 wei
                          args addr(m_param1), ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]), ext_call.return_data[32], ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                      require ext_call.success
                      require bool(ext_call.return_data[0]) == 1
                      if block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= 0:
                          return 1
                      else:
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 'i:token'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).log_demurrage_fees(address from, address to, uint256 value) with:
                               gas gas_remaining - 710 wei
                              args addr(m_param1), addr(ext_call.return_data[108 len 20]), block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                          require ext_call.success
                          return 1
                  else:
                      require ext_code.size(mresolverAddress)
                      call mresolverAddress.get_contract(bytes32 key) with:
                           gas gas_remaining - 710 wei
                          args 's:goldtoken'
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x1326a78a with:
                           gas gas_remaining - 710 wei
                          args addr(m_param1), ext_call.return_data[0], ext_call.return_data[32], ext_call.return_data[0]
                      require ext_call.success
                      require bool(ext_call.return_data[0]) == 1
                      return 1
          else:
              require ext_code.size(mresolverAddress)
              call mresolverAddress.get_contract(bytes32 key) with:
                   gas gas_remaining - 710 wei
                  args 's:goldtoken'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x1326a78a with:
                   gas gas_remaining - 710 wei
                  args addr(m_param1), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
              require ext_call.success
              require bool(ext_call.return_data[0]) == 1
              return 1
  else:
      if bool(ext_call.return_data[64]) == 1:
          require ext_code.size(mresolverAddress)
          call mresolverAddress.get_contract(bytes32 key) with:
               gas gas_remaining - 710 wei
              args 's:goldtoken'
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x1326a78a with:
               gas gas_remaining - 710 wei
              args addr(m_param1), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
          require ext_call.success
          require bool(ext_call.return_data[0]) == 1
          return 1
      else:
          if uint64(m_param1) << 96 != mem[1708 len 20]:
              require block.timestamp >= block.timestamp
              require ext_code.size(mresolverAddress)
              call mresolverAddress.get_contract(bytes32 key) with:
                   gas gas_remaining - 710 wei
                  args 's:goldtoken'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x1326a78a with:
                   gas gas_remaining - 710 wei
                  args addr(m_param1), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
              require ext_call.success
              require bool(ext_call.return_data[0]) == 1
              return 1
          else:
              require ext_code.size(mresolverAddress)
              call mresolverAddress.get_contract(bytes32 key) with:
                   gas gas_remaining - 710 wei
                  args 's:goldtoken'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x1326a78a with:
                   gas gas_remaining - 710 wei
                  args addr(m_param1), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
              require ext_call.success
              require bool(ext_call.return_data[0]) == 1
              return 1


# hash = 0x3943380c
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def key(): # not payable
  return mkey


# hash = 0x3f83acff
# getter = None
# const = None
# payable = False
def get_contract(bytes32 m_key): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args m_key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x76cab952
# getter = None
# const = None
# payable = False
def unknown76cab952(addr m_param1): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xa77af36e with:
       gas gas_remaining - 710 wei
  require ext_call.success
  mem[1696] = ext_call.return_data[108 len 20]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 's:goldtoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x9a0c130 with:
       gas gas_remaining - 710 wei
      args m_param1
  require ext_call.success
  if not ext_call.return_data[32]:
      if bool(ext_call.return_data[64]) != 1:
          if uint64(m_param1) << 96 != mem[1708 len 20]:
              require block.timestamp >= block.timestamp
      return ext_call.return_data[0]
  if bool(ext_call.return_data[64]) == 1:
      return ext_call.return_data[0]
  if uint64(m_param1) << 96 == mem[1708 len 20]:
      return ext_call.return_data[0]
  require block.timestamp >= ext_call.return_data[32]
  if block.timestamp - ext_call.return_data[32] / 24 * 3600:
      require ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600) >= ext_call.return_data[32]
  if not block.timestamp - ext_call.return_data[32] / 24 * 3600:
      return ext_call.return_data[0]
  require ext_call.return_data[32]
  require block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= ext_call.return_data[0]
  require ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]) >= ext_call.return_data[0]
  return (ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]))


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.locked() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require not ext_call.return_data[0]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.owner() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.0xc8b56bda with:
       gas gas_remaining - 710 wei
      args mkey
  require ext_call.success
  require ext_call.return_data[0]
  [93mselfdestruct([91maddr(ext_call.return_data[0])[93m)


# hash = 0x9bd315f6
# getter = None
# const = None
# payable = False
def unknown9bd315f6(array m_param1): # not payable
  mem[64] = (32 * m_param1.length) + 128
  mem[96] = m_param1.length
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < mem[96]
      [94m_727 = mem[(32 * [94midx) + 128]
      [94m_728 = mem[64]
      mem[64] = mem[64] + 416
      [94m_729 = mem[64]
      mem[64] = mem[64] + 160
      [94m_730 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_730] = 0
      mem[[94m_730 + 32] = 0
      mem[[94m_729] = [94m_730
      mem[[94m_729 + 32] = 0
      mem[[94m_729 + 64] = 0
      mem[[94m_729 + 96] = 0
      mem[[94m_728] = [94m_729
      [94m_731 = mem[64]
      mem[64] = mem[64] + 224
      mem[[94m_731] = 0
      mem[[94m_731 + 32] = 0
      [94m_732 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_732] = 0
      mem[[94m_732 + 32] = 0
      mem[[94m_731 + 64] = [94m_732
      [94m_733 = mem[64]
      mem[64] = mem[64] + 96
      [94m_734 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_734] = 0
      mem[[94m_734 + 32] = 0
      mem[[94m_733] = [94m_734
      mem[[94m_733 + 32] = 0
      mem[[94m_731 + 96] = [94m_733
      mem[[94m_728 + 32] = [94m_731
      mem[[94m_728 + 64] = 0
      [94m_735 = mem[64]
      mem[64] = mem[64] + 416
      [94m_736 = mem[64]
      mem[64] = mem[64] + 160
      [94m_737 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_737] = 0
      mem[[94m_737 + 32] = 0
      mem[[94m_736] = [94m_737
      mem[[94m_736 + 32] = 0
      mem[[94m_736 + 64] = 0
      mem[[94m_736 + 96] = 0
      mem[[94m_735] = [94m_736
      [94m_738 = mem[64]
      mem[64] = mem[64] + 224
      mem[[94m_738] = 0
      mem[[94m_738 + 32] = 0
      [94m_739 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_739] = 0
      mem[[94m_739 + 32] = 0
      mem[[94m_738 + 64] = [94m_739
      [94m_740 = mem[64]
      mem[64] = mem[64] + 96
      [94m_741 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_741 + 32] = 0
      mem[[94m_740] = [94m_741
      mem[[94m_740 + 32] = 0
      mem[[94m_738 + 96] = [94m_740
      mem[[94m_735 + 32] = [94m_738
      mem[[94m_735 + 64] = 0
      require ext_code.size(mresolverAddress)
      call mresolverAddress.get_contract(bytes32 key) with:
           gas gas_remaining - 710 wei
          args 's:goldtoken'
      require ext_call.success
      mem[mem[64] + 128] = 0
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0xa77af36e with:
           gas gas_remaining - 710 wei
      require ext_call.success
      mem[[94m_736 + 96] = ext_call.return_data[108 len 20]
      mem[[94m_736 + 64] = ext_call.return_data[64]
      mem[[94m_736 + 32] = ext_call.return_data[32]
      mem[[94m_737] = ext_call.return_data[0]
      mem[[94m_738] = addr([94m_727)
      require ext_code.size(mresolverAddress)
      call mresolverAddress.get_contract(bytes32 key) with:
           gas gas_remaining - 710 wei
          args 's:goldtoken'
      require ext_call.success
      mem[mem[64] + 96] = 0
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x9a0c130 with:
           gas gas_remaining - 710 wei
          args addr([94m_727)
      mem[mem[64] len 96] = ext_call.return_data[0 len 96]
      require ext_call.success
      mem[[94m_738 + 32] = bool(ext_call.return_data[64])
      mem[[94m_741] = ext_call.return_data[32]
      mem[[94m_739] = ext_call.return_data[0]
      [94m_779 = mem[64]
      mem[64] = mem[64] + 416
      [94m_780 = mem[64]
      mem[64] = mem[64] + 160
      [94m_781 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_781] = 0
      mem[[94m_781 + 32] = 0
      mem[[94m_780] = [94m_781
      mem[[94m_780 + 32] = 0
      mem[[94m_780 + 64] = 0
      mem[[94m_780 + 96] = 0
      mem[[94m_779] = [94m_780
      [94m_782 = mem[64]
      mem[64] = mem[64] + 224
      mem[[94m_782] = 0
      mem[[94m_782 + 32] = 0
      [94m_783 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_783] = 0
      mem[[94m_783 + 32] = 0
      mem[[94m_782 + 64] = [94m_783
      [94m_784 = mem[64]
      mem[64] = mem[64] + 96
      [94m_785 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_785] = 0
      mem[[94m_785 + 32] = 0
      mem[[94m_784] = [94m_785
      mem[[94m_784 + 32] = 0
      mem[[94m_782 + 96] = [94m_784
      mem[[94m_779 + 32] = [94m_782
      mem[[94m_779 + 64] = 0
      if ext_call.return_data[32]:
          if bool(ext_call.return_data[64]) == 1:
              mem[[94m_739 + 32] = ext_call.return_data[0]
              mem[[94m_737 + 32] = ext_call.return_data[0]
              mem[[94m_741 + 32] = block.timestamp
              require ext_code.size(mresolverAddress)
              call mresolverAddress.get_contract(bytes32 key) with:
                   gas gas_remaining - 710 wei
                  args 's:goldtoken'
              require ext_call.success
              mem[mem[64] + 4] = addr([94m_727)
              mem[mem[64] + 36] = ext_call.return_data[0]
              mem[mem[64] + 68] = block.timestamp
              mem[mem[64] + 100] = ext_call.return_data[0]
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x1326a78a with:
                   gas gas_remaining - 710 wei
                  args addr([94m_727), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
              mem[mem[64]] = ext_call.return_data[0]
              require ext_call.success
              require bool(ext_call.return_data[0]) == 1
              [94midx = [94midx + 1
              mcontinue 
          else:
              if uint64([94m_727) << 96 != mem[[94m_736 + 108 len 20]:
                  [94m_861 = mem[64]
                  mem[64] = mem[64] + 96
                  [94m_865 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_865] = 0
                  mem[[94m_865 + 32] = 0
                  mem[[94m_861] = [94m_865
                  mem[[94m_861 + 32] = 0
                  require block.timestamp >= ext_call.return_data[32]
                  mem[[94m_740 + 32] = block.timestamp - ext_call.return_data[32] / 24 * 3600
                  if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                      [94m_968 = mem[64]
                      mem[64] = mem[64] + 64
                      mem[[94m_968] = 0
                      mem[[94m_968 + 32] = 0
                      require ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600) >= ext_call.return_data[32]
                      mem[[94m_741 + 32] = ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600)
                      mem[[94m_740] = [94m_741
                      mem[[94m_738 + 96] = [94m_740
                      if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                          require ext_call.return_data[32]
                          mem[[94m_735 + 64] = block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                          [94m_1155 = mem[64]
                          mem[64] = mem[64] + 64
                          mem[[94m_1155] = 0
                          mem[[94m_1155 + 32] = 0
                          require block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= ext_call.return_data[0]
                          mem[[94m_739 + 32] = ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[[94m_738 + 64] = [94m_739
                          [94m_1224 = mem[64]
                          mem[64] = mem[64] + 64
                          mem[[94m_1224] = 0
                          mem[[94m_1224 + 32] = 0
                          require ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]) >= ext_call.return_data[0]
                          mem[[94m_737 + 32] = ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[[94m_736] = [94m_737
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 's:goldtoken'
                          require ext_call.success
                          mem[mem[64] + 4] = addr([94m_727)
                          mem[mem[64] + 36] = ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[mem[64] + 68] = ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600)
                          mem[mem[64] + 100] = ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x1326a78a with:
                               gas gas_remaining - 710 wei
                              args addr([94m_727), ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]), ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600), ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[mem[64]] = ext_call.return_data[0]
                          require ext_call.success
                          require bool(ext_call.return_data[0]) == 1
                          if block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= 0:
                              [94midx = [94midx + 1
                              mcontinue 
                          else:
                              require ext_code.size(mresolverAddress)
                              call mresolverAddress.get_contract(bytes32 key) with:
                                   gas gas_remaining - 710 wei
                                  args 'i:token'
                              require ext_call.success
                              mem[mem[64]] = 0x79f0b42700000000000000000000000000000000000000000000000000000000
                              mem[mem[64] + 4] = addr([94m_727)
                              mem[mem[64] + 36] = addr(ext_call.return_data[108 len 20])
                              mem[mem[64] + 68] = block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).log_demurrage_fees(address from, address to, uint256 value) with:
                                   gas gas_remaining - 710 wei
                                  args addr([94m_727), addr(ext_call.return_data[108 len 20]), block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                              require ext_call.success
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[[94m_739 + 32] = ext_call.return_data[0]
                          mem[[94m_737 + 32] = ext_call.return_data[0]
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 's:goldtoken'
                          require ext_call.success
                          mem[mem[64] + 4] = addr([94m_727)
                          mem[mem[64] + 36] = ext_call.return_data[0]
                          mem[mem[64] + 68] = ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600)
                          mem[mem[64] + 100] = ext_call.return_data[0]
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x1326a78a with:
                               gas gas_remaining - 710 wei
                              args addr([94m_727), ext_call.return_data[0], ext_call.return_data[32] + (24 * 3600 * block.timestamp - ext_call.return_data[32] / 24 * 3600), ext_call.return_data[0]
                          mem[mem[64]] = ext_call.return_data[0]
                          require ext_call.success
                          require bool(ext_call.return_data[0]) == 1
                          [94midx = [94midx + 1
                          mcontinue 
                  else:
                      mem[[94m_741 + 32] = ext_call.return_data[32]
                      mem[[94m_738 + 96] = [94m_740
                      if block.timestamp - ext_call.return_data[32] / 24 * 3600:
                          require ext_call.return_data[32]
                          mem[[94m_735 + 64] = block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                          [94m_1050 = mem[64]
                          mem[64] = mem[64] + 64
                          mem[[94m_1050] = 0
                          mem[[94m_1050 + 32] = 0
                          require block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= ext_call.return_data[0]
                          mem[[94m_739 + 32] = ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[[94m_738 + 64] = [94m_739
                          [94m_1156 = mem[64]
                          mem[64] = mem[64] + 64
                          mem[[94m_1156] = 0
                          mem[[94m_1156 + 32] = 0
                          require ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]) >= ext_call.return_data[0]
                          mem[[94m_737 + 32] = ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[[94m_736] = [94m_737
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 's:goldtoken'
                          require ext_call.success
                          mem[mem[64] + 4] = addr([94m_727)
                          mem[mem[64] + 36] = ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[mem[64] + 68] = ext_call.return_data[32]
                          mem[mem[64] + 100] = ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x1326a78a with:
                               gas gas_remaining - 710 wei
                              args addr([94m_727), ext_call.return_data[0] - (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]), ext_call.return_data[32], ext_call.return_data[0] + (block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32])
                          mem[mem[64]] = ext_call.return_data[0]
                          require ext_call.success
                          require bool(ext_call.return_data[0]) == 1
                          if block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32] <= 0:
                              [94midx = [94midx + 1
                              mcontinue 
                          else:
                              require ext_code.size(mresolverAddress)
                              call mresolverAddress.get_contract(bytes32 key) with:
                                   gas gas_remaining - 710 wei
                                  args 'i:token'
                              require ext_call.success
                              mem[mem[64]] = 0x79f0b42700000000000000000000000000000000000000000000000000000000
                              mem[mem[64] + 4] = addr([94m_727)
                              mem[mem[64] + 36] = addr(ext_call.return_data[108 len 20])
                              mem[mem[64] + 68] = block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).log_demurrage_fees(address from, address to, uint256 value) with:
                                   gas gas_remaining - 710 wei
                                  args addr([94m_727), addr(ext_call.return_data[108 len 20]), block.timestamp - ext_call.return_data[32] / 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[64] / ext_call.return_data[32]
                              require ext_call.success
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          mem[[94m_739 + 32] = ext_call.return_data[0]
                          mem[[94m_737 + 32] = ext_call.return_data[0]
                          require ext_code.size(mresolverAddress)
                          call mresolverAddress.get_contract(bytes32 key) with:
                               gas gas_remaining - 710 wei
                              args 's:goldtoken'
                          require ext_call.success
                          mem[mem[64] + 4] = addr([94m_727)
                          mem[mem[64] + 36] = ext_call.return_data[0]
                          mem[mem[64] + 68] = ext_call.return_data[32]
                          mem[mem[64] + 100] = ext_call.return_data[0]
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x1326a78a with:
                               gas gas_remaining - 710 wei
                              args addr([94m_727), ext_call.return_data[0], ext_call.return_data[32], ext_call.return_data[0]
                          mem[mem[64]] = ext_call.return_data[0]
                          require ext_call.success
                          require bool(ext_call.return_data[0]) == 1
                          [94midx = [94midx + 1
                          mcontinue 
              else:
                  mem[[94m_739 + 32] = ext_call.return_data[0]
                  mem[[94m_737 + 32] = ext_call.return_data[0]
                  mem[[94m_741 + 32] = block.timestamp
                  require ext_code.size(mresolverAddress)
                  call mresolverAddress.get_contract(bytes32 key) with:
                       gas gas_remaining - 710 wei
                      args 's:goldtoken'
                  require ext_call.success
                  mem[mem[64] + 4] = addr([94m_727)
                  mem[mem[64] + 36] = ext_call.return_data[0]
                  mem[mem[64] + 68] = block.timestamp
                  mem[mem[64] + 100] = ext_call.return_data[0]
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x1326a78a with:
                       gas gas_remaining - 710 wei
                      args addr([94m_727), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
                  mem[mem[64]] = ext_call.return_data[0]
                  require ext_call.success
                  require bool(ext_call.return_data[0]) == 1
                  [94midx = [94midx + 1
                  mcontinue 
      else:
          mem[[94m_741] = block.timestamp
          if bool(ext_call.return_data[64]) == 1:
              mem[[94m_739 + 32] = ext_call.return_data[0]
              mem[[94m_737 + 32] = ext_call.return_data[0]
              mem[[94m_741 + 32] = block.timestamp
              require ext_code.size(mresolverAddress)
              call mresolverAddress.get_contract(bytes32 key) with:
                   gas gas_remaining - 710 wei
                  args 's:goldtoken'
              require ext_call.success
              mem[mem[64] + 4] = addr([94m_727)
              mem[mem[64] + 36] = ext_call.return_data[0]
              mem[mem[64] + 68] = block.timestamp
              mem[mem[64] + 100] = ext_call.return_data[0]
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x1326a78a with:
                   gas gas_remaining - 710 wei
                  args addr([94m_727), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
              mem[mem[64]] = ext_call.return_data[0]
              require ext_call.success
              require bool(ext_call.return_data[0]) == 1
              [94midx = [94midx + 1
              mcontinue 
          else:
              if uint64([94m_727) << 96 != mem[[94m_736 + 108 len 20]:
                  [94m_866 = mem[64]
                  mem[64] = mem[64] + 96
                  [94m_873 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_873] = 0
                  mem[[94m_873 + 32] = 0
                  mem[[94m_866] = [94m_873
                  mem[[94m_866 + 32] = 0
                  require block.timestamp >= block.timestamp
                  mem[[94m_740 + 32] = 0 / 24 * 3600
                  mem[[94m_741 + 32] = block.timestamp
                  mem[[94m_738 + 96] = [94m_740
                  mem[[94m_739 + 32] = ext_call.return_data[0]
                  mem[[94m_737 + 32] = ext_call.return_data[0]
                  require ext_code.size(mresolverAddress)
                  call mresolverAddress.get_contract(bytes32 key) with:
                       gas gas_remaining - 710 wei
                      args 's:goldtoken'
                  require ext_call.success
                  mem[mem[64] + 4] = addr([94m_727)
                  mem[mem[64] + 36] = ext_call.return_data[0]
                  mem[mem[64] + 68] = block.timestamp
                  mem[mem[64] + 100] = ext_call.return_data[0]
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x1326a78a with:
                       gas gas_remaining - 710 wei
                      args addr([94m_727), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
                  mem[mem[64]] = ext_call.return_data[0]
                  require ext_call.success
                  require bool(ext_call.return_data[0]) == 1
                  [94midx = [94midx + 1
                  mcontinue 
              else:
                  mem[[94m_739 + 32] = ext_call.return_data[0]
                  mem[[94m_737 + 32] = ext_call.return_data[0]
                  mem[[94m_741 + 32] = block.timestamp
                  require ext_code.size(mresolverAddress)
                  call mresolverAddress.get_contract(bytes32 key) with:
                       gas gas_remaining - 710 wei
                      args 's:goldtoken'
                  require ext_call.success
                  mem[mem[64] + 4] = addr([94m_727)
                  mem[mem[64] + 36] = ext_call.return_data[0]
                  mem[mem[64] + 68] = block.timestamp
                  mem[mem[64] + 100] = ext_call.return_data[0]
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x1326a78a with:
                       gas gas_remaining - 710 wei
                      args addr([94m_727), ext_call.return_data[0], block.timestamp, ext_call.return_data[0]
                  mem[mem[64]] = ext_call.return_data[0]
                  require ext_call.success
                  require bool(ext_call.return_data[0]) == 1
                  [94midx = [94midx + 1
                  mcontinue 
  return 1


# hash = 0xdb4ecbc1
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def CONTRACT_ADDRESS(): # not payable
  return mCONTRACT_ADDRESS


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


