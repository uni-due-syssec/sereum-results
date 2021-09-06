# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x992b09B84C638F0082eF4b02483Ccc6b76D2B8Ba 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x13de5b49': 'unknown13de5b49(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    backupOwner # mask: a s
    # storage address 2
    unknown88b45046 # mask: a s
    # storage address 3
    unknownef95b90e # mask: a s
    # storage address 4
    unknownf51efd7a
    # storage address 5
    unknown585c5b83
    # storage address 6
    unknowne2603c30 # mask: a s
    # storage address 7
    unknown06b39862Address # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    unknown4b0177dc # mask: a s
    # storage address 10
    unknowna1579e73 # mask: a s
    # storage address 11
    unknowne343cf62 # mask: a s
    # storage address 12
    unknowneb391917 # mask: a s
    # storage address 13
    unknown39509a8f # mask: a s
    # storage address 14
    unknown17e55a0e # mask: a s
    # storage address 15
    unknown402c880d # mask: a s
    # storage address 16
    unknown9d2f6fb8 # mask: a s
    # storage address 17
    unknownd5e582bd # mask: a s
    # storage address 18
    unknowndeceaace # mask: a s
    # storage address 19
    unknownc390d401 # mask: a s
    # storage address 20
    unknown7ab33cf2 # mask: a s
    # storage address 21
    unknownffe06a99 # mask: a s
    # storage address 22
    unknown424a597c # mask: a s
    # storage address 23
    unknown6f6095ef # mask: a s
    # storage address 24
    unknown02a34ee1 # mask: a s
    # storage address 25
    unknownb1cb7f29 # mask: a s
    # storage address 26
    unknown446c3295 # mask: a s
    # storage address 27
    unknown17af4fd1 # mask: a s
    # storage address 28
    unknown37594aa2 # mask: a s
    # storage address 29
    unknown02195d75 # mask: a s
    # storage address 30
    unknowna4185663 # mask: a s
    # storage address 31
    unknown930432da # mask: a s
    # storage address 32
    unknown9a1ab774 # mask: a s
    # storage address 33
    unknown8ca7bd2f # mask: a s
    # storage address 34
    unknown3c2848ea
# hash = 0x02195d75
# getter = ['storage', 256, 0, 29]
# const = None
# payable = False
def unknown02195d75(): # not payable
  return munknown02195d75


# hash = 0x02a34ee1
# getter = ['bool', ['storage', 8, 0, 24]]
# const = None
# payable = False
def unknown02a34ee1(): # not payable
  return bool(munknown02a34ee1)


# hash = 0x030b7d87
# getter = None
# const = None
# payable = False
def unknown030b7d87(uint256 m_param1, uint256 m_param2): # not payable
  mem[208 len 0] = None
  mem[208] = mem[224 len 16]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[208 len 16]m]:
      revert with 0, 'permission deny'
  munknowna4185663 = m_param1
  munknown930432da = m_param2


# hash = 0x06b39862
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknown06b39862(): # not payable
  return munknown06b39862Address


# hash = 0x06b9d635
# getter = None
# const = None
# payable = False
def unknown06b9d635(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require ext_code.size(munknown06b39862Address)
  call munknown06b39862Address.0x4c577b95 with:
       gas gas_remaining wei
      args addr(m_param1), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp - ext_call.return_data[0] < munknown930432da:
      revert with 0, 'can not less than 24 hours'
  require ext_code.size(munknown06b39862Address)
  call munknown06b39862Address.0xe4fed460 with:
       gas gas_remaining wei
      args addr(m_param1), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown06b39862Address)
  call munknown06b39862Address.0x17ff16e2 with:
       gas gas_remaining wei
      args addr(m_param1), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_param3 > 0:
      revert with 0, 'draw excceed invest'
  return 1


# hash = 0x12065fe0
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getBalance = eth.balance(this.address)


