# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x88AB8A9DaC865662f4F470ad90882b37C7aEDf34 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x8334d195': 'viewToken(uint256 _tokenId)', '0x9886bcfa': 'unknown9886bcfa(?)', '0xb47770a8': 'unknownb47770a8(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    ownerOf
    # storage address 2
    approved
    # storage address 3
    balanceOf
    # storage address 4
    stor4
    # storage address 5
    name
    # storage address 6
    symbol
    # storage address 7
    tokenOfOwnerByIndex
    # storage address 8
    ownedTokensIndex
    # storage address 9
    allTokens
    # storage address 10
    allTokensIndex
    # storage address 11
    tokenURI
    # storage address 12
    owner # mask: a s
    # storage address 13
    tokenTypes
    # storage address 14
    unknown50dc1722
    # storage address 15
    unknown8da0b3ee
    # storage address 17
    unknowncfbb7d9a
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 20
    stor20 # mask: a s
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23
    # storage address 24
    unknowncb19273b
    # storage address 26
    unknown2eb8c1d3
    # storage address 27
    unknown6a22a976
    # storage address 28
    unknownef8998ae
    # storage address 29
    unknowndd29dc68
    # storage address 30
    unknown7c11d624
    # storage address 31
    walletAddress # mask: a s
    # storage address 32
    unknownd4db722e
    # storage address 33
    stor33 # mask: a s
    # storage address 34
    unknownd2f0a1c9
    # storage address 35
    unknowne9fb3589
    # storage address 36
    unknownc42e532b
    # storage address 37
    unknown01d4b66a
    # storage address 38
    stor38
    # storage address 39
    unknowne88583b9
    # storage address 40
    unknown1a3eec52
    # storage address 41
    fee # mask: a s
    # storage address 42
    unknown74c7c578 # mask: a s
    # storage address 43
    name
    # storage address 44
    stor44
    # storage address 45
    stor45
# hash = 0x00ad800c
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 43]]]]], ['sha3', ['data', ['cd', 4], 43]]]]
# const = None
# payable = False
def name(uint256 m_id): # not payable
  return mnamem[m_idm]m[0 len mnamem[m_idm]m.lengthm]


# hash = 0x01d4b66a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 37]]]]]
# const = None
# payable = False
def unknown01d4b66a(uint256 m_param1, uint256 m_param2): # not payable
  return munknown01d4b66am[m_param1m]m[m_param2m]


# hash = 0x01ffc9a7
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 0]]]]
# const = None
# payable = False
def supportsInterface(bytes4 m_interfaceId): # not payable
  return bool(mstor0m[Mask(32, 224, m_interfaceId)m])


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x081812fc
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def getApproved(uint256 m_tokenId): # not payable
  return mapprovedm[m_tokenIdm]


