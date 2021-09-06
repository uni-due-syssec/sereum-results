# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x96E12d3238a09ec5f73814448975983aD1AD3f74 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xcd61a95a': 'sellOrder(uint256 _sellPrice, uint256 _amount)', '0xef46e0ca': 'executeOrder(uint256 _assetId, uint256 _price)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown5f82c67eAddress # mask: a s
    # storage address 2
    unknown38013f02Address # mask: a s
    # storage address 3
    unknown878f7603Address # mask: a s
    # storage address 4
    unknown50fbd642Address # mask: a s
    # storage address 5
    stake # mask: a s
    # storage address 6
    unknown2fe7d446 # mask: a s
    # storage address 7
    unknown62141fcc # mask: a s
    # storage address 8
    unknown2f884710 # mask: a s
    # storage address 9
    unknown03eeb4ca # mask: a s
    # storage address 10
    unknown94d5567a # mask: a s
    # storage address 11
    unknown6f17591f # mask: a s
    # storage address 11
    unknown76017b64Address # mask: a s
    # storage address 11
    unknowne852e741 # mask: a s
    # storage address 12
    logicContractAddress # mask: a s
    # storage address 13
    unknownd95393ebAddress # mask: a s
    # storage address 14
    unknowncb0ef21dAddress # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    stor16 # mask: a s
# hash = 0x03eeb4ca
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def unknown03eeb4ca() payable: 
  return munknown03eeb4ca


