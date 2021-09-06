# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x412a694CE7Fccd33ad49Dc63D133189a213D78Bd 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    masterAddress # mask: a s
    # storage address 1
    unknown71a2b7f7
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    unknown01382858
    # storage address 5
    unknowneaf2c477Address # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 9
    unknownc15041d5 # mask: a s
    # storage address 10
    owner # mask: a s
    # storage address 11
    unknowna4c8f302 # mask: a s
    # storage address 13266533587207294913452937957360375543330675926631910040686153131278754095982
    stor1D54 # mask: a s
    # storage address 36573646070267130664335499229633087978925477367044670721849482075549280975728
    stor50DB # mask: a s
    # storage address 46088487022615998054955121338553328501035647402958509823967996202660145563220
    stor65E5 # mask: a s
    # storage address 58633555258402174977409287384061264392285359656226210808360254840632225268852
    stor81A1 # mask: a s
    # storage address 65270374034469294967220200932699974870353173495387108732622930851587599612353
    stor904D # mask: a s
    # storage address 80084422859880547211683076133703299733277748156566366325829078699459944778999
    stor80084422859880547211683076133703299733277748156566366325829078699459944778999
    # storage address 80084422859880547211683076133703299733277748156566366325829078699459944779000
    stor80084422859880547211683076133703299733277748156566366325829078699459944779000
    # storage address 104912549395226180171150298135771341420623246873482962791437719731167110080799
    storE7F2 # mask: a s
# hash = 0x01382858
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 16, 240, 0, ['cd', 4]], 4]]]
# const = None
# payable = True
def unknown01382858(uint16 _param1) payable: 
  require calldata.size - 4 >= 32
  return unknown01382858[Mask(16, 240, _param1)]


# hash = 0x015cb3ff
# getter = ['storage', 256, 0, 11]
# const = None
# payable = True
def unknown015cb3ff() payable: 
  return unknowna4c8f302


# hash = 0x01c09f14
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = True
def unknown01c09f14(addr _param1) payable: 
  require calldata.size - 4 >= 32
  return bool(stor3[_param1])


# hash = 0x04761396
# getter = None
# const = None
# payable = True
def unknown04761396(uint64 _param1) payable: 
  require calldata.size - 4 >= 32
  if Mask(64, 192, _param1) != 0x4d41535441444400000000000000000000000000000000000000000000000000:
      return Mask(64, 192, _param1), 0
  return Mask(64, 192, _param1), masterAddress


# hash = 0x22ce7254
# getter = None
# const = None
# payable = True
def unknown22ce7254(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (ext_call.return_data[12 len 20] == _param1)


# hash = 0x2d4c1152
# getter = None
# const = None
# payable = True
def unknown2d4c1152() payable: 
  if not unknown71a2b7f7.length:
      return 0
  require 1 <= unknown71a2b7f7.length
  require unknown71a2b7f7.length - 1 < unknown71a2b7f7.length
  return bool(unknown71a2b7f7[unknown71a2b7f7.length].field_0), 
         unknown71a2b7f7[unknown71a2b7f7.length].field_0,
         Mask(32, 224, unknown71a2b7f7[unknown71a2b7f7.length].field_0)


# hash = 0x2f54bf6e
# getter = None
# const = None
# payable = True
def isOwner(address _address) payable: 
  require calldata.size - 4 >= 32
  return (owner == _address)


# hash = 0x3a12507f
# getter = ['storage', 160, 0, ['sha3', ['data', 38112658034334528373441310388525495304914655139503976545641167368083101188096, 4]]]
# const = None
# payable = True
def unknown3a12507f() payable: 
  return unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000]