# hash = 0x08282431
# getter = None
# const = None
# payable = False
def unknown08282431(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require caller == mowner
  if m_param4:
      munknownd2f0a1c9m[m_param3m]m[m_param5m] = m_param4
  else:
      mfee = m_param1
      munknown74c7c578 = m_param2


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require mownerOfm[m_valuem]
  require m_spender != mownerOfm[m_valuem]
  if mownerOfm[m_valuem] != caller:
      require mstor4m[mstor1m[m_valuem]m]m[callerm]
  mapprovedm[m_valuem] = m_spender
  log Approval(
        address owner=ownerOf[_value],
        address spender=_spender,
        uint256 value=_value)


# hash = 0x1450d12b
# getter = None
# const = None
# payable = True
def unknown1450d12b(uint256 m_param1, array m_param2) payable: 
  require call.value == munknown74c7c578
  require caller == mownerOfm[m_param1m]
  call mwalletAddress with:
     value munknown74c7c578 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mnamem[m_param1m]m[m] = Array(len=m_param2.length, data=m_param2[allm])


# hash = 0x14a15afa
# getter = None
# const = None
# payable = True
def unknown14a15afa(uint256 m_param1) payable: 
  if munknown2eb8c1d3m[m_param1m] != caller:
      require mownerOfm[m_param1m] == caller
  require mstor23m[m_param1m]m.field_1024 < 3
  require mstor23m[m_param1m]m.field_512 + mstor19 >= mstor23m[m_param1m]m.field_512
  require mstor20 >= 0
  require block.timestamp < mstor23m[m_param1m]m.field_512 + mstor19 + mstor20
  require call.value == munknown74c7c578
  call mwalletAddress with:
     value call.value wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mstor23m[m_param1m]m.field_1024 = 0
  require block.timestamp + mstor18 >= block.timestamp
  mstor23m[m_param1m]m.field_512 = block.timestamp + mstor18


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def totalSupply(): # not payable
  return mallTokensm.length


# hash = 0x19fa8f50
# getter = None
# const = ['return', 904250603428552709895185118199468575982109441609966099573332780532423983104]
# payable = False
const InterfaceId_ERC165 = 0x1ffc9a700000000000000000000000000000000000000000000000000000000


# hash = 0x1a3eec52
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 40]]]
# const = None
# payable = False
def unknown1a3eec52(addr m_param1): # not payable
  return munknown1a3eec52m[m_param1m]


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require mownerOfm[m_valuem]
  if mownerOfm[m_valuem] != caller:
      if mapprovedm[m_valuem] != caller:
          require mstor4m[mstor1m[m_valuem]m]m[callerm]
  require m_from
  require m_to
  require mownerOfm[m_valuem]
  require mownerOfm[m_valuem] == m_from
  if mapprovedm[m_valuem]:
      mapprovedm[m_valuem] = 0
  require mownerOfm[m_valuem]
  require mownerOfm[m_valuem] == m_from
  require 1 <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m]--
  mownerOfm[m_valuem] = 0
  require 1 <= mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mownedTokensIndexm[m_valuem] < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mstor8m[m_valuem]m]m.field_0 = mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0 = 0
  mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0--
  if mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1:
      [94midx = mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1
      mwhile mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > [94midxm:
          mtokenOfOwnerByIndexm[addr(m_from)m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mownedTokensIndexm[m_valuem] = 0
  mownedTokensIndexm[mstor7m[addr(m_from)m]m[mstor7m[addr(m_from)m]m.field_0m]m.field_0m] = mownedTokensIndexm[m_valuem]
  require not mownerOfm[m_valuem]
  mownerOfm[m_valuem] = m_to
  require mbalanceOfm[addr(m_to)m] + 1 >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m]++
  mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0++
  mtokenOfOwnerByIndexm[addr(m_to)m]m[mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0m]m.field_0 = m_value
  mownedTokensIndexm[m_valuem] = mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_value)


# hash = 0x246f04ab
# getter = None
# const = None
# payable = False
def unknown246f04ab(addr m_param1): # not payable
  if not mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0:
      mem[(32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 128] = 32
      mem[(32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 160] = mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0
      mem[(32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 192 len floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)] = mem[128 len floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)]
      return memory
        from (32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 128
         [93mlen (96 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 64
  mem[128] = mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = mtokenOfOwnerByIndexm[addr(m_param1)m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 192 len floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)] = mem[128 len floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)]
  return Array(len=mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0, data=mem[128 len floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)], mem[(32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) + 192 len (32 * mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0) - floor32(mtokenOfOwnerByIndexm[addr(m_param1)m]m.field_0)]), 


# hash = 0x2eb8c1d3
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = False
def unknown2eb8c1d3(uint256 m_param1): # not payable
  return munknown2eb8c1d3m[m_param1m]


# hash = 0x2f745c59
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 7]]], ['cd', 36]]]
# const = None
# payable = False
def tokenOfOwnerByIndex(address m_owner, uint256 m_index): # not payable
  require m_owner
  require m_index < mbalanceOfm[addr(m_owner)m]
  require m_index < mtokenOfOwnerByIndexm[addr(m_owner)m]m.field_0
  return mtokenOfOwnerByIndexm[addr(m_owner)m]m[m_indexm]m.field_0


# hash = 0x33f6832a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = False
def tokenTypes(uint256 m_param1): # not payable
  return mtokenTypesm[m_param1m]


