# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x51F7593ac7f932db699101e945Ab2A010134e449 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown88b45046 # mask: a s
    # storage address 2
    unknownef95b90e # mask: a s
    # storage address 3
    unknownf51efd7a
    # storage address 4
    unknown585c5b83
    # storage address 5
    stor5
    # storage address 6
    tokenPrice
    # storage address 7
    unknownfaa9efe3
    # storage address 8
    unknowne57fb80e
    # storage address 9
    unknownb3fa871a
    # storage address 10
    stor10
    # storage address 11
    unknownee483063
    # storage address 12
    unknown17ff16e2
    # storage address 13
    unknown34e61612
    # storage address 14
    unknownea21a85d
    # storage address 15
    unknownb0cda0b7
    # storage address 16
    unknownbda75b77
    # storage address 17
    unknown4c577b95
    # storage address 18
    unknowne4fed460
    # storage address 19
    unknown98f5d445
    # storage address 20
    unknowndca4f9e1
    # storage address 21
    unknownd0817501
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 25
    unknown8215c67f
    # storage address 26
    unknown8b8edd03
    # storage address 27
    unknown21050266
    # storage address 28
    unknown059c657f
    # storage address 29
    unknowna30dbfd6
    # storage address 30
    unknown2b1e2eab
    # storage address 31
    stor31
    # storage address 32
    unknown8be11840
    # storage address 33
    unknownf3d2135c
    # storage address 34
    unknown4789dd6c
    # storage address 35
    unknownefde7d9b
    # storage address 36
    stor36
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884729
    stor660301456019777184113296434797620819555017468543624515662331739614079884729
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884730
    stor660301456019777184113296434797620819555017468543624515662331739614079884730
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884731
    stor660301456019777184113296434797620819555017468543624515662331739614079884731
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884732
    stor660301456019777184113296434797620819555017468543624515662331739614079884732
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884733
    stor660301456019777184113296434797620819555017468543624515662331739614079884733
    # storage address 660301456019777184113296434797620819555017468543624515662331739614079884734
    stor660301456019777184113296434797620819555017468543624515662331739614079884734
# hash = 0x059c657f
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 28]]]
# const = None
# payable = False
def unknown059c657f(addr _param1): # not payable
  return unknown059c657f[_param1]


# hash = 0x12065fe0
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getBalance = eth.balance(this.address)


# hash = 0x17ff16e2
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 12]]]]]
# const = None
# payable = False
def unknown17ff16e2(addr _param1, addr _param2): # not payable
  return unknown17ff16e2[_param1][_param2]


# hash = 0x1b71d0f2
# getter = None
# const = None
# payable = False
def unknown1b71d0f2(addr _param1, uint256 _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  unknownf51efd7a[addr(_param1)] = _param2


# hash = 0x1f69565f
# getter = None
# const = None
# payable = False
def unknown1f69565f(addr _param1): # not payable
  return stor22, 
         stor23,
         stor24,
         unknown8b8edd03[addr(_param1)],
         unknown8215c67f[addr(_param1)],
         unknownd0817501[addr(_param1)],
         tokenPrice[addr(_param1)],
         unknownfaa9efe3[addr(_param1)],
         unknowne57fb80e[addr(_param1)],
         unknownb3fa871a[addr(_param1)],
         unknownf3d2135c[addr(_param1)],
         unknown4789dd6c[addr(_param1)],
         unknownefde7d9b[addr(_param1)]


# hash = 0x21050266
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 27]]]
# const = None
# payable = False
def unknown21050266(addr _param1): # not payable
  return unknown21050266[_param1]


# hash = 0x2b1e2eab
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 30]]]
# const = None
# payable = False
def unknown2b1e2eab(addr _param1): # not payable
  return unknown2b1e2eab[_param1]


# hash = 0x313ce567
# getter = None
# const = ['return', 18]
# payable = False
const decimals = 18


