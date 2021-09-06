# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6bA33B70229cd20A674ddf842C87EebEae0735D0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x54d20439': 'unknown54d20439(?)', '0x7b100ec9': 'unknown7b100ec9(?)', '0xf57cb5a6': 'unknownf57cb5a6(?)', '0xfb7cf219': 'unknownfb7cf219(?)'} 

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
    tkAddress # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
# hash = 0x0788e72b
# getter = None
# const = None
# payable = True
def unknown0788e72b(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xe2264850 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _param2:
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xf480454a with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(unknowna0b2d57fAddress)
      static call unknowna0b2d57fAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4352000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor6))
      static call addr(stor6).0x832c2e40 with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  else:
      require ext_call.return_data[0] * _param2 / _param2 == ext_call.return_data[0]
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xf480454a with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(unknowna0b2d57fAddress)
      static call unknowna0b2d57fAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4352000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor6))
      static call addr(stor6).0x832c2e40 with:
              gas gas_remaining wei
             args _param1
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = mem[96]
      [94ms = ext_call.return_data[0] * _param2 / 100
      while [94midx < ext_call.return_data[0]:
          if not [94ms:
              if [94ms > 0:
                  if ext_call.return_data[0] > 0:
                      require 1 <= ext_call.return_data[0]
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xc8858703 with:
                           gas gas_remaining wei
                          args addr(_param1), ext_call.return_data[0] - 1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
              stop
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xb8ea578e with:
                  gas gas_remaining wei
                 args addr(_param1), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x24da7b69 with:
                  gas gas_remaining wei
                 args addr(_param1), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x43148d23 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x6a964451 with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[100] = addr(ext_call.return_data[0])
              mem[132] = ext_call.return_data[0]
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x2bc22628 with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), ext_call.return_data[0]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 0 <= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94ms + ext_call.return_data[0] >= ext_call.return_data[0]
              if 0 >= [94ms + ext_call.return_data[0]:
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0x34f15b69 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), addr(_param1), [94midx, [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor5))
                  call addr(stor5).mint(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if [94midx > 0:
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xc8858703 with:
                           gas gas_remaining wei
                          args addr(_param1), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  stop
              require ext_call.return_data[0] <= 0
              mem[164] = [94midx
              mem[196] = -ext_call.return_data[0]
              require ext_code.size(addr(stor6))
              call addr(stor6).0x34f15b69 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), addr(_param1), [94midx, -ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_call.return_data[0] <= 0
              mem[96] = 0x40c10f1900000000000000000000000000000000000000000000000000000000
              mem[100] = addr(ext_call.return_data[0])
              mem[132] = -ext_call.return_data[0]
              require ext_code.size(addr(stor5))
              call addr(stor5).mint(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), -ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_call.return_data[0] <= 0
              require -ext_call.return_data[0] <= [94ms
              [94midx = [94midx + 1
              [94ms = [94ms + ext_call.return_data[0]
              continue 
          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
          mem[100] = addr(ext_call.return_data[0])
          mem[132] = ext_call.return_data[0]
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x2bc22628 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] * ext_call.return_data[0] / 100 <= ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94ms + ext_call.return_data[0] >= ext_call.return_data[0]
          if ext_call.return_data[0] * ext_call.return_data[0] / 100 >= [94ms + ext_call.return_data[0]:
              require ext_code.size(addr(stor6))
              call addr(stor6).0x34f15b69 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), addr(_param1), [94midx, [94ms
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(stor5))
              call addr(stor5).mint(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), [94ms
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if [94midx > 0:
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0xc8858703 with:
                       gas gas_remaining wei
                      args addr(_param1), [94midx
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              stop
          require ext_call.return_data[0] <= ext_call.return_data[0] * ext_call.return_data[0] / 100
          mem[164] = [94midx
          mem[196] = (ext_call.return_data[0] * ext_call.return_data[0] / 100) - ext_call.return_data[0]
          require ext_code.size(addr(stor6))
          call addr(stor6).0x34f15b69 with:
               gas gas_remaining wei
              args addr(ext_call.return_data[0]), addr(_param1), [94midx, (ext_call.return_data[0] * ext_call.return_data[0] / 100) - ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_call.return_data[0] <= ext_call.return_data[0] * ext_call.return_data[0] / 100
          mem[96] = 0x40c10f1900000000000000000000000000000000000000000000000000000000
          mem[100] = addr(ext_call.return_data[0])
          mem[132] = (ext_call.return_data[0] * ext_call.return_data[0] / 100) - ext_call.return_data[0]
          require ext_code.size(addr(stor5))
          call addr(stor5).mint(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(ext_call.return_data[0]), (ext_call.return_data[0] * ext_call.return_data[0] / 100) - ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_call.return_data[0] <= ext_call.return_data[0] * ext_call.return_data[0] / 100
          require (ext_call.return_data[0] * ext_call.return_data[0] / 100) - ext_call.return_data[0] <= [94ms
          [94midx = [94midx + 1
          [94ms = [94ms - (ext_call.return_data[0] * ext_call.return_data[0] / 100) + ext_call.return_data[0]
          continue 
      if [94ms > 0:
          if ext_call.return_data[0] > 0:
              require 1 <= ext_call.return_data[0]
              require ext_code.size(addr(stor6))
              call addr(stor6).0xc8858703 with:
                   gas gas_remaining wei
                  args addr(_param1), ext_call.return_data[0] - 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]


# hash = 0x0ea9c984
# getter = None
# const = None
# payable = True
def unknown0ea9c984() payable: 
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.tokenAddress() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor4) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor4))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5444000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor6) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor6))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5443000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor5) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor5))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4352000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor8 = ext_call.return_data[12 len 20] or Mask(96, 160, stor8)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5144000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor7) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor7))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4d43000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor2) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor2))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor9 = ext_call.return_data[12 len 20] or Mask(96, 160, stor9)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4d52000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor3 = ext_call.return_data[12 len 20] or Mask(96, 160, stor3)
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5044000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  stor10 = ext_call.return_data[12 len 20] or Mask(96, 160, stor10)


# hash = 0x200537a4
# getter = None
# const = None
# payable = True
def unknown200537a4(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x3c2d4daf with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor5))
  static call addr(stor5).tokensLockedAtTime(address of, bytes32 reason, uint256 time) with:
          gas gas_remaining wei
         args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x21f408be
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def tk() payable: 
  return addr(tkAddress)


# hash = 0x33cb73de
# getter = None
# const = None
# payable = True
def unknown33cb73de(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(addr(stor6))
  static call addr(stor6).0x79ade32f with:
          gas gas_remaining wei
         args addr(_param1), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0x24da7b69 with:
          gas gas_remaining wei
         args addr(_param2), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xc1ed5a74 with:
          gas gas_remaining wei
         args addr(_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 224
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xff1b4504 with:
          gas gas_remaining wei
         args addr(_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xc1ed5a74 with:
          gas gas_remaining wei
         args addr(_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 224
  require ext_call.return_data[64] <= block.timestamp
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xc47ac1ac with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= block.timestamp - ext_call.return_data[64] / 24 * 3600:
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xff1b4504 with:
              gas gas_remaining wei
             args addr(_param1), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor6))
      static call addr(stor6).0x79ade32f with:
              gas gas_remaining wei
             args addr(_param1), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor5))
      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
              gas gas_remaining wei
             args addr(_param1), sha3(0, _param1, _param2, ext_call.return_data[0])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
          if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
              require 0 <= ext_call.return_data[96]
              require ext_call.return_data[0] <= ext_call.return_data[96]
              require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
              return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= ext_call.return_data[96]
          require ext_call.return_data[0] <= (2 * ext_call.return_data[96]) - (2 * ext_call.return_data[0]) - ext_call.return_data[160]
          require ext_call.return_data[160] <= (2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - ext_call.return_data[160]
          return ((2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (2 * ext_call.return_data[160]))
      require 0 <= ext_call.return_data[0]
      require ext_call.return_data[192] <= ext_call.return_data[0]
      if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
          require 0 <= ext_call.return_data[96]
          require ext_call.return_data[0] <= ext_call.return_data[96]
          require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
          return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
  else:
      require block.timestamp - ext_call.return_data[64] / 24 * 3600 <= ext_call.return_data[0]
      if not ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600):
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if not 0 / ext_call.return_data[0]:
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(_param1), sha3(0, _param1, _param2, ext_call.return_data[0])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                      require 0 <= ext_call.return_data[96]
                      require ext_call.return_data[0] <= ext_call.return_data[96]
                      require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
                      return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= (2 * ext_call.return_data[96]) - (2 * ext_call.return_data[0]) - ext_call.return_data[160]
                  require ext_call.return_data[160] <= (2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - ext_call.return_data[160]
                  return ((2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (2 * ext_call.return_data[160]))
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  require 0 <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= ext_call.return_data[96]
                  require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
                  return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
          else:
              require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == ext_call.return_data[96]
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(_param1), sha3(0, _param1, _param2, ext_call.return_data[0])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                  if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                      require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[96]
                      require ext_call.return_data[0] <= ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                      require ext_call.return_data[160] <= ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[0]
                      return (ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[0] - ext_call.return_data[160])
                  require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= (2 * ext_call.return_data[96]) - (2 * ext_call.return_data[0]) - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                  require ext_call.return_data[160] <= (2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                  return ((2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - (2 * ext_call.return_data[160]))
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                  require ext_call.return_data[160] <= ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[0]
                  return (ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[0] - ext_call.return_data[160])
      else:
          require (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600) == 100000
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if not (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0]:
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(_param1), sha3(0, _param1, _param2, ext_call.return_data[0])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                      require 0 <= ext_call.return_data[96]
                      require ext_call.return_data[0] <= ext_call.return_data[96]
                      require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
                      return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= (2 * ext_call.return_data[96]) - (2 * ext_call.return_data[0]) - ext_call.return_data[160]
                  require ext_call.return_data[160] <= (2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - ext_call.return_data[160]
                  return ((2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (2 * ext_call.return_data[160]))
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  require 0 <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= ext_call.return_data[96]
                  require ext_call.return_data[160] <= ext_call.return_data[96] - ext_call.return_data[0]
                  return (ext_call.return_data[96] - ext_call.return_data[0] - ext_call.return_data[160])
          else:
              require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] == ext_call.return_data[96]
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(_param1), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(_param1), sha3(0, _param1, _param2, ext_call.return_data[0])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                  if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                      require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[96]
                      require ext_call.return_data[0] <= ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                      require ext_call.return_data[160] <= ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[0]
                      return (ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[0] - ext_call.return_data[160])
                  require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= (2 * ext_call.return_data[96]) - (2 * ext_call.return_data[0]) - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                  require ext_call.return_data[160] <= (2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                  return ((2 * ext_call.return_data[96]) - (3 * ext_call.return_data[0]) - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - (2 * ext_call.return_data[160]))
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[96]
                  require ext_call.return_data[0] <= ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                  require ext_call.return_data[160] <= ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[0]
                  return (ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[0] - ext_call.return_data[160])
  require 0 <= ext_call.return_data[0]
  require ext_call.return_data[192] <= ext_call.return_data[0]
  require ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[96]
  require ext_call.return_data[0] <= ext_call.return_data[96] - ext_call.return_data[0] + ext_call.return_data[192]
  require ext_call.return_data[160] <= ext_call.return_data[96] - (2 * ext_call.return_data[0]) + ext_call.return_data[192]
  return (ext_call.return_data[96] - (2 * ext_call.return_data[0]) + ext_call.return_data[192] - ext_call.return_data[160])


# hash = 0x377a856c
# getter = None
# const = None
# payable = True
def unknown377a856c(addr _param1) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 32
  mem[100] = _param1
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xf480454a with:
          gas gas_remaining wei
         args _param1
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94midx = 0
  [94ms = 0
  [94ms = 0
  while [94midx < ext_call.return_data[0]:
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xa72c3520 with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor6))
      static call addr(stor6).0x24da7b69 with:
              gas gas_remaining wei
             args addr(_param1), [94midx
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xc1ed5a74 with:
              gas gas_remaining wei
             args addr(ext_call.return_data[0]), ext_call.return_data[0]
      mem[mem[64] len 224] = ext_call.return_data[0 len 224]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 224
      require ext_call.return_data[64] <= block.timestamp
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xc47ac1ac with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= block.timestamp - ext_call.return_data[64] / 24 * 3600:
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xff1b4504 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x79ade32f with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_130 = mem[64]
          mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 34] = addr(ext_call.return_data[0])
          mem[mem[64] + 54] = addr(_param1)
          mem[mem[64] + 74] = ext_call.return_data[0]
          [94m_131 = mem[64]
          mem[mem[64]] = 74
          mem[64] = mem[64] + 106
          [94m_133 = sha3(mem[[94m_131 + 32 len mem[[94m_131]])
          mem[[94m_130 + 110] = addr(ext_call.return_data[0])
          mem[[94m_130 + 142] = [94m_133
          require ext_code.size(addr(stor5))
          static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), [94m_133
          mem[[94m_130 + 106] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
              require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
              require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
              if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                  require [94ms >= [94ms
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  continue 
              require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
              require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
              require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms >= [94ms
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms
              continue 
          require 0 <= ext_call.return_data[0]
          require ext_call.return_data[192] <= ext_call.return_data[0]
          if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
              require [94ms >= [94ms
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = [94ms
              continue 
      else:
          require block.timestamp - ext_call.return_data[64] / 24 * 3600 <= ext_call.return_data[0]
          if not ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600):
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if not 0 / ext_call.return_data[0]:
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0xff1b4504 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x79ade32f with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_168 = mem[64]
                  mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 34] = addr(ext_call.return_data[0])
                  mem[mem[64] + 54] = addr(_param1)
                  mem[mem[64] + 74] = ext_call.return_data[0]
                  [94m_169 = mem[64]
                  mem[mem[64]] = 74
                  mem[64] = mem[64] + 106
                  [94m_171 = sha3(mem[[94m_169 + 32 len mem[[94m_169]])
                  mem[[94m_168 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_168 + 142] = [94m_171
                  require ext_code.size(addr(stor5))
                  static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), [94m_171
                  mem[[94m_168 + 106] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                      require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                      if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                          require [94ms >= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                      require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms
                      continue 
                  require 0 <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= ext_call.return_data[0]
                  if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                      require [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
              else:
                  require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == ext_call.return_data[96]
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0xff1b4504 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x79ade32f with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_179 = mem[64]
                  mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 34] = addr(ext_call.return_data[0])
                  mem[mem[64] + 54] = addr(_param1)
                  mem[mem[64] + 74] = ext_call.return_data[0]
                  [94m_180 = mem[64]
                  mem[mem[64]] = 74
                  mem[64] = mem[64] + 106
                  [94m_182 = sha3(mem[[94m_180 + 32 len mem[[94m_180]])
                  mem[[94m_179 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_179 + 142] = [94m_182
                  require ext_code.size(addr(stor5))
                  static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), [94m_182
                  mem[[94m_179 + 106] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                      require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                      if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                          require (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + [94ms >= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          [94ms = (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + [94ms
                          continue 
                      require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                      require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + [94ms
                      continue 
                  require 0 <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= ext_call.return_data[0]
                  if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                      require (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + [94ms
                      continue 
          else:
              require (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600) == 100000
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if not (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0]:
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0xff1b4504 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x79ade32f with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_174 = mem[64]
                  mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 34] = addr(ext_call.return_data[0])
                  mem[mem[64] + 54] = addr(_param1)
                  mem[mem[64] + 74] = ext_call.return_data[0]
                  [94m_175 = mem[64]
                  mem[mem[64]] = 74
                  mem[64] = mem[64] + 106
                  [94m_177 = sha3(mem[[94m_175 + 32 len mem[[94m_175]])
                  mem[[94m_174 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_174 + 142] = [94m_177
                  require ext_code.size(addr(stor5))
                  static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), [94m_177
                  mem[[94m_174 + 106] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                      require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                      if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                          require [94ms >= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                      require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + [94ms
                      continue 
                  require 0 <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= ext_call.return_data[0]
                  if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                      require [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
              else:
                  require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] == ext_call.return_data[96]
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0xff1b4504 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x79ade32f with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94m_184 = mem[64]
                  mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 34] = addr(ext_call.return_data[0])
                  mem[mem[64] + 54] = addr(_param1)
                  mem[mem[64] + 74] = ext_call.return_data[0]
                  [94m_185 = mem[64]
                  mem[mem[64]] = 74
                  mem[64] = mem[64] + 106
                  [94m_187 = sha3(mem[[94m_185 + 32 len mem[[94m_185]])
                  mem[[94m_184 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_184 + 142] = [94m_187
                  require ext_code.size(addr(stor5))
                  static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[0]), [94m_187
                  mem[[94m_184 + 106] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                      require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                      if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                          require (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + [94ms >= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          [94ms = (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + [94ms
                          continue 
                      require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                      require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + [94ms
                      continue 
                  require 0 <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= ext_call.return_data[0]
                  if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                      require (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + [94ms >= [94ms
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + [94ms
                      continue 
      require 0 <= ext_call.return_data[0]
      require ext_call.return_data[192] <= ext_call.return_data[0]
      require ext_call.return_data[0] - ext_call.return_data[192] + [94ms >= [94ms
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0]
      [94ms = ext_call.return_data[0] - ext_call.return_data[192] + [94ms
      continue 
  return [94ms


# hash = 0x463c24a3
# getter = None
# const = None
# payable = True
def unknown463c24a3(uint32 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(stor2))
  static call addr(stor2).0x3cb23b2d with:
          gas gas_remaining wei
         args Mask(32, 224, _param1)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x4c14b3a8
# getter = None
# const = None
# payable = True
def unknown4c14b3a8(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x3c2d4daf with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor5))
  static call addr(stor5).tokensLockedAtTime(address of, bytes32 reason, uint256 time) with:
          gas gas_remaining wei
         args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= 0:
      revert with 0, 'No cover note available'
  require ext_code.size(addr(stor6))
  call addr(stor6).0x8831d590 with:
       gas gas_remaining wei
      args _param1, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x6374299e
# getter = None
# const = None
# payable = True
def unknown6374299e(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 1 == bool(ext_call.return_data[0])
  require ext_code.size(addr(stor6))
  call addr(stor6).0xdfc2d1ba with:
       gas gas_remaining wei
      args caller, addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xc47ac1ac with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      require ext_code.size(addr(stor5))
      call addr(stor5).0xfa64f8c1 with:
           gas gas_remaining wei
          args caller, sha3(0, Mask(160, 96, caller) >> 96, _param1, ext_call.return_data[0]), _param2, 0
  else:
      require 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 24 * 3600
      require ext_code.size(addr(stor5))
      call addr(stor5).0xfa64f8c1 with:
           gas gas_remaining wei
          args caller, sha3(0, Mask(160, 96, caller) >> 96, _param1, ext_call.return_data[0]), _param2, 24 * 3600 * ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0x7dded30d
# getter = None
# const = None
# payable = True
def unknown7dded30d(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x3c2d4daf with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0x1dc130a2 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      require ext_code.size(addr(stor5))
      call addr(stor5).0x7aef5b73 with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), 0
  else:
      require 50 * ext_call.return_data[0] / ext_call.return_data[0] == 50
      require ext_code.size(addr(stor5))
      call addr(stor5).0x7aef5b73 with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), 50 * ext_call.return_data[0] / 100
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x85f52204
# getter = None
# const = None
# payable = True
def unknown85f52204(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x3c2d4daf with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x3c2d4daf with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor5))
  static call addr(stor5).tokensLockedAtTime(address of, bytes32 reason, uint256 time) with:
          gas gas_remaining wei
         args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(addr(stor5))
      call addr(stor5).0x80c7561a with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), _param1), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa0b2d57f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def unknowna0b2d57f() payable: 
  return unknowna0b2d57fAddress


# hash = 0xac5adaf6
# getter = None
# const = None
# payable = True
def unknownac5adaf6(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(tkAddress))
  static call addr(tkAddress).0x98fd371f with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (block.timestamp < ext_call.return_data[0])


# hash = 0xba903202
# getter = None
# const = None
# payable = True
def unknownba903202(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(addr(stor5))
  static call addr(stor5).tokensLockedAtTime(address of, bytes32 reason, uint256 time) with:
          gas gas_remaining wei
         args addr(_param1), sha3(0, _param1, _param2), block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xccace7df
# getter = None
# const = None
# payable = True
def unknownccace7df(uint256 _param1, uint256 _param2, addr _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x5834e67a with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor5))
  call addr(stor5).0x7aef5b73 with:
       gas gas_remaining wei
      args addr(_param3), 0x434c410000000000000000000000000000000000000000000000000000000000, _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0xbe5088ad: _param1, addr(_param3), _param2


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


# hash = 0xddcc90bd
# getter = None
# const = None
# payable = True
def unknownddcc90bd(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(addr(stor5))
  static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
          gas gas_remaining wei
         args addr(_param1), sha3(0, _param1, _param2, _param3)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xe8ed9214
# getter = None
# const = None
# payable = True
def unknowne8ed9214(addr _param1, uint256 _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param3 + block.timestamp >= block.timestamp
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x711acf86 with:
          gas gas_remaining wei
         args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param3 + block.timestamp >= ext_call.return_data[0]:
      require ext_code.size(addr(stor5))
      call addr(stor5).0x2c69d416 with:
           gas gas_remaining wei
          args addr(_param1), sha3(0, _param1, _param2), _param3 + block.timestamp
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0xf075be1f
# getter = None
# const = None
# payable = True
def unknownf075be1f(uint256 _param1, uint256 _param2, uint256 _param3, addr _param4) payable: 
  require calldata.size - 4 >= 128
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xce0a6d5f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require (24 * 3600 * _param2) + block.timestamp >= block.timestamp
  require ext_call.return_data[0] >= 0
  require ext_code.size(addr(stor6))
  call addr(stor6).0x4e718659 with:
       gas gas_remaining wei
      args _param3, _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(stor5))
  call addr(stor5).0xfa64f8c1 with:
       gas gas_remaining wei
      args addr(_param4), sha3(0, _param4, _param3), _param1, ext_call.return_data[0] + (24 * 3600 * _param2) + block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xf17a3bec
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def unknownf17a3bec() payable: 
  return unknownf17a3becAddress


# hash = 0xf9acac08
# getter = None
# const = None
# payable = True
def unknownf9acac08(uint256 _param1, uint32 _param2, uint256 _param3) payable: 
  mem[64] = 96
  require calldata.size - 4 >= 96
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor7))
  static call addr(stor7).0x8d16a105 with:
          gas gas_remaining wei
         args _param1
  mem[96 len 64] = ext_call.return_data[0 len 64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(addr(stor2))
  static call addr(stor2).0x3cb23b2d with:
          gas gas_remaining wei
         args Mask(32, 224, _param2)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(stor6))
  static call addr(stor6).0xf480454a with:
          gas gas_remaining wei
         args addr(ext_call.return_data[32])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _param3:
      require ext_call.return_data[0] > 0
      require ext_call.return_data[0]
      mem[100] = addr(ext_call.return_data[32])
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xf75ce5d4 with:
              gas gas_remaining wei
             args addr(ext_call.return_data[32])
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = mem[mem[64]]
      [94ms = 0
      [94ms = 0
      [94ms = 0 / ext_call.return_data[0]
      while [94midx < ext_call.return_data[0]:
          if not [94ms:
              if [94ms > 0:
                  if ext_call.return_data[0] > 0:
                      require 1 <= ext_call.return_data[0]
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xeaf53c77 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[32]), ext_call.return_data[0] - 1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
              stop
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xa72c3520 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[32]), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x24da7b69 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[32]), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xc1ed5a74 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          mem[mem[64] len 224] = ext_call.return_data[0 len 224]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 224
          require ext_call.return_data[64] <= block.timestamp
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xc47ac1ac with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] <= block.timestamp - ext_call.return_data[64] / 24 * 3600:
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1040 = mem[64]
              mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 34] = addr(ext_call.return_data[0])
              mem[mem[64] + 54] = addr(ext_call.return_data[32])
              mem[mem[64] + 74] = ext_call.return_data[0]
              [94m_1041 = mem[64]
              mem[mem[64]] = 74
              mem[64] = mem[64] + 106
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), sha3(mem[[94m_1041 + 32 len mem[[94m_1041]])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                      mem[[94m_1040 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1040 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1040 + 142] = ext_call.return_data[0]
                      mem[[94m_1040 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = [94midx + 1
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  mem[[94m_1040 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                  mem[[94m_1040 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_1040 + 142] = ext_call.return_data[0]
                  mem[[94m_1040 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0x14f07b3c with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                      [94midx = [94midx + 1
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x24da7b69 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[32]), [94midx
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(addr(stor5))
                      call addr(stor5).0x7aef5b73 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if [94midx:
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0xeaf53c77 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                      stop
                  call addr(stor6).0x48dc990 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[[94m_1040 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[[94m_1040 + 140] = addr(ext_call.return_data[0])
                  mem[[94m_1040 + 160] = addr(ext_call.return_data[32])
                  mem[[94m_1040 + 180] = [94midx
                  mem[[94m_1040 + 106] = 74
                  mem[64] = [94m_1040 + 212
                  mem[[94m_1040 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                  mem[[94m_1040 + 216] = addr(ext_call.return_data[0])
                  mem[[94m_1040 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                  mem[[94m_1040 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  require ext_code.size(addr(stor5))
                  call addr(stor5).0x7aef5b73 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                  [94midx = [94midx + 1
                  [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                  continue 
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  mem[[94m_1040 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                  mem[[94m_1040 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_1040 + 142] = ext_call.return_data[0]
                  mem[[94m_1040 + 174] = 0
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0x14f07b3c with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94midx = [94midx + 1
                  [94ms = 0
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  continue 
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              mem[[94m_1040 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
              mem[[94m_1040 + 110] = addr(ext_call.return_data[0])
              mem[[94m_1040 + 142] = ext_call.return_data[0]
              mem[[94m_1040 + 174] = 0
              require ext_code.size(addr(stor6))
              call addr(stor6).0x14f07b3c with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  continue 
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x24da7b69 with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[32]), [94midx
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                  call addr(stor6).0x48dc990 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor5))
                  call addr(stor5).0x7aef5b73 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if [94midx:
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xeaf53c77 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  stop
              call addr(stor6).0x48dc990 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[[94m_1040 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
              mem[[94m_1040 + 140] = addr(ext_call.return_data[0])
              mem[[94m_1040 + 160] = addr(ext_call.return_data[32])
              mem[[94m_1040 + 180] = [94midx
              mem[[94m_1040 + 106] = 74
              mem[64] = [94m_1040 + 212
              mem[[94m_1040 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
              mem[[94m_1040 + 216] = addr(ext_call.return_data[0])
              mem[[94m_1040 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
              mem[[94m_1040 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
          else:
              require block.timestamp - ext_call.return_data[64] / 24 * 3600 <= ext_call.return_data[0]
              if not ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600):
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if not 0 / ext_call.return_data[0]:
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1128 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1129 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1129 + 32 len mem[[94m_1129]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                              mem[[94m_1128 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1128 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1128 + 142] = ext_call.return_data[0]
                              mem[[94m_1128 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              [94midx = [94midx + 1
                              [94ms = 0
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1128 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1128 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1128 + 142] = ext_call.return_data[0]
                          mem[[94m_1128 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1128 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1128 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1128 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1128 + 180] = [94midx
                          mem[[94m_1128 + 106] = 74
                          mem[64] = [94m_1128 + 212
                          mem[[94m_1128 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1128 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1128 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1128 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1128 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1128 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1128 + 142] = ext_call.return_data[0]
                          mem[[94m_1128 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94midx = [94midx + 1
                          [94ms = 0
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1128 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1128 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1128 + 142] = ext_call.return_data[0]
                      mem[[94m_1128 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1128 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1128 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1128 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1128 + 180] = [94midx
                      mem[[94m_1128 + 106] = 74
                      mem[64] = [94m_1128 + 212
                      mem[[94m_1128 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1128 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1128 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1128 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
                  else:
                      require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == ext_call.return_data[96]
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1154 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1155 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1155 + 32 len mem[[94m_1155]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                              mem[[94m_1154 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1154 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1154 + 142] = ext_call.return_data[0]
                              mem[[94m_1154 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                                  [94ms = ext_call.return_data[0]
                                  [94ms = [94ms
                                  continue 
                              require ext_code.size(addr(stor6))
                              static call addr(stor6).0x24da7b69 with:
                                      gas gas_remaining wei
                                     args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(addr(stor6))
                              if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 >= [94ms:
                                  call addr(stor6).0x48dc990 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require ext_code.size(addr(stor5))
                                  call addr(stor5).0x7aef5b73 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  if [94midx:
                                      require ext_code.size(addr(stor6))
                                      call addr(stor6).0xeaf53c77 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data[32]), [94midx
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                  stop
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mem[[94m_1154 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                              mem[[94m_1154 + 140] = addr(ext_call.return_data[0])
                              mem[[94m_1154 + 160] = addr(ext_call.return_data[32])
                              mem[[94m_1154 + 180] = [94midx
                              mem[[94m_1154 + 106] = 74
                              mem[64] = [94m_1154 + 212
                              mem[[94m_1154 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                              mem[[94m_1154 + 216] = addr(ext_call.return_data[0])
                              mem[[94m_1154 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                              mem[[94m_1154 + 280] = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= [94ms
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                              continue 
                          require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1154 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 142] = ext_call.return_data[0]
                          mem[[94m_1154 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1154 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1154 + 180] = [94midx
                          mem[[94m_1154 + 106] = 74
                          mem[64] = [94m_1154 + 212
                          mem[[94m_1154 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1154 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1154 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 142] = ext_call.return_data[0]
                          mem[[94m_1154 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= 0:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1154 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1154 + 180] = [94midx
                          mem[[94m_1154 + 106] = 74
                          mem[64] = [94m_1154 + 212
                          mem[[94m_1154 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1154 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1154 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1154 + 280] = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1154 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1154 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1154 + 142] = ext_call.return_data[0]
                      mem[[94m_1154 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1154 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1154 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1154 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1154 + 180] = [94midx
                      mem[[94m_1154 + 106] = 74
                      mem[64] = [94m_1154 + 212
                      mem[[94m_1154 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1154 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1154 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1154 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
              else:
                  require (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600) == 100000
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if not (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0]:
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1149 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1150 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1150 + 32 len mem[[94m_1150]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                              mem[[94m_1149 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1149 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1149 + 142] = ext_call.return_data[0]
                              mem[[94m_1149 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              [94midx = [94midx + 1
                              [94ms = 0
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1149 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1149 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1149 + 142] = ext_call.return_data[0]
                          mem[[94m_1149 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1149 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1149 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1149 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1149 + 180] = [94midx
                          mem[[94m_1149 + 106] = 74
                          mem[64] = [94m_1149 + 212
                          mem[[94m_1149 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1149 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1149 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1149 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1149 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1149 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1149 + 142] = ext_call.return_data[0]
                          mem[[94m_1149 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94midx = [94midx + 1
                          [94ms = 0
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1149 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1149 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1149 + 142] = ext_call.return_data[0]
                      mem[[94m_1149 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1149 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1149 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1149 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1149 + 180] = [94midx
                      mem[[94m_1149 + 106] = 74
                      mem[64] = [94m_1149 + 212
                      mem[[94m_1149 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1149 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1149 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1149 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
                  else:
                      require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] == ext_call.return_data[96]
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1165 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1166 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1166 + 32 len mem[[94m_1166]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                              mem[[94m_1165 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1165 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1165 + 142] = ext_call.return_data[0]
                              mem[[94m_1165 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                                  [94ms = ext_call.return_data[0]
                                  [94ms = [94ms
                                  continue 
                              require ext_code.size(addr(stor6))
                              static call addr(stor6).0x24da7b69 with:
                                      gas gas_remaining wei
                                     args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(addr(stor6))
                              if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 >= [94ms:
                                  call addr(stor6).0x48dc990 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require ext_code.size(addr(stor5))
                                  call addr(stor5).0x7aef5b73 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  if [94midx:
                                      require ext_code.size(addr(stor6))
                                      call addr(stor6).0xeaf53c77 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data[32]), [94midx
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                  stop
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mem[[94m_1165 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                              mem[[94m_1165 + 140] = addr(ext_call.return_data[0])
                              mem[[94m_1165 + 160] = addr(ext_call.return_data[32])
                              mem[[94m_1165 + 180] = [94midx
                              mem[[94m_1165 + 106] = 74
                              mem[64] = [94m_1165 + 212
                              mem[[94m_1165 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                              mem[[94m_1165 + 216] = addr(ext_call.return_data[0])
                              mem[[94m_1165 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                              mem[[94m_1165 + 280] = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= [94ms
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                              continue 
                          require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1165 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 142] = ext_call.return_data[0]
                          mem[[94m_1165 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1165 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1165 + 180] = [94midx
                          mem[[94m_1165 + 106] = 74
                          mem[64] = [94m_1165 + 212
                          mem[[94m_1165 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1165 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1165 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 142] = ext_call.return_data[0]
                          mem[[94m_1165 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= 0:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1165 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1165 + 180] = [94midx
                          mem[[94m_1165 + 106] = 74
                          mem[64] = [94m_1165 + 212
                          mem[[94m_1165 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1165 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1165 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1165 + 280] = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1165 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1165 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1165 + 142] = ext_call.return_data[0]
                      mem[[94m_1165 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1165 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1165 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1165 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1165 + 180] = [94midx
                      mem[[94m_1165 + 106] = 74
                      mem[64] = [94m_1165 + 212
                      mem[[94m_1165 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1165 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1165 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1165 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
          require ext_code.size(addr(stor5))
          call addr(stor5).0x7aef5b73 with:
               gas gas_remaining wei
              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[0] - ext_call.return_data[192]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_call.return_data[0] - ext_call.return_data[192] <= [94ms
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
          [94ms = ext_call.return_data[0]
          [94ms = [94ms - ext_call.return_data[0] + ext_call.return_data[192]
          continue 
  else:
      require 10^18 * _param3 / _param3 == 10^18
      require ext_call.return_data[0] > 0
      require ext_call.return_data[0]
      mem[100] = addr(ext_call.return_data[32])
      require ext_code.size(addr(stor6))
      static call addr(stor6).0xf75ce5d4 with:
              gas gas_remaining wei
             args addr(ext_call.return_data[32])
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = mem[mem[64]]
      [94ms = 0
      [94ms = 0
      [94ms = 10^18 * _param3 / ext_call.return_data[0]
      while [94midx < ext_call.return_data[0]:
          if not [94ms:
              if [94ms > 0:
                  if ext_call.return_data[0] > 0:
                      require 1 <= ext_call.return_data[0]
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xeaf53c77 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[32]), ext_call.return_data[0] - 1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
              stop
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xa72c3520 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[32]), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0x24da7b69 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[32]), [94midx
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xc1ed5a74 with:
                  gas gas_remaining wei
                 args addr(ext_call.return_data[0]), ext_call.return_data[0]
          mem[mem[64] len 224] = ext_call.return_data[0 len 224]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 224
          require ext_call.return_data[64] <= block.timestamp
          require ext_code.size(addr(stor6))
          static call addr(stor6).0xc47ac1ac with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] <= block.timestamp - ext_call.return_data[64] / 24 * 3600:
              require ext_code.size(addr(stor6))
              static call addr(stor6).0xff1b4504 with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x79ade32f with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              [94m_1035 = mem[64]
              mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 34] = addr(ext_call.return_data[0])
              mem[mem[64] + 54] = addr(ext_call.return_data[32])
              mem[mem[64] + 74] = ext_call.return_data[0]
              [94m_1036 = mem[64]
              mem[mem[64]] = 74
              mem[64] = mem[64] + 106
              require ext_code.size(addr(stor5))
              static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[0]), sha3(mem[[94m_1036 + 32 len mem[[94m_1036]])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                      mem[[94m_1035 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1035 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1035 + 142] = ext_call.return_data[0]
                      mem[[94m_1035 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = [94midx + 1
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
                  require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                  require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                  mem[[94m_1035 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                  mem[[94m_1035 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_1035 + 142] = ext_call.return_data[0]
                  mem[[94m_1035 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0x14f07b3c with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                      [94midx = [94midx + 1
                      [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      continue 
                  require ext_code.size(addr(stor6))
                  static call addr(stor6).0x24da7b69 with:
                          gas gas_remaining wei
                         args addr(ext_call.return_data[32]), [94midx
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(stor6))
                  if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require ext_code.size(addr(stor5))
                      call addr(stor5).0x7aef5b73 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if [94midx:
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0xeaf53c77 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                      stop
                  call addr(stor6).0x48dc990 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  mem[[94m_1035 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                  mem[[94m_1035 + 140] = addr(ext_call.return_data[0])
                  mem[[94m_1035 + 160] = addr(ext_call.return_data[32])
                  mem[[94m_1035 + 180] = [94midx
                  mem[[94m_1035 + 106] = 74
                  mem[64] = [94m_1035 + 212
                  mem[[94m_1035 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                  mem[[94m_1035 + 216] = addr(ext_call.return_data[0])
                  mem[[94m_1035 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                  mem[[94m_1035 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  require ext_code.size(addr(stor5))
                  call addr(stor5).0x7aef5b73 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                  [94midx = [94midx + 1
                  [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                  continue 
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                  mem[[94m_1035 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                  mem[[94m_1035 + 110] = addr(ext_call.return_data[0])
                  mem[[94m_1035 + 142] = ext_call.return_data[0]
                  mem[[94m_1035 + 174] = 0
                  require ext_code.size(addr(stor6))
                  call addr(stor6).0x14f07b3c with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94midx = [94midx + 1
                  [94ms = 0
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  continue 
              require 0 <= ext_call.return_data[0]
              require ext_call.return_data[192] <= ext_call.return_data[0]
              mem[[94m_1035 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
              mem[[94m_1035 + 110] = addr(ext_call.return_data[0])
              mem[[94m_1035 + 142] = ext_call.return_data[0]
              mem[[94m_1035 + 174] = 0
              require ext_code.size(addr(stor6))
              call addr(stor6).0x14f07b3c with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  continue 
              require ext_code.size(addr(stor6))
              static call addr(stor6).0x24da7b69 with:
                      gas gas_remaining wei
                     args addr(ext_call.return_data[32]), [94midx
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(stor6))
              if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                  call addr(stor6).0x48dc990 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(stor5))
                  call addr(stor5).0x7aef5b73 with:
                       gas gas_remaining wei
                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if [94midx:
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0xeaf53c77 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  stop
              call addr(stor6).0x48dc990 with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[[94m_1035 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
              mem[[94m_1035 + 140] = addr(ext_call.return_data[0])
              mem[[94m_1035 + 160] = addr(ext_call.return_data[32])
              mem[[94m_1035 + 180] = [94midx
              mem[[94m_1035 + 106] = 74
              mem[64] = [94m_1035 + 212
              mem[[94m_1035 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
              mem[[94m_1035 + 216] = addr(ext_call.return_data[0])
              mem[[94m_1035 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
              mem[[94m_1035 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
          else:
              require block.timestamp - ext_call.return_data[64] / 24 * 3600 <= ext_call.return_data[0]
              if not ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600):
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if not 0 / ext_call.return_data[0]:
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1118 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1119 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1119 + 32 len mem[[94m_1119]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                              mem[[94m_1118 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1118 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1118 + 142] = ext_call.return_data[0]
                              mem[[94m_1118 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              [94midx = [94midx + 1
                              [94ms = 0
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1118 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1118 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1118 + 142] = ext_call.return_data[0]
                          mem[[94m_1118 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1118 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1118 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1118 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1118 + 180] = [94midx
                          mem[[94m_1118 + 106] = 74
                          mem[64] = [94m_1118 + 212
                          mem[[94m_1118 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1118 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1118 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1118 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1118 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1118 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1118 + 142] = ext_call.return_data[0]
                          mem[[94m_1118 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94midx = [94midx + 1
                          [94ms = 0
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1118 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1118 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1118 + 142] = ext_call.return_data[0]
                      mem[[94m_1118 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1118 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1118 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1118 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1118 + 180] = [94midx
                      mem[[94m_1118 + 106] = 74
                      mem[64] = [94m_1118 + 212
                      mem[[94m_1118 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1118 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1118 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1118 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
                  else:
                      require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == ext_call.return_data[96]
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1141 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1142 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1142 + 32 len mem[[94m_1142]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                              mem[[94m_1141 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1141 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1141 + 142] = ext_call.return_data[0]
                              mem[[94m_1141 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                                  [94ms = ext_call.return_data[0]
                                  [94ms = [94ms
                                  continue 
                              require ext_code.size(addr(stor6))
                              static call addr(stor6).0x24da7b69 with:
                                      gas gas_remaining wei
                                     args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(addr(stor6))
                              if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 >= [94ms:
                                  call addr(stor6).0x48dc990 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require ext_code.size(addr(stor5))
                                  call addr(stor5).0x7aef5b73 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  if [94midx:
                                      require ext_code.size(addr(stor6))
                                      call addr(stor6).0xeaf53c77 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data[32]), [94midx
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                  stop
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mem[[94m_1141 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                              mem[[94m_1141 + 140] = addr(ext_call.return_data[0])
                              mem[[94m_1141 + 160] = addr(ext_call.return_data[32])
                              mem[[94m_1141 + 180] = [94midx
                              mem[[94m_1141 + 106] = 74
                              mem[64] = [94m_1141 + 212
                              mem[[94m_1141 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                              mem[[94m_1141 + 216] = addr(ext_call.return_data[0])
                              mem[[94m_1141 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                              mem[[94m_1141 + 280] = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= [94ms
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                              continue 
                          require ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1141 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 142] = ext_call.return_data[0]
                          mem[[94m_1141 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1141 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1141 + 180] = [94midx
                          mem[[94m_1141 + 106] = 74
                          mem[64] = [94m_1141 + 212
                          mem[[94m_1141 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1141 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1141 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 142] = ext_call.return_data[0]
                          mem[[94m_1141 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= 0:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1141 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1141 + 180] = [94midx
                          mem[[94m_1141 + 106] = 74
                          mem[64] = [94m_1141 + 212
                          mem[[94m_1141 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1141 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1141 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1141 + 280] = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000 <= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (ext_call.return_data[96] * 0 / ext_call.return_data[0] / 100000)
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1141 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1141 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1141 + 142] = ext_call.return_data[0]
                      mem[[94m_1141 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1141 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1141 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1141 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1141 + 180] = [94midx
                      mem[[94m_1141 + 106] = 74
                      mem[64] = [94m_1141 + 212
                      mem[[94m_1141 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1141 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1141 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1141 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
              else:
                  require (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] - (block.timestamp - ext_call.return_data[64] / 24 * 3600) == 100000
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if not (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0]:
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1136 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1137 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1137 + 32 len mem[[94m_1137]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          if 0 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]:
                              mem[[94m_1136 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1136 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1136 + 142] = ext_call.return_data[0]
                              mem[[94m_1136 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              [94midx = [94midx + 1
                              [94ms = 0
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1136 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1136 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1136 + 142] = ext_call.return_data[0]
                          mem[[94m_1136 + 174] = ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1136 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1136 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1136 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1136 + 180] = [94midx
                          mem[[94m_1136 + 106] = 74
                          mem[64] = [94m_1136 + 212
                          mem[[94m_1136 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1136 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1136 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1136 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if 0 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1136 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1136 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1136 + 142] = ext_call.return_data[0]
                          mem[[94m_1136 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94midx = [94midx + 1
                          [94ms = 0
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1136 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1136 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1136 + 142] = ext_call.return_data[0]
                      mem[[94m_1136 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1136 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1136 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1136 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1136 + 180] = [94midx
                      mem[[94m_1136 + 106] = 74
                      mem[64] = [94m_1136 + 212
                      mem[[94m_1136 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1136 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1136 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1136 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
                  else:
                      require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] == ext_call.return_data[96]
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0xff1b4504 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x79ade32f with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      [94m_1159 = mem[64]
                      mem[mem[64] + 32] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 34] = addr(ext_call.return_data[0])
                      mem[mem[64] + 54] = addr(ext_call.return_data[32])
                      mem[mem[64] + 74] = ext_call.return_data[0]
                      [94m_1160 = mem[64]
                      mem[mem[64]] = 74
                      mem[64] = mem[64] + 106
                      require ext_code.size(addr(stor5))
                      static call addr(stor5).tokensLocked(address of, bytes32 reason) with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[0]), sha3(mem[[94m_1160 + 32 len mem[[94m_1160]])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] >=′ 0:
                          require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]:
                              mem[[94m_1159 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                              mem[[94m_1159 + 110] = addr(ext_call.return_data[0])
                              mem[[94m_1159 + 142] = ext_call.return_data[0]
                              mem[[94m_1159 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0x14f07b3c with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                                  [94ms = ext_call.return_data[0]
                                  [94ms = [94ms
                                  continue 
                              require ext_code.size(addr(stor6))
                              static call addr(stor6).0x24da7b69 with:
                                      gas gas_remaining wei
                                     args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require ext_code.size(addr(stor6))
                              if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 >= [94ms:
                                  call addr(stor6).0x48dc990 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require ext_code.size(addr(stor5))
                                  call addr(stor5).0x7aef5b73 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  if [94midx:
                                      require ext_code.size(addr(stor6))
                                      call addr(stor6).0xeaf53c77 with:
                                           gas gas_remaining wei
                                          args addr(ext_call.return_data[32]), [94midx
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                  stop
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              mem[[94m_1159 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                              mem[[94m_1159 + 140] = addr(ext_call.return_data[0])
                              mem[[94m_1159 + 160] = addr(ext_call.return_data[32])
                              mem[[94m_1159 + 180] = [94midx
                              mem[[94m_1159 + 106] = 74
                              mem[64] = [94m_1159 + 212
                              mem[[94m_1159 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                              mem[[94m_1159 + 216] = addr(ext_call.return_data[0])
                              mem[[94m_1159 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                              mem[[94m_1159 + 280] = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= [94ms
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                              continue 
                          require ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192] <= ext_call.return_data[0]
                          require ext_call.return_data[192] <= (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] + ext_call.return_data[192]
                          mem[[94m_1159 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 142] = ext_call.return_data[0]
                          mem[[94m_1159 + 174] = ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160] - ext_call.return_data[0] - ext_call.return_data[192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= 0:
                              [94midx = [94midx + 1
                              [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1159 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1159 + 180] = [94midx
                          mem[[94m_1159 + 106] = 74
                          mem[64] = [94m_1159 + 212
                          mem[[94m_1159 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1159 + 280] = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160] <= [94ms
                          [94midx = [94midx + 1
                          [94ms = (2 * ext_call.return_data[0]) - ext_call.return_data[96] + (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) + ext_call.return_data[160]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (2 * ext_call.return_data[0]) + ext_call.return_data[96] - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000) - ext_call.return_data[160]
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= ext_call.return_data[0] - ext_call.return_data[192]:
                          mem[[94m_1159 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 110] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 142] = ext_call.return_data[0]
                          mem[[94m_1159 + 174] = 0
                          require ext_code.size(addr(stor6))
                          call addr(stor6).0x14f07b3c with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= 0:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                              [94ms = ext_call.return_data[0]
                              [94ms = [94ms
                              continue 
                          require ext_code.size(addr(stor6))
                          static call addr(stor6).0x24da7b69 with:
                                  gas gas_remaining wei
                                 args addr(ext_call.return_data[32]), [94midx
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(addr(stor6))
                          if ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 >= [94ms:
                              call addr(stor6).0x48dc990 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require ext_code.size(addr(stor5))
                              call addr(stor5).0x7aef5b73 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if [94midx:
                                  require ext_code.size(addr(stor6))
                                  call addr(stor6).0xeaf53c77 with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[32]), [94midx
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                              stop
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[[94m_1159 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 140] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 160] = addr(ext_call.return_data[32])
                          mem[[94m_1159 + 180] = [94midx
                          mem[[94m_1159 + 106] = 74
                          mem[64] = [94m_1159 + 212
                          mem[[94m_1159 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                          mem[[94m_1159 + 216] = addr(ext_call.return_data[0])
                          mem[[94m_1159 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                          mem[[94m_1159 + 280] = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000 <= [94ms
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms - (ext_call.return_data[96] * (100000 * ext_call.return_data[0]) - (100000 * block.timestamp - ext_call.return_data[64] / 24 * 3600) / ext_call.return_data[0] / 100000)
                          continue 
                      require 0 <= ext_call.return_data[0]
                      require ext_call.return_data[192] <= ext_call.return_data[0]
                      mem[[94m_1159 + 106] = 0x14f07b3c00000000000000000000000000000000000000000000000000000000
                      mem[[94m_1159 + 110] = addr(ext_call.return_data[0])
                      mem[[94m_1159 + 142] = ext_call.return_data[0]
                      mem[[94m_1159 + 174] = 0
                      require ext_code.size(addr(stor6))
                      call addr(stor6).0x14f07b3c with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data[0] - ext_call.return_data[192] <= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
                          [94ms = ext_call.return_data[0]
                          [94ms = [94ms
                          continue 
                      require ext_code.size(addr(stor6))
                      static call addr(stor6).0x24da7b69 with:
                              gas gas_remaining wei
                             args addr(ext_call.return_data[32]), [94midx
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(stor6))
                      if ext_call.return_data[0] - ext_call.return_data[192] >= [94ms:
                          call addr(stor6).0x48dc990 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), ext_call.return_data[0], [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(addr(stor5))
                          call addr(stor5).0x7aef5b73 with:
                               gas gas_remaining wei
                              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), [94ms
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if [94midx:
                              require ext_code.size(addr(stor6))
                              call addr(stor6).0xeaf53c77 with:
                                   gas gas_remaining wei
                                  args addr(ext_call.return_data[32]), [94midx
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                          stop
                      call addr(stor6).0x48dc990 with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), ext_call.return_data[0], ext_call.return_data[0] - ext_call.return_data[192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[[94m_1159 + 138] = 0x5557000000000000000000000000000000000000000000000000000000000000
                      mem[[94m_1159 + 140] = addr(ext_call.return_data[0])
                      mem[[94m_1159 + 160] = addr(ext_call.return_data[32])
                      mem[[94m_1159 + 180] = [94midx
                      mem[[94m_1159 + 106] = 74
                      mem[64] = [94m_1159 + 212
                      mem[[94m_1159 + 212] = 0x7aef5b7300000000000000000000000000000000000000000000000000000000
                      mem[[94m_1159 + 216] = addr(ext_call.return_data[0])
                      mem[[94m_1159 + 248] = sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx)
                      mem[[94m_1159 + 280] = ext_call.return_data[0] - ext_call.return_data[192]
          require ext_code.size(addr(stor5))
          call addr(stor5).0x7aef5b73 with:
               gas gas_remaining wei
              args addr(ext_call.return_data[0]), sha3(0, addr(ext_call.return_data[0]), addr(ext_call.return_data[32]), [94midx), ext_call.return_data[0] - ext_call.return_data[192]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_call.return_data[0] - ext_call.return_data[192] <= [94ms
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0] - ext_call.return_data[192]
          [94ms = ext_call.return_data[0]
          [94ms = [94ms - ext_call.return_data[0] + ext_call.return_data[192]
          continue 
  if [94ms > 0:
      if ext_call.return_data[0] > 0:
          require 1 <= ext_call.return_data[0]
          require ext_code.size(addr(stor6))
          call addr(stor6).0xeaf53c77 with:
               gas gas_remaining wei
              args addr(ext_call.return_data[32]), ext_call.return_data[0] - 1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