# hash = 0x3e96a517
# getter = None
# const = None
# payable = False
def unknown3e96a517(addr m_param1): # not payable
  if not munknown6a22a976m[addr(m_param1)m]m.field_0:
      mem[(32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 128] = 32
      mem[(32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 160] = munknown6a22a976m[addr(m_param1)m]m.field_0
      mem[(32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 192 len floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)] = mem[128 len floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)]
      return memory
        from (32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 128
         [93mlen (96 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 64
  mem[128] = munknown6a22a976m[addr(m_param1)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = munknown6a22a976m[addr(m_param1)m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + 192 len floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)] = mem[128 len floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)]
  return Array(len=munknown6a22a976m[addr(m_param1)m]m.field_0, data=mem[128 len floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)], mem[(32 * munknown6a22a976m[addr(m_param1)m]m.field_0) + floor32(munknown6a22a976m[addr(m_param1)m]m.field_0) + 192 len (32 * munknown6a22a976m[addr(m_param1)m]m.field_0) - floor32(munknown6a22a976m[addr(m_param1)m]m.field_0)]), 


# hash = 0x42842e0e
# getter = None
# const = None
# payable = False
def safeTransferFrom(address m_from, address m_to, uint256 m_tokenId): # not payable
  require mownerOfm[m_tokenIdm]
  if mownerOfm[m_tokenIdm] != caller:
      if mapprovedm[m_tokenIdm] != caller:
          require mstor4m[mstor1m[m_tokenIdm]m]m[callerm]
  require mownerOfm[m_tokenIdm]
  if mownerOfm[m_tokenIdm] != caller:
      if mapprovedm[m_tokenIdm] != caller:
          require mstor4m[mstor1m[m_tokenIdm]m]m[callerm]
  require mownerOfm[m_tokenIdm]
  if mownerOfm[m_tokenIdm] != caller:
      if mapprovedm[m_tokenIdm] != caller:
          require mstor4m[mstor1m[m_tokenIdm]m]m[callerm]
  require m_from
  require m_to
  require mownerOfm[m_tokenIdm]
  require mownerOfm[m_tokenIdm] == m_from
  if mapprovedm[m_tokenIdm]:
      mapprovedm[m_tokenIdm] = 0
  require mownerOfm[m_tokenIdm]
  require mownerOfm[m_tokenIdm] == m_from
  require 1 <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m]--
  mownerOfm[m_tokenIdm] = 0
  require 1 <= mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mownedTokensIndexm[m_tokenIdm] < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mstor8m[m_tokenIdm]m]m.field_0 = mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0 = 0
  mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0--
  if mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1:
      [94midx = mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1
      mwhile mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > [94midxm:
          mtokenOfOwnerByIndexm[addr(m_from)m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mownedTokensIndexm[m_tokenIdm] = 0
  mownedTokensIndexm[mstor7m[addr(m_from)m]m[mstor7m[addr(m_from)m]m.field_0m]m.field_0m] = mownedTokensIndexm[m_tokenIdm]
  require not mownerOfm[m_tokenIdm]
  mownerOfm[m_tokenIdm] = m_to
  require mbalanceOfm[addr(m_to)m] + 1 >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m]++
  mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0++
  mtokenOfOwnerByIndexm[addr(m_to)m]m[mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0m]m.field_0 = m_tokenId
  mownedTokensIndexm[m_tokenIdm] = mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(m_to) > 0:
      require ext_code.size(m_to)
      call m_to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(m_from), m_tokenId, 128, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, ext_call.return_data[0]) == 0x150b7a0200000000000000000000000000000000000000000000000000000000


# hash = 0x42d8edea
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 10]]]
# const = None
# payable = False
def allTokensIndex(uint256 m_param1): # not payable
  return mallTokensIndexm[m_param1m]


# hash = 0x44ebea01
# getter = None
# const = None
# payable = False
def unknown44ebea01(uint256 m_param1): # not payable
  require mstor23m[m_param1m]m.field_512 + mstor19 >= mstor23m[m_param1m]m.field_512
  return (mstor23m[m_param1m]m.field_512 + mstor19)