# hash = 0x3291fa5f
# getter = None
# const = None
# payable = False
def unknown3291fa5f(array _param1, uint256 _param2): # not payable
  mem[128 len _param1.length] = _param1[all]
  if owner != caller:
      revert with 0, 'you are not the owner'
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]] = _param2


# hash = 0x34e61612
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 13]]]]]
# const = None
# payable = False
def unknown34e61612(addr _param1, addr _param2): # not payable
  return unknown34e61612[_param1][_param2]


# hash = 0x3af8e4ab
# getter = None
# const = ['return', 1396670739858187880424799297968028917416547616632]
# payable = False
const backupOwner = 0xf4a4e1cba7bbef0cb3200f2ede188950ade48778


# hash = 0x3e74d449
# getter = None
# const = None
# payable = False
def unknown3e74d449(addr _param1, uint256 _param2): # not payable
  mem[202 len 0] = None
  mem[202] = mem[212 len 2], Mask(80, 0, 'tansferETH'), mem[224 len 10]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[202 len 10]]:
      revert with 0, 'permission deny'
  if _param2 > unknownef95b90e:
      revert with 0, 'single excceed'
  call _param1 with:
     value _param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x4789dd6c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 34]]]
# const = None
# payable = False
def unknown4789dd6c(addr _param1): # not payable
  return unknown4789dd6c[_param1]


# hash = 0x4bf5cb14
# getter = ['struct', ['loc', 11]]
# const = None
# payable = False
def unknown4bf5cb14(uint256 _param1): # not payable
  require _param1 < unknownee483063.length
  return unknownee483063[_param1].field_512, unknownee483063[_param1].field_768, unknownee483063[_param1].field_1024


# hash = 0x4c577b95
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 17]]]]]
# const = None
# payable = False
def unknown4c577b95(addr _param1, addr _param2): # not payable
  return unknown4c577b95[_param1][_param2]


