# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC3D2736b3E4f0f78457D75b3b5f0191a14e8BD57 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xf1b2d6a3': 'unknownf1b2d6a3(?)'} 

# storage definitions
def storage:
    # storage address 3
    unknowneaaff394
    # storage address 5
    stor5
    # storage address 2
    paused # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    owner # mask: a s
    # storage address 4
    stor4
    # storage address 1
    stor1 # mask: a s
    # storage address 0
    stor0 # mask: a s
# hash = 0x16c38b3c
# getter = None
# const = None
# payable = False
def setPaused(bool _pause): # not payable
  require owner == caller
  stor2 = Mask(96, 0, _pause)


# hash = 0x2b0ff02d
# getter = None
# const = None
# payable = False
def unknown2b0ff02d(uint64 _param1, uint128 _param2, uint128 _param3, uint32 _param4): # not payable
  require ext_code.size(stor0)
  call stor0.ownerOf(uint256 tokenId) with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success
  require ext_call.return_data[12 len 20] == caller
  require ext_code.size(stor0)
  call stor0.0x2afb9fb1 with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success
  require ext_call.return_data[0]
  require ext_code.size(stor1)
  call stor1.0x24fd0a5c with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success
  require ext_call.return_data[0]
  if ext_code.size(caller):
      require stor4[caller]
  require not paused
  require _param2 > 27500 * 10^6 * 3600
  require _param2 <= 10 * 10^18
  require _param3 > 27500 * 10^6 * 3600
  require _param3 <= 10 * 10^18
  require _param4 % 16777216 > 21599
  require _param4 % 16777216 < 259201
  unknowneaaff394[_param1 << 192].field_0 = 0
  unknowneaaff394[_param1 << 192].field_256 = 0
  unknowneaaff394[_param1 << 192].field_64 = _param1
  unknowneaaff394[_param1 << 192].field_128 = uint64(block.timestamp)
  unknowneaaff394[_param1 << 192].field_256 = _param2
  unknowneaaff394[_param1 << 192].field_384 = _param3
  unknowneaaff394[_param1 << 192].field_512 = _param4 % 16777216
  stor5.length++
  if not stor5.length <= stor5.length + 1:
      [94midx = stor5.length + 4 / 4
      while stor5.length + 3 / 4 > [94midx:
          stor5[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  stor5[stor5.length.field_2].field_0 = _param1 * 256^(8 * stor5.length % 4) or stor5[stor5.length.field_2].field_0 and !(18446744073709551615 * 256^(8 * stor5.length % 4))
  unknowneaaff394[_param1 << 192].field_0 = uint64(stor5.length)


# hash = 0x4eddbd8d
# getter = None
# const = None
# payable = False
def unknown4eddbd8d(uint128 _param1, uint128 _param2, uint32 _param3, uint64 _param4): # not payable
  if _param4 >= _param3 % 16777216:
      return _param2
  require _param3 % 16777216
  return (_param1 + ((_param2 * _param4) - (_param1 * _param4) /′ _param3 % 16777216))


# hash = 0x5038c9c5
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def unknown5038c9c5(uint64 _param1): # not payable
  require _param1 < stor5.length
  return unknowneaaff394[stor5[uint64(_param1) / 4].field_(64 * _param1 % 4) - 192].field_0, 
         unknowneaaff394[stor5[uint64(_param1) / 4].field_(64 * _param1 % 4) - 192].field_0,
         unknowneaaff394[stor5[uint64(_param1) / 4].field_(64 * _param1 % 4) - 192].field_256,
         unknowneaaff394[stor5[uint64(_param1) / 4].field_(64 * _param1 % 4) - 192].field_256,
         unknowneaaff394[stor5[uint64(_param1) / 4].field_(64 * _param1 % 4) - 192].field_512


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 2]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  require owner == caller
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0x63de6ad6
# getter = None
# const = None
# payable = True
def unknown63de6ad6(uint64 _param1) payable: 
  require stor5.length
  require unknowneaaff394[_param1 << 192].field_128 > 0
  require not paused
  if uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128) >= unknowneaaff394[_param1 << 192].field_512:
      require call.value >= unknowneaaff394[_param1 << 192].field_384
      require ext_code.size(stor0)
      call stor0.ownerOf(uint256 tokenId) with:
           gas gas_remaining - 710 wei
          args _param1
      require ext_call.success
      if stor5.length > 1:
          require stor5.length - 1 < stor5.length
          require unknowneaaff394[_param1 << 192].field_0 < stor5.length
          stor5[stor3[_param1 << 192].field_2].field_0 = stor('array', ('div', 0.25, ('add', -1, ('stor', 256, 0, ('length', ('name', 'stor5', 5))))), ('name', 'stor5', 5))[uint8(stor5.length - 1)] * 256^(8 * unknowneaaff394[_param1 << 192].field_0) or stor5[stor3[_param1 << 192].field_2].field_0 and !(18446744073709551615 * 256^(8 * unknowneaaff394[_param1 << 192].field_0))
          unknowneaaff394[stor5[0.25 / stor5.length - 1].field_(64 * stor5.length - 1 % 4) - 192].field_0 = unknowneaaff394[_param1 << 192].field_0
      stor5.length--
      if not stor5.length <= stor5.length - 1:
          [94midx = stor5.length + 2 / 4
          while stor5.length + 3 / 4 > [94midx:
              stor5[[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      unknowneaaff394[_param1 << 192].field_0 = 0
      unknowneaaff394[_param1 << 192].field_256 = 0
      unknowneaaff394[_param1 << 192].field_512 = 0
      call addr(ext_call.return_data[0]) with:
         value unknowneaaff394[_param1 << 192].field_384 - (unknowneaaff394[_param1 << 192].field_384 / 100) wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
      if call.value - unknowneaaff394[_param1 << 192].field_384 > 10^12:
          call caller with:
             value call.value - unknowneaaff394[_param1 << 192].field_384 wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
  else:
      require unknowneaaff394[_param1 << 192].field_512
      require call.value >= unknowneaaff394[_param1 << 192].field_256 + ((unknowneaaff394[_param1 << 192].field_384 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) - (unknowneaaff394[_param1 << 192].field_256 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) /′ unknowneaaff394[_param1 << 192].field_512)
      require ext_code.size(stor0)
      call stor0.ownerOf(uint256 tokenId) with:
           gas gas_remaining - 710 wei
          args _param1
      require ext_call.success
      if stor5.length > 1:
          require stor5.length - 1 < stor5.length
          require unknowneaaff394[_param1 << 192].field_0 < stor5.length
          stor5[stor3[_param1 << 192].field_2].field_0 = stor('array', ('div', 0.25, ('add', -1, ('stor', 256, 0, ('length', ('name', 'stor5', 5))))), ('name', 'stor5', 5))[uint8(stor5.length - 1)] * 256^(8 * unknowneaaff394[_param1 << 192].field_0) or stor5[stor3[_param1 << 192].field_2].field_0 and !(18446744073709551615 * 256^(8 * unknowneaaff394[_param1 << 192].field_0))
          unknowneaaff394[stor5[0.25 / stor5.length - 1].field_(64 * stor5.length - 1 % 4) - 192].field_0 = unknowneaaff394[_param1 << 192].field_0
      stor5.length--
      if not stor5.length <= stor5.length - 1:
          [94midx = stor5.length + 2 / 4
          while stor5.length + 3 / 4 > [94midx:
              stor5[[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      unknowneaaff394[_param1 << 192].field_0 = 0
      unknowneaaff394[_param1 << 192].field_256 = 0
      unknowneaaff394[_param1 << 192].field_512 = 0
      call addr(ext_call.return_data[0]) with:
         value unknowneaaff394[_param1 << 192].field_256 + ((unknowneaaff394[_param1 << 192].field_384 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) - (unknowneaaff394[_param1 << 192].field_256 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) /′ unknowneaaff394[_param1 << 192].field_512) - (unknowneaaff394[_param1 << 192].field_256 + ((unknowneaaff394[_param1 << 192].field_384 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) - (unknowneaaff394[_param1 << 192].field_256 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) /′ unknowneaaff394[_param1 << 192].field_512) / 100) wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
      if call.value - unknowneaaff394[_param1 << 192].field_256 - ((unknowneaaff394[_param1 << 192].field_384 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) - (unknowneaaff394[_param1 << 192].field_256 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) /′ unknowneaaff394[_param1 << 192].field_512) > 10^12:
          call caller with:
             value call.value - unknowneaaff394[_param1 << 192].field_256 - ((unknowneaaff394[_param1 << 192].field_384 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) - (unknowneaaff394[_param1 << 192].field_256 * uint64(block.timestamp - unknowneaaff394[_param1 << 192].field_128)) /′ unknowneaaff394[_param1 << 192].field_512) wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
  require ext_code.size(stor0)
  call stor0.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining - 710 wei
      args addr(ext_call.return_data[0]), caller, _param1
  require ext_call.success


# hash = 0x6e9ffe2b
# getter = None
# const = None
# payable = False
def unknown6e9ffe2b(addr _param1): # not payable
  require owner == caller
  stor1 = _param1


# hash = 0x880cdc31
# getter = None
# const = None
# payable = False
def updateOwner(address _owner): # not payable
  require owner == caller
  owner = _owner


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8fb6d997
# getter = None
# const = None
# payable = False
def updateStorageContract(address _newStorage): # not payable
  require owner == caller
  stor0 = _newStorage


# hash = 0xa54c2a9a
# getter = None
# const = None
# payable = False
def unknowna54c2a9a(uint64 _param1): # not payable
  require stor5.length
  require unknowneaaff394[_param1 << 192].field_128 > 0
  require not paused
  require ext_code.size(stor0)
  call stor0.ownerOf(uint256 tokenId) with:
       gas gas_remaining - 710 wei
      args _param1
  require ext_call.success
  if ext_call.return_data[12 len 20] != caller:
      require block.timestamp - unknowneaaff394[_param1 << 192].field_128 > 336 * 24 * 3600
  if stor5.length > 1:
      require stor5.length - 1 < stor5.length
      require unknowneaaff394[_param1 << 192].field_0 < stor5.length
      stor5[stor3[_param1 << 192].field_2].field_0 = stor('array', ('div', 0.25, ('add', -1, ('stor', 256, 0, ('length', ('name', 'stor5', 5))))), ('name', 'stor5', 5))[uint8(stor5.length - 1)] * 256^(8 * unknowneaaff394[_param1 << 192].field_0) or stor5[stor3[_param1 << 192].field_2].field_0 and !(18446744073709551615 * 256^(8 * unknowneaaff394[_param1 << 192].field_0))
      unknowneaaff394[stor5[0.25 / stor5.length - 1].field_(64 * stor5.length - 1 % 4) - 192].field_0 = unknowneaaff394[_param1 << 192].field_0
  stor5.length--
  if not stor5.length <= stor5.length - 1:
      [94midx = stor5.length + 2 / 4
      while stor5.length + 3 / 4 > [94midx:
          stor5[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  unknowneaaff394[_param1 << 192].field_0 = 0
  unknowneaaff394[_param1 << 192].field_256 = 0
  unknowneaaff394[_param1 << 192].field_512 = 0


# hash = 0xa672990c
# getter = None
# const = None
# payable = False
def unknowna672990c(addr _param1, bool _param2): # not payable
  require owner == caller
  stor4[addr(_param1)] = uint8(_param2)


# hash = 0xa9014b0f
# getter = None
# const = None
# payable = False
def unknowna9014b0f(uint64 _param1): # not payable
  if stor5.length:
      return (unknowneaaff394[_param1 << 192].field_128 > 0)
  else:
      return 0


# hash = 0xeaaff394
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def unknowneaaff394(uint64 _param1): # not payable
  return unknowneaaff394[_param1 << 192].field_0, 
         unknowneaaff394[_param1 << 192].field_0,
         unknowneaaff394[_param1 << 192].field_256,
         unknowneaaff394[_param1 << 192].field_256,
         unknowneaaff394[_param1 << 192].field_512


# hash = 0xfd27b51e
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknownfd27b51e(): # not payable
  return stor5.length


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