# hash = 0x48eba03d
# getter = None
# const = None
# payable = False
def unknown48eba03d(addr m_param1): # not payable
  require caller == mowner
  mstor33 = m_param1


# hash = 0x4deb2fd5
# getter = None
# const = None
# payable = False
def unknown4deb2fd5(uint256 m_param1): # not payable
  if munknown2eb8c1d3m[m_param1m] != caller:
      require mownerOfm[m_param1m] == caller
  require not mstor38m[mstor13m[m_param1m]m]
  require mstor23m[m_param1m]m.field_512 > block.timestamp
  require mstor23m[m_param1m]m.field_256 >= 2
  require mstor23m[m_param1m]m.field_1024 < 3
  require 1 <= mstor23m[m_param1m]m.field_256
  if mstor23m[m_param1m]m.field_1280 < mstor23m[m_param1m]m.field_256 - 1:
      require caller
      require not mownerOfm[mstor9m.length + 1m]
      mownerOfm[mstor9m.length + 1m] = caller
      require mbalanceOfm[callerm] + 1 >= mbalanceOfm[callerm]
      mbalanceOfm[callerm]++
      mtokenOfOwnerByIndexm[callerm]m.field_0++
      mtokenOfOwnerByIndexm[callerm]m[mtokenOfOwnerByIndexm[callerm]m.field_0m]m.field_0 = mallTokensm.length + 1
      mownedTokensIndexm[mstor9m.length + 1m] = mtokenOfOwnerByIndexm[callerm]m.field_0
      log Transfer(
            address from=0,
            address to=caller,
            uint256 value=allTokens.length + 1)
      mallTokensIndexm[mstor9m.length + 1m] = mallTokensm.length
      mallTokensm.length++
      mallTokensm[mallTokensm.lengthm] = mallTokensm.length + 1
      require munknown01d4b66am[mstor13m[m_param1m]m]m[mstor14m[m_param1m]m] + 1 >= munknown01d4b66am[mstor13m[m_param1m]m]m[mstor14m[m_param1m]m]
      munknown01d4b66am[mstor13m[m_param1m]m]m[mstor14m[m_param1m]m]++
      mtokenTypesm[mstor9m.length + 1m] = mtokenTypesm[m_param1m]
      munknown50dc1722m[mstor9m.length + 1m] = munknown50dc1722m[m_param1m]
      munknown8da0b3eem[mstor9m.length + 1m] = 1
      mtokenTypesm[mstor9m.length + 1m] = mtokenTypesm[m_param1m]
      mstor23m[mstor9m.length + 1m]m.field_0 = block.timestamp
      mstor23m[mstor9m.length + 1m]m.field_256 = 1
      require block.timestamp + mstor18 >= block.timestamp
      mstor23m[mstor9m.length + 1m]m.field_512 = block.timestamp + mstor18
      mstor23m[mstor9m.length + 1m]m.field_768 = mstor23m[m_param1m]m.field_768
      mstor23m[mstor9m.length + 1m]m.field_1536 = m_param1
      munknowncb19273bm.length++
      munknowncb19273bm[munknowncb19273bm.lengthm] = mallTokensm.length + 1
      mstor23m[m_param1m]m.field_1280++
      mstor[('array', 5, ('map', ('param', '_param1'), ('name', 'stor23', 23))) + mstor23m[m_param1m]m.field_1280m]m.field_0 = mallTokensm.length + 1
      log 0x10d6b661: (allTokens.length + 1), caller


# hash = 0x4eaef239
# getter = None
# const = None
# payable = False
def unknown4eaef239(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, bool m_param5, bool m_param6, bool m_param7): # not payable
  require caller == mowner
  munknown7c11d624m[m_param1m]m[m_param2m]m[m_param3m] = m_param4
  mstor45m[m_param1m] = uint8(m_param5)
  mstor38m[m_param1m] = uint8(m_param6)
  mstor44m[m_param1m] = uint8(m_param7)


