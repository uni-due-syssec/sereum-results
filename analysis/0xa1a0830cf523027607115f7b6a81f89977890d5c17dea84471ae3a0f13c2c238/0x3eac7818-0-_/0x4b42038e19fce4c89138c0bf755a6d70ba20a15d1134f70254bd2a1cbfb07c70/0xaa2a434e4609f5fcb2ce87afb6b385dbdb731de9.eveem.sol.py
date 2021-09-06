# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAa2a434e4609F5fCb2CE87AfB6B385dbDb731De9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    stor6
    # storage address 7
    stor7
    # storage address 8
    stor8
    # storage address 9
    stor9
# hash = 0x0a8b7983
# getter = None
# const = None
# payable = True
def unknown0a8b7983(uint256 _param1, addr _param2, uint32 _param3) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp < ext_call.return_data[0]
  require uint8(stor9[_param1].field_104) <= 3
  require not uint8(stor9[_param1].field_104)
  if not stor1[_param1]:
      require stor2[_param1] == _param2
  else:
      require stor1[_param1] == _param2
  uint32(stor9[_param1].field_40) = _param3
  require ext_code.size(stor[_param1])
  call stor[_param1].0xb2f450ca with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_40)
  require ext_call.success
  return 0


# hash = 0x154d66f1
# getter = None
# const = None
# payable = True
def unknown154d66f1(uint256 _param1, addr _param2) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0x1cd61dae with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), _param2
  require ext_call.success


# hash = 0x2420319e
# getter = None
# const = None
# payable = True
def unknown2420319e(uint256 _param1, uint32 _param2) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0xc157f13d with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), _param2
  require ext_call.success


# hash = 0x29f2e907
# getter = None
# const = None
# payable = True
def unknown29f2e907(uint256 _param1, addr _param2, bool _param3) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp < ext_call.return_data[0]
  if _param3:
      if not stor3[_param1]:
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          return 0
      if stor3[_param1] != call.value:
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          return 0
  else:
      if not stor4[_param1]:
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          return 0
      if stor4[_param1] != call.value:
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          return 0
  require uint8(stor9[_param1].field_104) <= 3
  if uint8(stor9[_param1].field_104) == 2:
      call caller with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
      return 0
  if _param3:
      stor1[_param1] = _param2
      stor5[_param1] = stor3[_param1]
      stor3[_param1] = 0
      if not stor1[_param1]:
          uint8(stor9[_param1].field_104) = 1
          require ext_code.size(stor[_param1])
          call stor[_param1].0x1cd61dae with:
               gas gas_remaining - 710 wei
              args uint32(stor9[_param1].field_0), _param2
      else:
          call stor1[_param1] with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          require ext_code.size(stor[_param1])
          call stor[_param1].0xa41f3e3d with:
               gas gas_remaining - 710 wei
              args uint32(stor9[_param1].field_0), addr(_param2), _param3
  else:
      stor2[_param1] = _param2
      stor6[_param1] = stor4[_param1]
      stor4[_param1] = 0
      if not stor2[_param1]:
          uint8(stor9[_param1].field_104) = 1
          require ext_code.size(stor[_param1])
          call stor[_param1].0x1cd61dae with:
               gas gas_remaining - 710 wei
              args uint32(stor9[_param1].field_0), _param2
      else:
          call stor2[_param1] with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
          require ext_code.size(stor[_param1])
          call stor[_param1].0xa41f3e3d with:
               gas gas_remaining - 710 wei
              args uint32(stor9[_param1].field_0), addr(_param2), _param3
  require ext_call.success
  return 1