# hash = 0x4ecc9779
# getter = None
# const = None
# payable = True
def unknown4ecc9779(uint256 _param1, uint256 _param2) payable: 
  if _param2 <= 0:
      revert with 0, 'amt > 0'
  require _param1 < unknownee483063.length
  if unknownee483063[_param1].field_256 != caller:
      revert with 0, 'it is not your invest'
  if not unknownee483063[_param1].field_1280:
      revert with 0, 'this order is finished'
  require ext_code.size(unknownfaa9efe3[stor11[_param1].field_0])
  call unknownfaa9efe3[stor11[_param1].field_0].0xef98ffb5 with:
       gas gas_remaining wei
      args _param1, _param2, call.value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  unknownee483063[_param1].field_1024 += ext_call.return_data[0]
  unknownee483063[_param1].field_1280 = uint8(bool(ext_call.return_data[32]))
  if ext_call.return_data[64]:
      require tokenPrice[stor11[_param1].field_0]
      require ext_code.size(unknownee483063[_param1].field_0)
      call unknownee483063[_param1].field_0.0xd5078158 with:
           gas gas_remaining wei
          args caller, unknowne57fb80e[stor11[_param1].field_0], 10^18 * call.value * unknown8215c67f[stor11[_param1].field_0] / 10000 / tokenPrice[stor11[_param1].field_0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      unknown88b45046 += call.value * unknown059c657f[stor11[_param1].field_0] / 10000
      if call.value * unknown059c657f[stor11[_param1].field_0] / 10000 >= call.value:
          revert with 0, 'handlingFeeBuyETH error'
      unknownee483063.length++
      stor175B[stor11.length] = unknownee483063[_param1].field_0
      stor175B[stor11.length] = caller
      stor175B[stor11.length] = call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000)
      stor175B[stor11.length] = block.timestamp
      stor175B[stor11.length] = 0
      stor175B[stor11.length] = 1
      log 0x1e4558e8: unknownee483063.length + 1, call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000), block.timestamp, unknownee483063[_param1].field_0, caller
      unknown98f5d445[stor11[_param1].field_0][caller] = call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000)
      unknown17ff16e2[stor11[_param1].field_0][caller] = call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000) + unknown17ff16e2[stor11[_param1].field_0][caller]
      unknownf3d2135c[stor11[_param1].field_0] += (call.value * unknown8be11840[stor11[_param1].field_0]) - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000 * unknown8be11840[stor11[_param1].field_0]) / 10000
      require ext_code.size(unknownfaa9efe3[stor11[_param1].field_0])
      call unknownfaa9efe3[stor11[_param1].field_0].0x13de5b49 with:
           gas gas_remaining wei
          args unknownee483063[_param1].field_0, caller, call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      unknownb3fa871a[stor11[_param1].field_0] = call.value - (call.value * unknown059c657f[stor11[_param1].field_0] / 10000) + unknownb3fa871a[stor11[_param1].field_0]
  unknown88b45046 += ext_call.return_data[0] * unknowna30dbfd6[stor11[_param1].field_0] / 10000
  if ext_call.return_data[0] <= ext_call.return_data[0] * unknowna30dbfd6[stor11[_param1].field_0] / 10000:
      revert with 0, 'handlingFeeSellETH error'
  if ext_call.return_data[0] > unknownb3fa871a[stor11[_param1].field_0]:
      revert with 0, 'pool not enough'
  unknownb3fa871a[stor11[_param1].field_0] -= ext_call.return_data[0]
  call caller with:
     value ext_call.return_data[0] - (ext_call.return_data[0] * unknowna30dbfd6[stor11[_param1].field_0] / 10000) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require tokenPrice[stor11[_param1].field_0]
  require ext_code.size(unknownee483063[_param1].field_0)
  call unknownee483063[_param1].field_0.0xd5078158 with:
       gas gas_remaining wei
      args caller, unknowne57fb80e[stor11[_param1].field_0], 10^18 * ext_call.return_data[0] * unknown8b8edd03[stor11[_param1].field_0] / 10000 / tokenPrice[stor11[_param1].field_0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x63ba7464: _param1, ext_call.return_data[0] - (ext_call.return_data[0] * unknowna30dbfd6[stor11[_param1].field_0] / 10000), block.timestamp, unknownee483063[_param1].field_0, caller
  unknowne4fed460[stor11[_param1].field_0][caller] = ext_call.return_data[0] - (ext_call.return_data[0] * unknowna30dbfd6[stor11[_param1].field_0] / 10000) + unknowne4fed460[stor11[_param1].field_0][caller]


# hash = 0x4fab3bad
# getter = None
# const = None
# payable = False
def unknown4fab3bad(addr _param1, addr _param2): # not payable
  return unknownea21a85d[addr(_param1)][addr(_param2)], 
         unknownbda75b77[addr(_param1)][addr(_param2)],
         unknownb0cda0b7[addr(_param1)][addr(_param2)],
         unknown4c577b95[addr(_param1)][addr(_param2)],
         unknown17ff16e2[addr(_param1)][addr(_param2)],
         unknowne4fed460[addr(_param1)][addr(_param2)],
         unknown34e61612[addr(_param1)][addr(_param2)],
         unknowndca4f9e1[addr(_param1)][addr(_param2)],
         bool(stor31[addr(_param1)][addr(_param2)])


# hash = 0x56029aea
# getter = None
# const = None
# payable = False
def unknown56029aea(uint256 _param1): # not payable
  mem[212 len 0] = None
  mem[212] = mem[232 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[212 len 20]]:
      revert with 0, 'permission deny'
  unknownef95b90e = _param1


# hash = 0x585c5b83
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknown585c5b83(uint256 _param1): # not payable
  return unknown585c5b83[_param1]


# hash = 0x5bab7bae
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 31]]]]]]
# const = None
# payable = False
def unknown5bab7bae(addr _param1, addr _param2): # not payable
  return bool(stor31[_param1][_param2])