# hash = 0x2e27f486
# getter = None
# const = None
# payable = True
def unknown2e27f486() payable: 
  require ext_code.size(munknown76017b64Address)
  call munknown76017b64Address.0x17bfdfbc with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      if munknown50fbd642Address != munknown76017b64Address:
          require ext_code.size(munknown76017b64Address)
          static call munknown76017b64Address.underlying() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require ext_code.size(addr(ext_call.return_data[0]))
              static call addr(ext_call.return_data[0]).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  require ext_code.size(munknown38013f02Address)
                  static call munknown38013f02Address.getPrice(address token) with:
                          gas gas_remaining wei
                         args munknownd95393ebAddress
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0]:
                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                          require ext_code.size(munknown38013f02Address)
                          static call munknown38013f02Address.getPrice(address token) with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[0])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0]:
                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                  if ext_call.return_data[0] * ext_call.return_data[0]:
                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                      return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                  else:
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                      return (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                              else:
                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                  return (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                      else:
                          require ext_code.size(munknown38013f02Address)
                          static call munknown38013f02Address.getPrice(address token) with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[0])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_call.return_data[0]
                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                              require ext_call.return_data[0] * ext_call.return_data[0]
                              require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                              revert
      else:
          require ext_code.size(munknown38013f02Address)
          static call munknown38013f02Address.getPrice(address token) with:
                  gas gas_remaining wei
                 args munknownd95393ebAddress
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              if ext_call.return_data[0]:
                  require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  return (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
              else:
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  return (0 / ext_call.return_data[0])


# hash = 0x2f884710
# getter = ['storage', 256, 0, 8]
# const = None
# payable = True
def unknown2f884710() payable: 
  return munknown2f884710


# hash = 0x2fe7d446
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def unknown2fe7d446() payable: 
  return munknown2fe7d446


# hash = 0x38013f02
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def unknown38013f02() payable: 
  return munknown38013f02Address


# hash = 0x3a4b66f1
# getter = ['storage', 256, 0, 5]
# const = None
# payable = True
def stake() payable: 
  return mstake


# hash = 0x3bc3c23b
# getter = None
# const = None
# payable = True
def unknown3bc3c23b() payable: 
  if not munknowne852e741:
      if addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
          require ext_code.size(addr(mstor15))
          static call addr(mstor15).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require ext_code.size(munknown878f7603Address)
              call munknown878f7603Address.0xbd6d894d with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  require ext_code.size(munknown878f7603Address)
                  static call munknown878f7603Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0]:
                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                          require ext_code.size(munknown76017b64Address)
                          call munknown76017b64Address.0x17bfdfbc with:
                               gas gas_remaining wei
                              args this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if munknown50fbd642Address != munknown76017b64Address:
                                  require ext_code.size(munknown76017b64Address)
                                  static call munknown76017b64Address.underlying() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args munknownd95393ebAddress
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                                  require ext_code.size(munknown38013f02Address)
                                                  static call munknown38013f02Address.getPrice(address token) with:
                                                          gas gas_remaining wei
                                                         args addr(ext_call.return_data[0])
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] < 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                                  require ext_code.size(munknown5f82c67eAddress)
                                                                  static call munknown5f82c67eAddress.markets(address param1) with:
                                                                          gas gas_remaining wei
                                                                         args munknown76017b64Address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 64
                                                                      require ext_call.return_data[0] <= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                      if (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                          require (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                              return 1, 
                                                                                     munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                          else:
                                                                              require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                              return 0, 
                                                                                     (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                      else:
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                              return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                          else:
                                                                              require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                              return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                      require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                      return 1, 
                                                                             munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  else:
                                                                      require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      return 0, 
                                                                             ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                          else:
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                                  require ext_code.size(munknown5f82c67eAddress)
                                                                  static call munknown5f82c67eAddress.markets(address param1) with:
                                                                          gas gas_remaining wei
                                                                         args munknown76017b64Address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 64
                                                                      require ext_call.return_data[0] <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                      if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                          require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                              return 1, 
                                                                                     munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                          else:
                                                                              require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                              return 0, 
                                                                                     (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                      else:
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                              return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                          else:
                                                                              require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                              return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                      require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                      return 1, 
                                                                             munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  else:
                                                                      require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      return 0, 
                                                                             ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if ext_call.return_data[0] < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require ext_call.return_data[0] <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                      require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, 
                                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, 
                                                                         munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                              else:
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  return 0, 
                                                                         ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                              else:
                                                  require ext_code.size(munknown38013f02Address)
                                                  static call munknown38013f02Address.getPrice(address token) with:
                                                          gas gas_remaining wei
                                                         args addr(ext_call.return_data[0])
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                                      revert
                              else:
                                  require ext_code.size(munknown38013f02Address)
                                  static call munknown38013f02Address.getPrice(address token) with:
                                          gas gas_remaining wei
                                         args munknownd95393ebAddress
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] < 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                              require ext_code.size(munknown5f82c67eAddress)
                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                      gas gas_remaining wei
                                                     args munknown76017b64Address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  require ext_call.return_data[0] <= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                                  if (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0]:
                                                      require (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                          return 1, 
                                                                 munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, 
                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                          else:
                                              require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                              if ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]):
                                                  require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                                  return 1, 
                                                         munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0] - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                              else:
                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) <= ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  return 0, 
                                                         ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] < 0 / ext_call.return_data[0]:
                                              require ext_code.size(munknown5f82c67eAddress)
                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                      gas gas_remaining wei
                                                     args munknown76017b64Address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  require ext_call.return_data[0] <= 0 / ext_call.return_data[0]
                                                  if (0 / ext_call.return_data[0]) - ext_call.return_data[0]:
                                                      require (10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                          return 1, 
                                                                 munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, 
                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                          else:
                                              require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                              require munknown2fe7d446 + (0 / ext_call.return_data[0]) >= 0 / ext_call.return_data[0]
                                              if ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / ext_call.return_data[0]):
                                                  require ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / ext_call.return_data[0])
                                                  return 1, 
                                                         munknown2fe7d446 + (0 / ext_call.return_data[0]) - ext_call.return_data[0] - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                              else:
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[0]) <= ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  return 0, 
                                                         ext_call.return_data[0] + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[0])
                      else:
                          require ext_code.size(munknown76017b64Address)
                          call munknown76017b64Address.0x17bfdfbc with:
                               gas gas_remaining wei
                              args this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if munknown50fbd642Address != munknown76017b64Address:
                                  require ext_code.size(munknown76017b64Address)
                                  static call munknown76017b64Address.underlying() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args munknownd95393ebAddress
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                                  require ext_code.size(munknown38013f02Address)
                                                  static call munknown38013f02Address.getPrice(address token) with:
                                                          gas gas_remaining wei
                                                         args addr(ext_call.return_data[0])
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] < 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                                  require ext_code.size(munknown5f82c67eAddress)
                                                                  static call munknown5f82c67eAddress.markets(address param1) with:
                                                                          gas gas_remaining wei
                                                                         args munknown76017b64Address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 64
                                                                      require ext_call.return_data[0] <= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                      if (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                          require (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                          if 0 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                              require 0 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                              return 1, 
                                                                                     munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                          else:
                                                                              require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= 0
                                                                              return 0, 
                                                                                     -munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                      else:
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                          if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                              require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                              return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          else:
                                                                              require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                              return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[0] >= 0
                                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if ext_call.return_data[0] < munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                      require ext_call.return_data[0] <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                      return 1, 
                                                                             munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]
                                                                  else:
                                                                      require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0]
                                                                      return 0, 
                                                                             ext_call.return_data[0] - munknown2fe7d446 - (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                          else:
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                                  require ext_code.size(munknown5f82c67eAddress)
                                                                  static call munknown5f82c67eAddress.markets(address param1) with:
                                                                          gas gas_remaining wei
                                                                         args munknown76017b64Address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 64
                                                                      require ext_call.return_data[0] <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                      if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                          require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                          if 0 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                              require 0 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                              return 1, 
                                                                                     munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                          else:
                                                                              require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= 0
                                                                              return 0, 
                                                                                     -munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                      else:
                                                                          require ext_call.return_data[32] > 0
                                                                          require ext_call.return_data[32]
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                          if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                              require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                              return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          else:
                                                                              require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                              return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[0] >= 0
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if ext_call.return_data[0] < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                      require ext_call.return_data[0] <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                      return 1, munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]
                                                                  else:
                                                                      require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0]
                                                                      return 0, ext_call.return_data[0] - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if ext_call.return_data[0] < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require ext_call.return_data[0] <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]:
                                                                      require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= 0
                                                                          return 0, 
                                                                                 -munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                          return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require ext_call.return_data[0] >= 0
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if ext_call.return_data[0] < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require ext_call.return_data[0] <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - ext_call.return_data[0]
                                                              else:
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= ext_call.return_data[0]
                                                                  return 0, ext_call.return_data[0] - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                              else:
                                                  require ext_code.size(munknown38013f02Address)
                                                  static call munknown38013f02Address.getPrice(address token) with:
                                                          gas gas_remaining wei
                                                         args addr(ext_call.return_data[0])
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                                      revert
                              else:
                                  require ext_code.size(munknown38013f02Address)
                                  static call munknown38013f02Address.getPrice(address token) with:
                                          gas gas_remaining wei
                                         args munknownd95393ebAddress
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] < 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                              require ext_code.size(munknown5f82c67eAddress)
                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                      gas gas_remaining wei
                                                     args munknown76017b64Address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  require ext_call.return_data[0] <= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                                  if (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0]:
                                                      require (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                      if 0 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                          require 0 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                          return 1, 
                                                                 munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                      else:
                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= 0
                                                          return 0, 
                                                                 -munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                      if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                          require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      else:
                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                          return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                          else:
                                              require ext_call.return_data[0] >= 0
                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                              if ext_call.return_data[0] < munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]):
                                                  require ext_call.return_data[0] <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                                  return 1, munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - ext_call.return_data[0]
                                              else:
                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) <= ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] - munknown2fe7d446 - (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] < 0 / ext_call.return_data[0]:
                                              require ext_code.size(munknown5f82c67eAddress)
                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                      gas gas_remaining wei
                                                     args munknown76017b64Address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  require ext_call.return_data[0] <= 0 / ext_call.return_data[0]
                                                  if (0 / ext_call.return_data[0]) - ext_call.return_data[0]:
                                                      require (10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / (0 / ext_call.return_data[0]) - ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) >= (10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]
                                                      if 0 < munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]):
                                                          require 0 <= munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                          return 1, 
                                                                 munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                      else:
                                                          require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32]) <= 0
                                                          return 0, 
                                                                 -munknown2fe7d446 - ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0]) / ext_call.return_data[32])
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                      if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                          require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      else:
                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                          return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                          else:
                                              require ext_call.return_data[0] >= 0
                                              require munknown2fe7d446 + (0 / ext_call.return_data[0]) >= 0 / ext_call.return_data[0]
                                              if ext_call.return_data[0] < munknown2fe7d446 + (0 / ext_call.return_data[0]):
                                                  require ext_call.return_data[0] <= munknown2fe7d446 + (0 / ext_call.return_data[0])
                                                  return 1, munknown2fe7d446 + (0 / ext_call.return_data[0]) - ext_call.return_data[0]
                                              else:
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[0]) <= ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] - munknown2fe7d446 - (0 / ext_call.return_data[0])
      else:
          require ext_code.size(munknown878f7603Address)
          call munknown878f7603Address.0xbd6d894d with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require ext_code.size(munknown878f7603Address)
              static call munknown878f7603Address.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ext_call.return_data[0]:
                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                      require ext_code.size(munknown76017b64Address)
                      call munknown76017b64Address.0x17bfdfbc with:
                           gas gas_remaining wei
                          args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if munknown50fbd642Address != munknown76017b64Address:
                              require ext_code.size(munknown76017b64Address)
                              static call munknown76017b64Address.underlying() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args munknownd95393ebAddress
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                              require ext_code.size(munknown38013f02Address)
                                              static call munknown38013f02Address.getPrice(address token) with:
                                                      gas gas_remaining wei
                                                     args addr(ext_call.return_data[0])
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) < 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                      require (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, 
                                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, 
                                                                         munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                              else:
                                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  return 0, 
                                                                         eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require eth.balance(this.address) <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                      require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, 
                                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, 
                                                                         munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                              else:
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  return 0, 
                                                                         eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if eth.balance(this.address) < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require ext_code.size(munknown5f82c67eAddress)
                                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                                  gas gas_remaining wei
                                                                 args munknown76017b64Address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 64
                                                              require eth.balance(this.address) <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                  require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                  require ext_call.return_data[32] > 0
                                                                  require ext_call.return_data[32]
                                                                  require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                      return 1, 
                                                                             munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  else:
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                      return 0, 
                                                                             (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[32] > 0
                                                                  require ext_call.return_data[32]
                                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                                  else:
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                                      return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                      else:
                                                          require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                              require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                              return 1, 
                                                                     munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                          else:
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                              return 0, 
                                                                     eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                          else:
                                              require ext_code.size(munknown38013f02Address)
                                              static call munknown38013f02Address.getPrice(address token) with:
                                                      gas gas_remaining wei
                                                     args addr(ext_call.return_data[0])
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                                  revert
                          else:
                              require ext_code.size(munknown38013f02Address)
                              static call munknown38013f02Address.getPrice(address token) with:
                                      gas gas_remaining wei
                                     args munknownd95393ebAddress
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if ext_call.return_data[0]:
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if eth.balance(this.address) < 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                          require ext_code.size(munknown5f82c67eAddress)
                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                  gas gas_remaining wei
                                                 args munknown76017b64Address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                              if (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address):
                                                  require (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                      return 1, 
                                                             munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  else:
                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      return 0, 
                                                             (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                              else:
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  else:
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                      else:
                                          require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                          if eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]):
                                              require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                              return 1, 
                                                     munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                          else:
                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) <= eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                              return 0, 
                                                     eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if eth.balance(this.address) < 0 / ext_call.return_data[0]:
                                          require ext_code.size(munknown5f82c67eAddress)
                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                  gas gas_remaining wei
                                                 args munknown76017b64Address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              require eth.balance(this.address) <= 0 / ext_call.return_data[0]
                                              if (0 / ext_call.return_data[0]) - eth.balance(this.address):
                                                  require (10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                      return 1, 
                                                             munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  else:
                                                      require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      return 0, 
                                                             (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                              else:
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                  else:
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[32])
                                      else:
                                          require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) >= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          require munknown2fe7d446 + (0 / ext_call.return_data[0]) >= 0 / ext_call.return_data[0]
                                          if eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) < munknown2fe7d446 + (0 / ext_call.return_data[0]):
                                              require eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) <= munknown2fe7d446 + (0 / ext_call.return_data[0])
                                              return 1, 
                                                     munknown2fe7d446 + (0 / ext_call.return_data[0]) - eth.balance(this.address) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                          else:
                                              require munknown2fe7d446 + (0 / ext_call.return_data[0]) <= eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                              return 0, 
                                                     eth.balance(this.address) + (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - munknown2fe7d446 - (0 / ext_call.return_data[0])
                  else:
                      require ext_code.size(munknown76017b64Address)
                      call munknown76017b64Address.0x17bfdfbc with:
                           gas gas_remaining wei
                          args this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if munknown50fbd642Address != munknown76017b64Address:
                              require ext_code.size(munknown76017b64Address)
                              static call munknown76017b64Address.underlying() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args munknownd95393ebAddress
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                              require ext_code.size(munknown38013f02Address)
                                              static call munknown38013f02Address.getPrice(address token) with:
                                                      gas gas_remaining wei
                                                     args addr(ext_call.return_data[0])
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) < 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                      require (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= 0
                                                                          return 0, 
                                                                                 -munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                          return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require eth.balance(this.address) >= 0
                                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if eth.balance(this.address) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require eth.balance(this.address) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, 
                                                                         munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address)
                                                              else:
                                                                  require munknown2fe7d446 + (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address)
                                                                  return 0, 
                                                                         eth.balance(this.address) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                              require ext_code.size(munknown5f82c67eAddress)
                                                              static call munknown5f82c67eAddress.markets(address param1) with:
                                                                      gas gas_remaining wei
                                                                     args munknown76017b64Address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 64
                                                                  require eth.balance(this.address) <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                                  if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                      require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                          return 1, 
                                                                                 munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= 0
                                                                          return 0, 
                                                                                 -munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                  else:
                                                                      require ext_call.return_data[32] > 0
                                                                      require ext_call.return_data[32]
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                      if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                          require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                          return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                      else:
                                                                          require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                          return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                          else:
                                                              require eth.balance(this.address) >= 0
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if eth.balance(this.address) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                                  require eth.balance(this.address) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                                  return 1, munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address)
                                                              else:
                                                                  require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address)
                                                                  return 0, eth.balance(this.address) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if eth.balance(this.address) < 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require ext_code.size(munknown5f82c67eAddress)
                                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                                  gas gas_remaining wei
                                                                 args munknown76017b64Address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 64
                                                              require eth.balance(this.address) <= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                              if (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address):
                                                                  require (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                                  require ext_call.return_data[32] > 0
                                                                  require ext_call.return_data[32]
                                                                  require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                                  if 0 < munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                                      require 0 <= munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                      return 1, 
                                                                             munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                                  else:
                                                                      require munknown2fe7d446 + ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= 0
                                                                      return 0, 
                                                                             -munknown2fe7d446 - ((10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                              else:
                                                                  require ext_call.return_data[32] > 0
                                                                  require ext_call.return_data[32]
                                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                                  if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                                      require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                                  else:
                                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                                      return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                                      else:
                                                          require eth.balance(this.address) >= 0
                                                          require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) >= 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          if eth.balance(this.address) < munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]):
                                                              require eth.balance(this.address) <= munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                              return 1, munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) - eth.balance(this.address)
                                                          else:
                                                              require munknown2fe7d446 + (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]) <= eth.balance(this.address)
                                                              return 0, eth.balance(this.address) - munknown2fe7d446 - (0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                          else:
                                              require ext_code.size(munknown38013f02Address)
                                              static call munknown38013f02Address.getPrice(address token) with:
                                                      gas gas_remaining wei
                                                     args addr(ext_call.return_data[0])
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                                  revert
                          else:
                              require ext_code.size(munknown38013f02Address)
                              static call munknown38013f02Address.getPrice(address token) with:
                                      gas gas_remaining wei
                                     args munknownd95393ebAddress
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if ext_call.return_data[0]:
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if eth.balance(this.address) < 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                          require ext_code.size(munknown5f82c67eAddress)
                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                  gas gas_remaining wei
                                                 args munknown76017b64Address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                              if (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address):
                                                  require (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                  if 0 < munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                      require 0 <= munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                      return 1, 
                                                             munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                  else:
                                                      require munknown2fe7d446 + ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= 0
                                                      return 0, 
                                                             -munknown2fe7d446 - ((10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                              else:
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                  if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                      require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                  else:
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                      return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                      else:
                                          require eth.balance(this.address) >= 0
                                          require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) >= 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                          if eth.balance(this.address) < munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]):
                                              require eth.balance(this.address) <= munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                              return 1, munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) - eth.balance(this.address)
                                          else:
                                              require munknown2fe7d446 + (10^18 * ext_call.return_data[0] / ext_call.return_data[0]) <= eth.balance(this.address)
                                              return 0, eth.balance(this.address) - munknown2fe7d446 - (10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if eth.balance(this.address) < 0 / ext_call.return_data[0]:
                                          require ext_code.size(munknown5f82c67eAddress)
                                          static call munknown5f82c67eAddress.markets(address param1) with:
                                                  gas gas_remaining wei
                                                 args munknown76017b64Address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              require eth.balance(this.address) <= 0 / ext_call.return_data[0]
                                              if (0 / ext_call.return_data[0]) - eth.balance(this.address):
                                                  require (10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / (0 / ext_call.return_data[0]) - eth.balance(this.address) == 10^18
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) >= (10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]
                                                  if 0 < munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]):
                                                      require 0 <= munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                      return 1, 
                                                             munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                                  else:
                                                      require munknown2fe7d446 + ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32]) <= 0
                                                      return 0, 
                                                             -munknown2fe7d446 - ((10^18 * 0 / ext_call.return_data[0]) - (10^18 * eth.balance(this.address)) / ext_call.return_data[32])
                                              else:
                                                  require ext_call.return_data[32] > 0
                                                  require ext_call.return_data[32]
                                                  require munknown2fe7d446 + (0 / ext_call.return_data[32]) >= 0 / ext_call.return_data[32]
                                                  if 0 < munknown2fe7d446 + (0 / ext_call.return_data[32]):
                                                      require 0 <= munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                      return 1, munknown2fe7d446 + (0 / ext_call.return_data[32])
                                                  else:
                                                      require munknown2fe7d446 + (0 / ext_call.return_data[32]) <= 0
                                                      return 0, -munknown2fe7d446 - (0 / ext_call.return_data[32])
                                      else:
                                          require eth.balance(this.address) >= 0
                                          require munknown2fe7d446 + (0 / ext_call.return_data[0]) >= 0 / ext_call.return_data[0]
                                          if eth.balance(this.address) < munknown2fe7d446 + (0 / ext_call.return_data[0]):
                                              require eth.balance(this.address) <= munknown2fe7d446 + (0 / ext_call.return_data[0])
                                              return 1, munknown2fe7d446 + (0 / ext_call.return_data[0]) - eth.balance(this.address)
                                          else:
                                              require munknown2fe7d446 + (0 / ext_call.return_data[0]) <= eth.balance(this.address)
                                              return 0, eth.balance(this.address) - munknown2fe7d446 - (0 / ext_call.return_data[0])
  else:
      if munknown94d5567a < munknown2fe7d446:
          require munknown94d5567a <= munknown2fe7d446
          return 1, munknown2fe7d446 - munknown94d5567a
      else:
          require munknown2fe7d446 <= munknown94d5567a
          return 0, munknown94d5567a - munknown2fe7d446


