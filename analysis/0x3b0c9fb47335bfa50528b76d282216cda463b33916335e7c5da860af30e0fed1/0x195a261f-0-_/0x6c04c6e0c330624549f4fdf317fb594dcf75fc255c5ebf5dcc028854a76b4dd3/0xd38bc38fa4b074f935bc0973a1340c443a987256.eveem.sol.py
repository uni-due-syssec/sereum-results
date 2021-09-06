# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD38BC38FA4b074f935BC0973A1340c443a987256 
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
def unknown06c0770e(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[100] = this.address
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  mem[96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >=′ 32
  [94midx = 0
  mwhile [94midx < mexchangesm.lengthm:
      mem[0] = m_param1
      mem[32] = sha3(mexchangesm[[94midxm]m.field_0, 19)
      if munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0:
          require [94midx < mexchangesm.length
          mem[32] = sha3(mexchangesm[[94midxm]m.field_0, 19)
          require ext_code.size(mexchangesm[[94midxm]m.field_256)
          call mexchangesm[[94midxm]m.field_256.0xd7d1c4d5 with:
               gas gas_remaining wei
              args mexchangesm[[94midxm]m.field_0, munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0, m_param1
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
              require [94midx < mexchangesm.length
              mem[32] = 21
              if mstor21m[addr(m_param1)m]:
                  if block.timestamp + 1800 < block.timestamp:
                      revert with 0, 'ds-math-add-overflow'
                  munknowncc460a02m[addr(m_param1)m] = block.timestamp + 1800
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_256 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_512 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768 = 0
                  if munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m] - 1 > munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m]:
                      revert with 0, 'ds-math-sub-underflow'
                  mem[32] = 20
                  munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m]--
              if [94m_63 < 0:
                  revert with 0, 'ds-math-add-overflow'
          require [94midx < mexchangesm.length
          mem[0] = 16
      [94midx = [94midx + 1
      mcontinue 
  mstor21m[addr(m_param1)m] = 0
  if ext_call.return_data[0] < 0:
      revert with 0, 'ds-math-add-overflow'
  return ext_call.return_data[0]


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mowner = m_newOwner
  log LogSetOwner(address owner=_newOwner)


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(minitialized)


# hash = 0x1644bea7
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 18]]]]
# const = None
# payable = False
def unknown1644bea7(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  return bool(mstor18m[m_param1m])


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
  mwhile [94midx < 2m:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  require calldata.size >′ 195
  require 260 <= calldata.size
  [94midx = 0
  [94ms = 164
  [94mt = 160
  mwhile [94midx < 3m:
      mem[[94mt] = cd[[94ms]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  require cd[68] <= 2
  require cd[68] <= 2
  if not cd[68]:
      mem[352] = mem[108 len 20]
      mem[384] = mem[140 len 20]
      munknownec7dd7bbm.length++
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_0 = addr(cd[4])
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_256 = cd[36]
      require cd[68] <= 2
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_512 = cd[68] or Mask(248, 8, munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_512)
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_520 = mem[364 len 20]
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_768 = mem[396 len 20]
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1024 = mem[160]
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1280 = mem[192]
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1536 = block.timestamp
      munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1792 = mem[224]
  else:
      if cd[68] == 1:
          require cd[68] <= 2
          mem[352] = mem[108 len 20]
          mem[384] = mem[140 len 20]
          munknownec7dd7bbm.length++
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_0 = addr(cd[4])
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_256 = cd[36]
          require cd[68] <= 2
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_512 = cd[68] or Mask(248, 8, munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_512)
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_520 = mem[364 len 20]
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_768 = mem[396 len 20]
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1024 = mem[160]
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1280 = mem[192]
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1536 = block.timestamp
          munknownec7dd7bbm[munknownec7dd7bbm.lengthm]m.field_1792 = mem[224]


# hash = 0x19ab7f43
# getter = None
# const = None
# payable = False
def unknown19ab7f43(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      require ext_code.size(munknown365a86fcAddress)
      call munknown365a86fcAddress.manager() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(munknown365a86fcAddress)
          call munknown365a86fcAddress.isShutDown() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'Sender is not this contract or manager'
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args mstor9
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(m_param1)
  call m_param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mstor9, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args mstor9
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
def unknown19c8916b(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >=′ 64
  return block.timestamp >= munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_256


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return munknown20531bc9Address


# hash = 0x249204ac
# getter = None
# const = None
# payable = False
def unknown249204ac(): # not payable
  require calldata.size - 4 >=′ 32
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require m('cd', 4).length <= 18446744073709551615
  require (32 * m('cd', 4).length) + 128 >= 96 and (32 * m('cd', 4).length) + 128 <= 18446744073709551615
  mem[64] = (32 * m('cd', 4).length) + 128
  mem[96] = m('cd', 4).length
  require cd[4] + (32 * m('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  mwhile [94midx < m('cd', 4).lengthm:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
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
          mem[mem[64] + 4] = mstor9
          require ext_code.size(addr([94m_150))
          call addr([94m_150).balanceOf(address owner) with:
               gas gas_remaining wei
              args mstor9
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
              args mstor9, [94m_162
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >=′ 32
          mem[mem[64] + 4] = mstor9
          require ext_code.size(addr([94m_150))
          call addr([94m_150).balanceOf(address owner) with:
               gas gas_remaining wei
              args mstor9
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
          require ext_code.size(munknown365a86fcAddress)
          call munknown365a86fcAddress.manager() with:
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
              mem[mem[64] + 4] = mstor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args mstor9
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
                  args mstor9, [94m_169
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              mem[mem[64] + 4] = mstor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args mstor9
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
              require ext_code.size(munknown365a86fcAddress)
              call munknown365a86fcAddress.isShutDown() with:
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
              mem[mem[64] + 4] = mstor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args mstor9
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
                  args mstor9, [94m_177
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              mem[mem[64] + 4] = mstor9
              require ext_code.size(addr([94m_150))
              call addr([94m_150).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args mstor9
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
      mcontinue 


# hash = 0x2839fc29
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def exchanges(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require m_param1 < mexchangesm.length
  return mexchangesm[m_param1m]m.field_0, mexchangesm[m_param1m]m.field_256, bool(mexchangesm[m_param1m]m.field_416)


# hash = 0x28f5cd02
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 20]]]
# const = None
# payable = False
def unknown28f5cd02(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  return munknown28f5cd02m[m_param1m]


# hash = 0x2e62efbb
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 19]]]]]
# const = None
# payable = False
def unknown2e62efbb(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >=′ 64
  return munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_0, 
         munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_256,
         munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_512


# hash = 0x365a86fc
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown365a86fc(): # not payable
  return munknown365a86fcAddress


# hash = 0x3eb544e0
# getter = None
# const = ['return', 1800]
# payable = False
const unknown3eb544e0 = 1800


# hash = 0x4a194903
# getter = None
# const = None
# payable = True
def unknown4a194903(addr m_param1) payable: 
  mem[64] = 96
  require not call.value
  require calldata.size - 4 >=′ 32
  [94midx = 0
  mwhile [94midx < mexchangesm.lengthm:
      mem[0] = m_param1
      mem[32] = sha3(mexchangesm[[94midxm]m.field_0, 19)
      if munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0:
          require [94midx < mexchangesm.length
          mem[32] = sha3(mexchangesm[[94midxm]m.field_0, 19)
          require ext_code.size(mexchangesm[[94midxm]m.field_256)
          call mexchangesm[[94midxm]m.field_256.0xd7d1c4d5 with:
               gas gas_remaining wei
              args mexchangesm[[94midxm]m.field_0, munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0, m_param1
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
              require [94midx < mexchangesm.length
              mem[32] = 21
              if mstor21m[addr(m_param1)m]:
                  if block.timestamp + 1800 < block.timestamp:
                      revert with 0, 'ds-math-add-overflow'
                  munknowncc460a02m[addr(m_param1)m] = block.timestamp + 1800
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_0 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_256 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_512 = 0
                  munknown2e62efbbm[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768 = 0
                  if munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m] - 1 > munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m]:
                      revert with 0, 'ds-math-sub-underflow'
                  mem[32] = 20
                  munknown28f5cd02m[mstor19m[mstor16m[[94midxm]m.field_0m]m[addr(m_param1)m]m.field_768m]--
              if [94m_55 < 0:
                  revert with 0, 'ds-math-add-overflow'
          require [94midx < mexchangesm.length
          mem[0] = 16
      [94midx = [94midx + 1
      mcontinue 
  mstor21m[addr(m_param1)m] = 0
  return 0


# hash = 0x5202d6d6
# getter = None
# const = None
# payable = False
def unknown5202d6d6(addr m_param1, addr m_param2, addr m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require calldata.size - 4 >=′ 160
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  if mstor21m[addr(m_param2)m]:
      revert with 0, 'Asset already in open order'
  if 0 >= munknownec7dd7bbm.length:
      revert with 0, 'No orders in array'
  if block.timestamp + (24 * 3600) < block.timestamp:
      revert with 0, 'ds-math-add-overflow'
  if not m_param5:
      if block.timestamp + (24 * 3600) <= block.timestamp:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      mstor21m[addr(m_param2)m] = 1
      munknowncc460a02m[addr(m_param2)m] = block.timestamp + 88200
      if munknown28f5cd02m[addr(m_param3)m] + 1 < munknown28f5cd02m[addr(m_param3)m]:
          revert with 0, 'ds-math-add-overflow'
      munknown28f5cd02m[addr(m_param3)m]++
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_0 = m_param4
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_256 = block.timestamp + (24 * 3600)
  else:
      if m_param5 > block.timestamp + (24 * 3600):
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      if m_param5 <= block.timestamp:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'Expiry time greater than max order lifespan or has already passed'
      mstor21m[addr(m_param2)m] = 1
      if m_param5 + 1800 < m_param5:
          revert with 0, 'ds-math-add-overflow'
      munknowncc460a02m[addr(m_param2)m] = m_param5 + 1800
      if munknown28f5cd02m[addr(m_param3)m] + 1 < munknown28f5cd02m[addr(m_param3)m]:
          revert with 0, 'ds-math-add-overflow'
      munknown28f5cd02m[addr(m_param3)m]++
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_0 = m_param4
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_256 = m_param5
  if munknownec7dd7bbm.length - 1 > munknownec7dd7bbm.length:
      revert with 0, 'ds-math-sub-underflow'
  munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_512 = munknownec7dd7bbm.length - 1
  munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_768 = m_param3


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return mversionAddress


# hash = 0x69bfce2f
# getter = None
# const = None
# payable = False
def unknown69bfce2f(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[896] = mstor23m[m_param1m]m[10m]m.field_0
  [94midx = 896
  [94ms = 0
  mwhile mstor23m[m_param1m]m[10m]m.length + 864 > [94midxm:
      mem[[94midx + 32] = mstor23m[m_param1m]m[[94ms + 10m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 928] = mstor23m[m_param1m]m[11m]m.field_0
  [94midx = ceil32(mstor23m[m_param1m]m[10m]m.length) + 928
  [94ms = 0
  mwhile ceil32(mstor23m[m_param1m]m[10m]m.length) + mstor23m[m_param1m]m[11m]m.length + 896 > [94midxm:
      mem[[94midx + 32] = mstor23m[m_param1m]m[[94ms + 11m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  if ceil32(mstor23m[m_param1m]m[10m]m.length) <= mstor23m[m_param1m]m[10m]m.length:
      mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 1376] = mstor23m[m_param1m]m[11m]m.length
      mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 1408 len ceil32(mstor23m[m_param1m]m[11m]m.length)] = mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 928 len ceil32(mstor23m[m_param1m]m[11m]m.length)]
      if ceil32(mstor23m[m_param1m]m[11m]m.length) > mstor23m[m_param1m]m[11m]m.length:
          mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[11m]m.length + 1408] = 0
      return 32, mstor23m[m_param1m]m.field_0, 
             mstor23m[m_param1m]m.field_256,
             mstor23m[m_param1m]m.field_512,
             mstor23m[m_param1m]m.field_768,
             mstor23m[m_param1m]m.field_1024,
             mstor23m[m_param1m]m.field_1280,
             mstor23m[m_param1m]m.field_1536,
             mstor23m[m_param1m]m.field_1792,
             mstor23m[m_param1m]m.field_2048,
             mstor23m[m_param1m]m.field_2304,
             384,
             ceil32(mstor23m[m_param1m]m[10m]m.length) + 416,
             mstor23m[m_param1m]m[10m]m.length,
             mem[896 len ceil32(mstor23m[m_param1m]m[10m]m.length)],
             mstor23m[m_param1m]m[11m]m.length,
             mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 928 len ceil32(mstor23m[m_param1m]m[11m]m.length)]
  mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[10m]m.length + 1376] = 0
  mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 1376] = mstor23m[m_param1m]m[11m]m.length
  mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 1408 len ceil32(mstor23m[m_param1m]m[11m]m.length)] = mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 928 len ceil32(mstor23m[m_param1m]m[11m]m.length)]
  if ceil32(mstor23m[m_param1m]m[11m]m.length) > mstor23m[m_param1m]m[11m]m.length:
      mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[11m]m.length + 1408] = 0
  return 32, mstor23m[m_param1m]m.field_0, 
         mstor23m[m_param1m]m.field_256,
         mstor23m[m_param1m]m.field_512,
         mstor23m[m_param1m]m.field_768,
         mstor23m[m_param1m]m.field_1024,
         mstor23m[m_param1m]m.field_1280,
         mstor23m[m_param1m]m.field_1536,
         mstor23m[m_param1m]m.field_1792,
         mstor23m[m_param1m]m.field_2048,
         mstor23m[m_param1m]m.field_2304,
         384,
         ceil32(mstor23m[m_param1m]m[10m]m.length) + 416,
         mstor23m[m_param1m]m[10m]m.length,
         mem[896 len mstor23m[m_param1m]m[10m]m.length],
         0,
         mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[10m]m.length + 1408 len ceil32(mstor23m[m_param1m]m[10m]m.length) + ceil32(mstor23m[m_param1m]m[11m]m.length) - mstor23m[m_param1m]m[10m]m.length]


# hash = 0x77076855
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 21]]]]
# const = None
# payable = False
def unknown77076855(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  return bool(mstor21m[m_param1m])


# hash = 0x7a9e5e4b
# getter = None
# const = None
# payable = False
def setAuthority(address m_authority): # not payable
  require calldata.size - 4 >=′ 32
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mauthorityAddress = m_authority_
  log LogSetAuthority(address authority=_authority_)


# hash = 0x7b103999
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def registry(): # not payable
  return mregistryAddress


# hash = 0x83259ed9
# getter = None
# const = None
# payable = False
def unknown83259ed9(addr m_param1, addr m_param2, addr m_param3, addr m_param4, addr m_param5, addr m_param6, addr m_param7, addr m_param8, addr m_param9, addr m_param10, addr m_param11, addr m_param12): # not payable
  require calldata.size - 4 >=′ 384
  require calldata.size >= 388
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  require caller == munknown365a86fcAddress
  if minitialized:
      revert with 0, 'Already initialized'
  mstor3 = m_param1
  mstor4 = m_param2
  mstor5 = m_param3
  mstor6 = m_param4
  mstor7 = m_param5
  mstor8 = m_param6
  mstor9 = m_param7
  munknown20531bc9Address = m_param8
  mregistryAddress = m_param9
  mversionAddress = m_param10
  munknownc9d4623fAddress = m_param11
  munknown8a471df9Address = m_param12
  minitialized = 1
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, addr(this.address), mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mowner = 0
  log LogSetOwner(address owner)
  log 0x0 


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return munknown8a471df9Address


# hash = 0x8bc5b3c5
# getter = None
# const = None
# payable = False
def unknown8bc5b3c5(): # not payable
  mem[96] = mexchangesm.length
  if not mexchangesm.length:
      mem[(32 * mexchangesm.length) + 128] = mexchangesm.length
      mem[(64 * mexchangesm.length) + 160] = mexchangesm.length
      mem[64] = (98 * mexchangesm.length) + 192
      [94midx = 0
      mwhile [94midx < mexchangesm.lengthm:
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = mexchangesm[[94midxm]m.field_0
          require [94midx < mexchangesm.length
          require [94midx < mem[(32 * mexchangesm.length) + 128]
          mem[(32 * mexchangesm.length) + (32 * [94midx) + 160] = mexchangesm[[94midxm]m.field_256
          require [94midx < mexchangesm.length
          mem[0] = 16
          require [94midx < mem[(64 * mexchangesm.length) + 160]
          mem[(64 * mexchangesm.length) + (32 * [94midx) + 192] = bool(mexchangesm[[94midxm]m.field_416)
          [94midx = [94midx + 1
          mcontinue 
      [94m_34 = mem[64]
      mem[mem[64]] = 96
      [94m_44 = mem[96]
      mem[mem[64] + 96] = mem[96]
      [94midx = 0
      [94ms = 128
      [94mt = mem[64] + 128
      mwhile [94midx < [94m_44m:
          mem[[94mt] = mem[[94ms + 12 len 20]
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          mcontinue 
      mem[mem[64] + 32] = (32 * [94m_44) + 128
      [94m_64 = mem[(32 * mexchangesm.length) + 128]
      mem[[94m_34 + (32 * [94m_44) + 128] = mem[(32 * mexchangesm.length) + 128]
      [94midx = 0
      [94ms = (32 * mexchangesm.length) + 160
      [94mt = [94m_34 + (32 * [94m_44) + 160
      mwhile [94midx < [94m_64m:
          mem[[94mt] = mem[[94ms + 12 len 20]
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          mcontinue 
      mem[[94m_34 + 64] = (32 * [94m_44) + (32 * [94m_64) + 160
      [94m_76 = mem[(64 * mexchangesm.length) + 160]
      mem[[94m_34 + (32 * [94m_44) + (32 * [94m_64) + 160] = mem[(64 * mexchangesm.length) + 160]
      [94midx = 0
      [94ms = (64 * mexchangesm.length) + 192
      [94mt = [94m_34 + (32 * [94m_44) + (32 * [94m_64) + 192
      mwhile [94midx < [94m_76m:
          mem[[94mt] = bool(mem[[94ms])
          [94midx = [94midx + 1
          [94ms = [94ms + 32
          [94mt = [94mt + 32
          mcontinue 
      return memory
        from mem[64]
         [93mlen [94m_34 + (32 * [94m_44) + (32 * [94m_64) + (32 * [94m_76) + -mem[64] + 192
  mem[128 len 32 * mexchangesm.length] = code.data[16133 len 32 * mexchangesm.length]
  mem[(32 * mexchangesm.length) + 128] = mexchangesm.length
  mem[(32 * mexchangesm.length) + 160 len 32 * mexchangesm.length] = code.data[16133 len 32 * mexchangesm.length]
  mem[(64 * mexchangesm.length) + 160] = mexchangesm.length
  mem[64] = (98 * mexchangesm.length) + 192
  mem[(64 * mexchangesm.length) + 192 len 32 * mexchangesm.length] = code.data[16133 len 32 * mexchangesm.length]
  [94midx = 0
  mwhile [94midx < mexchangesm.lengthm:
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = mexchangesm[[94midxm]m.field_0
      require [94midx < mexchangesm.length
      require [94midx < mem[(32 * mexchangesm.length) + 128]
      mem[(32 * mexchangesm.length) + (32 * [94midx) + 160] = mexchangesm[[94midxm]m.field_256
      require [94midx < mexchangesm.length
      mem[0] = 16
      require [94midx < mem[(64 * mexchangesm.length) + 160]
      mem[(64 * mexchangesm.length) + (32 * [94midx) + 192] = bool(mexchangesm[[94midxm]m.field_416)
      [94midx = [94midx + 1
      mcontinue 
  [94m_37 = mem[64]
  mem[mem[64]] = 96
  [94m_45 = mem[96]
  mem[mem[64] + 96] = mem[96]
  [94midx = 0
  [94ms = 128
  [94mt = mem[64] + 128
  mwhile [94midx < [94m_45m:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  mem[[94m_37 + 32] = (32 * [94m_45) + 128
  [94m_65 = mem[(32 * mexchangesm.length) + 128]
  mem[[94m_37 + (32 * [94m_45) + 128] = mem[(32 * mexchangesm.length) + 128]
  [94midx = 0
  [94ms = (32 * mexchangesm.length) + 160
  [94mt = [94m_37 + (32 * [94m_45) + 160
  mwhile [94midx < [94m_65m:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  mem[[94m_37 + 64] = (32 * [94m_45) + (32 * [94m_65) + 160
  [94m_77 = mem[(64 * mexchangesm.length) + 160]
  mem[[94m_37 + (32 * [94m_45) + (32 * [94m_65) + 160] = mem[(64 * mexchangesm.length) + 160]
  [94midx = 0
  [94ms = (64 * mexchangesm.length) + 192
  [94mt = [94m_37 + (32 * [94m_45) + (32 * [94m_65) + 192
  mwhile [94midx < [94m_77m:
      mem[[94mt] = bool(mem[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  return memory
    from mem[64]
     [93mlen [94m_37 + (32 * [94m_45) + (32 * [94m_65) + (32 * [94m_77) + -mem[64] + 192


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9b91f84a
# getter = ['struct', ['loc', 19]]
# const = None
# payable = False
def unknown9b91f84a(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >=′ 64
  return munknown2e62efbbm[m_param1m]m[m_param2m]m.field_0, 
         munknown2e62efbbm[m_param1m]m[m_param2m]m.field_256,
         munknown2e62efbbm[m_param1m]m[m_param2m]m.field_512,
         munknown2e62efbbm[m_param1m]m[m_param2m]m.field_768


# hash = 0xa85c38ef
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def orders(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require m_param1 < munknownec7dd7bbm.length
  require munknownec7dd7bbm[m_param1m]m.field_512 < 3
  return munknownec7dd7bbm[m_param1m]m.field_0, 
         munknownec7dd7bbm[m_param1m]m.field_256,
         munknownec7dd7bbm[m_param1m]m.field_512,
         munknownec7dd7bbm[m_param1m]m.field_512,
         munknownec7dd7bbm[m_param1m]m.field_768,
         munknownec7dd7bbm[m_param1m]m.field_1024,
         munknownec7dd7bbm[m_param1m]m.field_1280,
         munknownec7dd7bbm[m_param1m]m.field_1536,
         munknownec7dd7bbm[m_param1m]m.field_1792


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
  return mstor3, 
         mstor4,
         mstor5,
         mstor6,
         mstor7,
         mstor8,
         mstor9,
         munknown20531bc9Address,
         mregistryAddress,
         mversionAddress,
         munknownc9d4623fAddress,
         munknown8a471df9Address


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return mauthorityAddress


# hash = 0xc3394ef7
# getter = None
# const = None
# payable = False
def unknownc3394ef7(): # not payable
  require calldata.size - 4 >=′ 64
  require cd[36] <= 18446744073709551615
  require calldata.size + -cd[36] - 4 >=′ 384
  require m('cd', 36)[9] <= 18446744073709551615
  require calldata.size >′ cd[36] + m('cd', 36)[9] + 35
  require cd[(cd[36] + m('cd', 36)[9] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 512 >= 480 and ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 512 <= 18446744073709551615
  require cd[36] + m('cd', 36)[9] + cd[(cd[36] + m('cd', 36)[9] + 4)] + 36 <= calldata.size
  require m('cd', 36)[10] <= 18446744073709551615
  require calldata.size >′ cd[36] + m('cd', 36)[10] + 35
  require cd[(cd[36] + m('cd', 36)[10] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[36] + m('cd', 36)[10] + 4)]) + 544 >= 512 and ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + ceil32(cd[(cd[36] + m('cd', 36)[10] + 4)]) + 544 <= 18446744073709551615
  mem[ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 512] = cd[(cd[36] + m('cd', 36)[10] + 4)]
  require cd[36] + m('cd', 36)[10] + cd[(cd[36] + m('cd', 36)[10] + 4)] + 36 <= calldata.size
  mem[ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 544 len cd[(cd[36] + m('cd', 36)[10] + 4)]] = call.data[cd[36] + m('cd', 36)[10] + 36 len cd[(cd[36] + m('cd', 36)[10] + 4)]]
  mem[cd[(cd[36] + m('cd', 36)[10] + 4)] + ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 544] = 0
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  mstor23m[cd[4]m]m.field_0 = addr(m('cd', 36).length)
  mstor23m[cd[4]m]m.field_256 = addr(m('cd', 36)[0])
  mstor23m[cd[4]m]m.field_512 = addr(m('cd', 36)[1])
  mstor23m[cd[4]m]m.field_768 = addr(m('cd', 36)[2])
  mstor23m[cd[4]m]m.field_1024 = m('cd', 36)[3]
  mstor23m[cd[4]m]m.field_1280 = m('cd', 36)[4]
  mstor23m[cd[4]m]m.field_1536 = m('cd', 36)[5]
  mstor23m[cd[4]m]m.field_1792 = m('cd', 36)[6]
  mstor23m[cd[4]m]m.field_2048 = m('cd', 36)[7]
  mstor23m[cd[4]m]m.field_2304 = m('cd', 36)[8]
  mstor23m[cd[4]m]m[10m]m[m]m.field_0 = Array(len=cd[(cd[36] + m('cd', 36)[9] + 4)], data=call.data[cd[36] + m('cd', 36)[9] + 36 len cd[(cd[36] + m('cd', 36)[9] + 4)]])
  mstor23m[cd[4]m]m[11m]m[m]m.field_0 = Array(len=Mask(8 * -ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + cd[(cd[36] + m('cd', 36)[9] + 4)] + 32, 0, 0), mem[cd[(cd[36] + m('cd', 36)[9] + 4)] + 544 len -cd[(cd[36] + m('cd', 36)[9] + 4)] + ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)])], data=mem[ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + 544 len Mask(8 * -ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)]) + cd[(cd[36] + m('cd', 36)[9] + 4)] + 32, 0, 0), mem[cd[(cd[36] + m('cd', 36)[9] + 4)] + 544 len -cd[(cd[36] + m('cd', 36)[9] + 4)] + ceil32(cd[(cd[36] + m('cd', 36)[9] + 4)])]])


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return munknownc9d4623fAddress


# hash = 0xcc460a02
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 22]]]
# const = None
# payable = False
def unknowncc460a02(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  return munknowncc460a02m[m_param1m]


# hash = 0xda855f3a
# getter = None
# const = None
# payable = False
def unknownda855f3a(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  mem[128] = mstor23m[m_param1m]m[10m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor23m[m_param1m]m[10m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor23m[m_param1m]m[[94ms + 10m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 160] = mstor23m[m_param1m]m[11m]m.field_0
  [94midx = ceil32(mstor23m[m_param1m]m[10m]m.length) + 160
  [94ms = 0
  mwhile ceil32(mstor23m[m_param1m]m[10m]m.length) + mstor23m[m_param1m]m[11m]m.length + 128 > [94midxm:
      mem[[94midx + 32] = mstor23m[m_param1m]m[[94ms + 11m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  if ceil32(mstor23m[m_param1m]m[10m]m.length) > mstor23m[m_param1m]m[10m]m.length:
      mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[10m]m.length + 576] = 0
  mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 576] = mstor23m[m_param1m]m[11m]m.length
  mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + 608 len ceil32(mstor23m[m_param1m]m[11m]m.length)] = mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 160 len ceil32(mstor23m[m_param1m]m[11m]m.length)]
  if ceil32(mstor23m[m_param1m]m[11m]m.length) > mstor23m[m_param1m]m[11m]m.length:
      mem[(2 * ceil32(mstor23m[m_param1m]m[10m]m.length)) + ceil32(mstor23m[m_param1m]m[11m]m.length) + mstor23m[m_param1m]m[11m]m.length + 608] = 0
  return mstor23m[m_param1m]m.field_0, 
         mstor23m[m_param1m]m.field_256,
         mstor23m[m_param1m]m.field_512,
         mstor23m[m_param1m]m.field_768,
         mstor23m[m_param1m]m.field_1024,
         mstor23m[m_param1m]m.field_1280,
         mstor23m[m_param1m]m.field_1536,
         mstor23m[m_param1m]m.field_1792,
         mstor23m[m_param1m]m.field_2048,
         mstor23m[m_param1m]m.field_2304,
         Array(len=mstor23m[m_param1m]m[10m]m.length, data=mem[128 len ceil32(mstor23m[m_param1m]m[10m]m.length)], mstor23m[m_param1m]m[11m]m.length, mem[ceil32(mstor23m[m_param1m]m[10m]m.length) + 160 len ceil32(mstor23m[m_param1m]m[11m]m.length)]),
         ceil32(mstor23m[m_param1m]m[10m]m.length) + 416


# hash = 0xec7dd7bb
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknownec7dd7bb(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require m_param1 < munknownec7dd7bbm.length
  require munknownec7dd7bbm[m_param1m]m.field_512 <= 2
  return munknownec7dd7bbm[m_param1m]m.field_512, 
         munknownec7dd7bbm[m_param1m]m.field_768,
         munknownec7dd7bbm[m_param1m]m.field_1024,
         munknownec7dd7bbm[m_param1m]m.field_1280


# hash = 0xfcfdcf8a
# getter = None
# const = None
# payable = False
def unknownfcfdcf8a(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >=′ 64
  if caller != this.address:
      revert with 0, 'Sender is not this contract'
  if mstor21m[addr(m_param2)m]:
      if block.timestamp + 1800 < block.timestamp:
          revert with 0, 'ds-math-add-overflow'
      munknowncc460a02m[addr(m_param2)m] = block.timestamp + 1800
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_0 = 0
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_256 = 0
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_512 = 0
      munknown2e62efbbm[addr(m_param1)m]m[addr(m_param2)m]m.field_768 = 0
      if munknown28f5cd02m[mstor19m[addr(m_param1)m]m[addr(m_param2)m]m.field_768m] - 1 > munknown28f5cd02m[mstor19m[addr(m_param1)m]m[addr(m_param2)m]m.field_768m]:
          revert with 0, 'ds-math-sub-underflow'
      munknown28f5cd02m[mstor19m[addr(m_param1)m]m[addr(m_param2)m]m.field_768m]--


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