# hash = 0x64020558
# getter = None
# const = None
# payable = False
def unknown64020558(uint256 _param1, addr _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  if _param1 != 201901261442:
      revert with 0, 'password is not right'
  [93mselfdestruct([91m_param2[93m)


# hash = 0x66f7900f
# getter = None
# const = None
# payable = True
def unknown66f7900f(addr _param1) payable: 
  if bool(stor5[addr(_param1)]) != 1:
      revert with 0, 'ilegal token'
  if call.value < stor23:
      revert with 0, 'msg value is not right'
  if call.value > stor24:
      revert with 0, 'msg value is not right'
  if eth.balance(this.address) > stor22:
      revert with 0, 'no Amount'
  if block.timestamp <= unknowndca4f9e1[addr(_param1)][caller]:
      revert with 0, 'invest interval limited'
  if block.timestamp - unknowndca4f9e1[addr(_param1)][caller] < unknownd0817501[addr(_param1)]:
      revert with 0, 'invest interval limited'
  unknowndca4f9e1[addr(_param1)][caller] = block.timestamp
  require tokenPrice[addr(_param1)]
  require ext_code.size(_param1)
  call _param1.0xd5078158 with:
       gas gas_remaining wei
      args caller, unknowne57fb80e[addr(_param1)], 10^18 * call.value * unknown8215c67f[addr(_param1)] / 10000 / tokenPrice[addr(_param1)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknown88b45046 += call.value * unknown059c657f[addr(_param1)] / 10000
  if call.value * unknown059c657f[addr(_param1)] / 10000 >= call.value:
      revert with 0, 'handlingFeeBuyETH error'
  unknownee483063.length++
  stor175B[stor11.length] = _param1
  stor175B[stor11.length] = caller
  stor175B[stor11.length] = call.value - (call.value * unknown059c657f[addr(_param1)] / 10000)
  stor175B[stor11.length] = block.timestamp
  stor175B[stor11.length] = 0
  stor175B[stor11.length] = 1
  log 0x1e4558e8: unknownee483063.length + 1, call.value - (call.value * unknown059c657f[addr(_param1)] / 10000), block.timestamp, _param1, caller
  unknown98f5d445[addr(_param1)][caller] = call.value - (call.value * unknown059c657f[addr(_param1)] / 10000)
  unknown17ff16e2[addr(_param1)][caller] = call.value - (call.value * unknown059c657f[addr(_param1)] / 10000) + unknown17ff16e2[addr(_param1)][caller]
  unknownf3d2135c[addr(_param1)] += (call.value * unknown8be11840[addr(_param1)]) - (call.value * unknown059c657f[addr(_param1)] / 10000 * unknown8be11840[addr(_param1)]) / 10000
  require ext_code.size(unknownfaa9efe3[addr(_param1)])
  call unknownfaa9efe3[addr(_param1)].0x13de5b49 with:
       gas gas_remaining wei
      args addr(_param1), caller, call.value - (call.value * unknown059c657f[addr(_param1)] / 10000)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknownb3fa871a[addr(_param1)] = call.value - (call.value * unknown059c657f[addr(_param1)] / 10000) + unknownb3fa871a[addr(_param1)]


# hash = 0x67565017
# getter = None
# const = None
# payable = True
def unknown67565017(addr _param1, addr _param2) payable: 
  if bool(stor5[addr(_param2)]) != 1:
      revert with 0, 'ilegal token'
  if caller == _param1:
      revert with 0, 'Can't refer self'
  if unknown34e61612[addr(_param2)][caller]:
      revert with 0, 'you have already set refer'
  unknown34e61612[addr(_param2)][caller] = _param1
  unknownea21a85d[addr(_param2)][addr(_param1)]++
  log 0x6cbfe858: _param1, caller
  if bool(stor5[addr(_param2)]) != 1:
      revert with 0, 'ilegal token'
  if call.value < stor23:
      revert with 0, 'msg value is not right'
  if call.value > stor24:
      revert with 0, 'msg value is not right'
  if eth.balance(this.address) > stor22:
      revert with 0, 'no Amount'
  if block.timestamp <= unknowndca4f9e1[addr(_param2)][caller]:
      revert with 0, 'invest interval limited'
  if block.timestamp - unknowndca4f9e1[addr(_param2)][caller] < unknownd0817501[addr(_param2)]:
      revert with 0, 'invest interval limited'
  unknowndca4f9e1[addr(_param2)][caller] = block.timestamp
  require tokenPrice[addr(_param2)]
  require ext_code.size(_param2)
  call _param2.0xd5078158 with:
       gas gas_remaining wei
      args caller, unknowne57fb80e[addr(_param2)], 10^18 * call.value * unknown8215c67f[addr(_param2)] / 10000 / tokenPrice[addr(_param2)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknown88b45046 += call.value * unknown059c657f[addr(_param2)] / 10000
  if call.value * unknown059c657f[addr(_param2)] / 10000 >= call.value:
      revert with 0, 'handlingFeeBuyETH error'
  unknownee483063.length++
  stor175B[stor11.length] = _param2
  stor175B[stor11.length] = caller
  stor175B[stor11.length] = call.value - (call.value * unknown059c657f[addr(_param2)] / 10000)
  stor175B[stor11.length] = block.timestamp
  stor175B[stor11.length] = 0
  stor175B[stor11.length] = 1
  log 0x1e4558e8: unknownee483063.length + 1, call.value - (call.value * unknown059c657f[addr(_param2)] / 10000), block.timestamp, _param2, caller
  unknown98f5d445[addr(_param2)][caller] = call.value - (call.value * unknown059c657f[addr(_param2)] / 10000)
  unknown17ff16e2[addr(_param2)][caller] = call.value - (call.value * unknown059c657f[addr(_param2)] / 10000) + unknown17ff16e2[addr(_param2)][caller]
  unknownf3d2135c[addr(_param2)] += (call.value * unknown8be11840[addr(_param2)]) - (call.value * unknown059c657f[addr(_param2)] / 10000 * unknown8be11840[addr(_param2)]) / 10000
  require ext_code.size(unknownfaa9efe3[addr(_param2)])
  call unknownfaa9efe3[addr(_param2)].0x13de5b49 with:
       gas gas_remaining wei
      args addr(_param2), caller, call.value - (call.value * unknown059c657f[addr(_param2)] / 10000)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknownb3fa871a[addr(_param2)] = call.value - (call.value * unknown059c657f[addr(_param2)] / 10000) + unknownb3fa871a[addr(_param2)]


# hash = 0x6a6d42b3
# getter = None
# const = None
# payable = False
def unknown6a6d42b3(addr _param1, uint256 _param2): # not payable
  if bool(stor5[addr(_param1)]) != 1:
      revert with 0, 'ilegal call'
  if bool(stor31[addr(_param1)][caller]) != 1:
      revert with 0, 'you are not super address'
  require ext_code.size(unknownfaa9efe3[addr(_param1)])
  call unknownfaa9efe3[addr(_param1)].0x1268b86e with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'contrDrawCheck failed'
  if _param2 > unknownf3d2135c[addr(_param1)]:
      revert with 0, 'contrDrawAcctBalance not enough'
  unknownf3d2135c[addr(_param1)] -= _param2
  unknown4789dd6c[addr(_param1)] += _param2
  unknownefde7d9b[addr(_param1)] = block.timestamp
  if _param2 > unknownb3fa871a[addr(_param1)]:
      revert with 0, 'ethpool not enough'
  unknownb3fa871a[addr(_param1)] -= _param2
  call caller with:
     value _param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x4942a19c: _param2, block.timestamp, _param1, caller


# hash = 0x6c887157
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 10]]]]
# const = None
# payable = False
def unknown6c887157(addr _param1): # not payable
  return bool(stor10[_param1])


# hash = 0x6e5de674
# getter = None
# const = None
# payable = False
def unknown6e5de674(addr _param1): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  owner = _param1


# hash = 0x756742f8
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 5]]]]
# const = None
# payable = False
def unknown756742f8(addr _param1): # not payable
  return bool(stor5[_param1])