# hash = 0x5187680d
# getter = None
# const = None
# payable = True
def unknown5187680d(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 < unknown71a2b7f7.length
  return _param1, 
         bool(unknown71a2b7f7[_param1].field_0),
         unknown71a2b7f7[_param1].field_256,
         Mask(32, 224, unknown71a2b7f7[_param1].field_512)


# hash = 0x5834e67a
# getter = None
# const = None
# payable = True
def unknown5834e67a(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (ext_call.return_data[12 len 20] == _param1)


# hash = 0x65a8c523
# getter = None
# const = None
# payable = True
def unknown65a8c523(uint16 _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[12 len 20] == caller
  if Mask(16, 240, _param1) != 0x4756000000000000000000000000000000000000000000000000000000000000:
      if Mask(16, 240, _param1) != 0x4d52000000000000000000000000000000000000000000000000000000000000:
          if Mask(16, 240, _param1) != 0x5043000000000000000000000000000000000000000000000000000000000000:
              require Mask(16, 240, _param1) == 0x5443000000000000000000000000000000000000000000000000000000000000
  require ext_code.size(unknown01382858[Mask(16, 240, _param1)])
  call unknown01382858[Mask(16, 240, _param1)].upgradeTo(address newImplementation) with:
       gas gas_remaining wei
      args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x71a2b7f7
# getter = ['struct', ['loc', 1]]
# const = None
# payable = True
def unknown71a2b7f7(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 < unknown71a2b7f7.length
  return bool(unknown71a2b7f7[_param1].field_0), 
         unknown71a2b7f7[_param1].field_256,
         Mask(32, 224, unknown71a2b7f7[_param1].field_512)


# hash = 0x78ddbed4
# getter = None
# const = None
# payable = True
def unknown78ddbed4(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require 1 == bool(stor3[caller])
  unknowna4c8f302 = _param1


# hash = 0x872f1eb3
# getter = None
# const = None
# payable = True
def unknown872f1eb3() payable: 
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Not authorized'
  if unknown01382858[0x5031000000000000000000000000000000000000000000000000000000000000] != caller:
      require caller == unknown01382858[0x4756000000000000000000000000000000000000000000000000000000000000]
  unknown71a2b7f7.length++
  unknown71a2b7f7[unknown71a2b7f7.length].field_0 = 1
  storB10E[stor1.length] = block.timestamp
  storB10E[stor1.length].field_0 = 0
  storB10E[stor1.length].field_256 = 0
  require ext_code.size(stor65E5)
  call stor65E5.0xd8ea6b08 with:
       gas gas_remaining wei
      args unknowna4c8f302
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  stor6 = stor50DB
  require ext_code.size(stor50DB)
  call stor50DB.0x38021671 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 10]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x8dd7ff9a
# getter = None
# const = None
# payable = True
def unknown8dd7ff9a(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if uint8(stor9.field_160):
      revert with 0, 'Reentrant call.'
  uint8(stor9.field_160) = 1
  require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
  static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0xfd3e44d5 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
  static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x3277be96 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknown71a2b7f7.length:
      require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
      static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x371e6e12 with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if Mask(32, 224, ext_call.return_data[0]) == 0x434f560000000000000000000000000000000000000000000000000000000000:
          require ext_code.size(unknown01382858[0x5154000000000000000000000000000000000000000000000000000000000000])
          call unknown01382858[0x5154000000000000000000000000000000000000000000000000000000000000].0xf4136f7f with:
               gas gas_remaining wei
              args ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          if Mask(32, 224, ext_call.return_data[0]) == 0x434c410000000000000000000000000000000000000000000000000000000000:
              stor7 = unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000]
              require ext_code.size(unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000])
              call unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000].0x7f6715c9 with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              if Mask(32, 224, ext_call.return_data[0]) == 0x4d43524600000000000000000000000000000000000000000000000000000000:
                  require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
                  static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x702ddaab with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] + uint64(ext_call.return_data[0]) >= uint64(ext_call.return_data[0])
                  if ext_call.return_data[0] + uint64(ext_call.return_data[0]) < block.timestamp:
                      require ext_code.size(unknown01382858[0x4d43000000000000000000000000000000000000000000000000000000000000])
                      call unknown01382858[0x4d43000000000000000000000000000000000000000000000000000000000000].0x80f34275 with:
                           gas gas_remaining wei
                          args uint64(ext_call.return_data[0])
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
              else:
                  if Mask(32, 224, ext_call.return_data[0]) == 0x554c540000000000000000000000000000000000000000000000000000000000:
                      require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
                      static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x6549ff58 with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] + uint64(ext_call.return_data[0]) >= uint64(ext_call.return_data[0])
                      if ext_call.return_data[0] + uint64(ext_call.return_data[0]) < block.timestamp:
                          require ext_code.size(unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000])
                          call unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000].0xf720036c with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
  else:
      require 1 <= unknown71a2b7f7.length
      require unknown71a2b7f7.length - 1 < unknown71a2b7f7.length
      if bool(unknown71a2b7f7[unknown71a2b7f7.length].field_0) != 1:
          require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
          static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x371e6e12 with:
                  gas gas_remaining wei
                 args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if Mask(32, 224, ext_call.return_data[0]) == 0x434f560000000000000000000000000000000000000000000000000000000000:
              require ext_code.size(unknown01382858[0x5154000000000000000000000000000000000000000000000000000000000000])
              call unknown01382858[0x5154000000000000000000000000000000000000000000000000000000000000].0xf4136f7f with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              if Mask(32, 224, ext_call.return_data[0]) == 0x434c410000000000000000000000000000000000000000000000000000000000:
                  stor7 = unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000]
                  require ext_code.size(unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000])
                  call unknown01382858[0x4352000000000000000000000000000000000000000000000000000000000000].0x7f6715c9 with:
                       gas gas_remaining wei
                      args ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  if Mask(32, 224, ext_call.return_data[0]) == 0x4d43524600000000000000000000000000000000000000000000000000000000:
                      require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
                      static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x702ddaab with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] + uint64(ext_call.return_data[0]) >= uint64(ext_call.return_data[0])
                      if ext_call.return_data[0] + uint64(ext_call.return_data[0]) < block.timestamp:
                          require ext_code.size(unknown01382858[0x4d43000000000000000000000000000000000000000000000000000000000000])
                          call unknown01382858[0x4d43000000000000000000000000000000000000000000000000000000000000].0x80f34275 with:
                               gas gas_remaining wei
                              args uint64(ext_call.return_data[0])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                  else:
                      if Mask(32, 224, ext_call.return_data[0]) == 0x554c540000000000000000000000000000000000000000000000000000000000:
                          require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
                          static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x6549ff58 with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_call.return_data[0] + uint64(ext_call.return_data[0]) >= uint64(ext_call.return_data[0])
                          if ext_call.return_data[0] + uint64(ext_call.return_data[0]) < block.timestamp:
                              require ext_code.size(unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000])
                              call unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000].0xf720036c with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
      else:
          if Mask(32, 224, ext_call.return_data[0]) == 0x4550000000000000000000000000000000000000000000000000000000000000:
              require unknowna4c8f302 + uint64(ext_call.return_data[0]) >= uint64(ext_call.return_data[0])
              if unknowna4c8f302 + uint64(ext_call.return_data[0]) < block.timestamp:
                  if unknown71a2b7f7.length:
                      require 1 <= unknown71a2b7f7.length
                      require unknown71a2b7f7.length - 1 < unknown71a2b7f7.length
                      if Mask(32, 224, unknown71a2b7f7[unknown71a2b7f7.length].field_0) == 0x4142000000000000000000000000000000000000000000000000000000000000:
                          if unknown01382858[0x5031000000000000000000000000000000000000000000000000000000000000] != caller:
                              require caller == unknown01382858[0x4756000000000000000000000000000000000000000000000000000000000000]
                          unknown71a2b7f7.length++
                          unknown71a2b7f7[unknown71a2b7f7.length].field_0 = 0
                          storB10E[stor1.length] = block.timestamp
                          storB10E[stor1.length].field_0 = 0
                          storB10E[stor1.length].field_256 = 0
                          stor6 = stor50DB
                          require ext_code.size(stor50DB)
                          call stor50DB.0x75a0f521 with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require ext_code.size(stor6)
                          call stor6.0x9755fafe with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
  if Mask(32, 224, ext_call.return_data[0]):
      require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
      call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x61b6c00f with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  uint8(stor9.field_160) = 0