# hash = 0x1268b86e
# getter = None
# const = None
# payable = False
def unknown1268b86e(addr m_param1, uint256 m_param2): # not payable
  if m_param2 > munknown9a1ab774:
      revert with 0, 'amt illgel'
  require ext_code.size(munknown06b39862Address)
  call munknown06b39862Address.0xefde7d9b with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp <= ext_call.return_data[0]:
      revert with 0, 'time limited'
  require ext_code.size(munknown06b39862Address)
  call munknown06b39862Address.0xefde7d9b with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp - ext_call.return_data[0] < 3600 * munknown8ca7bd2f:
      revert with 0, 'time limited'
  return 1


# hash = 0x169d8b77
# getter = None
# const = None
# payable = False
def unknown169d8b77(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, uint256 m_param6, uint256 m_param7, uint256 m_param8, uint256 m_param9, uint256 m_param10): # not payable
  mem[200 len 0] = None
  mem[200] = mem[208 len 8], uint64('setRatio'), mem[224 len 8]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[200 len 8]m]:
      revert with 0, 'permission deny'
  munknown4b0177dc = m_param1
  munknowna1579e73 = m_param2
  munknowne343cf62 = m_param3
  munknowneb391917 = m_param4
  munknown39509a8f = m_param5
  munknown17e55a0e = m_param6
  munknown402c880d = m_param7
  munknown9d2f6fb8 = m_param8
  munknownd5e582bd = m_param9
  munknowndeceaace = m_param10


# hash = 0x17af4fd1
# getter = ['storage', 256, 0, 27]
# const = None
# payable = False
def unknown17af4fd1(): # not payable
  return munknown17af4fd1


# hash = 0x17e55a0e
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown17e55a0e(): # not payable
  return munknown17e55a0e


# hash = 0x1933c4f0
# getter = None
# const = None
# payable = False
def unknown1933c4f0(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('setWeekRatio'), mem[224 len 12]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[204 len 12]m]:
      revert with 0, 'permission deny'
  munknown446c3295 = m_param1
  munknown17af4fd1 = m_param2
  munknown37594aa2 = m_param3
  munknown02195d75 = m_param4


# hash = 0x1b71d0f2
# getter = None
# const = None
# payable = False
def unknown1b71d0f2(addr m_param1, uint256 m_param2): # not payable
  if mowner != caller:
      revert with 0, 'you are not the owner'
  munknownf51efd7am[addr(m_param1)m] = m_param2


# hash = 0x3291fa5f
# getter = None
# const = None
# payable = False
def unknown3291fa5f(array m_param1, uint256 m_param2): # not payable
  mem[128 len m_param1.length] = m_param1[allm]
  if mowner != caller:
      revert with 0, 'you are not the owner'
  mem[ceil32(m_param1.length) + 160 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[ceil32(m_param1.length) + floor32(m_param1.length) + -(m_param1.length % 32) + 192 len m_param1.length % 32] = mem[-(m_param1.length % 32) + floor32(m_param1.length) + 160 len m_param1.length % 32]
  mem[m_param1.length + ceil32(m_param1.length) + 160 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160] = 256^(-(m_param1.length % 32) + 32) - 1 and mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160] or mem[ceil32(m_param1.length) + floor32(m_param1.length) + 160] and !(256^(-(m_param1.length % 32) + 32) - 1)
  munknown585c5b83m[call.data[m_param1 + 36 len floor32(m_param1.length)]m][mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160 len m_param1.length % 32]m] = m_param2


# hash = 0x37594aa2
# getter = ['storage', 256, 0, 28]
# const = None
# payable = False
def unknown37594aa2(): # not payable
  return munknown37594aa2


# hash = 0x39509a8f
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown39509a8f(): # not payable
  return munknown39509a8f


# hash = 0x3af8e4ab
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def backupOwner(): # not payable
  return mbackupOwner