# hash = 0x50fbd642
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def unknown50fbd642() payable: 
  return munknown50fbd642Address


# hash = 0x59690e70
# getter = None
# const = None
# payable = True
def unknown59690e70() payable: 
  require ext_code.size(munknown878f7603Address)
  call munknown878f7603Address.0xbd6d894d with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_code.size(munknown878f7603Address)
      static call munknown878f7603Address.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if ext_call.return_data[0]:
              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
              require ext_code.size(munknown5f82c67eAddress)
              static call munknown5f82c67eAddress.markets(address param1) with:
                      gas gas_remaining wei
                     args munknown76017b64Address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 64
                  require ext_code.size(munknown76017b64Address)
                  call munknown76017b64Address.0x17bfdfbc with:
                       gas gas_remaining wei
                      args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if munknown50fbd642Address != munknown76017b64Address:
                          require ext_code.size(munknown76017b64Address)
                          static call munknown76017b64Address.underlying() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(addr(ext_call.return_data[0]))
                              static call addr(ext_call.return_data[0]).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(munknown38013f02Address)
                                  static call munknown38013f02Address.getPrice(address token) with:
                                          gas gas_remaining wei
                                         args munknownd95393ebAddress
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args addr(ext_call.return_data[0])
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  if ext_call.return_data[0] * ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                              return 1, 
                                                                     (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                          else:
                                                              require 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              return 0, 
                                                                     (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32])
                                                      else:
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 0 / ext_call.return_data[32]:
                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[32]
                                                              return 1, (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                          else:
                                                              require 0 / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (0 / ext_call.return_data[32])
                                                  else:
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                              return 1, 
                                                                     (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                          else:
                                                              require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              return 0, 
                                                                     (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32])
                                                      else:
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 0 / ext_call.return_data[32]:
                                                              require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[32]
                                                              return 1, (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                          else:
                                                              require 0 / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                              return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (0 / ext_call.return_data[32])
                                              else:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                          return 1, 
                                                                 (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, 
                                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32])
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 0 / ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[32]
                                                          return 1, (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                                      else:
                                                          require 0 / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (0 / ext_call.return_data[32])
                                      else:
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args addr(ext_call.return_data[0])
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0]
                                              require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                              revert
                      else:
                          require ext_code.size(munknown38013f02Address)
                          static call munknown38013f02Address.getPrice(address token) with:
                                  gas gas_remaining wei
                                 args munknownd95393ebAddress
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0]:
                                  require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                  require ext_call.return_data[0] > 0
                                  require ext_call.return_data[0]
                                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                      require 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]:
                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]
                                          return 1, 
                                                 (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                      else:
                                          require 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          return 0, 
                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32])
                                  else:
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 0 / ext_call.return_data[32]:
                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[32]
                                          return 1, (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (0 / ext_call.return_data[32])
                              else:
                                  require ext_call.return_data[0] > 0
                                  require ext_call.return_data[0]
                                  if 0 / ext_call.return_data[0]:
                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]:
                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]
                                          return 1, 
                                                 (10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                      else:
                                          require 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          return 0, 
                                                 (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32])
                                  else:
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18 < 0 / ext_call.return_data[32]:
                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[32]
                                          return 1, (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 / ext_call.return_data[32] <= ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                          return 0, (ext_call.return_data[0] * ext_call.return_data[0] / 10^18) - (0 / ext_call.return_data[32])
          else:
              require ext_code.size(munknown5f82c67eAddress)
              static call munknown5f82c67eAddress.markets(address param1) with:
                      gas gas_remaining wei
                     args munknown76017b64Address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 64
                  require ext_code.size(munknown76017b64Address)
                  call munknown76017b64Address.0x17bfdfbc with:
                       gas gas_remaining wei
                      args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if munknown50fbd642Address != munknown76017b64Address:
                          require ext_code.size(munknown76017b64Address)
                          static call munknown76017b64Address.underlying() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(addr(ext_call.return_data[0]))
                              static call addr(ext_call.return_data[0]).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(munknown38013f02Address)
                                  static call munknown38013f02Address.getPrice(address token) with:
                                          gas gas_remaining wei
                                         args munknownd95393ebAddress
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args addr(ext_call.return_data[0])
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  if ext_call.return_data[0] * ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if 0 < 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                              require 0 <= 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                              return 1, 
                                                                     10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                          else:
                                                              require 10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= 0
                                                              return 0, 
                                                                     -10^18 * 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                      else:
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if 0 < 0 / ext_call.return_data[32]:
                                                              require 0 <= 0 / ext_call.return_data[32]
                                                              return 1, 0 / ext_call.return_data[32]
                                                          else:
                                                              require 0 / ext_call.return_data[32] <= 0
                                                              return 0, -0 / ext_call.return_data[32]
                                                  else:
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                          require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if 0 < 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                              require 0 <= 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                              return 1, 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                          else:
                                                              require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= 0
                                                              return 0, -10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                      else:
                                                          require ext_call.return_data[32] > 0
                                                          require ext_call.return_data[32]
                                                          if 0 < 0 / ext_call.return_data[32]:
                                                              require 0 <= 0 / ext_call.return_data[32]
                                                              return 1, 0 / ext_call.return_data[32]
                                                          else:
                                                              require 0 / ext_call.return_data[32] <= 0
                                                              return 0, -0 / ext_call.return_data[32]
                                              else:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      if 0 < 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]:
                                                          require 0 <= 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                          return 1, 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                      else:
                                                          require 10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32] <= 0
                                                          return 0, -10^18 * 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32] > 0
                                                      require ext_call.return_data[32]
                                                      if 0 < 0 / ext_call.return_data[32]:
                                                          require 0 <= 0 / ext_call.return_data[32]
                                                          return 1, 0 / ext_call.return_data[32]
                                                      else:
                                                          require 0 / ext_call.return_data[32] <= 0
                                                          return 0, -0 / ext_call.return_data[32]
                                      else:
                                          require ext_code.size(munknown38013f02Address)
                                          static call munknown38013f02Address.getPrice(address token) with:
                                                  gas gas_remaining wei
                                                 args addr(ext_call.return_data[0])
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0]
                                              require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                              revert
                      else:
                          require ext_code.size(munknown38013f02Address)
                          static call munknown38013f02Address.getPrice(address token) with:
                                  gas gas_remaining wei
                                 args munknownd95393ebAddress
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0]:
                                  require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                  require ext_call.return_data[0] > 0
                                  require ext_call.return_data[0]
                                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                      require 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if 0 < 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]:
                                          require 0 <= 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]
                                          return 1, 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]
                                      else:
                                          require 10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32] <= 0
                                          return 0, -10^18 * 10^18 * ext_call.return_data[0] / ext_call.return_data[0] / ext_call.return_data[32]
                                  else:
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if 0 < 0 / ext_call.return_data[32]:
                                          require 0 <= 0 / ext_call.return_data[32]
                                          return 1, 0 / ext_call.return_data[32]
                                      else:
                                          require 0 / ext_call.return_data[32] <= 0
                                          return 0, -0 / ext_call.return_data[32]
                              else:
                                  require ext_call.return_data[0] > 0
                                  require ext_call.return_data[0]
                                  if 0 / ext_call.return_data[0]:
                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if 0 < 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]:
                                          require 0 <= 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]
                                          return 1, 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]
                                      else:
                                          require 10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32] <= 0
                                          return 0, -10^18 * 0 / ext_call.return_data[0] / ext_call.return_data[32]
                                  else:
                                      require ext_call.return_data[32] > 0
                                      require ext_call.return_data[32]
                                      if 0 < 0 / ext_call.return_data[32]:
                                          require 0 <= 0 / ext_call.return_data[32]
                                          return 1, 0 / ext_call.return_data[32]
                                      else:
                                          require 0 / ext_call.return_data[32] <= 0
                                          return 0, -0 / ext_call.return_data[32]