# hash = 0x78f5baa9
# getter = None
# const = None
# payable = False
def unknown78f5baa9(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  mem[207 len 0] = None
  mem[207] = uint16('setGlobalConfig'), mem[224 len 15]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[207 len 15]]:
      revert with 0, 'permission deny'
  stor22 = _param1
  stor23 = _param2
  stor24 = _param3


# hash = 0x7b1c88be
# getter = None
# const = None
# payable = False
def unknown7b1c88be(addr _param1, uint256 _param2): # not payable
  mem[206 len 0] = None
  mem[206] = uint32('transferIncome'), mem[224 len 14]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[206 len 14]]:
      revert with 0, 'permission deny'
  if _param2 > unknown88b45046:
      revert with 0, '_value excceed error'
  unknown88b45046 -= _param2
  call _param1 with:
     value _param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x7b74d6a6
# getter = None
# const = None
# payable = False
def unknown7b74d6a6(addr _param1, bool _param2): # not payable
  mem[206 len 0] = None
  mem[206] = uint32('setMasterRefer'), mem[224 len 14]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[206 len 14]]:
      revert with 0, 'permission deny'
  stor36[addr(_param1)] = uint8(_param2)


# hash = 0x8215c67f
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 25]]]
# const = None
# payable = False
def unknown8215c67f(addr _param1): # not payable
  return unknown8215c67f[_param1]