# hash = 0x3a7fdfe6
# getter = None
# const = None
# payable = True
def unknown3a7fdfe6(uint256 _param1, addr _param2, uint32 _param3, uint8 _param4, bool _param5, uint32 _param6) payable: 
  if _param4 != 5:
      require 10 == _param4
  stor[_param1] = caller
  uint32(stor9[_param1].field_0) = _param6
  uint8(stor9[_param1].field_32) = _param4
  Mask(224, 0, stor9[_param1].field_32) = 0
  uint32(stor9[_param1].field_40) = _param3
  Mask(184, 0, stor9[_param1].field_72) = 0
  require _param4 + 1
  require uint8(stor9[_param1].field_32) - 1
  if _param5:
      require 10 * 10^18 / _param4 + 1 == call.value
  else:
      require 10 * 10^18 / uint8(stor9[_param1].field_32) - 1 == call.value
  if not _param5:
      stor2[_param1] = _param2
      stor3[_param1] = 10 * 10^18 / _param4 + 1
      stor6[_param1] = 10 * 10^18 / uint8(stor9[_param1].field_32) - 1
      stor4[_param1] = 0
  else:
      stor1[_param1] = _param2
      stor4[_param1] = 10 * 10^18 / uint8(stor9[_param1].field_32) - 1
      stor5[_param1] = 10 * 10^18 / _param4 + 1
      stor3[_param1] = 0
  uint8(stor9[_param1].field_104) = 0


# hash = 0x458bdfba
# getter = None
# const = None
# payable = True
def unknown458bdfba(uint256 _param1, bool _param2) payable: 
  require ext_code.size(stor[_param1])
  if not _param2:
      call stor[_param1].0xe37d86d6 with:
           gas gas_remaining - 710 wei
          args uint32(stor9[_param1].field_0), stor4[_param1], _param2
  else:
      call stor[_param1].0xe37d86d6 with:
           gas gas_remaining - 710 wei
          args uint32(stor9[_param1].field_0), stor3[_param1], _param2
  require ext_call.success


# hash = 0x641ee6a3
# getter = None
# const = None
# payable = True
def unknown641ee6a3(uint256 _param1, addr _param2, bool _param3) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0xa41f3e3d with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), addr(_param2), _param3
  require ext_call.success


# hash = 0x6b31d0a8
# getter = None
# const = None
# payable = True
def unknown6b31d0a8(uint256 _param1) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0x8f0be74a with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require ext_call.return_data[28 len 4]
  return ext_call.return_data[28 len 4]


# hash = 0x9017c954
# getter = None
# const = None
# payable = True
def unknown9017c954(uint256 _param1) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0x76f77017 with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0)
  require ext_call.success


# hash = 0xacbbf3ac
# getter = None
# const = None
# payable = True
def unknownacbbf3ac(uint256 _param1) payable: 
  require _param1 + 1
  return (10 * 10^18 / _param1 + 1)


# hash = 0xca12323a
# getter = None
# const = None
# payable = True
def unknownca12323a(uint256 _param1, uint32 _param2) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0x619ec1b3 with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), _param2
  require ext_call.success


