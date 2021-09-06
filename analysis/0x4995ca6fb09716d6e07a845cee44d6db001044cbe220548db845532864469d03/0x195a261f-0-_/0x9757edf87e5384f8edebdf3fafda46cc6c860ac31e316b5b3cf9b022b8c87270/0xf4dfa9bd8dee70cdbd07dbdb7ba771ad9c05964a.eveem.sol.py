# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xf4dFA9BD8Dee70CdBD07DBDb7Ba771Ad9c05964a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xe4ca5492': 'unknowne4ca5492(?)'} 

# storage definitions
def storage:
    # storage address 0
    authorityAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    unknown365a86fcAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    unknown20531bc9Address # mask: a s
    # storage address 11
    registryAddress # mask: a s
    # storage address 12
    versionAddress # mask: a s
    # storage address 13
    unknownc9d4623fAddress # mask: a s
    # storage address 14
    unknown8a471df9Address # mask: a s
    # storage address 15
    initialized # mask: a s
    # storage address 16
    exchanges
    # storage address 17
    unknownec7dd7bb
    # storage address 18
    stor18
    # storage address 19
    unknown2e62efbb
    # storage address 20
    unknown28f5cd02
    # storage address 21
    stor21
    # storage address 22
    unknowncc460a02
    # storage address 23
    stor23
