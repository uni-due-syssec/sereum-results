# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x677aA1dc08B9429c595efD4425b2D218cC22fD6E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x7e944756': 'unknown7e944756(?)'} 

# storage definitions
def storage:
    # storage address 1
    ownerOf
    # storage address 0
    balanceOf
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    totalSupply # mask: a s
    # storage address 4
    stor4
    # storage address 3
    stor3
    # storage address 6
    paused # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    owner # mask: a s
    # storage address 2
    stor2
# hash = 0x06fdde03
# getter = None
# const = ['return', ['data', ['arr', 8, ['mask_shl', 64, 0, 0, "'EtherGen'"]]]]
# payable = False
const name = 'EtherGen'


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require mownerOfm[m_value << 192m]m.field_256 == caller
  mstor4m[m_value << 192m] = m_spender
  log Approval(
        address owner=caller,
        address spender=addr(_spender),
        uint256 value=uint64(_value))


# hash = 0x16c38b3c
# getter = None
# const = None
# payable = False
def setPaused(bool m_pause): # not payable
  require mowner == caller
  mstor6 = Mask(96, 0, m_pause)


# hash = 0x18160ddd
# getter = ['storage', 64, 0, 5]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require mownerOfm[m_value << 192m]m.field_256 == m_from
  if not mstor2m[callerm]:
      require mstor4m[m_value << 192m] == caller
  if not mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_256:
      require not mownerOfm[m_value << 192m]m.field_512
  require ext_code.size(addr(mstor5m.field_64))
  call addr(mstor5m.field_64).0x24fd0a5c with:
       gas gas_remaining - 710 wei
      args uint64(m_value)
  require ext_call.success
  require ext_call.return_data[0]
  require not mpaused
  if mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 > 1:
      require mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1 < mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0
      require mownerOfm[m_value << 192m]m.field_64 < mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0
      mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[mstor1m[m_value << 192m]m.field_66m]m.field_0 = mstor('array', ('div', 0.25, ('add', -1, ('stor', 256, 0, ('map', ('stor', 160, 256, ('map', ('mask_shl', 64, 0, 192, ('param', '_value')), ('name', 'stor1', 1))), ('name', 'stor0', 0))))), ('map', ('stor', 160, 256, ('map', ('mask_shl', 64, 0, 192, ('param', '_value')), ('name', 'stor1', 1))), ('name', 'stor0', 0)))m[uint8(mstor0m[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1)m] * 256^(8 * mownerOfm[m_value << 192m]m.field_64) or mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[mstor1m[m_value << 192m]m.field_66m]m.field_0 and !(18446744073709551615 * 256^(8 * mownerOfm[m_value << 192m]m.field_64))
      mownerOfm[mstor0m[mownerOfm[m_value << 192m]m.field_256m]m[0.25 / mstor0m[mownerOfm[m_value << 192m]m.field_256m]m.field_0 - 1m]m.field_(64 * stor0[ownerOf[_value << 192].field_256].field_0 - 1 % 4) - 192m]m.field_64 = mownerOfm[m_value << 192m]m.field_64
  mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0--
  if not mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 <= mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1:
      [94midx = mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 + 2 / 4
      mwhile mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 + 3 / 4 > [94midxm:
          mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mownerOfm[m_value << 192m]m.field_256 = 0
  if m_to:
      mownerOfm[m_value << 192m]m.field_256 = m_to
      mbalanceOfm[addr(m_to)m]m.field_0++
      if not mbalanceOfm[addr(m_to)m]m.field_0 <= mbalanceOfm[addr(m_to)m]m.field_0 + 1:
          [94midx = mbalanceOfm[addr(m_to)m]m.field_0 + 4 / 4
          mwhile mbalanceOfm[addr(m_to)m]m.field_0 + 3 / 4 > [94midxm:
              mbalanceOfm[addr(m_to)m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      mbalanceOfm[addr(m_to)m]m[mbalanceOfm[addr(m_to)m]m.field_2m]m.field_0 = uint64(m_value) * 256^(8 * mbalanceOfm[addr(m_to)m]m.field_0) or mbalanceOfm[addr(m_to)m]m[mbalanceOfm[addr(m_to)m]m.field_2m]m.field_0 and !(18446744073709551615 * 256^(8 * mbalanceOfm[addr(m_to)m]m.field_0))
      mownerOfm[m_value << 192m]m.field_64 = mbalanceOfm[addr(m_to)m]m.field_0
  log Transfer(
        address from=addr(_from),
        address to=addr(_to),
        uint256 value=uint64(_value))


# hash = 0x2afb9fb1
# getter = None
# const = None
# payable = False
def unknown2afb9fb1(uint64 m_param1): # not payable
  if mbalanceOfm[mstor1m[m_param1 << 192m]m.field_256m]m.field_256:
      return bool(mbalanceOfm[mstor1m[m_param1 << 192m]m.field_256m]m.field_256)
  return not bool(mownerOfm[m_param1 << 192m]m.field_512)


# hash = 0x3c2aba9f
# getter = None
# const = None
# payable = False
def unknown3c2aba9f(addr m_param1, bool m_param2): # not payable
  require mowner == caller
  mstor2m[addr(m_param1)m] = uint8(m_param2)


# hash = 0x45ddcf99
# getter = None
# const = None
# payable = False
def unknown45ddcf99(addr m_param1): # not payable
  require mstor2m[callerm]
  mbalanceOfm[addr(m_param1)m]m.field_256 = 1


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x6352211e
# getter = ['storage', 160, 0, ['add', 1, ['sha3', ['data', ['mask_shl', 64, 0, 192, ['cd', 4]], 1]]]]
# const = None
# payable = False
def ownerOf(uint256 m_tokenId): # not payable
  return mownerOfm[m_tokenId << 192m]m.field_256


# hash = 0x6e9ffe2b
# getter = None
# const = None
# payable = False
def unknown6e9ffe2b(addr m_param1): # not payable
  require mowner == caller
  addr(mstor5m.field_64) = m_param1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]m.field_0


# hash = 0x8462151c
# getter = None
# const = None
# payable = False
def tokensOfOwner(address m_owner): # not payable
  if not mbalanceOfm[addr(m_owner)m]m.field_0:
      mem[(32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 160] = 32
      mem[(32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 192] = mbalanceOfm[addr(m_owner)m]m.field_0
      mem[(32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 224 len floor32(mbalanceOfm[addr(m_owner)m]m.field_0)] = mem[160 len floor32(mbalanceOfm[addr(m_owner)m]m.field_0)]
      return memory
        from (32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 160
         [93mlen (96 * mbalanceOfm[addr(m_owner)m]m.field_0) + 64
  mem[160] = mbalanceOfm[addr(m_owner)m]m.field_0
  [94midx = 160
  [94ms = 0
  mwhile (32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 128 > [94midxm:
      mem[[94midx + 32] = mbalanceOfm[addr(m_owner)m]m.field_8 * (8 * -(s + 15 / 32) + 1) + s - (s + 15 / 32 * s)
      [94midx = [94midx + 32
      [94ms = (8 * -([94ms + 15 / 32) + 1) + [94ms - ([94ms + 15 / 32 * [94ms)
      mcontinue 
  mem[(32 * mbalanceOfm[addr(m_owner)m]m.field_0) + 224 len floor32(mbalanceOfm[addr(m_owner)m]m.field_0)] = mem[160 len floor32(mbalanceOfm[addr(m_owner)m]m.field_0)]
  return Array(len=mbalanceOfm[addr(m_owner)m]m.field_0, data=mem[160 len floor32(mbalanceOfm[addr(m_owner)m]m.field_0)], mem[(32 * mbalanceOfm[addr(m_owner)m]m.field_0) + floor32(mbalanceOfm[addr(m_owner)m]m.field_0) + 224 len (32 * mbalanceOfm[addr(m_owner)m]m.field_0) - floor32(mbalanceOfm[addr(m_owner)m]m.field_0)]), 


# hash = 0x880cdc31
# getter = None
# const = None
# payable = False
def updateOwner(address m_owner): # not payable
  require mowner == caller
  mowner = m_owner


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x95d89b41
# getter = None
# const = ['return', ['data', ['arr', 3, ['mask_shl', 24, 0, 0, "'ETG'"]]]]
# payable = False
const symbol = 'ETG'


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  require mownerOfm[m_value << 192m]m.field_256 == caller
  if not mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_256:
      require not mownerOfm[m_value << 192m]m.field_512
  require ext_code.size(addr(mstor5m.field_64))
  call addr(mstor5m.field_64).0x24fd0a5c with:
       gas gas_remaining - 710 wei
      args uint64(m_value)
  require ext_call.success
  require ext_call.return_data[0]
  require not mpaused
  if mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 > 1:
      require mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1 < mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0
      require mownerOfm[m_value << 192m]m.field_64 < mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0
      mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[mstor1m[m_value << 192m]m.field_66m]m.field_0 = mstor('array', ('div', 0.25, ('add', -1, ('stor', 256, 0, ('map', ('stor', 160, 256, ('map', ('mask_shl', 64, 0, 192, ('param', '_value')), ('name', 'stor1', 1))), ('name', 'stor0', 0))))), ('map', ('stor', 160, 256, ('map', ('mask_shl', 64, 0, 192, ('param', '_value')), ('name', 'stor1', 1))), ('name', 'stor0', 0)))m[uint8(mstor0m[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1)m] * 256^(8 * mownerOfm[m_value << 192m]m.field_64) or mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[mstor1m[m_value << 192m]m.field_66m]m.field_0 and !(18446744073709551615 * 256^(8 * mownerOfm[m_value << 192m]m.field_64))
      mownerOfm[mstor0m[mownerOfm[m_value << 192m]m.field_256m]m[0.25 / mstor0m[mownerOfm[m_value << 192m]m.field_256m]m.field_0 - 1m]m.field_(64 * stor0[ownerOf[_value << 192].field_256].field_0 - 1 % 4) - 192m]m.field_64 = mownerOfm[m_value << 192m]m.field_64
  mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0--
  if not mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 <= mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 - 1:
      [94midx = mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 + 2 / 4
      mwhile mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m.field_0 + 3 / 4 > [94midxm:
          mbalanceOfm[mstor1m[m_value << 192m]m.field_256m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mownerOfm[m_value << 192m]m.field_256 = 0
  if m_to:
      mownerOfm[m_value << 192m]m.field_256 = m_to
      mbalanceOfm[addr(m_to)m]m.field_0++
      if not mbalanceOfm[addr(m_to)m]m.field_0 <= mbalanceOfm[addr(m_to)m]m.field_0 + 1:
          [94midx = mbalanceOfm[addr(m_to)m]m.field_0 + 4 / 4
          mwhile mbalanceOfm[addr(m_to)m]m.field_0 + 3 / 4 > [94midxm:
              mbalanceOfm[addr(m_to)m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      mbalanceOfm[addr(m_to)m]m[mbalanceOfm[addr(m_to)m]m.field_2m]m.field_0 = uint64(m_value) * 256^(8 * mbalanceOfm[addr(m_to)m]m.field_0) or mbalanceOfm[addr(m_to)m]m[mbalanceOfm[addr(m_to)m]m.field_2m]m.field_0 and !(18446744073709551615 * 256^(8 * mbalanceOfm[addr(m_to)m]m.field_0))
      mownerOfm[m_value << 192m]m.field_64 = mbalanceOfm[addr(m_to)m]m.field_0
  log Transfer(
        address from=caller,
        address to=addr(_to),
        uint256 value=uint64(_value))


# hash = 0xcfbed755
# getter = None
# const = None
# payable = False
def unknowncfbed755(uint64 m_param1): # not payable
  if mownerOfm[m_param1 << 192m]m.field_520:
      if mbalanceOfm[mstor1m[m_param1 << 192m]m.field_256m]m.field_256:
          return mownerOfm[m_param1 << 192m]m.field_256, 
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 1,
                 1
      if not mownerOfm[m_param1 << 192m]m.field_512:
          return mownerOfm[m_param1 << 192m]m.field_256, 
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 mownerOfm[m_param1 << 192m]m.field_256,
                 1,
                 1
      return mownerOfm[m_param1 << 192m]m.field_256, 
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             1,
             0
  if mbalanceOfm[mstor1m[m_param1 << 192m]m.field_256m]m.field_256:
      return mownerOfm[m_param1 << 192m]m.field_256, 
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             0,
             1
  if not mownerOfm[m_param1 << 192m]m.field_512:
      return mownerOfm[m_param1 << 192m]m.field_256, 
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             mownerOfm[m_param1 << 192m]m.field_256,
             0,
             1
  return mownerOfm[m_param1 << 192m]m.field_256, 
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         mownerOfm[m_param1 << 192m]m.field_256,
         0,
         0


# hash = 0xd213ed96
# getter = None
# const = None
# payable = False
def unknownd213ed96(addr m_param1, bool m_param2): # not payable
  require mowner == caller
  mstor3m[addr(m_param1)m] = uint8(m_param2)


# hash = 0xfd6ba459
# getter = None
# const = None
# payable = False
def unknownfd6ba459(addr m_param1, uint8 m_param2, uint8 m_param3, uint8 m_param4, uint8 m_param5, uint8 m_param6, uint8 m_param7, uint8 m_param8, uint8 m_param9, uint8 m_param10, uint8 m_param11, uint8 m_param12, uint8 m_param13, uint8 m_param14, uint8 m_param15): # not payable
  require mstor3m[callerm]
  require not mpaused
  mtotalSupply = uint64(mtotalSupply + 1)
  mownerOfm[uint64(mstor5m.field_0)m]m.field_0 = mtotalSupply
  mownerOfm[uint64(mstor5m.field_0)m]m.field_64 = 0
  mownerOfm[uint64(mstor5m.field_0)m]m.field_256 = 0
  mownerOfm[uint64(mstor5m.field_0)m]m.field_256 = m_param1
  mownerOfm[uint64(mstor5m.field_0)m]m.field_416 = m_param2
  mownerOfm[uint64(mstor5m.field_0)m]m.field_424 = m_param3
  mownerOfm[uint64(mstor5m.field_0)m]m.field_432 = m_param4
  mownerOfm[uint64(mstor5m.field_0)m]m.field_440 = m_param5
  mownerOfm[uint64(mstor5m.field_0)m]m.field_448 = m_param6
  mownerOfm[uint64(mstor5m.field_0)m]m.field_456 = m_param7
  mownerOfm[uint64(mstor5m.field_0)m]m.field_464 = m_param8
  mownerOfm[uint64(mstor5m.field_0)m]m.field_472 = m_param9
  mownerOfm[uint64(mstor5m.field_0)m]m.field_480 = m_param10
  mownerOfm[uint64(mstor5m.field_0)m]m.field_488 = m_param11
  mownerOfm[uint64(mstor5m.field_0)m]m.field_496 = m_param12
  mownerOfm[uint64(mstor5m.field_0)m]m.field_504 = m_param13
  mownerOfm[uint64(mstor5m.field_0)m]m.field_512 = uint8(bool(1 == m_param15))
  mownerOfm[uint64(mstor5m.field_0)m]m.field_520 = Mask(248, 0, bool(1 == m_param14))
  mbalanceOfm[addr(m_param1)m]m.field_0++
  if not mbalanceOfm[addr(m_param1)m]m.field_0 <= mbalanceOfm[addr(m_param1)m]m.field_0 + 1:
      [94midx = mbalanceOfm[addr(m_param1)m]m.field_0 + 4 / 4
      mwhile mbalanceOfm[addr(m_param1)m]m.field_0 + 3 / 4 > [94midxm:
          mbalanceOfm[addr(m_param1)m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mbalanceOfm[addr(m_param1)m]m[mbalanceOfm[addr(m_param1)m]m.field_2m]m.field_0 = mtotalSupply * 256^(8 * mbalanceOfm[addr(m_param1)m]m.field_0) or !(18446744073709551615 * 256^(8 * mbalanceOfm[addr(m_param1)m]m.field_0)) and mbalanceOfm[addr(m_param1)m]m[mbalanceOfm[addr(m_param1)m]m.field_2m]m.field_0
  mownerOfm[uint64(mstor5m.field_0)m]m.field_64 = mbalanceOfm[addr(m_param1)m]m.field_0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