# hash = 0xd30d447d
# getter = None
# const = None
# payable = True
def unknownd30d447d(uint256 _param1) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp >= ext_call.return_data[0]
  if block.timestamp >= ext_call.return_data[0] + (24 * 3600):
      require uint8(stor9[_param1].field_104) <= 3
      require uint8(stor9[_param1].field_104) != 2
      require uint8(stor9[_param1].field_32) + 1
      require uint8(stor9[_param1].field_32) - 1
      require ext_code.size(stor[_param1])
      call stor[_param1].0x8f0be74a with:
           gas gas_remaining - 710 wei
      require ext_call.success
      require ext_call.return_data[28 len 4]
      uint32(stor9[_param1].field_72) = uint32(ext_call.return_data[0])
      require uint8(stor9[_param1].field_104) <= 3
      if uint8(stor9[_param1].field_104):
          uint8(stor9[_param1].field_104) = 2
          require uint32(stor9[_param1].field_72)
          if uint32(stor9[_param1].field_72) <= uint32(100 * uint32(stor9[_param1].field_40)):
              require uint32(stor9[_param1].field_72)
              stor7[_param1] = (10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) + 1)
              if 10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) - 1:
                  stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                  call stor1[_param1] with:
                     value stor7[_param1] wei
                       gas 2300 * is_zero(value) wei
                  call stor2[_param1] with:
                     value stor8[_param1] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0x619ec1b3 with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
                  else:
                      stor7[_param1] = 0
                      stor8[_param1] = 0
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0xc157f13d with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
              else:
                  stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                  stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                  call stor1[_param1] with:
                     value stor7[_param1] wei
                       gas 2300 * is_zero(value) wei
                  call stor2[_param1] with:
                     value stor8[_param1] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0x619ec1b3 with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
                  else:
                      stor7[_param1] = 0
                      stor8[_param1] = 0
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0xc157f13d with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
          else:
              require uint32(stor9[_param1].field_72)
              stor8[_param1] = (10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
              if 10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) + 1:
                  stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                  call stor1[_param1] with:
                     value stor7[_param1] wei
                       gas 2300 * is_zero(value) wei
                  call stor2[_param1] with:
                     value stor8[_param1] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0x619ec1b3 with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
                  else:
                      stor7[_param1] = 0
                      stor8[_param1] = 0
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0xc157f13d with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
              else:
                  stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                  stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                  call stor1[_param1] with:
                     value stor7[_param1] wei
                       gas 2300 * is_zero(value) wei
                  call stor2[_param1] with:
                     value stor8[_param1] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0x619ec1b3 with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
                  else:
                      stor7[_param1] = 0
                      stor8[_param1] = 0
                      require ext_code.size(stor[_param1])
                      call stor[_param1].0xc157f13d with:
                           gas gas_remaining - 710 wei
                          args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                      require ext_call.success
                      if eth.balance(this.address) <= 0:
                          stop
                      else:
                          call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                             value eth.balance(this.address) wei
                               gas 2300 * is_zero(value) wei
                          require ext_call.success
                          stop
      else:
          uint8(stor9[_param1].field_104) = 2
          if stor1[_param1]:
              call stor1[_param1] with:
                 value 10 * 10^18 / uint8(stor9[_param1].field_32) + 1 wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
              require ext_code.size(stor[_param1])
              call stor[_param1].0xc157f13d with:
                   gas gas_remaining - 710 wei
                  args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
              require ext_call.success
              if eth.balance(this.address) <= 0:
                  stop
              else:
                  call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  stop
          else:
              call stor2[_param1] with:
                 value 10 * 10^18 / uint8(stor9[_param1].field_32) - 1 wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
              require ext_code.size(stor[_param1])
              call stor[_param1].0xc157f13d with:
                   gas gas_remaining - 710 wei
                  args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
              require ext_call.success
              if eth.balance(this.address) <= 0:
                  stop
              else:
                  call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                     value eth.balance(this.address) wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  stop
  else:
      if 0x7a1ea7cd101d6d1457389591a69c08a168585074 == caller:
          require uint8(stor9[_param1].field_104) <= 3
          require uint8(stor9[_param1].field_104) != 2
          require uint8(stor9[_param1].field_32) + 1
          require uint8(stor9[_param1].field_32) - 1
          require ext_code.size(stor[_param1])
          call stor[_param1].0x8f0be74a with:
               gas gas_remaining - 710 wei
          require ext_call.success
          require ext_call.return_data[28 len 4]
          uint32(stor9[_param1].field_72) = uint32(ext_call.return_data[0])
          require uint8(stor9[_param1].field_104) <= 3
          if uint8(stor9[_param1].field_104):
              uint8(stor9[_param1].field_104) = 2
              require uint32(stor9[_param1].field_72)
              if uint32(stor9[_param1].field_72) <= uint32(100 * uint32(stor9[_param1].field_40)):
                  require uint32(stor9[_param1].field_72)
                  stor7[_param1] = (10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) + 1)
                  if 10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) - 1:
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                  else:
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
              else:
                  require uint32(stor9[_param1].field_72)
                  stor8[_param1] = (10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                  if 10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) + 1:
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                  else:
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
          else:
              uint8(stor9[_param1].field_104) = 2
              if stor1[_param1]:
                  call stor1[_param1] with:
                     value 10 * 10^18 / uint8(stor9[_param1].field_32) + 1 wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require ext_code.size(stor[_param1])
                  call stor[_param1].0xc157f13d with:
                       gas gas_remaining - 710 wei
                      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                  require ext_call.success
                  if eth.balance(this.address) <= 0:
                      stop
                  else:
                      call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                         value eth.balance(this.address) wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      stop
              else:
                  call stor2[_param1] with:
                     value 10 * 10^18 / uint8(stor9[_param1].field_32) - 1 wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require ext_code.size(stor[_param1])
                  call stor[_param1].0xc157f13d with:
                       gas gas_remaining - 710 wei
                      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                  require ext_call.success
                  if eth.balance(this.address) <= 0:
                      stop
                  else:
                      call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                         value eth.balance(this.address) wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      stop
      else:
          require stor[_param1] == caller
          require uint8(stor9[_param1].field_104) <= 3
          require uint8(stor9[_param1].field_104) != 2
          require uint8(stor9[_param1].field_32) + 1
          require uint8(stor9[_param1].field_32) - 1
          require ext_code.size(stor[_param1])
          call stor[_param1].0x8f0be74a with:
               gas gas_remaining - 710 wei
          require ext_call.success
          require ext_call.return_data[28 len 4]
          uint32(stor9[_param1].field_72) = uint32(ext_call.return_data[0])
          require uint8(stor9[_param1].field_104) <= 3
          if uint8(stor9[_param1].field_104):
              uint8(stor9[_param1].field_104) = 2
              require uint32(stor9[_param1].field_72)
              if uint32(stor9[_param1].field_72) <= uint32(100 * uint32(stor9[_param1].field_40)):
                  require uint32(stor9[_param1].field_72)
                  stor7[_param1] = (10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) + 1)
                  if 10 * 10^18 * uint32((100 * uint32(stor9[_param1].field_40)) - uint32(stor9[_param1].field_72)) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) - 1:
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                  else:
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor7[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
              else:
                  require uint32(stor9[_param1].field_72)
                  stor8[_param1] = (10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72)) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                  if 10 * 10^18 * uint32(uint32(stor9[_param1].field_72) - (100 * uint32(stor9[_param1].field_40))) / uint32(stor9[_param1].field_72) <= 10 * 10^18 / uint8(stor9[_param1].field_32) + 1:
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                  else:
                      stor8[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1)
                      stor7[_param1] = (10 * 10^18 / uint8(stor9[_param1].field_32) + 1) + (10 * 10^18 / uint8(stor9[_param1].field_32) - 1) - stor8[_param1]
                      call stor1[_param1] with:
                         value stor7[_param1] wei
                           gas 2300 * is_zero(value) wei
                      call stor2[_param1] with:
                         value stor8[_param1] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0x619ec1b3 with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
                      else:
                          stor7[_param1] = 0
                          stor8[_param1] = 0
                          require ext_code.size(stor[_param1])
                          call stor[_param1].0xc157f13d with:
                               gas gas_remaining - 710 wei
                              args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                          require ext_call.success
                          if eth.balance(this.address) <= 0:
                              stop
                          else:
                              call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                                 value eth.balance(this.address) wei
                                   gas 2300 * is_zero(value) wei
                              require ext_call.success
                              stop
          else:
              uint8(stor9[_param1].field_104) = 2
              if stor1[_param1]:
                  call stor1[_param1] with:
                     value 10 * 10^18 / uint8(stor9[_param1].field_32) + 1 wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require ext_code.size(stor[_param1])
                  call stor[_param1].0xc157f13d with:
                       gas gas_remaining - 710 wei
                      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                  require ext_call.success
                  if eth.balance(this.address) <= 0:
                      stop
                  else:
                      call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                         value eth.balance(this.address) wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      stop
              else:
                  call stor2[_param1] with:
                     value 10 * 10^18 / uint8(stor9[_param1].field_32) - 1 wei
                       gas 2300 * is_zero(value) wei
                  require ext_call.success
                  require ext_code.size(stor[_param1])
                  call stor[_param1].0xc157f13d with:
                       gas gas_remaining - 710 wei
                      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_72)
                  require ext_call.success
                  if eth.balance(this.address) <= 0:
                      stop
                  else:
                      call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
                         value eth.balance(this.address) wei
                           gas 2300 * is_zero(value) wei
                      require ext_call.success
                      stop