# hash = 0x838eea99
# getter = None
# const = None
# payable = False
def unknown838eea99(uint256 _param1, addr _param2): # not payable
  if bool(stor36[caller]) != 1:
      if bool(stor5[addr(_param2)]) != 1:
          revert with 0, 'ilegal token'
      if _param1 <= 0:
          revert with 0, 'amt must bigger than zero'
      require ext_code.size(unknownfaa9efe3[addr(_param2)])
      call unknownfaa9efe3[addr(_param2)].0x6b9d635 with:
           gas gas_remaining wei
          args addr(_param2), caller, _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if bool(ext_call.return_data[0]) != 1:
          revert with 0, 'withdraw check failed'
      if _param1 > unknownb0cda0b7[addr(_param2)][caller]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'amt can not bigger than refer balance'
      unknownb0cda0b7[addr(_param2)][caller] -= _param1
      unknownbda75b77[addr(_param2)][caller] += _param1
      unknown4c577b95[addr(_param2)][caller] = block.timestamp
  unknown88b45046 += _param1 * unknown2b1e2eab[addr(_param2)] / 10000
  if _param1 <= _param1 * unknown2b1e2eab[addr(_param2)] / 10000:
      revert with 0, 'referDrawFeeETH error'
  if _param1 > unknownb3fa871a[addr(_param2)]:
      revert with 0, 'pool not enough'
  unknownb3fa871a[addr(_param2)] -= _param1
  call caller with:
     value _param1 - (_param1 * unknown2b1e2eab[addr(_param2)] / 10000) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require tokenPrice[addr(_param2)]
  require ext_code.size(_param2)
  call _param2.0xd5078158 with:
       gas gas_remaining wei
      args caller, unknowne57fb80e[addr(_param2)], 10^18 * _param1 * unknown21050266[addr(_param2)] / 10000 / tokenPrice[addr(_param2)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x425e355f: _param1, block.timestamp, _param2, caller


# hash = 0x84ba3f69
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def tokenPrice(address _param1): # not payable
  return tokenPrice[_param1]


# hash = 0x88b45046
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def unknown88b45046(): # not payable
  return unknown88b45046


# hash = 0x8b8edd03
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = False
def unknown8b8edd03(addr _param1): # not payable
  return unknown8b8edd03[_param1]


# hash = 0x8be11840
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 32]]]
# const = None
# payable = False
def unknown8be11840(addr _param1): # not payable
  return unknown8be11840[_param1]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8dbc5813
