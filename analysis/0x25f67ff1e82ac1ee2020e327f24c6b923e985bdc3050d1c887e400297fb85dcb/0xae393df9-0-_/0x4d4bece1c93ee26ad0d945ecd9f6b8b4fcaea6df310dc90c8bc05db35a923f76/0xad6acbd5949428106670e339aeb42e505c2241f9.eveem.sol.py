# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAd6AcBd5949428106670e339aEb42E505C2241f9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x41becc07': 'unknown41becc07(?)', '0x63bb23be': 'unknown63bb23be(?)', '0x7f6715c9': 'unknown7f6715c9(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknowna0b2d57fAddress # mask: a s
    # storage address 1
    unknownf17a3becAddress # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
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
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 12
    stor12 # mask: a s
# hash = 0x0900f010
# getter = None
# const = None
# payable = True
def upgrade(address _implementation) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor2))
  static call addr(stor2).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(addr(stor2))
      call addr(stor2).transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_implementation), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]


# hash = 0x0ea9c984
# getter = None
# const = None
# payable = True
def unknown0ea9c984() payable: 
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x434c000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor7 = ext_call.return_data[12 len 20] or Mask(96, 160, stor7)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4344000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor8) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor8))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.tokenAddress() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor2) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor2))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5443000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor3 = ext_call.return_data[12 len 20] or Mask(96, 160, stor3)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5444000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor5) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor5))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5446000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor4) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor4))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5031000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor9 = ext_call.return_data[12 len 20] or Mask(96, 160, stor9)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5032000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor10 = ext_call.return_data[12 len 20] or Mask(96, 160, stor10)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5044000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor11 = ext_call.return_data[12 len 20] or Mask(96, 160, stor11)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5144000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor6 = ext_call.return_data[12 len 20] or Mask(96, 160, stor6)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor12) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor12))