# hash = 0xd61c3f09
# getter = None
# const = None
# payable = True
def unknownd61c3f09(uint256 _param1) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].0xb2f450ca with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0), uint32(stor9[_param1].field_40)
  require ext_call.success


# hash = 0xd87789e0
# getter = None
# const = None
# payable = True
def unknownd87789e0(uint256 _param1) payable: 
  require _param1 - 1
  return (10 * 10^18 / _param1 - 1)


# hash = 0xe0c703dc
# getter = None
# const = None
# payable = True
def unknowne0c703dc(uint256 _param1, addr _param2) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp < ext_call.return_data[0]
  require uint8(stor9[_param1].field_104) <= 3
  require not uint8(stor9[_param1].field_104)
  if stor1[_param1]:
      require not stor2[_param1]
      require stor1[_param1] == _param2
      require uint8(stor9[_param1].field_32) + 1
      uint8(stor9[_param1].field_104) = 2
      call stor1[_param1] with:
         value 10 * 10^18 / uint8(stor9[_param1].field_32) + 1 wei
           gas 2300 * is_zero(value) wei
  else:
      if stor2[_param1] == _param2:
          require uint8(stor9[_param1].field_32) - 1
          uint8(stor9[_param1].field_104) = 2
          call stor2[_param1] with:
             value 10 * 10^18 / uint8(stor9[_param1].field_32) - 1 wei
               gas 2300 * is_zero(value) wei
      else:
          require not stor2[_param1]
          require stor1[_param1] == _param2
          require uint8(stor9[_param1].field_32) + 1
          uint8(stor9[_param1].field_104) = 2
          call stor1[_param1] with:
             value 10 * 10^18 / uint8(stor9[_param1].field_32) + 1 wei
               gas 2300 * is_zero(value) wei
  require ext_call.success
  if eth.balance(this.address) > 0:
      call 0x7a1ea7cd101d6d1457389591a69c08a168585074 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
  require ext_code.size(stor[_param1])
  call stor[_param1].0x76f77017 with:
       gas gas_remaining - 710 wei
      args uint32(stor9[_param1].field_0)
  require ext_call.success