# getter = None
# const = None
# payable = False
def unknown8dbc5813(array _param1): # not payable
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  mem[_param1.length + ceil32(_param1.length) + 160] = unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]]
  return memory
    from _param1.length + ceil32(_param1.length) + 160
     [93mlen 32


# hash = 0x98f5d445
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 19]]]]]
# const = None
# payable = False
def unknown98f5d445(addr _param1, addr _param2): # not payable
  return unknown98f5d445[_param1][_param2]


# hash = 0x9e49ebff
# getter = None
# const = None
# payable = False
def unknown9e49ebff(addr _param1, addr _param2, uint256 _param3): # not payable
  if bool(stor10[caller]) != 1:
      revert with 0, 'ilegal call'
  unknownb0cda0b7[addr(_param1)][addr(_param2)] += _param3


# hash = 0xa30dbfd6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 29]]]
# const = None
# payable = False
def unknowna30dbfd6(addr _param1): # not payable
  return unknowna30dbfd6[_param1]


# hash = 0xa78db3e7
# getter = None
# const = None
# payable = True
def unknowna78db3e7(addr _param1) payable: 
  if bool(stor10[addr(_param1)]) != 1:
      revert with 0, 'ilegal _proxyAddress'
  require ext_code.size(_param1)
  call _param1.0x32ffd1ce with:
       gas gas_remaining wei
      args caller, call.value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xaa8ee3ae
# getter = None
# const = None
# payable = False
def unknownaa8ee3ae(addr _param1): # not payable
  if caller != 0xf4a4e1cba7bbef0cb3200f2ede188950ade48778:
      revert with 0, 'you are not backupOwner'
  owner = _param1


# hash = 0xb0cda0b7
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 15]]]]]
# const = None
# payable = False
def unknownb0cda0b7(addr _param1, addr _param2): # not payable
  return unknownb0cda0b7[_param1][_param2]


# hash = 0xb3fa871a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknownb3fa871a(addr _param1): # not payable
  return unknownb3fa871a[_param1]


# hash = 0xbda75b77
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 16]]]]]
# const = None
# payable = False
def unknownbda75b77(addr _param1, addr _param2): # not payable
  return unknownbda75b77[_param1][_param2]


# hash = 0xd0817501
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 21]]]
# const = None
# payable = False
def unknownd0817501(addr _param1): # not payable
  return unknownd0817501[_param1]


# hash = 0xdca4f9e1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 20]]]]]
# const = None
# payable = False
def unknowndca4f9e1(addr _param1, addr _param2): # not payable
  return unknowndca4f9e1[_param1][_param2]


# hash = 0xddbb695f
# getter = None
# const = None
# payable = False
def unknownddbb695f(addr _param1, bool _param2, uint256 _param3, addr _param4, addr _param5, uint256 _param6, uint256 _param7, uint256 _param8, uint256 _param9, uint256 _param10): # not payable
  mem[207 len 0] = None
  mem[207] = uint16('setAllowedToken'), mem[224 len 15]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[207 len 15]]:
      revert with 0, 'permission deny'
  stor5[addr(_param1)] = uint8(_param2)
  tokenPrice[addr(_param1)] = _param3
  unknownfaa9efe3[addr(_param1)] = _param4
  stor10[addr(_param4)] = 1
  unknowne57fb80e[addr(_param1)] = _param5
  unknown8be11840[addr(_param1)] = _param6
  unknown8215c67f[addr(_param1)] = _param7
  unknown8b8edd03[addr(_param1)] = _param8
  unknownd0817501[addr(_param1)] = _param9
  unknown21050266[addr(_param1)] = _param10