# hash = 0x4f558e79
# getter = None
# const = None
# payable = False
def exists(uint256 m_tokenId): # not payable
  return not not mownerOfm[m_tokenIdm]


# hash = 0x4f6ccce7
# getter = ['storage', 256, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def tokenByIndex(uint256 m_index): # not payable
  require m_index < mallTokensm.length
  return mallTokensm[m_indexm]


# hash = 0x50dc1722
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = False
def unknown50dc1722(uint256 m_param1): # not payable
  return munknown50dc1722m[m_param1m]


# hash = 0x521eb273
# getter = ['storage', 160, 0, 31]
# const = None
# payable = False
def wallet(): # not payable
  return mwalletAddress


# hash = 0x59ec682a
# getter = None
# const = None
# payable = True
def unknown59ec682a(uint256 m_param1) payable: 
  if munknown2eb8c1d3m[m_param1m] != caller:
      require mownerOfm[m_param1m] == caller
  require call.value == mfee
  require mstor23m[m_param1m]m.field_1024 < 3
  require mstor23m[m_param1m]m.field_512 + mstor19 >= mstor23m[m_param1m]m.field_512
  require mstor20 >= 0
  require mstor23m[m_param1m]m.field_512 + mstor19 + mstor20 > block.timestamp
  call mwalletAddress with:
     value call.value wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require block.timestamp + mstor22 >= block.timestamp
  mstor23m[m_param1m]m.field_512 = block.timestamp + mstor22


# hash = 0x5be4ef4b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 38]]]]
# const = None
# payable = False
def unknown5be4ef4b(uint256 m_param1): # not payable
  return bool(mstor38m[m_param1m])


# hash = 0x634282af
# getter = ['storage', 256, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def allTokens(uint256 m_param1): # not payable
  require m_param1 < mallTokensm.length
  return mallTokensm[m_param1m]


# hash = 0x6352211e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def ownerOf(uint256 m_tokenId): # not payable
  require mownerOfm[m_tokenIdm]
  return mownerOfm[m_tokenIdm]


# hash = 0x6a22a976
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 27]]], ['cd', 36]]]
# const = None
# payable = False
def unknown6a22a976(addr m_param1, uint256 m_param2): # not payable
  require m_param2 < munknown6a22a976m[m_param1m]m.field_0
  return munknown6a22a976m[m_param1m]m[m_param2m]m.field_0


# hash = 0x6bef835c
# getter = None
# const = None
# payable = False
def unknown6bef835c(uint256 m_param1, uint256 m_param2, uint256 m_param3, array m_param4): # not payable
  require caller == mowner
  munknowne88583b9m[m_param1m]m[m_param2m]m[m_param3m]m[m] = Array(len=m_param4.length, data=m_param4[allm])


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  require m_owner
  return mbalanceOfm[addr(m_owner)m]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x74c7c578
# getter = ['storage', 256, 0, 42]
# const = None
# payable = False
def unknown74c7c578(): # not payable
  return munknown74c7c578


# hash = 0x74e24367
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def ownedTokensIndex(uint256 m_param1): # not payable
  return mownedTokensIndexm[m_param1m]


# hash = 0x7561d020
# getter = ['storage', 256, 0, 32]
# const = None
# payable = False
def unknown7561d020(): # not payable
  return munknownd4db722em.length


# hash = 0x7c11d624
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 30]]]]]]]
# const = None
# payable = False
def unknown7c11d624(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  return munknown7c11d624m[m_param1m]m[m_param2m]m[m_param3m]


# hash = 0x7f05ebf2
# getter = None
# const = None
# payable = False
def unknown7f05ebf2(uint256 m_param1): # not payable
  require caller == mstor33
  munknownef8998aem[m_param1m] = 0


# hash = 0x8da0b3ee
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 15]]]
# const = None
# payable = False
def unknown8da0b3ee(uint256 m_param1): # not payable
  return munknown8da0b3eem[m_param1m]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0xa22cb465