# hash = 0x06c0770e
# getter = None
# const = None
# payable = False
def unknown06c0770e(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[100] = this.address
  require ext_code.size(_param1)
  call _param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >=′ 32
  [94midx = 0
  while [94midx < exchanges.length:
      mem[0] = _param1
      mem[32] = sha3(exchanges[[94midx].field_0, 19)
      if unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0:
          require [94midx < exchanges.length
          mem[32] = sha3(exchanges[[94midx].field_0, 19)
          require ext_code.size(exchanges[[94midx].field_256)
          call exchanges[[94midx].field_256.0xd7d1c4d5 with:
               gas gas_remaining wei
              args exchanges[[94midx].field_0, unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0, _param1
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_60 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 128
          [94m_63 = mem[[94m_60 + 64]
          if mem[[94m_60 + 64]:
              if mem[[94m_60 + 64] < 0:
                  revert with 0, 'ds-math-add-overflow'
          else:
              require [94midx < exchanges.length
              mem[32] = 21
              if stor21[addr(_param1)]:
                  if block.timestamp + 1800 < block.timestamp:
                      revert with 0, 'ds-math-add-overflow'
                  unknowncc460a02[addr(_param1)] = block.timestamp + 1800
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_256 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_512 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_768 = 0
                  if unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768] - 1 > unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768]:
                      revert with 0, 'ds-math-sub-underflow'
                  mem[32] = 20
                  unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768]--
              if [94m_63 < 0:
                  revert with 0, 'ds-math-add-overflow'
          require [94midx < exchanges.length
          mem[0] = 16
      [94midx = [94midx + 1
      continue 
  stor21[addr(_param1)] = 0
  if ext_call.return_data[0] < 0:
      revert with 0, 'ds-math-add-overflow'
  return ext_call.return_data[0]


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  owner = _newOwner
  log LogSetOwner(address owner=_newOwner)


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(initialized)


# hash = 0x1644bea7
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 18]]]]
# const = None
# payable = False
def unknown1644bea7(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  return bool(stor18[_param1])


# hash = 0x195a261f
# getter = None
# const = None
# payable = False
def unknown195a261f(): # not payable
  require calldata.size - 4 >=′ 256
  require cd[68] < 3
  require calldata.size >′ 131
  require 164 <= calldata.size
  [94midx = 0
  [94ms = 100
  [94mt = 96
  while [94midx < 2:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require calldata.size >′ 195
  require 260 <= calldata.size
  [94midx = 0
  [94ms = 164
  [94mt = 160
  while [94midx < 3:
      mem[[94mt] = cd[[94ms]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  require cd[68] <= 2
  require cd[68] <= 2
  if not cd[68]:
      mem[352] = mem[108 len 20]
      mem[384] = mem[140 len 20]
      unknownec7dd7bb.length++
      unknownec7dd7bb[unknownec7dd7bb.length].field_0 = addr(cd[4])
      unknownec7dd7bb[unknownec7dd7bb.length].field_256 = cd[36]
      require cd[68] <= 2
      unknownec7dd7bb[unknownec7dd7bb.length].field_512 = cd[68] or Mask(248, 8, unknownec7dd7bb[unknownec7dd7bb.length].field_512)
      unknownec7dd7bb[unknownec7dd7bb.length].field_520 = mem[364 len 20]
      unknownec7dd7bb[unknownec7dd7bb.length].field_768 = mem[396 len 20]
      unknownec7dd7bb[unknownec7dd7bb.length].field_1024 = mem[160]
      unknownec7dd7bb[unknownec7dd7bb.length].field_1280 = mem[192]
      unknownec7dd7bb[unknownec7dd7bb.length].field_1536 = block.timestamp
      unknownec7dd7bb[unknownec7dd7bb.length].field_1792 = mem[224]
  else:
      if cd[68] == 1:
          require cd[68] <= 2
          mem[352] = mem[108 len 20]
          mem[384] = mem[140 len 20]
          unknownec7dd7bb.length++
          unknownec7dd7bb[unknownec7dd7bb.length].field_0 = addr(cd[4])
          unknownec7dd7bb[unknownec7dd7bb.length].field_256 = cd[36]
          require cd[68] <= 2
          unknownec7dd7bb[unknownec7dd7bb.length].field_512 = cd[68] or Mask(248, 8, unknownec7dd7bb[unknownec7dd7bb.length].field_512)
          unknownec7dd7bb[unknownec7dd7bb.length].field_520 = mem[364 len 20]
          unknownec7dd7bb[unknownec7dd7bb.length].field_768 = mem[396 len 20]
          unknownec7dd7bb[unknownec7dd7bb.length].field_1024 = mem[160]
          unknownec7dd7bb[unknownec7dd7bb.length].field_1280 = mem[192]
          unknownec7dd7bb[unknownec7dd7bb.length].field_1536 = block.timestamp
          unknownec7dd7bb[unknownec7dd7bb.length].field_1792 = mem[224]


# hash = 0x19ab7f43
# getter = None
# const = None
# payable = False
def unknown19ab7f43(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      require ext_code.size(unknown365a86fcAddress)
      call unknown365a86fcAddress.manager() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(unknown365a86fcAddress)
          call unknown365a86fcAddress.isShutDown() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'Sender is not this contract or manager'
  require ext_code.size(_param1)
  call _param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(_param1)
  call _param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args stor9
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(_param1)
  call _param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args stor9, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(_param1)
  call _param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args stor9
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if 2 * ext_call.return_data[0] != ext_call.return_data[0]:
      revert with 0, 'Receiver did not receive tokens in transfer'


# hash = 0x19c8916b
# getter = None
# const = None
# payable = False
def unknown19c8916b(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >=′ 64
  return block.timestamp >= unknown2e62efbb[addr(_param1)][addr(_param2)].field_256


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return unknown20531bc9Address


# hash = 0x249204ac
# getter = None
# const = None
# payable = False
def unknown249204ac(): # not payable
  require calldata.size - 4 >=′ 32
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require ('cd', 4).length <= 18446744073709551615
  require (32 * ('cd', 4).length) + 128 >= 96 and (32 * ('cd', 4).length) + 128 <= 18446744073709551615
  mem[64] = (32 * ('cd', 4).length) + 128
  mem[96] = ('cd', 4).length
  require cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  while [94midx < ('cd', 4).length:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < mem[96]
      [94m_150 = mem[(32 * [94midx) + 128]
      if this.address == caller:
          mem[mem[64] + 4] = this.address
          require ext_code.size(addr([94m_150))
          call addr([94m_150).balanceOf(address owner) with:
               gas gas_remaining wei
              args addr(this.address)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_159 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          [94m_162 = mem[[94m_159]
          mem[mem[64] + 4] = stor9
          require ext_code.size(addr([94m_150))
          call addr([94m_150).balanceOf(address owner) with:
               gas gas_remaining wei
              args stor9
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_172 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          [94m_175 = mem[[94m_172]
          mem[mem[64] + 36] = [94m_162
          require ext_code.size(addr([94m_150))
          call addr([94m_150).transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args stor9, [94m_162
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          mem[mem[64] + 4] = stor9
          require ext_code.size(addr([94m_150))
          call addr([94m_150).balanceOf(address owner) with:
               gas gas_remaining wei
              args stor9
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_196 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          if [94m_175 + [94m_162 < [94m_175:
              revert with 0, 'ds-math-add-overflow'
          if [94m_175 + [94m_162 != mem[[94m_196]:
              revert with 0, 'Receiver did not receive tokens in transfer'
      else:
          require ext_code.size(unknown365a86fcAddress)
          call unknown365a86fcAddress.manager() with:
               gas gas_remaining wei
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_154 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          if caller == mem[[94m_154 + 12 len 20]:
              mem[mem[64] + 4] = this.address
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args addr(this.address)
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_168 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              [94m_169 = mem[[94m_168]
              mem[mem[64] + 4] = stor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args stor9
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_180 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              [94m_182 = mem[[94m_180]
              mem[mem[64] + 36] = [94m_169
              require ext_code.size(addr([94m_150))
              call addr([94m_150).transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args stor9, [94m_169
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              mem[mem[64] + 4] = stor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args stor9
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_204 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              if [94m_182 + [94m_169 < [94m_182:
                  revert with 0, 'ds-math-add-overflow'
              if [94m_182 + [94m_169 != mem[[94m_204]:
                  revert with 0, 'Receiver did not receive tokens in transfer'
          else:
              require ext_code.size(unknown365a86fcAddress)
              call unknown365a86fcAddress.isShutDown() with:
                   gas gas_remaining wei
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_161 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              if not mem[[94m_161]:
                  revert with 0, 'Sender is not this contract or manager'
              mem[mem[64] + 4] = this.address
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args addr(this.address)
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_176 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              [94m_177 = mem[[94m_176]
              mem[mem[64] + 4] = stor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args stor9
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_187 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              [94m_189 = mem[[94m_187]
              mem[mem[64] + 36] = [94m_177
              require ext_code.size(addr([94m_150))
              call addr([94m_150).transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args stor9, [94m_177
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              mem[mem[64] + 4] = stor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args stor9
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_212 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              if [94m_189 + [94m_177 < [94m_189:
                  revert with 0, 'ds-math-add-overflow'
              if [94m_189 + [94m_177 != mem[[94m_212]:
                  revert with 0, 'Receiver did not receive tokens in transfer'
      [94midx = [94midx + 1
      continue 


# hash = 0x2839fc29
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def exchanges(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require _param1 < exchanges.length
  return exchanges[_param1].field_0, exchanges[_param1].field_256, bool(exchanges[_param1].field_416)


# hash = 0x28f5cd02
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 20]]]
# const = None
# payable = False
def unknown28f5cd02(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  return unknown28f5cd02[_param1]


# hash = 0x2e62efbb
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 19]]]]]
# const = None
# payable = False
def unknown2e62efbb(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >=′ 64
  return unknown2e62efbb[addr(_param1)][addr(_param2)].field_0, 
         unknown2e62efbb[addr(_param1)][addr(_param2)].field_256,
         unknown2e62efbb[addr(_param1)][addr(_param2)].field_512


# hash = 0x365a86fc
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown365a86fc(): # not payable
  return unknown365a86fcAddress


# hash = 0x3eb544e0
# getter = None
# const = ['return', 1800]
# payable = False
const unknown3eb544e0 = 1800


# hash = 0x4a194903
# getter = None
# const = None
# payable = True
def unknown4a194903(addr _param1) payable: 
  mem[64] = 96
  require not call.value
  require calldata.size - 4 >=′ 32
  [94midx = 0
  while [94midx < exchanges.length:
      mem[0] = _param1
      mem[32] = sha3(exchanges[[94midx].field_0, 19)
      if unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0:
          require [94midx < exchanges.length
          mem[32] = sha3(exchanges[[94midx].field_0, 19)
          require ext_code.size(exchanges[[94midx].field_256)
          call exchanges[[94midx].field_256.0xd7d1c4d5 with:
               gas gas_remaining wei
              args exchanges[[94midx].field_0, unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0, _param1
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_52 = mem[64]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 128
          [94m_55 = mem[[94m_52 + 64]
          if mem[[94m_52 + 64]:
              if mem[[94m_52 + 64] < 0:
                  revert with 0, 'ds-math-add-overflow'
          else:
              require [94midx < exchanges.length
              mem[32] = 21
              if stor21[addr(_param1)]:
                  if block.timestamp + 1800 < block.timestamp:
                      revert with 0, 'ds-math-add-overflow'
                  unknowncc460a02[addr(_param1)] = block.timestamp + 1800
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_0 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_256 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_512 = 0
                  unknown2e62efbb[stor16[[94midx].field_0][addr(_param1)].field_768 = 0
                  if unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768] - 1 > unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768]:
                      revert with 0, 'ds-math-sub-underflow'
                  mem[32] = 20
                  unknown28f5cd02[stor19[stor16[[94midx].field_0][addr(_param1)].field_768]--
              if [94m_55 < 0:
                  revert with 0, 'ds-math-add-overflow'
          require [94midx < exchanges.length
          mem[0] = 16
      [94midx = [94midx + 1
      continue 
  stor21[addr(_param1)] = 0
  return 0


# hash = 0x5202d6d6
# getter = None
# const = None
# payable = False
def unknown5202d6d6(addr _param1, addr _param2, addr _param3, uint256 _param4, uint256 _param5): # not payable
  require calldata.size - 4 >=′ 160
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  if stor21[addr(_param2)]:
      revert with 0, 'Asset already in open order'
  if 0 >= unknownec7dd7bb.length:
      revert with 0, 'No orders in array'
  if block.timestamp + (24 * 3600) < block.timestamp:
      revert with 0, 'ds-math-add-overflow'
  if not _param5:
      if block.timestamp + (24 * 3600) <= block.timestamp:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      stor21[addr(_param2)] = 1
      unknowncc460a02[addr(_param2)] = block.timestamp + 88200
      if unknown28f5cd02[addr(_param3)] + 1 < unknown28f5cd02[addr(_param3)]:
          revert with 0, 'ds-math-add-overflow'
      unknown28f5cd02[addr(_param3)]++
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_0 = _param4
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_256 = block.timestamp + (24 * 3600)
  else:
      if _param5 > block.timestamp + (24 * 3600):
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      if _param5 <= block.timestamp:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      stor21[addr(_param2)] = 1
      if _param5 + 1800 < _param5:
          revert with 0, 'ds-math-add-overflow'
      unknowncc460a02[addr(_param2)] = _param5 + 1800
      if unknown28f5cd02[addr(_param3)] + 1 < unknown28f5cd02[addr(_param3)]:
          revert with 0, 'ds-math-add-overflow'
      unknown28f5cd02[addr(_param3)]++
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_0 = _param4
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_256 = _param5
  if unknownec7dd7bb.length - 1 > unknownec7dd7bb.length:
      revert with 0, 'ds-math-sub-underflow'
  unknown2e62efbb[addr(_param1)][addr(_param2)].field_512 = unknownec7dd7bb.length - 1
  unknown2e62efbb[addr(_param1)][addr(_param2)].field_768 = _param3


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return versionAddress


# hash = 0x69bfce2f
# getter = None
# const = None
# payable = False
def unknown69bfce2f(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[896] = stor23[_param1][10].field_0
  [94midx = 896
  [94ms = 0
  while stor23[_param1][10].length + 864 > [94midx:
      mem[[94midx + 32] = stor23[_param1][[94ms + 10].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor23[_param1][10].length) + 928] = stor23[_param1][11].field_0
  [94midx = ceil32(stor23[_param1][10].length) + 928
  [94ms = 0
  while ceil32(stor23[_param1][10].length) + stor23[_param1][11].length + 896 > [94midx:
      mem[[94midx + 32] = stor23[_param1][[94ms + 11].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  if ceil32(stor23[_param1][10].length) <= stor23[_param1][10].length:
      mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 1376] = stor23[_param1][11].length
      mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 1408 len ceil32(stor23[_param1][11].length)] = mem[ceil32(stor23[_param1][10].length) + 928 len ceil32(stor23[_param1][11].length)]
      if ceil32(stor23[_param1][11].length) > stor23[_param1][11].length:
          mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + stor23[_param1][11].length + 1408] = 0
      return 32, stor23[_param1].field_0, 
             stor23[_param1].field_256,
             stor23[_param1].field_512,
             stor23[_param1].field_768,
             stor23[_param1].field_1024,
             stor23[_param1].field_1280,
             stor23[_param1].field_1536,
             stor23[_param1].field_1792,
             stor23[_param1].field_2048,
             stor23[_param1].field_2304,
             384,
             ceil32(stor23[_param1][10].length) + 416,
             stor23[_param1][10].length,
             mem[896 len ceil32(stor23[_param1][10].length)],
             stor23[_param1][11].length,
             mem[ceil32(stor23[_param1][10].length) + 928 len ceil32(stor23[_param1][11].length)]
  mem[ceil32(stor23[_param1][10].length) + ceil32(stor23[_param1][11].length) + stor23[_param1][10].length + 1376] = 0
  mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 1376] = stor23[_param1][11].length
  mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 1408 len ceil32(stor23[_param1][11].length)] = mem[ceil32(stor23[_param1][10].length) + 928 len ceil32(stor23[_param1][11].length)]
  if ceil32(stor23[_param1][11].length) > stor23[_param1][11].length:
      mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + stor23[_param1][11].length + 1408] = 0
  return 32, stor23[_param1].field_0, 
         stor23[_param1].field_256,
         stor23[_param1].field_512,
         stor23[_param1].field_768,
         stor23[_param1].field_1024,
         stor23[_param1].field_1280,
         stor23[_param1].field_1536,
         stor23[_param1].field_1792,
         stor23[_param1].field_2048,
         stor23[_param1].field_2304,
         384,
         ceil32(stor23[_param1][10].length) + 416,
         stor23[_param1][10].length,
         mem[896 len stor23[_param1][10].length],
         0,
         mem[ceil32(stor23[_param1][10].length) + ceil32(stor23[_param1][11].length) + stor23[_param1][10].length + 1408 len ceil32(stor23[_param1][10].length) + ceil32(stor23[_param1][11].length) - stor23[_param1][10].length]


# hash = 0x77076855
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 21]]]]
# const = None
# payable = False
def unknown77076855(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  return bool(stor21[_param1])


# hash = 0x7a9e5e4b
# getter = None
# const = None
# payable = False
def setAuthority(address _authority): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  authorityAddress = _authority_
  log LogSetAuthority(address authority=_authority_)


# hash = 0x7b103999
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def registry(): # not payable
  return registryAddress


# hash = 0x83259ed9
# getter = None
# const = None
# payable = False
def unknown83259ed9(addr _param1, addr _param2, addr _param3, addr _param4, addr _param5, addr _param6, addr _param7, addr _param8, addr _param9, addr _param10, addr _param11, addr _param12): # not payable
  require calldata.size - 4 >=′ 384
  require calldata.size >= 388
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  require caller == unknown365a86fcAddress
  if initialized:
      revert with 0, 'Already initialized'
  stor3 = _param1
  stor4 = _param2
  stor5 = _param3
  stor6 = _param4
  stor7 = _param5
  stor8 = _param6
  stor9 = _param7
  unknown20531bc9Address = _param8
  registryAddress = _param9
  versionAddress = _param10
  unknownc9d4623fAddress = _param11
  unknown8a471df9Address = _param12
  initialized = 1
  if caller != this.address:
      if owner != caller:
          if not authorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(authorityAddress)
          call authorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), call.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  owner = 0
  log LogSetOwner(address owner)
  log 0x0 


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return unknown8a471df9Address


# hash = 0x8bc5b3c5
# getter = None
# const = None
# payable = False
def unknown8bc5b3c5(): # not payable
  mem[96] = exchanges.length
  if not exchanges.length:
      mem[(32 * exchanges.length) + 128] = exchanges.length
      mem[(64 * exchanges.length) + 160] = exchanges.length
      mem[64] = (98 * exchanges.length) + 192
      [94midx = 0
      while [94midx < exchanges.length:
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = exchanges[[94midx].field_0
          require [94midx < exchanges.length
          require [94midx < mem[(32 * exchanges.length) + 128]
          mem[(32 * exchanges.length) + (32 * [94midx) + 160] = exchanges[[94midx].field_256
          require [94midx < exchanges.length
          mem[0] = 16
          require [94midx < mem[(64 * exchanges.length) + 160]
          mem[(64 * exchanges.length) + (32 * [94midx) + 192] = bool(exchanges[[94midx].field_416)
          [94midx = [94midx + 1
          continue 
      [94m_34 = mem[64]
      mem[mem[64]] = 96
      [94m_44 = mem[96]
      mem[mem[64] + 96] = mem[96]
      [94midx = 0
      [94ms = 128
      [94mt = mem[64] + 128
      while [94midx < [94m_44:
          mem[[94mt] = mem[[94ms + 12 len 20]
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          continue 
      mem[[94m_34 + 32] = (32 * [94m_44) + 128
      [94m_64 = mem[(32 * exchanges.length) + 128]
      mem[[94m_34 + (32 * [94m_44) + 128] = mem[(32 * exchanges.length) + 128]
      [94midx = 0
      [94ms = (32 * exchanges.length) + 160
      [94mt = [94m_34 + (32 * [94m_44) + 160
      while [94midx < [94m_64:
          mem[[94mt] = mem[[94ms + 12 len 20]
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          continue 
      mem[[94m_34 + 64] = (32 * [94m_44) + (32 * [94m_64) + 160
      [94m_76 = mem[(64 * exchanges.length) + 160]
      mem[[94m_34 + (32 * [94m_44) + (32 * [94m_64) + 160] = mem[(64 * exchanges.length) + 160]
      [94midx = 0
      [94ms = (64 * exchanges.length) + 192
      [94mt = [94m_34 + (32 * [94m_44) + (32 * [94m_64) + 192
      while [94midx < [94m_76:
          mem[[94mt] = bool(mem[[94ms])
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          continue 
      return memory
        from mem[64]
         [93mlen [94m_34 + (32 * [94m_44) + (32 * [94m_64) + (32 * [94m_76) + -mem[64] + 192
  mem[128 len 32 * exchanges.length] = code.data[16133 len 32 * exchanges.length]
  mem[(32 * exchanges.length) + 128] = exchanges.length
  mem[(32 * exchanges.length) + 160 len 32 * exchanges.length] = code.data[16133 len 32 * exchanges.length]
  mem[(64 * exchanges.length) + 160] = exchanges.length
  mem[64] = (98 * exchanges.length) + 192
  mem[(64 * exchanges.length) + 192 len 32 * exchanges.length] = code.data[16133 len 32 * exchanges.length]
  [94midx = 0
  while [94midx < exchanges.length:
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = exchanges[[94midx].field_0
      require [94midx < exchanges.length
      require [94midx < mem[(32 * exchanges.length) + 128]
      mem[(32 * exchanges.length) + (32 * [94midx) + 160] = exchanges[[94midx].field_256
      require [94midx < exchanges.length
      mem[0] = 16
      require [94midx < mem[(64 * exchanges.length) + 160]
      mem[(64 * exchanges.length) + (32 * [94midx) + 192] = bool(exchanges[[94midx].field_416)
      [94midx = [94midx + 1
      continue 
  [94m_37 = mem[64]
  mem[mem[64]] = 96
  [94m_45 = mem[96]
  mem[mem[64] + 96] = mem[96]
  [94midx = 0
  [94ms = 128
  [94mt = mem[64] + 128
  while [94midx < [94m_45:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  mem[[94m_37 + 32] = (32 * [94m_45) + 128
  [94m_65 = mem[(32 * exchanges.length) + 128]
  mem[[94m_37 + (32 * [94m_45) + 128] = mem[(32 * exchanges.length) + 128]
  [94midx = 0
  [94ms = (32 * exchanges.length) + 160
  [94mt = [94m_37 + (32 * [94m_45) + 160
  while [94midx < [94m_65:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  mem[[94m_37 + 64] = (32 * [94m_45) + (32 * [94m_65) + 160
  [94m_77 = mem[(64 * exchanges.length) + 160]
  mem[[94m_37 + (32 * [94m_45) + (32 * [94m_65) + 160] = mem[(64 * exchanges.length) + 160]
  [94midx = 0
  [94ms = (64 * exchanges.length) + 192
  [94mt = [94m_37 + (32 * [94m_45) + (32 * [94m_65) + 192
  while [94midx < [94m_77:
      mem[[94mt] = bool(mem[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  return memory
    from mem[64]
     [93mlen [94m_37 + (32 * [94m_45) + (32 * [94m_65) + (32 * [94m_77) + -mem[64] + 192


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9b91f84a
# getter = ['struct', ['loc', 19]]
# const = None
# payable = False
def unknown9b91f84a(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >=′ 64
  return unknown2e62efbb[_param1][_param2].field_0, 
         unknown2e62efbb[_param1][_param2].field_256,
         unknown2e62efbb[_param1][_param2].field_512,
         unknown2e62efbb[_param1][_param2].field_768


# hash = 0xa85c38ef
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def orders(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require _param1 < unknownec7dd7bb.length
  require unknownec7dd7bb[_param1].field_512 < 3
  return unknownec7dd7bb[_param1].field_0, 
         unknownec7dd7bb[_param1].field_256,
         unknownec7dd7bb[_param1].field_512,
         unknownec7dd7bb[_param1].field_512,
         unknownec7dd7bb[_param1].field_768,
         unknownec7dd7bb[_param1].field_1024,
         unknownec7dd7bb[_param1].field_1280,
         unknownec7dd7bb[_param1].field_1536,
         unknownec7dd7bb[_param1].field_1792


# hash = 0xa8c1e5de
# getter = None
# const = ['return', 86400]
# payable = False
const unknowna8c1e5de = (24 * 3600)


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return stor3, 
         stor4,
         stor5,
         stor6,
         stor7,
         stor8,
         stor9,
         unknown20531bc9Address,
         registryAddress,
         versionAddress,
         unknownc9d4623fAddress,
         unknown8a471df9Address


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return authorityAddress


# hash = 0xc3394ef7
# getter = None
# const = None
# payable = False
def unknownc3394ef7(): # not payable
  require calldata.size - 4 >=′ 64
  require cd[36] <= 18446744073709551615
  require calldata.size + -cd[36] - 4 >=′ 384
  require ('cd', 36)[9] <= 18446744073709551615
  require calldata.size >′ cd[36] + ('cd', 36)[9] + 35
  require cd[(cd[36] + ('cd', 36)[9] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 512 >= 480 and ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 512 <= 18446744073709551615
  require cd[36] + ('cd', 36)[9] + cd[(cd[36] + ('cd', 36)[9] + 4)] + 36 <= calldata.size
  require ('cd', 36)[10] <= 18446744073709551615
  require calldata.size >′ cd[36] + ('cd', 36)[10] + 35
  require cd[(cd[36] + ('cd', 36)[10] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[36] + ('cd', 36)[10] + 4)]) + 544 >= 512 and ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + ceil32(cd[(cd[36] + ('cd', 36)[10] + 4)]) + 544 <= 18446744073709551615
  mem[ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 512] = cd[(cd[36] + ('cd', 36)[10] + 4)]
  require cd[36] + ('cd', 36)[10] + cd[(cd[36] + ('cd', 36)[10] + 4)] + 36 <= calldata.size
  mem[ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 544 len cd[(cd[36] + ('cd', 36)[10] + 4)]] = call.data[cd[36] + ('cd', 36)[10] + 36 len cd[(cd[36] + ('cd', 36)[10] + 4)]]
  mem[cd[(cd[36] + ('cd', 36)[10] + 4)] + ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 544] = 0
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  stor23[cd[4]].field_0 = addr(('cd', 36).length)
  stor23[cd[4]].field_256 = addr(('cd', 36)[0])
  stor23[cd[4]].field_512 = addr(('cd', 36)[1])
  stor23[cd[4]].field_768 = addr(('cd', 36)[2])
  stor23[cd[4]].field_1024 = ('cd', 36)[3]
  stor23[cd[4]].field_1280 = ('cd', 36)[4]
  stor23[cd[4]].field_1536 = ('cd', 36)[5]
  stor23[cd[4]].field_1792 = ('cd', 36)[6]
  stor23[cd[4]].field_2048 = ('cd', 36)[7]
  stor23[cd[4]].field_2304 = ('cd', 36)[8]
  stor23[cd[4]][10][].field_0 = Array(len=cd[(cd[36] + ('cd', 36)[9] + 4)], data=call.data[cd[36] + ('cd', 36)[9] + 36 len cd[(cd[36] + ('cd', 36)[9] + 4)]])
  stor23[cd[4]][11][].field_0 = Array(len=Mask(8 * -ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + cd[(cd[36] + ('cd', 36)[9] + 4)] + 32, 0, 0), mem[cd[(cd[36] + ('cd', 36)[9] + 4)] + 544 len -cd[(cd[36] + ('cd', 36)[9] + 4)] + ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)])], data=mem[ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + 544 len Mask(8 * -ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)]) + cd[(cd[36] + ('cd', 36)[9] + 4)] + 32, 0, 0), mem[cd[(cd[36] + ('cd', 36)[9] + 4)] + 544 len -cd[(cd[36] + ('cd', 36)[9] + 4)] + ceil32(cd[(cd[36] + ('cd', 36)[9] + 4)])]])


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return unknownc9d4623fAddress


# hash = 0xcc460a02
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 22]]]
# const = None
# payable = False
def unknowncc460a02(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  return unknowncc460a02[_param1]


# hash = 0xda855f3a
# getter = None
# const = None
# payable = False
def unknownda855f3a(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[128] = stor23[_param1][10].field_0
  [94midx = 128
  [94ms = 0
  while stor23[_param1][10].length + 96 > [94midx:
      mem[[94midx + 32] = stor23[_param1][[94ms + 10].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor23[_param1][10].length) + 160] = stor23[_param1][11].field_0
  [94midx = ceil32(stor23[_param1][10].length) + 160
  [94ms = 0
  while ceil32(stor23[_param1][10].length) + stor23[_param1][11].length + 128 > [94midx:
      mem[[94midx + 32] = stor23[_param1][[94ms + 11].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  if ceil32(stor23[_param1][10].length) > stor23[_param1][10].length:
      mem[ceil32(stor23[_param1][10].length) + ceil32(stor23[_param1][11].length) + stor23[_param1][10].length + 576] = 0
  mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 576] = stor23[_param1][11].length
  mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + 608 len ceil32(stor23[_param1][11].length)] = mem[ceil32(stor23[_param1][10].length) + 160 len ceil32(stor23[_param1][11].length)]
  if ceil32(stor23[_param1][11].length) > stor23[_param1][11].length:
      mem[(2 * ceil32(stor23[_param1][10].length)) + ceil32(stor23[_param1][11].length) + stor23[_param1][11].length + 608] = 0
  return stor23[_param1].field_0, 
         stor23[_param1].field_256,
         stor23[_param1].field_512,
         stor23[_param1].field_768,
         stor23[_param1].field_1024,
         stor23[_param1].field_1280,
         stor23[_param1].field_1536,
         stor23[_param1].field_1792,
         stor23[_param1].field_2048,
         stor23[_param1].field_2304,
         Array(len=stor23[_param1][10].length, data=mem[128 len ceil32(stor23[_param1][10].length)], stor23[_param1][11].length, mem[ceil32(stor23[_param1][10].length) + 160 len ceil32(stor23[_param1][11].length)]),
         ceil32(stor23[_param1][10].length) + 416


# hash = 0xec7dd7bb
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknownec7dd7bb(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require _param1 < unknownec7dd7bb.length
  require unknownec7dd7bb[_param1].field_512 <= 2
  return unknownec7dd7bb[_param1].field_512, 
         unknownec7dd7bb[_param1].field_768,
         unknownec7dd7bb[_param1].field_1024,
         unknownec7dd7bb[_param1].field_1280


# hash = 0xfcfdcf8a
# getter = None
# const = None
# payable = False
def unknownfcfdcf8a(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >=′ 64
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  if stor21[addr(_param2)]:
      if block.timestamp + 1800 < block.timestamp:
          revert with 0, 'ds-math-add-overflow'
      unknowncc460a02[addr(_param2)] = block.timestamp + 1800
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_0 = 0
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_256 = 0
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_512 = 0
      unknown2e62efbb[addr(_param1)][addr(_param2)].field_768 = 0
      if unknown28f5cd02[stor19[addr(_param1)][addr(_param2)].field_768] - 1 > unknown28f5cd02[stor19[addr(_param1)][addr(_param2)].field_768]:
          revert with 0, 'ds-math-sub-underflow'
      unknown28f5cd02[stor19[addr(_param1)][addr(_param2)].field_768]--


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