# hash = 0xe2dd7b7b
# getter = None
# const = None
# payable = False
def unknowne2dd7b7b(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('setFeeUseETH'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  unknown059c657f[addr(_param1)] = _param2
  unknowna30dbfd6[addr(_param1)] = _param3
  unknown2b1e2eab[addr(_param1)] = _param4


# hash = 0xe4fed460
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 18]]]]]
# const = None
# payable = False
def unknowne4fed460(addr _param1, addr _param2): # not payable
  return unknowne4fed460[_param1][_param2]


# hash = 0xe57fb80e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def unknowne57fb80e(addr _param1): # not payable
  return unknowne57fb80e[_param1]


# hash = 0xe6206c71
# getter = None
# const = None
# payable = False
def unknowne6206c71(addr _param1, bool _param2): # not payable
  mem[207 len 0] = None
  mem[207] = uint16('setAllowedProxy'), mem[224 len 15]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[207 len 15]]:
      revert with 0, 'permission deny'
  stor10[addr(_param1)] = uint8(_param2)


# hash = 0xe67b6444
# getter = None
# const = None
# payable = False
def unknowne67b6444(addr _param1, addr _param2, uint256 _param3): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('tansferERC20'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  require ext_code.size(_param1)
  call _param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xea21a85d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 14]]]]]
# const = None
# payable = False
def unknownea21a85d(addr _param1, addr _param2): # not payable
  return unknownea21a85d[_param1][_param2]


# hash = 0xed47b26e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 27]]]
# const = None
# payable = False
def unknowned47b26e(addr _param1): # not payable
  return unknown21050266[addr(_param1)]


# hash = 0xedfb2ff3
# getter = None
# const = None
# payable = False
def unknownedfb2ff3(addr _param1, addr _param2, bool _param3): # not payable
  mem[211 len 0] = None
  mem[211] = mem[230 len 13]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[211 len 19]]:
      revert with 0, 'permission deny'
  stor31[addr(_param1)][addr(_param2)] = uint8(_param3)


# hash = 0xee483063
# getter = ['struct', ['loc', 11]]
# const = None
# payable = False
def unknownee483063(uint256 _param1): # not payable
  require _param1 < unknownee483063.length
  return unknownee483063[_param1].field_0, 
         bool(unknownee483063[_param1].field_1280),
         unknownee483063[_param1].field_256,
         unknownee483063[_param1].field_512,
         unknownee483063[_param1].field_768,
         unknownee483063[_param1].field_1024


# hash = 0xef95b90e
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknownef95b90e(): # not payable
  return unknownef95b90e


# hash = 0xefde7d9b
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 35]]]
# const = None
# payable = False
def unknownefde7d9b(addr _param1): # not payable
  return unknownefde7d9b[_param1]


# hash = 0xf3d2135c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 33]]]
# const = None
# payable = False
def unknownf3d2135c(addr _param1): # not payable
  return unknownf3d2135c[_param1]


# hash = 0xf51efd7a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def unknownf51efd7a(addr _param1): # not payable
  return unknownf51efd7a[_param1]


# hash = 0xf720f80b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 36]]]]
# const = None
# payable = False
def unknownf720f80b(addr _param1): # not payable
  return bool(stor36[_param1])


# hash = 0xfaa9efe3
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknownfaa9efe3(addr _param1): # not payable
  return unknownfaa9efe3[_param1]


# hash = 0xfc4524a8
# getter = None
# const = None
# payable = False
def unknownfc4524a8(addr _param1, addr _param2): # not payable
  if bool(stor5[addr(_param1)]) != 1:
      revert with 0, 'ilegal token'
  if caller == _param2:
      revert with 0, 'Can't refer self'
  if unknown34e61612[addr(_param1)][caller]:
      revert with 0, 'you have already set refer'
  unknown34e61612[addr(_param1)][caller] = _param2
  unknownea21a85d[addr(_param1)][addr(_param2)]++
  log 0x6cbfe858: _param2, caller


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