# hash = 0x35afb14e
# getter = None
# const = None
# payable = True
def unknown35afb14e(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x34f19e2c with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x4ecffeb with:
          gas gas_remaining wei
         args _param1
  mem[96 len 64] = ext_call.return_data[0 len 64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  [94midx = mem[96]
  [94ms = 0
  while [94midx < ext_call.return_data[0]:
      require ext_code.size(addr(stor8))
      static call addr(stor8).0xfc57c9bb with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(addr(stor8))
          static call addr(stor8).0x54a1b431 with:
                  gas gas_remaining wei
                 args ext_call.return_data[0]
          mem[96 len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[100] = ext_call.return_data[32]
              require ext_code.size(addr(stor8))
              static call addr(stor8).0x4e06c014 with:
                      gas gas_remaining wei
                     args ext_call.return_data[32]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ('signextend', 0, ('ext_call.return_data', 0, 32)):
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[0]
                              continue 
                  else:
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[0]
                              continue 
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x274d865f with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = ext_call.return_data[32]
  [94mt = [94ms
  while [94midx < ext_call.return_data[0]:
      require ext_code.size(addr(stor8))
      static call addr(stor8).0xf2d16e2a with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(addr(stor8))
          static call addr(stor8).0x54a1b431 with:
                  gas gas_remaining wei
                 args ext_call.return_data[0]
          mem[96 len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[100] = ext_call.return_data[32]
              require ext_code.size(addr(stor8))
              static call addr(stor8).0x4e06c014 with:
                      gas gas_remaining wei
                     args ext_call.return_data[32]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ('signextend', 0, ('ext_call.return_data', 0, 32)):
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94mt = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      [94midx = [94midx + 1
                                      [94mt = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94mt = ext_call.return_data[0]
                              continue 
                  else:
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94mt = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      [94midx = [94midx + 1
                                      [94mt = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94mt = ext_call.return_data[0]
                              continue 
  require ext_code.size(addr(stor5))
  static call addr(stor5).0x6101c166 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor5))
  static call addr(stor5).0x3f4a7efa with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor4))
  static call addr(stor4).0xf57cb5a6 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor12))
  static call addr(stor12).0x4df9d6ba with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] <= ext_call.return_data[0]
  require ext_call.return_data[0] >= 0
  require ext_call.return_data[0] >= ext_call.return_data[0]
  require ext_call.return_data[0] >= 0
  return (2 * ext_call.return_data[0])


# hash = 0x452efce9
# getter = None
# const = None
# payable = True
def unknown452efce9(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x34f19e2c with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x4ecffeb with:
          gas gas_remaining wei
         args _param1
  mem[96 len 64] = ext_call.return_data[0 len 64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  [94midx = mem[96]
  [94ms = 0
  while [94midx < ext_call.return_data[0]:
      require ext_code.size(addr(stor8))
      static call addr(stor8).0xfc57c9bb with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(addr(stor8))
          static call addr(stor8).0x54a1b431 with:
                  gas gas_remaining wei
                 args ext_call.return_data[0]
          mem[96 len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[100] = ext_call.return_data[32]
              require ext_code.size(addr(stor8))
              static call addr(stor8).0x4e06c014 with:
                      gas gas_remaining wei
                     args ext_call.return_data[32]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ('signextend', 0, ('ext_call.return_data', 0, 32)):
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[0]
                              continue 
                  else:
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[0]
                              continue 
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x274d865f with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = ext_call.return_data[32]
  [94mt = [94ms
  while [94midx < ext_call.return_data[0]:
      require ext_code.size(addr(stor8))
      static call addr(stor8).0xf2d16e2a with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(addr(stor8))
          static call addr(stor8).0x54a1b431 with:
                  gas gas_remaining wei
                 args ext_call.return_data[0]
          mem[96 len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[100] = ext_call.return_data[32]
              require ext_code.size(addr(stor8))
              static call addr(stor8).0x4e06c014 with:
                      gas gas_remaining wei
                     args ext_call.return_data[32]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ('signextend', 0, ('ext_call.return_data', 0, 32)):
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94mt = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      [94midx = [94midx + 1
                                      [94mt = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94mt = ext_call.return_data[0]
                              continue 
                  else:
                      if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                          [94midx = [94midx + 1
                          [94mt = ext_call.return_data[0]
                          continue 
                      else:
                          if not ext_call.return_data[96]:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              mem[96 len 96] = ext_call.return_data[0 len 96]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      [94midx = [94midx + 1
                                      [94mt = ext_call.return_data[0]
                                      continue 
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          require 0 / 100 * ext_call.return_data[64] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      require 0 / 100 * ext_call.return_data[64] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          mem[96 len 96] = ext_call.return_data[0 len 96]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          require 0 / 100 * ext_call.return_data[32] >= 0
                                                          [94midx = [94midx + 1
                                                          [94mt = ext_call.return_data[0]
                                                          continue 
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      require 0 / 100 * ext_call.return_data[32] >= 0
                                                      [94midx = [94midx + 1
                                                      [94mt = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                          else:
                              [94midx = [94midx + 1
                              [94mt = ext_call.return_data[0]
                              continue 
  return 0


# hash = 0xa0b2d57f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def unknowna0b2d57f() payable: 
  return unknowna0b2d57fAddress


# hash = 0xd46655f4
# getter = None
# const = None
# payable = True
def unknownd46655f4(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if unknowna0b2d57fAddress:
      if unknowna0b2d57fAddress != caller:
          revert with 0, 'Not master'
  unknowna0b2d57fAddress = _param1
  unknownf17a3becAddress = _param1


# hash = 0xdf31f208
# getter = None
# const = None
# payable = True
def unknowndf31f208(uint256 _param1, uint256 _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(addr(stor8))
  static call addr(stor8).0x54a1b431 with:
          gas gas_remaining wei
         args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 128
      require ext_code.size(addr(stor8))
      static call addr(stor8).0x4e06c014 with:
              gas gas_remaining wei
             args ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if ('signextend', 0, ('ext_call.return_data', 0, 32)):
              if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                  return 0, 0, ext_call.return_data[0], 0
              else:
                  if not ext_call.return_data[96]:
                      if _param1 != 1:
                          require ext_code.size(addr(stor8))
                          static call addr(stor8).0xc49a8b19 with:
                                  gas gas_remaining wei
                                 args ext_call.return_data[32]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 96
                              if not ext_call.return_data[32]:
                                  return 0, 0, ext_call.return_data[0], ext_call.return_data[32]
                              else:
                                  if _param1 != 1:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                      else:
                          require ext_code.size(addr(stor8))
                          static call addr(stor8).0xc49a8b19 with:
                                  gas gas_remaining wei
                                 args ext_call.return_data[32]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 96
                              if not ext_call.return_data[0]:
                                  return 0, 0, ext_call.return_data[0], ext_call.return_data[0]
                              else:
                                  if _param1 != 1:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                 0,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                  else:
                      if _param3 != 1:
                          return 0, 0, ext_call.return_data[0], 0
                      else:
                          if _param1 != 1:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      return 0, 0, ext_call.return_data[0], ext_call.return_data[32]
                                  else:
                                      if _param1 != 1:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                      else:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                          else:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      return 0, 0, ext_call.return_data[0], ext_call.return_data[0]
                                  else:
                                      if _param1 != 1:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                      else:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                     0,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 0, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
          else:
              if ('signextend', 0, ('ext_call.return_data', 0, 32)) != ('signextend', 0, ('ext_call.return_data', 64, 32)):
                  return 0, 1, ext_call.return_data[0], 0
              else:
                  if not ext_call.return_data[96]:
                      if _param1 != 1:
                          require ext_code.size(addr(stor8))
                          static call addr(stor8).0xc49a8b19 with:
                                  gas gas_remaining wei
                                 args ext_call.return_data[32]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 96
                              if not ext_call.return_data[32]:
                                  return 0, 1, ext_call.return_data[0], ext_call.return_data[32]
                              else:
                                  if _param1 != 1:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[32]:
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[32]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                              else:
                                                  require ext_call.return_data[32]
                                                  require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[32]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                  revert
                      else:
                          require ext_code.size(addr(stor8))
                          static call addr(stor8).0xc49a8b19 with:
                                  gas gas_remaining wei
                                 args ext_call.return_data[32]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 96
                              if not ext_call.return_data[0]:
                                  return 0, 1, ext_call.return_data[0], ext_call.return_data[0]
                              else:
                                  if _param1 != 1:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0x949d9d76 with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                  else:
                                      if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[64]:
                                                  require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[64] > 0
                                                      require 100 * ext_call.return_data[64]
                                                      return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                                      else:
                                          require ext_code.size(addr(stor8))
                                          static call addr(stor8).0xdbd0064c with:
                                                  gas gas_remaining wei
                                                 args ext_call.return_data[32]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 96
                                              if ext_call.return_data[32]:
                                                  require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if ext_call.return_data[0] * ext_call.return_data[0]:
                                                          require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                 1,
                                                                 ext_call.return_data[0],
                                                                 ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require 100 * ext_call.return_data[32] > 0
                                                      require 100 * ext_call.return_data[32]
                                                      return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                              else:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0]
                                                  require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                  revert
                  else:
                      if _param3 != 1:
                          return 0, 1, ext_call.return_data[0], 0
                      else:
                          if _param1 != 1:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[32]:
                                      return 0, 1, ext_call.return_data[0], ext_call.return_data[32]
                                  else:
                                      if _param1 != 1:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                      else:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[64], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[32]:
                                                          require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[32]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / 100 * ext_call.return_data[32], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[32]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[32]
                                                  else:
                                                      require ext_call.return_data[32]
                                                      require ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[32] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[32]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[32] / ext_call.return_data[0] * ext_call.return_data[32] != ext_call.return_data[64]
                                                      revert
                          else:
                              require ext_code.size(addr(stor8))
                              static call addr(stor8).0xc49a8b19 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[32]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 96
                                  if not ext_call.return_data[0]:
                                      return 0, 1, ext_call.return_data[0], ext_call.return_data[0]
                                  else:
                                      if _param1 != 1:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0x949d9d76 with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                      else:
                                          if ('signextend', 0, ('ext_call.return_data', 64, 32)) != 1:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[64]:
                                                      require 100 * ext_call.return_data[64] / ext_call.return_data[64] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[64], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[64] > 0
                                                              require 100 * ext_call.return_data[64]
                                                              return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[64] > 0
                                                          require 100 * ext_call.return_data[64]
                                                          return 0 / 100 * ext_call.return_data[64], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert
                                          else:
                                              require ext_code.size(addr(stor8))
                                              static call addr(stor8).0xdbd0064c with:
                                                      gas gas_remaining wei
                                                     args ext_call.return_data[32]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 96
                                                  if ext_call.return_data[32]:
                                                      require 100 * ext_call.return_data[32] / ext_call.return_data[32] == 100
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          if ext_call.return_data[0] * ext_call.return_data[0]:
                                                              require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] == ext_call.return_data[64]
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / 100 * ext_call.return_data[32], 
                                                                     1,
                                                                     ext_call.return_data[0],
                                                                     ext_call.return_data[0]
                                                          else:
                                                              require 100 * ext_call.return_data[32] > 0
                                                              require 100 * ext_call.return_data[32]
                                                              return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                      else:
                                                          require 100 * ext_call.return_data[32] > 0
                                                          require 100 * ext_call.return_data[32]
                                                          return 0 / 100 * ext_call.return_data[32], 1, ext_call.return_data[0], ext_call.return_data[0]
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0]
                                                      require ext_call.return_data[64] * ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] * ext_call.return_data[0] != ext_call.return_data[64]
                                                      revert


# hash = 0xf17a3bec
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def unknownf17a3bec() payable: 
  return unknownf17a3becAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