# hash = 0xf5471307
# getter = None
# const = None
# payable = True
def unknownf5471307(uint256 _param1, bool _param2) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp >= ext_call.return_data[0] + (24 * 3600)
  require uint8(stor9[_param1].field_104) <= 3
  require uint8(stor9[_param1].field_104) != 2
  if caller != 0x7a1ea7cd101d6d1457389591a69c08a168585074:
      if stor1[_param1] != caller:
          require stor2[_param1] == caller
  uint8(stor9[_param1].field_104) = 2
  if not _param2:
      if stor8[_param1] > 0:
          stor7[_param1] = 0
          call stor1[_param1] with:
             value stor8[_param1] wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
  else:
      if stor7[_param1] > 0:
          stor7[_param1] = 0
          call stor1[_param1] with:
             value stor7[_param1] wei
               gas 2300 * is_zero(value) wei
          require ext_call.success


# hash = 0xfe7a0fb9
# getter = None
# const = None
# payable = True
def unknownfe7a0fb9(uint256 _param1, addr _param2, uint256 _param3, bool _param4) payable: 
  require ext_code.size(stor[_param1])
  call stor[_param1].expireDate() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require block.timestamp < ext_call.return_data[0]
  if _param4:
      require _param2 == stor1[_param1]
  else:
      require _param2 == stor2[_param1]
  require uint8(stor9[_param1].field_104) <= 3
  require uint8(stor9[_param1].field_104) != 2
  require stor1[_param1]
  require stor2[_param1]
  if not _param4:
      stor4[_param1] = _param3
      require ext_code.size(stor[_param1])
      call stor[_param1].0xe37d86d6 with:
           gas gas_remaining - 710 wei
          args uint32(stor9[_param1].field_0), stor4[_param1], _param4
  else:
      stor3[_param1] = _param3
      require ext_code.size(stor[_param1])
      call stor[_param1].0xe37d86d6 with:
           gas gas_remaining - 710 wei
          args uint32(stor9[_param1].field_0), stor3[_param1], _param4
  require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