# getter = None
# const = None
# payable = False
def setApprovalForAll(address m_to, bool m_approved): # not payable
  require m_to != caller
  mstor4m[callerm]m[addr(m_to)m] = uint8(m_approved)
  log ApprovalForAll(
        address owner=_approved,
        address operator=caller,
        bool approved=_to)


# hash = 0xaf6c011f
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 45]]]]
# const = None
# payable = False
def unknownaf6c011f(uint256 m_param1): # not payable
  return bool(mstor45m[m_param1m])


# hash = 0xb88d4fde
# getter = None
# const = None
# payable = False
def safeTransferFrom(address m_from, address m_to, uint256 m_tokenId, bytes m_data): # not payable
  require mownerOfm[m_tokenIdm]
  if mownerOfm[m_tokenIdm] != caller:
      if mapprovedm[m_tokenIdm] != caller:
          require mstor4m[mstor1m[m_tokenIdm]m]m[callerm]
  require mownerOfm[m_tokenIdm]
  if mownerOfm[m_tokenIdm] != caller:
      if mapprovedm[m_tokenIdm] != caller:
          require mstor4m[mstor1m[m_tokenIdm]m]m[callerm]
  require m_from
  require m_to
  require mownerOfm[m_tokenIdm]
  require mownerOfm[m_tokenIdm] == m_from
  if mapprovedm[m_tokenIdm]:
      mapprovedm[m_tokenIdm] = 0
  require mownerOfm[m_tokenIdm]
  require mownerOfm[m_tokenIdm] == m_from
  require 1 <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m]--
  mownerOfm[m_tokenIdm] = 0
  require 1 <= mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  require mownedTokensIndexm[m_tokenIdm] < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mstor8m[m_tokenIdm]m]m.field_0 = mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0
  require mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1 < mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0
  mtokenOfOwnerByIndexm[addr(m_from)m]m[mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0m]m.field_0 = 0
  mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0--
  if mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1:
      [94midx = mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 - 1
      mwhile mtokenOfOwnerByIndexm[addr(m_from)m]m.field_0 > [94midxm:
          mtokenOfOwnerByIndexm[addr(m_from)m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mownedTokensIndexm[m_tokenIdm] = 0
  mownedTokensIndexm[mstor7m[addr(m_from)m]m[mstor7m[addr(m_from)m]m.field_0m]m.field_0m] = mownedTokensIndexm[m_tokenIdm]
  require not mownerOfm[m_tokenIdm]
  mownerOfm[m_tokenIdm] = m_to
  require mbalanceOfm[addr(m_to)m] + 1 >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m]++
  mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0++
  mtokenOfOwnerByIndexm[addr(m_to)m]m[mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0m]m.field_0 = m_tokenId
  mownedTokensIndexm[m_tokenIdm] = mtokenOfOwnerByIndexm[addr(m_to)m]m.field_0
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(m_to) > 0:
      require ext_code.size(m_to)
      call m_to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas gas_remaining wei
          args caller, addr(m_from), m_tokenId, Array(len=m_data.length, data=m_data[allm])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, ext_call.return_data[0]) == 0x150b7a0200000000000000000000000000000000000000000000000000000000


# hash = 0xba563365
# getter = None
# const = None
# payable = False
def unknownba563365(array m_param1): # not payable
  require caller == mowner
  munknownd4db722em.length++
  munknownd4db722em[munknownd4db722em.lengthm]m[m] = Array(len=m_param1.length, data=m_param1[allm])


# hash = 0xbaa79caf
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 39]]]]]]]]], ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 39]]]]]]]]
# const = None
# payable = False
def unknownbaa79caf(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  return munknowne88583b9m[m_param1m]m[m_param2m]m[m_param3m]m[0 len munknowne88583b9m[m_param1m]m[m_param2m]m[m_param3m]m.lengthm]


# hash = 0xbb19f507
# getter = None
# const = None
# payable = False
def unknownbb19f507(uint256 m_param1): # not payable
  if mstor38m[mstor13m[m_param1m]m]:
      return 0
  if mstor23m[m_param1m]m.field_1024 >= 1:
      return mstor23m[m_param1m]m.field_1024 >= 1
  require mstor23m[m_param1m]m.field_512 + mstor19 >= mstor23m[m_param1m]m.field_512
  return (mstor23m[m_param1m]m.field_512 + mstor19 < block.timestamp)


# hash = 0xc42e532b
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 36]]]
# const = None
# payable = False
def unknownc42e532b(uint256 m_param1): # not payable
  return munknownc42e532bm[m_param1m]