# hash = 0x3c2848ea
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 34]]]]]
# const = None
# payable = False
def unknown3c2848ea(addr m_param1, addr m_param2): # not payable
  return munknown3c2848eam[m_param1m]m[m_param2m]


# hash = 0x3e74d449
# getter = None
# const = None
# payable = False
def unknown3e74d449(addr m_param1, uint256 m_param2): # not payable
  mem[202 len 0] = None
  mem[202] = mem[212 len 2], Mask(80, 0, 'tansferETH'), mem[224 len 10]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[202 len 10]m]:
      revert with 0, 'permission deny'
  if m_param2 > munknownef95b90e:
      revert with 0, 'single excceed'
  call m_param1 with:
     value m_param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x402c880d
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown402c880d(): # not payable
  return munknown402c880d


# hash = 0x424a597c
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknown424a597c(): # not payable
  return munknown424a597c


# hash = 0x446c3295
# getter = ['storage', 256, 0, 26]
# const = None
# payable = False
def unknown446c3295(): # not payable
  return munknown446c3295


# hash = 0x4b0177dc
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown4b0177dc(): # not payable
  return munknown4b0177dc


# hash = 0x56029aea
# getter = None
# const = None
# payable = False
def unknown56029aea(uint256 m_param1): # not payable
  mem[212 len 0] = None
  mem[212] = mem[232 len 12]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[212 len 20]m]:
      revert with 0, 'permission deny'
  munknownef95b90e = m_param1


# hash = 0x585c5b83
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknown585c5b83(uint256 m_param1): # not payable
  return munknown585c5b83m[m_param1m]