# hash = 0x5f2d554b
# getter = None
# const = None
# payable = True
def unknown5f2d554b() payable: 
  require ext_code.size(munknown878f7603Address)
  call munknown878f7603Address.0xbd6d894d with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown878f7603Address)
  static call munknown878f7603Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
  return (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)


# hash = 0x5f82c67e
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def unknown5f82c67e() payable: 
  return munknown5f82c67eAddress


# hash = 0x62141fcc
# getter = ['storage', 256, 0, 7]
# const = None
# payable = True
def unknown62141fcc() payable: 
  return munknown62141fcc


# hash = 0x6db153de
# getter = None
# const = None
# payable = True
def unknown6db153de() payable: 
  require ext_code.size(munknown878f7603Address)
  call munknown878f7603Address.0xbd6d894d with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_code.size(munknown878f7603Address)
      static call munknown878f7603Address.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if ext_call.return_data[0]:
              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
              require ext_code.size(munknown76017b64Address)
              call munknown76017b64Address.0x17bfdfbc with:
                   gas gas_remaining wei
                  args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if munknown50fbd642Address != munknown76017b64Address:
                      require ext_code.size(munknown76017b64Address)
                      static call munknown76017b64Address.underlying() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_code.size(addr(ext_call.return_data[0]))
                          static call addr(ext_call.return_data[0]).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(munknown38013f02Address)
                              static call munknown38013f02Address.getPrice(address token) with:
                                      gas gas_remaining wei
                                     args munknownd95393ebAddress
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if ext_call.return_data[0]:
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args addr(ext_call.return_data[0])
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              if ext_call.return_data[0] * ext_call.return_data[0]:
                                                  require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18:
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * ext_call.return_data[0] / 10^18 == 10^18
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          return (0 / 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      return -1
                                              else:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^18:
                                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * ext_call.return_data[0] / 10^18 == 10^18
                                                          require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                      else:
                                                          require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                          require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                          return (0 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      return -1
                                          else:
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                              if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18:
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * ext_call.return_data[0] / 10^18 == 10^18
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      return (0 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                              else:
                                                  return -1
                                  else:
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args addr(ext_call.return_data[0])
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_call.return_data[0]
                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                          require ext_call.return_data[0] * ext_call.return_data[0]
                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                          revert
                  else:
                      require ext_code.size(munknown38013f02Address)
                      static call munknown38013f02Address.getPrice(address token) with:
                              gas gas_remaining wei
                             args munknownd95393ebAddress
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0]:
                              require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                              require ext_call.return_data[0] > 0
                              require ext_call.return_data[0]
                              if 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18:
                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * ext_call.return_data[0] / 10^18 == 10^18
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] > 0
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                      return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / 10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                                  else:
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] > 0
                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                      return (0 / 10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                              else:
                                  return -1
                          else:
                              require ext_call.return_data[0] > 0
                              require ext_call.return_data[0]
                              if 0 / ext_call.return_data[0]:
                                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^18:
                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * ext_call.return_data[0] / 10^18 == 10^18
                                      require 0 / ext_call.return_data[0] > 0
                                      require 0 / ext_call.return_data[0]
                                      return (10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^18 / 0 / ext_call.return_data[0])
                                  else:
                                      require 0 / ext_call.return_data[0] > 0
                                      require 0 / ext_call.return_data[0]
                                      return (0 / 0 / ext_call.return_data[0])
                              else:
                                  return -1
          else:
              require ext_code.size(munknown76017b64Address)
              call munknown76017b64Address.0x17bfdfbc with:
                   gas gas_remaining wei
                  args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if munknown50fbd642Address != munknown76017b64Address:
                      require ext_code.size(munknown76017b64Address)
                      static call munknown76017b64Address.underlying() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_code.size(addr(ext_call.return_data[0]))
                          static call addr(ext_call.return_data[0]).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(munknown38013f02Address)
                              static call munknown38013f02Address.getPrice(address token) with:
                                      gas gas_remaining wei
                                     args munknownd95393ebAddress
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if ext_call.return_data[0]:
                                      require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] / ext_call.return_data[0] == 10^uint8(ext_call.return_data[0])
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args addr(ext_call.return_data[0])
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              if ext_call.return_data[0] * ext_call.return_data[0]:
                                                  require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == 10^18
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      return (0 / 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      return -1
                                              else:
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                      require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                      return (0 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                                  else:
                                                      return -1
                                          else:
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                              require 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                              if 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]:
                                                  require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0] > 0
                                                  require 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0]
                                                  return (0 / 0 / 10^uint8(ext_call.return_data[0]) * ext_call.return_data[0])
                                              else:
                                                  return -1
                                  else:
                                      require ext_code.size(munknown38013f02Address)
                                      static call munknown38013f02Address.getPrice(address token) with:
                                              gas gas_remaining wei
                                             args addr(ext_call.return_data[0])
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_call.return_data[0]
                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                          require ext_call.return_data[0] * ext_call.return_data[0]
                                          require 10^18 * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != 10^18
                                          revert
                  else:
                      require ext_code.size(munknown38013f02Address)
                      static call munknown38013f02Address.getPrice(address token) with:
                              gas gas_remaining wei
                             args munknownd95393ebAddress
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0]:
                              require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                              require ext_call.return_data[0] > 0
                              require ext_call.return_data[0]
                              if 10^18 * ext_call.return_data[0] / ext_call.return_data[0]:
                                  require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] > 0
                                  require 10^18 * ext_call.return_data[0] / ext_call.return_data[0]
                                  return (0 / 10^18 * ext_call.return_data[0] / ext_call.return_data[0])
                              else:
                                  return -1
                          else:
                              require ext_call.return_data[0] > 0
                              require ext_call.return_data[0]
                              if 0 / ext_call.return_data[0]:
                                  require 0 / ext_call.return_data[0] > 0
                                  require 0 / ext_call.return_data[0]
                                  return (0 / 0 / ext_call.return_data[0])
                              else:
                                  return -1