# hash = 0xc70d5f3b
# getter = None
# const = None
# payable = False
def unknownc70d5f3b(uint256 m_param1, uint256 m_param2): # not payable
  munknownef8998aem[m_param1m] = m_param2
  if not mstor38m[mstor13m[m_param1m]m]:
      require mstor23m[m_param1m]m.field_1024 < 1
      require mstor23m[m_param1m]m.field_512 + mstor19 >= mstor23m[m_param1m]m.field_512
      require mstor23m[m_param1m]m.field_512 + mstor19 >= block.timestamp
  require mownerOfm[m_param1m] == caller
  if m_param2 > 0:
      require ext_code.size(mstor33)
      call mstor33.0x119a80f1 with:
           gas gas_remaining wei
          args m_param1, mtokenTypesm[m_param1m]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require mownerOfm[m_param1m]
      require mstor33 != mownerOfm[m_param1m]
      if mownerOfm[m_param1m] != caller:
          require mstor4m[mstor1m[m_param1m]m]m[callerm]
      mapprovedm[m_param1m] = mstor33
      log Approval(
            address owner=ownerOf[_param1],
            address spender=stor33,
            uint256 value=_param1)


# hash = 0xc87b56dd
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 11]]]]], ['sha3', ['data', ['cd', 4], 11]]]]
# const = None
# payable = False
def tokenURI(uint256 m_tokenId): # not payable
  return mtokenURIm[m_tokenIdm]m[0 len mtokenURIm[m_tokenIdm]m.lengthm]


# hash = 0xc92bb4ff
# getter = None
# const = None
# payable = False
def unknownc92bb4ff(uint256 m_param1, array m_param2): # not payable
  require caller == mowner
  munknowncfbb7d9am[m_param1m]++
  munknowncfbb7d9am[m_param1m]m[munknowncfbb7d9am[m_param1m]m]m[m] = Array(len=m_param2.length, data=m_param2[allm])


# hash = 0xcb19273b
# getter = ['storage', 256, 0, ['add', ['sha3', 24], ['cd', 4]]]
# const = None
# payable = False
def unknowncb19273b(uint256 m_param1): # not payable
  require m_param1 < munknowncb19273bm.length
  return munknowncb19273bm[m_param1m]


# hash = 0xcfbb7d9a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 17]]]
# const = None
# payable = False
def unknowncfbb7d9a(uint256 m_param1): # not payable
  return munknowncfbb7d9am[m_param1m]


# hash = 0xd2f0a1c9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 34]]]]]
# const = None
# payable = False
def unknownd2f0a1c9(uint256 m_param1, uint256 m_param2): # not payable
  return munknownd2f0a1c9m[m_param1m]m[m_param2m]


# hash = 0xd4db722e
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', ['sha3', 32], ['cd', 4]]]]], ['add', ['sha3', 32], ['cd', 4]]]]
# const = None
# payable = False
def unknownd4db722e(uint256 m_param1): # not payable
  return munknownd4db722em[m_param1m]m[0 len munknownd4db722em[m_param1m]m.lengthm]


# hash = 0xdd29dc68
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 29]]]
# const = None
# payable = False
def unknowndd29dc68(uint256 m_param1): # not payable
  return munknowndd29dc68m[m_param1m]


# hash = 0xddca3f43
# getter = ['storage', 256, 0, 41]
# const = None
# payable = False
def fee(): # not payable
  return mfee


# hash = 0xe149f036
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 7]]], ['cd', 36]]]
# const = None
# payable = False
def ownedTokens(address m_param1, uint256 m_param2): # not payable
  require m_param2 < mtokenOfOwnerByIndexm[m_param1m]m.field_0
  return mtokenOfOwnerByIndexm[m_param1m]m[m_param2m]m.field_0