# hash = 0x64020558
# getter = None
# const = None
# payable = False
def unknown64020558(uint256 m_param1, addr m_param2): # not payable
  if mowner != caller:
      revert with 0, 'you are not the owner'
  if m_param1 != 201901261442:
      revert with 0, 'password is not right'
  [93mselfdestruct([91m_param2[93m)


# hash = 0x6e5de674
# getter = None
# const = None
# payable = False
def unknown6e5de674(addr m_param1): # not payable
  if mowner != caller:
      revert with 0, 'you are not the owner'
  mowner = m_param1


# hash = 0x6f6095ef
# getter = ['storage', 256, 0, 23]
# const = None
# payable = False
def unknown6f6095ef(): # not payable
  return munknown6f6095ef


# hash = 0x78a1bf05
# getter = None
# const = None
# payable = False
def unknown78a1bf05(): # not payable
  return munknown930432da, munknown446c3295, munknown17af4fd1, munknown37594aa2, munknown02195d75, munknowna4185663


# hash = 0x7ab33cf2
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def unknown7ab33cf2(): # not payable
  return munknown7ab33cf2


# hash = 0x85ab0dd7
# getter = None
# const = None
# payable = False
def unknown85ab0dd7(uint256 m_param1): # not payable
  require ext_code.size(mstor8)
  call mstor8.0x4bf5cb14 with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  require munknowna4185663
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 7:
      revert with 0, 'nowday < 7'
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 14:
      if ((-7 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) < ext_call.return_data[64]:
          revert with 0, 'w2 safe check'
      return ((-7 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) - ext_call.return_data[64], 
             0,
             0
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 21:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((-14 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) / 10000) < ext_call.return_data[64]:
          revert with 0, 'w3 safe check'
      return ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((-14 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) / 10000) - ext_call.return_data[64], 
             0,
             0
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 >= 28:
      if (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (2 * 7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 * munknown02195d75 / 10000) < ext_call.return_data[64]:
          revert with 0, 'wo cao ,dont say impossible'
      return (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (2 * 7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 * munknown02195d75 / 10000) - ext_call.return_data[64], 
             1,
             ext_call.return_data[0]
  if ((-21 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) / 10000) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) < ext_call.return_data[64]:
      revert with 0, 'w4 safe check'
  return ((-21 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) / 10000) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) - ext_call.return_data[64], 
         0,
         0


# hash = 0x88b45046
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown88b45046(): # not payable
  return munknown88b45046


# hash = 0x8ca7bd2f
# getter = ['storage', 256, 0, 33]
# const = None
# payable = False
def unknown8ca7bd2f(): # not payable
  return munknown8ca7bd2f


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8dbc5813
# getter = None
# const = None
# payable = False
def unknown8dbc5813(array m_param1): # not payable
  mem[128 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + 160 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[ceil32(m_param1.length) + floor32(m_param1.length) + -(m_param1.length % 32) + 192 len m_param1.length % 32] = mem[-(m_param1.length % 32) + floor32(m_param1.length) + 160 len m_param1.length % 32]
  mem[m_param1.length + ceil32(m_param1.length) + 160 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160] = 256^(-(m_param1.length % 32) + 32) - 1 and mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160] or mem[ceil32(m_param1.length) + floor32(m_param1.length) + 160] and !(256^(-(m_param1.length % 32) + 32) - 1)
  mem[m_param1.length + ceil32(m_param1.length) + 160] = munknown585c5b83m[call.data[m_param1 + 36 len floor32(m_param1.length)]m][mem[m_param1.length + ceil32(m_param1.length) + floor32(m_param1.length) + 160 len m_param1.length % 32]m]
  return memory
    from m_param1.length + ceil32(m_param1.length) + 160
     [93mlen 32


# hash = 0x930432da
# getter = ['storage', 256, 0, 31]
# const = None
# payable = False
def unknown930432da(): # not payable
  return munknown930432da


# hash = 0x954785a5
# getter = None
# const = None
# payable = False
def unknown954785a5(uint256 m_param1, uint256 m_param2): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('setContrDraw'), mem[224 len 12]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[204 len 12]m]:
      revert with 0, 'permission deny'
  munknown9a1ab774 = m_param1
  munknown8ca7bd2f = m_param2


# hash = 0x9a1ab774
# getter = ['storage', 256, 0, 32]
# const = None
# payable = False
def unknown9a1ab774(): # not payable
  return munknown9a1ab774


# hash = 0x9d2f6fb8
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown9d2f6fb8(): # not payable
  return munknown9d2f6fb8


# hash = 0xa1579e73
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknowna1579e73(): # not payable
  return munknowna1579e73


# hash = 0xa4185663
# getter = ['storage', 256, 0, 30]
# const = None
# payable = False
def unknowna4185663(): # not payable
  return munknowna4185663


# hash = 0xaa8ee3ae
# getter = None
# const = None
# payable = False
def unknownaa8ee3ae(addr m_param1): # not payable
  if mbackupOwner != caller:
      revert with 0, 'you are not backupOwner'
  mowner = m_param1


# hash = 0xab4258e8
# getter = None
# const = None
# payable = False
def unknownab4258e8(bool m_param1, uint256 m_param2): # not payable
  mem[205 len 0] = None
  mem[205] = 'setReferLevel' % 281474976710656, mem[224 len 13]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[205 len 13]m]:
      revert with 0, 'permission deny'
  munknown02a34ee1 = uint8(m_param1)
  munknownb1cb7f29 = m_param2


# hash = 0xb1b57156
# getter = None
# const = None
# payable = False
def unknownb1b57156(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  mem[201 len 0] = None
  mem[201] = mem[210 len 5], Mask(72, 0, 'setRatio2'), mem[224 len 9]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[201 len 9]m]:
      revert with 0, 'permission deny'
  munknownc390d401 = m_param1
  munknown7ab33cf2 = m_param2
  munknownffe06a99 = m_param3
  munknown424a597c = m_param4
  munknown6f6095ef = m_param5


# hash = 0xb1cb7f29
# getter = ['storage', 256, 0, 25]
# const = None
# payable = False
def unknownb1cb7f29(): # not payable
  return munknownb1cb7f29


# hash = 0xc390d401
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def unknownc390d401(): # not payable
  return munknownc390d401


# hash = 0xd5e582bd
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknownd5e582bd(): # not payable
  return munknownd5e582bd


# hash = 0xdeceaace
# getter = ['storage', 256, 0, 18]
# const = None
# payable = False
def unknowndeceaace(): # not payable
  return munknowndeceaace


# hash = 0xe2603c30
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknowne2603c30(): # not payable
  return munknowne2603c30


# hash = 0xe343cf62
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknowne343cf62(): # not payable
  return munknowne343cf62


# hash = 0xe67b6444
# getter = None
# const = None
# payable = False
def unknowne67b6444(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('tansferERC20'), mem[224 len 12]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[204 len 12]m]:
      revert with 0, 'permission deny'
  require ext_code.size(m_param1)
  call m_param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param2), m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xeb391917
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknowneb391917(): # not payable
  return munknowneb391917


# hash = 0xef95b90e
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknownef95b90e(): # not payable
  return munknownef95b90e


# hash = 0xef98ffb5
# getter = None
# const = None
# payable = False
def unknownef98ffb5(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require ext_code.size(mstor8)
  call mstor8.0x4bf5cb14 with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  if m_param2 > (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 * munknown02195d75 / 10000) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100):
      revert with 0, 'amt is not right'
  require munknowna4185663
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 7:
      revert with 0, 'nowday < 7'
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 14:
      if ((-7 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) < ext_call.return_data[64]:
          revert with 0, 'w2 safe check'
      if ((-7 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown17af4fd1 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) - ext_call.return_data[64] < m_param2:
          revert with 0, 'w2 excceed'
      return m_param2, 1, 0
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 21:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((-14 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) / 10000) < ext_call.return_data[64]:
          revert with 0, 'w3 safe check'
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((-14 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown37594aa2 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) / 10000) - ext_call.return_data[64] < m_param2:
          revert with 0, 'w3 excceed'
      return m_param2, 1, 0
  if block.timestamp - ext_call.return_data[32] / munknowna4185663 < 28:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((-21 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) / 10000) < ext_call.return_data[64]:
          revert with 0, 'w4 safe check'
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + ((-21 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / munknowna4185663 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) / 10000) - ext_call.return_data[64] < m_param2:
          revert with 0, 'w4 excceed'
      return m_param2, 1, 0
  if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (7 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 / 10000) >= ext_call.return_data[64]:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (7 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 / 10000) - ext_call.return_data[64] >= m_param2:
          return m_param2, 1, 0
  if m_param3 < ext_call.return_data[0]:
      revert with 0, 're-take amt wrong'
  if m_param3 > munknowne2603c30:
      revert with 0, 'maxPerInvest excceed'
  if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (7 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 / 10000) + (7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 * munknown02195d75 / 10000) < ext_call.return_data[64]:
      revert with 0, 'wo cao ,dont say impossible'
  return ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100) + (7 * munknown02195d75 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 / 10000) + (7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * munknown446c3295 / 10000) / 100 * munknown17af4fd1 / 10000) / 100 * munknown37594aa2 / 10000) / 100 * munknown02195d75 / 10000) - ext_call.return_data[64], 
         0,
         1


# hash = 0xf51efd7a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknownf51efd7a(addr m_param1): # not payable
  return munknownf51efd7am[m_param1m]


# hash = 0xfd91b20d
# getter = None
# const = None
# payable = False
def unknownfd91b20d(uint256 m_param1, addr m_param2): # not payable
  mem[207 len 0] = None
  mem[207] = uint16('setInvestConfig'), mem[224 len 15]
  if munknownf51efd7am[callerm] < munknown585c5b83m[mem[207 len 15]m]:
      revert with 0, 'permission deny'
  munknowne2603c30 = m_param1
  munknown06b39862Address = m_param2
  mstor8 = m_param2


# hash = 0xffe06a99
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknownffe06a99(): # not payable
  return munknownffe06a99


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