# hash = 0x8f16c41c
# getter = None
# const = None
# payable = True
def unknown8f16c41c(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if bool(stor3[addr(_param1)]) != 1:
      return 0
  return 1


# hash = 0x92b0a156
# getter = None
# const = None
# payable = True
def unknown92b0a156(uint16 _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[12 len 20] == caller
  require _param2
  if Mask(16, 240, _param1) == 0x5154000000000000000000000000000000000000000000000000000000000000:
      require ext_code.size(stor1D54)
      call stor1D54.0xe2629974 with:
           gas gas_remaining wei
          args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      if Mask(16, 240, _param1) != 0x5446000000000000000000000000000000000000000000000000000000000000:
          if Mask(16, 240, _param1) != 0x434c000000000000000000000000000000000000000000000000000000000000:
              if Mask(16, 240, _param1) != 0x4352000000000000000000000000000000000000000000000000000000000000:
                  if Mask(16, 240, _param1) != 0x5031000000000000000000000000000000000000000000000000000000000000:
                      if Mask(16, 240, _param1) != 0x5032000000000000000000000000000000000000000000000000000000000000:
                          if Mask(16, 240, _param1) != 0x4d43000000000000000000000000000000000000000000000000000000000000:
                              revert with 0, 'Not upgradable contract'
      if Mask(16, 240, _param1) == 0x5154000000000000000000000000000000000000000000000000000000000000:
          require ext_code.size(stor1D54)
          call stor1D54.0xe2629974 with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          if Mask(16, 240, _param1) != 0x4352000000000000000000000000000000000000000000000000000000000000:
              if Mask(16, 240, _param1) == 0x5031000000000000000000000000000000000000000000000000000000000000:
                  require ext_code.size(stor65E5)
                  call stor65E5.0x66fd551d with:
                       gas gas_remaining wei
                      args _param2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  if Mask(16, 240, _param1) == 0x5032000000000000000000000000000000000000000000000000000000000000:
                      require ext_code.size(storE7F2)
                      call storE7F2.0x6dce9b3d with:
                           gas gas_remaining wei
                          args _param2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
          else:
              require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
              call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].addToWhitelist(address user) with:
                   gas gas_remaining wei
                  args _param2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
              call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].removeFromWhitelist(address user) with:
                   gas gas_remaining wei
                  args stor81A1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              stor7 = stor81A1
              require ext_code.size(stor81A1)
              call stor81A1.upgrade(address implementation) with:
                   gas gas_remaining wei
                  args _param2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
  stor3[stor4[Mask(16, 240, _param1)]] = 0
  unknown01382858[Mask(16, 240, _param1)] = _param2
  require ext_code.size(masterAddress)
  static call masterAddress.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if masterAddress != this.address:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Neither master nor Authorised'
  [94midx = 0
  while [94midx < stor2.length:
      mem[32] = 4
      addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
      mem[96] = 0xd46655f400000000000000000000000000000000000000000000000000000000
      mem[100] = masterAddress
      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xd46655f4 with:
           gas gas_remaining wei
          args masterAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < stor2.length
      require [94midx < stor2.length
      if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
          mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
          mem[32] = 4
          mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
          mem[100] = masterAddress
          require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
          call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
               gas gas_remaining wei
              args masterAddress
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          require [94midx < stor2.length
          if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
              mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
              mem[32] = 4
              mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
              mem[100] = masterAddress
              require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
              call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                   gas gas_remaining wei
                  args masterAddress
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < stor2.length
              if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                  mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                  mem[32] = 4
                  mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                  mem[100] = masterAddress
                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                       gas gas_remaining wei
                      args masterAddress
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  mem[0] = 2
                  if 0x5443000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                      require [94midx < stor2.length
                      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                      mem[32] = 4
                      mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                      mem[100] = masterAddress
                      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                           gas gas_remaining wei
                          args masterAddress
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  stor3[this.address] = 0
  stor3[stor0] = 1
  [94midx = 0
  while [94midx < stor2.length:
      stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
      mem[32] = 4
      addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
      mem[96] = 0xea9c98400000000000000000000000000000000000000000000000000000000
      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xea9c984 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 


# hash = 0x9d76ea58
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def tokenAddress() payable: 
  return unknowneaf2c477Address


# hash = 0xa230c524
# getter = None
# const = None
# payable = True
def isMember(address _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(unknown01382858[0x4d52000000000000000000000000000000000000000000000000000000000000])
  static call unknown01382858[0x4d52000000000000000000000000000000000000000000000000000000000000].0x505ef22f with:
          gas gas_remaining wei
         args addr(_param1), 2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0xa4c8f302
# getter = ['storage', 256, 0, 11]
# const = None
# payable = True
def unknowna4c8f302() payable: 
  return unknowna4c8f302


# hash = 0xa97ea794
# getter = None
# const = None
# payable = True
def unknowna97ea794(array _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = 0
  require caller == owner
  require not unknownc15041d5
  if _param1.length != stor2.length:
      revert with 0, 'array length not same'
  else:
      unknownc15041d5 = 1
      require 14 < _param1.length
      require ext_code.size(mem[588 len 20])
      static call mem[588 len 20].0xf17a3bec with:
              gas gas_remaining wei
      mem[(32 * _param1.length) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          [94midx = 0
          while [94midx < stor2.length:
              require [94midx < _param1.length
              require mem[(32 * [94midx) + 140 len 20]
              require [94midx < stor2.length
              if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                  if not addr(ext_call.return_data[0]):
                      require [94midx < stor2.length
                      require [94midx < _param1.length
                      [94m_180 = mem[(32 * [94midx) + 128]
                      mem[(32 * _param1.length) + 128 len 1237] = 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f
                      mem[(32 * _param1.length) + 1365] = addr([94m_180)
                      create contract with 0 wei
                                      code: 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f, addr(_180)
                      if not create.new_address:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = addr(create.new_address)
                          mem[0] = addr(create.new_address)
                          mem[32] = 3
                          stor3[addr(create.new_address)] = 1
                          if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x4d52000000000000000000000000000000000000000000000000000000000000:
                              [94midx = [94midx + 1
                              continue 
                          else:
                              mem[0] = 0x5446000000000000000000000000000000000000000000000000000000000000
                              mem[32] = 4
                              mem[(32 * _param1.length) + 128] = 0x1b5c6ded00000000000000000000000000000000000000000000000000000000
                              mem[(32 * _param1.length) + 132] = owner
                              mem[(32 * _param1.length) + 164] = stor904D
                              require ext_code.size(addr(create.new_address))
                              call addr(create.new_address).0x1b5c6ded with:
                                   gas gas_remaining wei
                                  args owner, stor904D
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  [94midx = [94midx + 1
                                  continue 
                  else:
                      require [94midx < _param1.length
                      require [94midx < stor2.length
                      unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = mem[(32 * [94midx) + 140 len 20]
                      mem[0] = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                      mem[32] = 3
                      stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
                      [94midx = [94midx + 1
                      continue 
              else:
                  require [94midx < stor2.length
                  if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                      if not addr(ext_call.return_data[0]):
                          require [94midx < stor2.length
                          require [94midx < _param1.length
                          [94m_194 = mem[(32 * [94midx) + 128]
                          mem[(32 * _param1.length) + 128 len 1237] = 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f
                          mem[(32 * _param1.length) + 1365] = addr([94m_194)
                          create contract with 0 wei
                                          code: 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f, addr(_194)
                          if not create.new_address:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = addr(create.new_address)
                              mem[0] = addr(create.new_address)
                              mem[32] = 3
                              stor3[addr(create.new_address)] = 1
                              if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x4d52000000000000000000000000000000000000000000000000000000000000:
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  mem[0] = 0x5446000000000000000000000000000000000000000000000000000000000000
                                  mem[32] = 4
                                  mem[(32 * _param1.length) + 128] = 0x1b5c6ded00000000000000000000000000000000000000000000000000000000
                                  mem[(32 * _param1.length) + 132] = owner
                                  mem[(32 * _param1.length) + 164] = stor904D
                                  require ext_code.size(addr(create.new_address))
                                  call addr(create.new_address).0x1b5c6ded with:
                                       gas gas_remaining wei
                                      args owner, stor904D
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      [94midx = [94midx + 1
                                      continue 
                      else:
                          require [94midx < _param1.length
                          require [94midx < stor2.length
                          unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = mem[(32 * [94midx) + 140 len 20]
                          mem[0] = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                          mem[32] = 3
                          stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
                          [94midx = [94midx + 1
                          continue 
                  else:
                      require [94midx < stor2.length
                      if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                          if not addr(ext_call.return_data[0]):
                              require [94midx < stor2.length
                              require [94midx < _param1.length
                              [94m_210 = mem[(32 * [94midx) + 128]
                              mem[(32 * _param1.length) + 128 len 1237] = 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f
                              mem[(32 * _param1.length) + 1365] = addr([94m_210)
                              create contract with 0 wei
                                              code: 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f, addr(_210)
                              if not create.new_address:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = addr(create.new_address)
                                  mem[0] = addr(create.new_address)
                                  mem[32] = 3
                                  stor3[addr(create.new_address)] = 1
                                  if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x4d52000000000000000000000000000000000000000000000000000000000000:
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      mem[0] = 0x5446000000000000000000000000000000000000000000000000000000000000
                                      mem[32] = 4
                                      mem[(32 * _param1.length) + 128] = 0x1b5c6ded00000000000000000000000000000000000000000000000000000000
                                      mem[(32 * _param1.length) + 132] = owner
                                      mem[(32 * _param1.length) + 164] = stor904D
                                      require ext_code.size(addr(create.new_address))
                                      call addr(create.new_address).0x1b5c6ded with:
                                           gas gas_remaining wei
                                          args owner, stor904D
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          [94midx = [94midx + 1
                                          continue 
                          else:
                              require [94midx < _param1.length
                              require [94midx < stor2.length
                              unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = mem[(32 * [94midx) + 140 len 20]
                              mem[0] = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                              mem[32] = 3
                              stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
                              [94midx = [94midx + 1
                              continue 
                      else:
                          require [94midx < stor2.length
                          if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x5443000000000000000000000000000000000000000000000000000000000000:
                              require [94midx < _param1.length
                              require [94midx < stor2.length
                              mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                              mem[32] = 4
                              unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = mem[(32 * [94midx) + 140 len 20]
                              [94midx = [94midx + 1
                              continue 
                          else:
                              if not addr(ext_call.return_data[0]):
                                  require [94midx < stor2.length
                                  require [94midx < _param1.length
                                  [94m_233 = mem[(32 * [94midx) + 128]
                                  mem[(32 * _param1.length) + 128 len 1237] = 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f
                                  mem[(32 * _param1.length) + 1365] = addr([94m_233)
                                  create contract with 0 wei
                                                  code: 0xfe608060405234801561001057600080fd5b506040516020806104d58339810180604052602081101561003057600080fd5b505161004233610057602090811b901c565b6100518161008c60201b60201c565b50610149565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b600061009c61010460201b60201c565b9050816001600160a01b0316816001600160a01b031614156100bd57600080fd5b6100cc8261012760201b60201c565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b60008060405180806104b360229139604051908190036022019020549392505050565b600060405180806104b360229139604051908190036022019020929092555050565b61035b806101586000396000f3fe60806040526004361061003f5760003560e01c8063025313a2146100835780633659cfe6146100b45780635c60da1b146100e9578063f1739cae146100fe575b6000610049610131565b90506001600160a01b03811661005e57600080fd5b60405136600082376000803683855af43d806000843e81801561007f578184f35b8184fd5b34801561008f57600080fd5b50610098610154565b604080516001600160a01b039092168252519081900360200190f35b3480156100c057600080fd5b506100e7600480360360208110156100d757600080fd5b50356001600160a01b031661018a565b005b3480156100f557600080fd5b50610098610131565b34801561010a57600080fd5b506100e76004803603602081101561012157600080fd5b50356001600160a01b03166101bb565b600080604051808061030e60229139604051908190036022019020549392505050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e657200000000000000815290519081900360190190205490565b610192610154565b6001600160a01b0316336001600160a01b0316146101af57600080fd5b6101b88161024a565b50565b6101c3610154565b6001600160a01b0316336001600160a01b0316146101e057600080fd5b6001600160a01b0381166101f357600080fd5b6101fc816102b6565b7f5a3e66efaa1e445ebd894728a69d6959842ea1e97bd79b892797106e270efcd9610225610154565b604080516001600160a01b03928316815291841660208301528051918290030190a150565b6000610254610131565b9050816001600160a01b0316816001600160a01b0316141561027557600080fd5b61027e826102eb565b6040516001600160a01b038316907fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b90600090a25050565b604080517f6f72672e676f76626c6f636b732e70726f78792e6f776e6572000000000000008152905190819003601901902055565b6000604051808061030e6022913960405190819003602201902092909255505056fe6f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f6ea165627a7a723058206870606a08d39cd582e65c880d54753c2c1a89f81be1bb59b117f3baa536266800296f72672e676f76626c6f636b732e70726f78792e696d706c656d656e746174696f, addr(_233)
                                  if not create.new_address:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = addr(create.new_address)
                                      mem[0] = addr(create.new_address)
                                      mem[32] = 3
                                      stor3[addr(create.new_address)] = 1
                                      if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x4d52000000000000000000000000000000000000000000000000000000000000:
                                          [94midx = [94midx + 1
                                          continue 
                                      else:
                                          mem[0] = 0x5446000000000000000000000000000000000000000000000000000000000000
                                          mem[32] = 4
                                          mem[(32 * _param1.length) + 128] = 0x1b5c6ded00000000000000000000000000000000000000000000000000000000
                                          mem[(32 * _param1.length) + 132] = owner
                                          mem[(32 * _param1.length) + 164] = stor904D
                                          require ext_code.size(addr(create.new_address))
                                          call addr(create.new_address).0x1b5c6ded with:
                                               gas gas_remaining wei
                                              args owner, stor904D
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                              else:
                                  require [94midx < _param1.length
                                  require [94midx < stor2.length
                                  unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240] = mem[(32 * [94midx) + 140 len 20]
                                  mem[0] = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                                  mem[32] = 3
                                  stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
                                  [94midx = [94midx + 1
                                  continue 
          if addr(ext_call.return_data[0]):
              stop
          else:
              require ext_code.size(this.address)
              static call this.address.0xc15041d5 with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  require ext_call.return_data[0]
                  if this.address == this.address:
                      [94ms = 0
                      while [94ms < stor2.length:
                          mem[32] = 4
                          addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240]
                          mem[(32 * _param1.length) + 128] = 0xd46655f400000000000000000000000000000000000000000000000000000000
                          mem[(32 * _param1.length) + 132] = this.address
                          require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                          call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].0xd46655f4 with:
                               gas gas_remaining wei
                              args this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require [94ms < stor2.length
                              if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240:
                                  require [94ms < stor2.length
                                  mem[0] = stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240
                                  mem[32] = 4
                                  mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                  mem[(32 * _param1.length) + 132] = this.address
                                  require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                                  call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].transferProxyOwnership(address newOwner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      [94ms = [94ms + 1
                                      continue 
                              else:
                                  require [94ms < stor2.length
                                  if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240:
                                      require [94ms < stor2.length
                                      mem[0] = stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240
                                      mem[32] = 4
                                      mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                      mem[(32 * _param1.length) + 132] = this.address
                                      require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                                      call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].transferProxyOwnership(address newOwner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          [94ms = [94ms + 1
                                          continue 
                                  else:
                                      require [94ms < stor2.length
                                      if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240:
                                          require [94ms < stor2.length
                                          mem[0] = stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240
                                          mem[32] = 4
                                          mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                          mem[(32 * _param1.length) + 132] = this.address
                                          require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                                          call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].transferProxyOwnership(address newOwner) with:
                                               gas gas_remaining wei
                                              args this.address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              [94ms = [94ms + 1
                                              continue 
                                      else:
                                          require [94ms < stor2.length
                                          mem[0] = 2
                                          if stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240 != 0x5443000000000000000000000000000000000000000000000000000000000000:
                                              [94ms = [94ms + 1
                                              continue 
                                          else:
                                              require [94ms < stor2.length
                                              mem[0] = stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240
                                              mem[32] = 4
                                              mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                              mem[(32 * _param1.length) + 132] = this.address
                                              require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                                              call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].transferProxyOwnership(address newOwner) with:
                                                   gas gas_remaining wei
                                                  args this.address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  [94ms = [94ms + 1
                                                  continue 
                      stor3[this.address] = 0
                      stor3[this.address] = 1
                      [94ms = 0
                      while [94ms < stor2.length:
                          stor3[stor4[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240]] = 1
                          mem[0] = stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240
                          mem[32] = 4
                          addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240]
                          mem[(32 * _param1.length) + 128] = 0xea9c98400000000000000000000000000000000000000000000000000000000
                          require ext_code.size(unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240])
                          call unknown01382858[stor2[0.0625 / [94ms] / 256^(2 * [94ms % 16) << 240].0xea9c984 with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              [94ms = [94ms + 1
                              continue 
                      require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
                      call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].changeOperator(address newOperator) with:
                           gas gas_remaining wei
                          args unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
                          call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].addToWhitelist(address user) with:
                               gas gas_remaining wei
                              args owner
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              stop
                  else:
                      require ext_code.size(masterAddress)
                      static call masterAddress.0x1382858 with:
                              gas gas_remaining wei
                             args 0x4756000000000000000000000000000000000000000000000000000000000000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if addr(ext_call.return_data[0]) != caller:
                              revert with 0, 'Neither master nor Authorised'
                          else:
                              [94midx = 0
                              while [94midx < stor2.length:
                                  mem[32] = 4
                                  addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                                  mem[(32 * _param1.length) + 128] = 0xd46655f400000000000000000000000000000000000000000000000000000000
                                  mem[(32 * _param1.length) + 132] = this.address
                                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xd46655f4 with:
                                       gas gas_remaining wei
                                      args this.address
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require [94midx < stor2.length
                                      if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                                          require [94midx < stor2.length
                                          mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                                          mem[32] = 4
                                          mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                          mem[(32 * _param1.length) + 132] = this.address
                                          require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                          call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                                               gas gas_remaining wei
                                              args this.address
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                                      else:
                                          require [94midx < stor2.length
                                          if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                                              require [94midx < stor2.length
                                              mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                                              mem[32] = 4
                                              mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                              mem[(32 * _param1.length) + 132] = this.address
                                              require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                              call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                                                   gas gas_remaining wei
                                                  args this.address
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  [94midx = [94midx + 1
                                                  continue 
                                          else:
                                              require [94midx < stor2.length
                                              if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                                                  require [94midx < stor2.length
                                                  mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                                                  mem[32] = 4
                                                  mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                                  mem[(32 * _param1.length) + 132] = this.address
                                                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                                                       gas gas_remaining wei
                                                      args this.address
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require [94midx < stor2.length
                                                  mem[0] = 2
                                                  if stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240 != 0x5443000000000000000000000000000000000000000000000000000000000000:
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require [94midx < stor2.length
                                                      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                                                      mem[32] = 4
                                                      mem[(32 * _param1.length) + 128] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                                                      mem[(32 * _param1.length) + 132] = this.address
                                                      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                                      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                                                           gas gas_remaining wei
                                                          args this.address
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          [94midx = [94midx + 1
                                                          continue 
                              stor3[this.address] = 0
                              stor3[this.address] = 1
                              [94midx = 0
                              while [94midx < stor2.length:
                                  stor3[stor4[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]] = 1
                                  mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                                  mem[32] = 4
                                  addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
                                  mem[(32 * _param1.length) + 128] = 0xea9c98400000000000000000000000000000000000000000000000000000000
                                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xea9c984 with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      [94midx = [94midx + 1
                                      continue 
                              require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
                              call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].changeOperator(address newOperator) with:
                                   gas gas_remaining wei
                                  args unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000])
                                  call unknown01382858[0x5443000000000000000000000000000000000000000000000000000000000000].addToWhitelist(address user) with:
                                       gas gas_remaining wei
                                      args owner
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      stop


# hash = 0xad4cc43e
# getter = None
# const = None
# payable = True
def unknownad4cc43e(uint64 _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Not authorized'
  require _param2
  if Mask(64, 192, _param1) != 0x4d41535441444400000000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid param code'
  require ext_code.size(_param2)
  static call _param2.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if _param2 != this.address:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Neither master nor Authorised'
  [94midx = 0
  while [94midx < stor2.length:
      mem[32] = 4
      addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
      mem[96] = 0xd46655f400000000000000000000000000000000000000000000000000000000
      mem[100] = _param2
      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xd46655f4 with:
           gas gas_remaining wei
          args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < stor2.length
      require [94midx < stor2.length
      if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
          mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
          mem[32] = 4
          mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
          mem[100] = _param2
          require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
          call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          require [94midx < stor2.length
          if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
              mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
              mem[32] = 4
              mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
              mem[100] = _param2
              require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
              call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                   gas gas_remaining wei
                  args _param2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < stor2.length
              if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                  mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                  mem[32] = 4
                  mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                  mem[100] = _param2
                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                       gas gas_remaining wei
                      args _param2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  mem[0] = 2
                  if 0x5443000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                      require [94midx < stor2.length
                      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                      mem[32] = 4
                      mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                      mem[100] = _param2
                      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                           gas gas_remaining wei
                          args _param2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  stor3[this.address] = 0
  stor3[_param2] = 1


# hash = 0xbf1f2819
# getter = None
# const = None
# payable = True
def unknownbf1f2819(uint64 _param1) payable: 
  require calldata.size - 4 >= 32
  if Mask(64, 192, _param1) == 0x4d5357414c4c4554000000000000000000000000000000000000000000000000:
      require ext_code.size(unknown01382858[0x5444000000000000000000000000000000000000000000000000000000000000])
      static call unknown01382858[0x5444000000000000000000000000000000000000000000000000000000000000].walletAddress() with:
              gas gas_remaining wei
  else:
      if Mask(64, 192, _param1) == 'MCRNOTA' << 200:
          require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
          static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x428dfd38 with:
                  gas gas_remaining wei
      else:
          if Mask(64, 192, _param1) == 0x4441494645454400000000000000000000000000000000000000000000000000:
              require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
              static call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0xf0f9f254 with:
                      gas gas_remaining wei
          else:
              if Mask(64, 192, _param1) == 0x554e495357414444000000000000000000000000000000000000000000000000:
                  require ext_code.size(unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000])
                  static call unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000].0x3655ac3c with:
                          gas gas_remaining wei
              else:
                  if Mask(64, 192, _param1) == 0x4f574e4552000000000000000000000000000000000000000000000000000000:
                      return Mask(64, 192, _param1), owner
                  if Mask(64, 192, _param1) == 0x51554f4155544800000000000000000000000000000000000000000000000000:
                      require ext_code.size(unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000])
                      static call unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000].0xe2c2a5bb with:
                              gas gas_remaining wei
                  else:
                      if Mask(64, 192, _param1) != 0x4b59434155544800000000000000000000000000000000000000000000000000:
                          return Mask(64, 192, _param1), 0
                      require ext_code.size(unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000])
                      static call unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000].0x84434b9f with:
                              gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return Mask(64, 192, _param1), addr(ext_call.return_data[0])


# hash = 0xc15041d5
# getter = ['bool', ['storage', 8, 168, 9]]
# const = None
# payable = True
def unknownc15041d5() payable: 
  return bool(unknownc15041d5)


# hash = 0xc74de065
# getter = None
# const = None
# payable = True
def unknownc74de065() payable: 
  mem[96] = stor2.length
  if not stor2.length:
      mem[(32 * stor2.length) + 128] = stor2.length
      mem[64] = (64 * stor2.length) + 160
  else:
      mem[128 len 32 * stor2.length] = code.data[15080 len 32 * stor2.length]
      mem[(32 * stor2.length) + 128] = stor2.length
      mem[64] = (64 * stor2.length) + 160
      mem[(32 * stor2.length) + 160 len 32 * stor2.length] = code.data[15080 len 32 * stor2.length]
  [94midx = 0
  while [94midx < stor2.length:
      require [94midx < stor2.length
      mem[(32 * [94midx) + 128] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
      require [94midx < stor2.length
      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
      mem[32] = 4
      require [94midx < mem[(32 * stor2.length) + 128]
      mem[(32 * [94midx) + (32 * stor2.length) + 160] = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
      [94midx = [94midx + 1
      continue 
  mem[(64 * stor2.length) + 160] = 64
  mem[(64 * stor2.length) + 224] = stor2.length
  [94ms = 0
  while stor2.length < 32 * stor2.length:
      mem[stor2.length + mem[64] + 96] = mem[stor2.length + 128]
      [94ms = stor2.length + 32
      continue 
  mem[(64 * stor2.length) + 192] = (32 * stor2.length) + 96
  mem[(98 * stor2.length) + 256] = mem[(32 * stor2.length) + 128]
  mem[(98 * stor2.length) + 288 len floor32(mem[(32 * stor2.length) + 128])] = mem[(32 * stor2.length) + 160 len floor32(mem[(32 * stor2.length) + 128])]
  return memory
    from mem[64]
     [93mlen (32 * mem[(32 * stor2.length) + 128]) + (98 * stor2.length) + -mem[64] + 288


# hash = 0xd365a08e
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def masterAddress() payable: 
  return masterAddress


# hash = 0xd46655f4
# getter = None
# const = None
# payable = True
def unknownd46655f4(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(_param1)
  static call _param1.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if _param1 != this.address:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Neither master nor Authorised'
  [94midx = 0
  while [94midx < stor2.length:
      mem[32] = 4
      addr(stor9.field_0) = unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240]
      mem[96] = 0xd46655f400000000000000000000000000000000000000000000000000000000
      mem[100] = _param1
      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].0xd46655f4 with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < stor2.length
      require [94midx < stor2.length
      if 0x4d52000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
          mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
          mem[32] = 4
          mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
          mem[100] = _param1
          require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
          call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          require [94midx < stor2.length
          if 0x4756000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
              mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
              mem[32] = 4
              mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
              mem[100] = _param1
              require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
              call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                   gas gas_remaining wei
                  args _param1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < stor2.length
              if 0x5043000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                  mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                  mem[32] = 4
                  mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                  mem[100] = _param1
                  require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                  call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                       gas gas_remaining wei
                      args _param1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  mem[0] = 2
                  if 0x5443000000000000000000000000000000000000000000000000000000000000 == stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240:
                      require [94midx < stor2.length
                      mem[0] = stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240
                      mem[32] = 4
                      mem[96] = 0xf1739cae00000000000000000000000000000000000000000000000000000000
                      mem[100] = _param1
                      require ext_code.size(unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240])
                      call unknown01382858[stor2[0.0625 / [94midx] / 256^(2 * [94midx % 16) << 240].transferProxyOwnership(address newOwner) with:
                           gas gas_remaining wei
                          args _param1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  stor3[this.address] = 0
  stor3[_param1] = 1


# hash = 0xe2cab14d
# getter = None
# const = None
# payable = True
def unknowne2cab14d(uint64 _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Not authorized'
  if Mask(64, 192, _param1) == 0x4d5357414c4c4554000000000000000000000000000000000000000000000000:
      require ext_code.size(unknown01382858[0x5444000000000000000000000000000000000000000000000000000000000000])
      call unknown01382858[0x5444000000000000000000000000000000000000000000000000000000000000].changeWalletAddress(address newAddress) with:
           gas gas_remaining wei
          args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      if Mask(64, 192, _param1) == 'MCRNOTA' << 200:
          require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
          call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0x6576ffed with:
               gas gas_remaining wei
              args _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      else:
          if Mask(64, 192, _param1) == 0x4441494645454400000000000000000000000000000000000000000000000000:
              require ext_code.size(unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000])
              call unknown01382858[0x5044000000000000000000000000000000000000000000000000000000000000].0xca0d4c86 with:
                   gas gas_remaining wei
                  args _param2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              if Mask(64, 192, _param1) == 0x554e495357414444000000000000000000000000000000000000000000000000:
                  require ext_code.size(unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000])
                  call unknown01382858[0x5032000000000000000000000000000000000000000000000000000000000000].0xb19ab66d with:
                       gas gas_remaining wei
                      args _param2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              else:
                  if Mask(64, 192, _param1) == 0x4f574e4552000000000000000000000000000000000000000000000000000000:
                      require ext_code.size(unknown01382858[0x4d52000000000000000000000000000000000000000000000000000000000000])
                      call unknown01382858[0x4d52000000000000000000000000000000000000000000000000000000000000].0x90a79368 with:
                           gas gas_remaining wei
                          args _param2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      owner = _param2
                  else:
                      if Mask(64, 192, _param1) == 0x51554f4155544800000000000000000000000000000000000000000000000000:
                          require ext_code.size(unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000])
                          call unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000].0x1407264b with:
                               gas gas_remaining wei
                              args _param2
                      else:
                          if Mask(64, 192, _param1) != 0x4b59434155544800000000000000000000000000000000000000000000000000:
                              revert with 0, 'Invalid param code'
                          require ext_code.size(unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000])
                          call unknown01382858[0x5144000000000000000000000000000000000000000000000000000000000000].0x549a65f4 with:
                               gas gas_remaining wei
                              args _param2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xeaf2c477
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def unknowneaf2c477() payable: 
  return unknowneaf2c477Address


# hash = 0xfa3c8a90
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def unknownfa3c8a90() payable: 
  return unknown71a2b7f7.length


# hash = 0xff0938a7
# getter = None
# const = None
# payable = True
def isPause() payable: 
  if not unknown71a2b7f7.length:
      return 0
  require 1 <= unknown71a2b7f7.length
  require unknown71a2b7f7.length - 1 < unknown71a2b7f7.length
  if bool(unknown71a2b7f7[unknown71a2b7f7.length].field_0) != 1:
      return 0
  return 1


# hash = 0xffa39929
# getter = None
# const = None
# payable = True
def unknownffa39929(bool _param1) payable: 
  require calldata.size - 4 >= 64
  if unknown01382858[0x5031000000000000000000000000000000000000000000000000000000000000] != caller:
      require caller == unknown01382858[0x4756000000000000000000000000000000000000000000000000000000000000]
  unknown71a2b7f7.length++
  unknown71a2b7f7[unknown71a2b7f7.length].field_0 = uint8(_param1)
  storB10E[stor1.length] = block.timestamp
  storB10E[stor1.length].field_0 = 0
  storB10E[stor1.length].field_256 = 0
  if not _param1:
      stor6 = stor50DB
      require ext_code.size(stor50DB)
      call stor50DB.0x75a0f521 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(stor6)
      call stor6.0x9755fafe with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