# hash = 0x6f17591f
# getter = ['bool', ['storage', 8, 168, 11]]
# const = None
# payable = True
def unknown6f17591f() payable: 
  return bool(munknown6f17591f)


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  require caller == mowner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x7461df11
# getter = None
# const = None
# payable = True
def unknown7461df11() payable: 
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
      return eth.balance(this.address)
  require ext_code.size(addr(mstor15))
  static call addr(mstor15).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x76017b64
# getter = ['storage', 160, 0, 11]
# const = None
# payable = True
def unknown76017b64() payable: 
  return munknown76017b64Address


# hash = 0x878f7603
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def unknown878f7603() payable: 
  return munknown878f7603Address


# hash = 0x8b98a2c5
# getter = None
# const = ['return', ['data', 32, 4, 0]]
# payable = True
const unknown8b98a2c5 = ''


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = True
def isOwner() payable: 
  return (caller == mowner)


# hash = 0x94d5567a
# getter = ['storage', 256, 0, 10]
# const = None
# payable = True
def unknown94d5567a() payable: 
  return munknown94d5567a


# hash = 0xab7b1c89
# getter = None
# const = None
# payable = True
def unknownab7b1c89(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  require munknown03eeb4ca > 0
  if munknown50fbd642Address == munknown76017b64Address:
      require addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      require ext_code.size(mstor16)
      static call mstor16.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
              gas gas_remaining wei
             args addr(mstor15), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_call.return_data[32]
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
          require ext_code.size(mstor16)
          call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
             value m_param1 wei
               gas gas_remaining wei
              args 0, uint32(mstor15), m_param1, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require eth.balance(this.address) <= eth.balance(this.address)
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[0]:
                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                      else:
                          require ext_code.size(addr(mstor15))
                          static call addr(mstor15).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if 18 < ext_call.return_data[31 len 1]:
                              require ext_call.return_data[31 len 1] - 18 <= 18
                          else:
                              require -ext_call.return_data[31 len 1] + 18 <= 18
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      if ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                              if 18 < ext_call.return_data[31 len 1]:
                                  require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                              if 18 < ext_call.return_data[31 len 1]:
                                  require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require -ext_call.return_data[31 len 1] + 18 <= 18
              revert
          require ext_code.size(addr(mstor15))
          call addr(mstor15).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args munknowncb0ef21dAddress, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require eth.balance(this.address) <= eth.balance(this.address)
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[0]:
                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                      else:
                          require ext_code.size(addr(mstor15))
                          static call addr(mstor15).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if 18 < ext_call.return_data[31 len 1]:
                              require ext_call.return_data[31 len 1] - 18 <= 18
                          else:
                              require -ext_call.return_data[31 len 1] + 18 <= 18
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      if ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                              if 18 < ext_call.return_data[31 len 1]:
                                  require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                              if 18 < ext_call.return_data[31 len 1]:
                                  require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require -ext_call.return_data[31 len 1] + 18 <= 18
              revert
          require ext_code.size(addr(mstor15))
          static call addr(mstor15).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= eth.balance(this.address)
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0]
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
              if ext_call.return_data[31 len 1] < 18:
                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  require ext_call.return_data[0]
              else:
                  require ext_call.return_data[31 len 1] - 18 <= 18
                  require 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require eth.balance(this.address) - ext_call.return_data[0]
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0] <= 10000000000 * 10^18
              if 18 < ext_call.return_data[31 len 1]:
                  require ext_call.return_data[31 len 1] - 18 <= 18
                  require eth.balance(this.address) - ext_call.return_data[0]
              else:
                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  require (eth.balance(this.address) * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                  require eth.balance(this.address) - ext_call.return_data[0]
      else:
          require ext_code.size(addr(mstor15))
          static call addr(mstor15).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require ext_code.size(mstor16)
              call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
                 value m_param1 wei
                   gas gas_remaining wei
                  args 0, uint32(mstor15), m_param1, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          else:
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, m_param1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              require ext_code.size(mstor16)
              call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
                   gas gas_remaining wei
                  args 0, uint32(mstor15), m_param1, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              if addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= ext_call.return_data[0]
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= 10000000000 * 10^18
                              if 18 < ext_call.return_data[31 len 1]:
                                  require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require -ext_call.return_data[31 len 1] + 18 <= 18
                                  require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                  else:
                      require ext_code.size(addr(mstor15))
                      static call addr(mstor15).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[31 len 1] < 18:
                          require -ext_call.return_data[31 len 1] + 18 <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if 18 < ext_call.return_data[31 len 1]:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                                  else:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                                      require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                      else:
                          require ext_call.return_data[31 len 1] - 18 <= 18
                          if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if 18 < ext_call.return_data[31 len 1]:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                                  else:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                                      require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                  revert
          require eth.balance(this.address) <= ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
              require ext_call.return_data[0]
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
              if ext_call.return_data[31 len 1] < 18:
                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  require ext_call.return_data[0]
              else:
                  require ext_call.return_data[31 len 1] - 18 <= 18
                  require 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
              require ext_call.return_data[0] <= 10000000000 * 10^18
              require ext_call.return_data[0] - eth.balance(this.address)
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
              require ext_call.return_data[0] <= 10000000000 * 10^18
              if 18 < ext_call.return_data[31 len 1]:
                  require ext_call.return_data[31 len 1] - 18 <= 18
                  require ext_call.return_data[0] - eth.balance(this.address)
              else:
                  require -ext_call.return_data[31 len 1] + 18 <= 18
                  require (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (eth.balance(this.address) * 10^(-ext_call.return_data[31 len 1] + 18))
                  require ext_call.return_data[0] - eth.balance(this.address)
  else:
      require ext_code.size(munknown76017b64Address)
      static call munknown76017b64Address.underlying() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require addr(mstor15) != ext_call.return_data[12 len 20]
      require ext_code.size(mstor16)
      static call mstor16.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
              gas gas_remaining wei
             args addr(mstor15), addr(ext_call.return_data[0]), m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_call.return_data[32]
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
          require ext_code.size(mstor16)
          call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
             value m_param1 wei
               gas gas_remaining wei
              args 0, uint32(mstor15), m_param1, addr(ext_call.return_data[0]), addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require eth.balance(this.address) <= eth.balance(this.address)
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                              else:
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if ext_call.return_data[31 len 1] < 18:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if 18 < ext_call.return_data[31 len 1]:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                                  else:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                              else:
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                  else:
                                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                  else:
                      require ext_code.size(addr(mstor15))
                      static call addr(mstor15).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[31 len 1] < 18:
                          require -ext_call.return_data[31 len 1] + 18 <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require ext_call.return_data[31 len 1] - 18 <= 18
                          if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if 18 < ext_call.return_data[31 len 1]:
                          require ext_call.return_data[31 len 1] - 18 <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require -ext_call.return_data[31 len 1] + 18 <= 18
                          if 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                  else:
                      require ext_code.size(addr(mstor15))
                      static call addr(mstor15).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                          if 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
              revert
          require ext_code.size(addr(mstor15))
          call addr(mstor15).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args munknowncb0ef21dAddress, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require eth.balance(this.address) <= eth.balance(this.address)
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[0]:
                          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                              else:
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if ext_call.return_data[31 len 1] < 18:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                          else:
                              require ext_code.size(addr(mstor15))
                              static call addr(mstor15).decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if 18 < ext_call.return_data[31 len 1]:
                                      require ext_call.return_data[31 len 1] - 18 <= 18
                                  else:
                                      require -ext_call.return_data[31 len 1] + 18 <= 18
                              else:
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  static call addr(ext_call.return_data[0]).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= 10000000000 * 10^18
                                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                  else:
                                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                  else:
                      require ext_code.size(addr(mstor15))
                      static call addr(mstor15).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[31 len 1] < 18:
                          require -ext_call.return_data[31 len 1] + 18 <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require ext_call.return_data[31 len 1] - 18 <= 18
                          if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if 18 < ext_call.return_data[31 len 1]:
                          require ext_call.return_data[31 len 1] - 18 <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require -ext_call.return_data[31 len 1] + 18 <= 18
                          if 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                  else:
                      require ext_code.size(addr(mstor15))
                      static call addr(mstor15).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 10000000000 * 10^18
                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      else:
                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                          if 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])) * ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
              revert
          require ext_code.size(addr(mstor15))
          static call addr(mstor15).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= eth.balance(this.address)
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0]
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]
          else:
              require ext_code.size(addr(ext_call.return_data[0]))
              static call addr(ext_call.return_data[0]).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  if 18 < ext_call.return_data[31 len 1]:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require ext_call.return_data[0]
                  else:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                      require ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      require 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])) * ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require eth.balance(this.address) - ext_call.return_data[0]
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require eth.balance(this.address) - ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require (eth.balance(this.address) * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                      require eth.balance(this.address) - ext_call.return_data[0]
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if 18 < ext_call.return_data[31 len 1]:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require eth.balance(this.address) - ext_call.return_data[0]
                  else:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require (eth.balance(this.address) * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                      require eth.balance(this.address) - ext_call.return_data[0]
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require eth.balance(this.address) - ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                      require eth.balance(this.address) - ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      require (eth.balance(this.address) * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                      require eth.balance(this.address) - ext_call.return_data[0]
      else:
          require ext_code.size(addr(mstor15))
          static call addr(mstor15).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              require ext_code.size(mstor16)
              call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
                 value m_param1 wei
                   gas gas_remaining wei
                  args 0, uint32(mstor15), m_param1, addr(ext_call.return_data[0]), addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          else:
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, m_param1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              require ext_code.size(mstor16)
              call mstor16.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
                   gas gas_remaining wei
                  args 0, uint32(mstor15), m_param1, addr(ext_call.return_data[0]), addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0, 256, 4, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
          if addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
              require ext_code.size(addr(mstor15))
              call addr(mstor15).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknowncb0ef21dAddress, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              if addr(mstor15) != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= ext_call.return_data[0]
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if ext_call.return_data[0]:
                              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < 18:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                          require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                              else:
                                  require ext_code.size(addr(mstor15))
                                  static call addr(mstor15).decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if 18 < ext_call.return_data[31 len 1]:
                                          require ext_call.return_data[31 len 1] - 18 <= 18
                                      else:
                                          require -ext_call.return_data[31 len 1] + 18 <= 18
                                          require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                  else:
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      static call addr(ext_call.return_data[0]).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= 10000000000 * 10^18
                                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                          require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                      else:
                                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                          require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                      else:
                          require ext_code.size(addr(mstor15))
                          static call addr(mstor15).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if ext_call.return_data[31 len 1] < 18:
                              require -ext_call.return_data[31 len 1] + 18 <= 18
                              if ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                          else:
                              require ext_call.return_data[31 len 1] - 18 <= 18
                              if 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                  else:
                      require ext_code.size(addr(ext_call.return_data[0]))
                      static call addr(ext_call.return_data[0]).decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if 18 < ext_call.return_data[31 len 1]:
                              require ext_call.return_data[31 len 1] - 18 <= 18
                              if ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                          else:
                              require -ext_call.return_data[31 len 1] + 18 <= 18
                              if 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                      else:
                          require ext_code.size(addr(mstor15))
                          static call addr(mstor15).decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= 10000000000 * 10^18
                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                              if ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                          else:
                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                              if 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])) * ext_call.return_data[0]:
                                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < 18:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18))
                                  else:
                                      require ext_code.size(addr(mstor15))
                                      static call addr(mstor15).decimals() with:
                                              gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if 18 < ext_call.return_data[31 len 1]:
                                              require ext_call.return_data[31 len 1] - 18 <= 18
                                          else:
                                              require -ext_call.return_data[31 len 1] + 18 <= 18
                                              require not (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18))
                                      else:
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          static call addr(ext_call.return_data[0]).decimals() with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 32
                                          require ext_call.return_data[0] <= 10000000000 * 10^18
                                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                              require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                                          else:
                                              require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                                              require not (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                  revert
          require eth.balance(this.address) <= ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  require ext_call.return_data[0]
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require 10^(ext_call.return_data[31 len 1] - 18) * ext_call.return_data[0]
          else:
              require ext_code.size(addr(ext_call.return_data[0]))
              static call addr(ext_call.return_data[0]).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  if 18 < ext_call.return_data[31 len 1]:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require ext_call.return_data[0]
                  else:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]
              else:
                  require ext_code.size(addr(mstor15))
                  static call addr(mstor15).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                      require ext_call.return_data[0]
                  else:
                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      require 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])) * ext_call.return_data[0]
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(mstor15):
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  require ext_call.return_data[0] - eth.balance(this.address)
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require ext_call.return_data[0] - eth.balance(this.address)
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - 18)) - (eth.balance(this.address) * 10^(ext_call.return_data[31 len 1] - 18))
                      require ext_call.return_data[0] - eth.balance(this.address)
          else:
              require ext_code.size(addr(mstor15))
              static call addr(mstor15).decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(ext_call.return_data[0]):
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if 18 < ext_call.return_data[31 len 1]:
                      require ext_call.return_data[31 len 1] - 18 <= 18
                      require ext_call.return_data[0] - eth.balance(this.address)
                  else:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                      require (ext_call.return_data[0] * 10^(-ext_call.return_data[31 len 1] + 18)) - (eth.balance(this.address) * 10^(-ext_call.return_data[31 len 1] + 18))
                      require ext_call.return_data[0] - eth.balance(this.address)
              else:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  static call addr(ext_call.return_data[0]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] - eth.balance(this.address) <= 10000000000 * 10^18
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                      require uint8(ext_call.return_data[0]) - ext_call.return_data[31 len 1] <= 18
                      require ext_call.return_data[0] - eth.balance(this.address)
                  else:
                      require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                      require (ext_call.return_data[0] * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]))) - (eth.balance(this.address) * 10^(ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0])))
                      require ext_call.return_data[0] - eth.balance(this.address)
  require ext_call.return_data[0] > 0
  require ext_code.size(munknown76017b64Address)
  call munknown76017b64Address.0x17bfdfbc with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown76017b64Address)
  call munknown76017b64Address.0x4e4d9fea with:
     value ext_call.return_data[0] wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xcb0ef21d
# getter = ['storage', 160, 0, 14]
# const = None
# payable = True
def unknowncb0ef21d() payable: 
  return munknowncb0ef21dAddress


# hash = 0xcc0e97c9
# getter = ['storage', 160, 0, 12]
# const = None
# payable = True
def logicContract() payable: 
  return mlogicContractAddress


# hash = 0xd95393eb
# getter = ['storage', 160, 0, 13]
# const = None
# payable = True
def unknownd95393eb() payable: 
  return munknownd95393ebAddress


# hash = 0xe852e741
# getter = ['bool', ['storage', 8, 160, 11]]
# const = None
# payable = True
def unknowne852e741() payable: 
  return bool(munknowne852e741)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf7fa7202
# getter = None
# const = None
# payable = True
def unknownf7fa7202() payable: 
  require ext_code.size(munknown5f82c67eAddress)
  static call munknown5f82c67eAddress.markets(address param1) with:
          gas gas_remaining wei
         args munknown76017b64Address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[32]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