# hash = 0xe88583b9
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 39]]]]]]]]], ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 39]]]]]]]]
# const = None
# payable = False
def unknowne88583b9(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  return munknowne88583b9m[m_param1m]m[m_param2m]m[m_param3m]m[0 len munknowne88583b9m[m_param1m]m[m_param2m]m[m_param3m]m.lengthm]


# hash = 0xe985e9c5
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]]]]
# const = None
# payable = False
def isApprovedForAll(address m_owner, address m_operator): # not payable
  return bool(mstor4m[addr(m_owner)m]m[addr(m_operator)m])


# hash = 0xe9fb3589
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 35]]]]]
# const = None
# payable = False
def unknowne9fb3589(uint256 m_param1, uint256 m_param2): # not payable
  return munknowne9fb3589m[m_param1m]m[m_param2m]


# hash = 0xed9b079a
# getter = None
# const = None
# payable = False
def unknowned9b079a(uint256 m_param1): # not payable
  if mownerOfm[m_param1m] != caller:
      if munknown2eb8c1d3m[m_param1m] != caller:
          require caller == mstor33
  if munknown2eb8c1d3m[m_param1m]:
      munknown2eb8c1d3m[m_param1m] = 0
      require 1 <= munknown6a22a976m[mstor26m[m_param1m]m]m.field_0
      require munknown6a22a976m[mstor26m[m_param1m]m]m.field_0 - 1 < munknown6a22a976m[mstor26m[m_param1m]m]m.field_0
      munknowndd29dc68m[mstor27m[mstor26m[m_param1m]m]m[mstor27m[mstor26m[m_param1m]m]m.field_0m]m.field_0m] = munknowndd29dc68m[m_param1m]
      require munknowndd29dc68m[m_param1m] < munknown6a22a976m[mstor26m[m_param1m]m]m.field_0
      munknown6a22a976m[mstor26m[m_param1m]m]m[mstor29m[m_param1m]m]m.field_0 = munknown6a22a976m[mstor26m[m_param1m]m]m[munknown6a22a976m[mstor26m[m_param1m]m]m.field_0m]m.field_0
      munknown6a22a976m[mstor26m[m_param1m]m]m.field_0--
      if munknown6a22a976m[mstor26m[m_param1m]m]m.field_0 > munknown6a22a976m[mstor26m[m_param1m]m]m.field_0 - 1:
          [94midx = munknown6a22a976m[mstor26m[m_param1m]m]m.field_0 - 1
          mwhile munknown6a22a976m[mstor26m[m_param1m]m]m.field_0 > [94midxm:
              munknown6a22a976m[mstor26m[m_param1m]m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 


# hash = 0xef8998ae
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 28]]]
# const = None
# payable = False
def unknownef8998ae(uint256 m_param1): # not payable
  return munknownef8998aem[m_param1m]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf317d7dd
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', ['sha3', ['sha3', ['data', ['cd', 4], 17]]], ['cd', 36]]]]], ['add', ['sha3', ['sha3', ['data', ['cd', 4], 17]]], ['cd', 36]]]]
# const = None
# payable = False
def unknownf317d7dd(uint256 m_param1, uint256 m_param2): # not payable
  return munknowncfbb7d9am[m_param1m]m[m_param2m]m[0 len munknowncfbb7d9am[m_param1m]m[m_param2m]m.lengthm]


# hash = 0xf362ce98
# getter = None
# const = None
# payable = False
def unknownf362ce98(uint256 m_param1, addr m_param2): # not payable
  require caller == mownerOfm[m_param1m]
  munknown2eb8c1d3m[m_param1m] = m_param2
  munknown6a22a976m[addr(m_param2)m]m.field_0++
  munknown6a22a976m[addr(m_param2)m]m[munknown6a22a976m[addr(m_param2)m]m.field_0m]m.field_0 = m_param1
  require 1 <= munknown6a22a976m[addr(m_param2)m]m.field_0
  munknowndd29dc68m[m_param1m] = munknown6a22a976m[addr(m_param2)m]m.field_0 - 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


