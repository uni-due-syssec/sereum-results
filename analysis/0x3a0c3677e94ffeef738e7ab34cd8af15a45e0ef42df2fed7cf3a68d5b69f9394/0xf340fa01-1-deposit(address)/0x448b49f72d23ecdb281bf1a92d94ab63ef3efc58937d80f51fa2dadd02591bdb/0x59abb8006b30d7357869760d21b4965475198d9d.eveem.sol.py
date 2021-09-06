# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x59ABb8006B30D7357869760d21B4965475198d9D 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x3253fc7d': 'unknown3253fc7d(?)', '0x50771c87': 'unknown50771c87(?)', '0x7833abb1': 'unknown7833abb1(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    stor1
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6
    # storage address 7
    stor7
    # storage address 8
    unknowna970d378
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10
    # storage address 11
    stor11
    # storage address 12
    unknown8d6f4091
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    stor16 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    stor19
    # storage address 20
    stor20
    # storage address 21
    unknowndb1c7b9b # mask: a s
    # storage address 95949769290960679919915568476335582553435826563121580797397853711946803546973
    storD421 # mask: a s
    # storage address 95949769290960679919915568476335582553435826563121580797397853711946803546974
    storD421 # mask: a s
    # storage address 95949769290960679919915568476335582553435826563121580797397853711946803546975
    storD421 # mask: a s
    # storage address 95949769290960679919915568476335582553435826563121580797397853711946803546977
    stor95949769290960679919915568476335582553435826563121580797397853711946803546977
# hash = 0x0636bebe
# getter = None
# const = None
# payable = False
def unknown0636bebe(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require stor11[_param1]
  require stor7[_param2]
  require not unknown8d6f4091[stor11[_param1]][4][_param2].field_0
  require _param3 >= 1
  require _param3 <= 100000
  if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
      revert with 0, 'SafeMath add failed'
  require unknown8d6f4091[stor11[_param1]].field_512 + _param3 <= 100000
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['newShareholder'][this.address].field_256:
      stor0['newShareholder'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['newShareholder'][this.address][2][caller].field_0 = 1
      stor0['newShareholder'][this.address][3][stor0['newShareholder'][this.address].field_256].field_0 = caller
      stor0['newShareholder'][this.address].field_256++
      if ext_call.return_data[0] == stor0['newShareholder'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['newShareholder'][this.address].field_256:
              stor0['newShareholder'][this.address][2][stor0['newShareholder'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['newShareholder'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('newShareholder', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['newShareholder'][this.address][3][[94midx].field_0
              continue 
          stor0['newShareholder'][this.address].field_0 = 0
          stor0['newShareholder'][this.address].field_256 = 0
          if unknown8d6f4091[stor11[_param1]].field_768 + 1 < unknown8d6f4091[stor11[_param1]].field_768:
              revert with 0, 'SafeMath add failed'
          if unknowna970d378[stor7[_param2]].field_1024 + 1 < unknowna970d378[stor7[_param2]].field_1024:
              revert with 0, 'SafeMath add failed'
          unknowna970d378[stor7[_param2]].field_1024++
          unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]].field_1024 + 1].field_0 = stor11[_param1]
          unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]].field_1024 + 1].field_256 = _param3
          unknowna970d378[stor7[_param2]][5][_param1].field_0 = unknowna970d378[stor7[_param2]].field_1024 + 1
          if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
              revert with 0, 'SafeMath add failed'
          unknown8d6f4091[stor11[_param1]].field_512 += _param3
          unknown8d6f4091[stor11[_param1]].field_768++
          unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]].field_768 + 1].field_0 = stor7[_param2]
          unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]].field_768 + 1].field_256 = _param3
          unknown8d6f4091[stor11[_param1]][4][_param2].field_0 = unknown8d6f4091[stor11[_param1]].field_768 + 1
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['newShareholder'][this.address].field_0:
          if not stor0['newShareholder'][this.address][2][caller].field_0:
              stor0['newShareholder'][this.address][2][caller].field_0 = 1
              stor0['newShareholder'][this.address][3][stor0['newShareholder'][this.address].field_256].field_0 = caller
              stor0['newShareholder'][this.address].field_256++
          if ext_call.return_data[0] == stor0['newShareholder'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['newShareholder'][this.address].field_256:
                  stor0['newShareholder'][this.address][2][stor0['newShareholder'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['newShareholder'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('newShareholder', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['newShareholder'][this.address][3][[94midx].field_0
                  continue 
              stor0['newShareholder'][this.address].field_0 = 0
              stor0['newShareholder'][this.address].field_256 = 0
              if unknown8d6f4091[stor11[_param1]].field_768 + 1 < unknown8d6f4091[stor11[_param1]].field_768:
                  revert with 0, 'SafeMath add failed'
              if unknowna970d378[stor7[_param2]].field_1024 + 1 < unknowna970d378[stor7[_param2]].field_1024:
                  revert with 0, 'SafeMath add failed'
              unknowna970d378[stor7[_param2]].field_1024++
              unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]].field_1024 + 1].field_0 = stor11[_param1]
              unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]].field_1024 + 1].field_256 = _param3
              unknowna970d378[stor7[_param2]][5][_param1].field_0 = unknowna970d378[stor7[_param2]].field_1024 + 1
              if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
                  revert with 0, 'SafeMath add failed'
              unknown8d6f4091[stor11[_param1]].field_512 += _param3
              unknown8d6f4091[stor11[_param1]].field_768++
              unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]].field_768 + 1].field_0 = stor7[_param2]
              unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]].field_768 + 1].field_256 = _param3
              unknown8d6f4091[stor11[_param1]][4][_param2].field_0 = unknown8d6f4091[stor11[_param1]].field_768 + 1
  log 0xfb002d08 


# hash = 0x0839e0fb
# getter = None
# const = None
# payable = False
def migrationReceiver_setup(): # not payable
  if addr(stor1.length) != caller:
      require 0xe752b7d837a6969a5986467b0109bdf052e45bdb == caller
  stor9 = 0
  stor13 = 0
  return 1


# hash = 0x0efcf295
# getter = None
# const = None
# payable = False
def deleteAnyProposal(bytes32 _whatFunction): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  [94midx = 0
  [94ms = 0
  while [94midx < stor0[_whatFunction][this.address].field_256:
      stor0[_whatFunction][this.address][2][stor0[_whatFunction][this.address][3][[94midx].field_0].field_0 = 0
      stor0[_whatFunction][this.address][3][[94midx].field_0 = 0
      mem[0] = sha3(_whatFunction, this.address)
      mem[32] = 0
      [94midx = [94midx + 1
      [94ms = stor0[_whatFunction][this.address][3][[94midx].field_0
      continue 
  stor0[_whatFunction][this.address].field_0 = 0
  stor0[_whatFunction][this.address].field_256 = 0
  log 0xd126b186 


# hash = 0x0f9c0b10
# getter = ['struct', ['loc', 8]]
# const = None
# payable = False
def unknown0f9c0b10(uint256 _param1): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknowna970d378[stor7[_param1]].field_0, 
         unknowna970d378[stor7[_param1]].field_256,
         unknowna970d378[stor7[_param1]].field_1024,
         unknowna970d378[stor7[_param1]].field_768 / 10^18


# hash = 0x1e7bcf9a
# getter = None
# const = None
# payable = False
def unknown1e7bcf9a(): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require bool(stor1.length.field_160) == 1
  require 1 > stor3
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['migrate3_corp'][this.address].field_256:
      stor0['migrate3_corp'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['migrate3_corp'][this.address][2][caller].field_0 = 1
      stor0['migrate3_corp'][this.address][3][stor0['migrate3_corp'][this.address].field_256].field_0 = caller
      stor0['migrate3_corp'][this.address].field_256++
      if ext_call.return_data[0] == stor0['migrate3_corp'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['migrate3_corp'][this.address].field_256:
              stor0['migrate3_corp'][this.address][2][stor0['migrate3_corp'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['migrate3_corp'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('migrate3_corp', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['migrate3_corp'][this.address][3][[94midx].field_0
              continue 
          stor0['migrate3_corp'][this.address].field_0 = 0
          stor0['migrate3_corp'][this.address].field_256 = 0
          require ext_code.size(stor2)
          call stor2.0xba3c623d with:
               gas gas_remaining wei
              args stor2, storD421, storD421, storD421
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 1 == bool(ext_call.return_data[0]):
              [94midx = 1
              while [94midx <= storD421:
                  mem[268] = 1
                  mem[300] = [94midx
                  mem[332] = storD421[[94midx].field_0
                  mem[364] = unknowna970d378[storD421[[94midx].field_0].field_512
                  mem[396] = storD421[[94midx].field_256
                  require ext_code.size(stor2)
                  call stor2.0x4c36e831 with:
                       gas gas_remaining wei
                      args 1, [94midx, storD421[[94midx].field_0, unknowna970d378[storD421[[94midx].field_0].field_512, storD421[[94midx].field_256
                  mem[264] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = 1
                  mem[32] = 12
                  if bool(ext_call.return_data[0]) != 1:
                      [94midx = [94midx
                      continue 
                  [94midx = [94midx + 1
                  continue 
              stor3 = 1
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['migrate3_corp'][this.address].field_0:
          if not stor0['migrate3_corp'][this.address][2][caller].field_0:
              stor0['migrate3_corp'][this.address][2][caller].field_0 = 1
              stor0['migrate3_corp'][this.address][3][stor0['migrate3_corp'][this.address].field_256].field_0 = caller
              stor0['migrate3_corp'][this.address].field_256++
          if ext_call.return_data[0] == stor0['migrate3_corp'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['migrate3_corp'][this.address].field_256:
                  stor0['migrate3_corp'][this.address][2][stor0['migrate3_corp'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['migrate3_corp'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('migrate3_corp', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['migrate3_corp'][this.address][3][[94midx].field_0
                  continue 
              stor0['migrate3_corp'][this.address].field_0 = 0
              stor0['migrate3_corp'][this.address].field_256 = 0
              require ext_code.size(stor2)
              call stor2.0xba3c623d with:
                   gas gas_remaining wei
                  args stor2, storD421, storD421, storD421
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 1 == bool(ext_call.return_data[0]):
                  [94midx = 1
                  while [94midx <= storD421:
                      mem[268] = 1
                      mem[300] = [94midx
                      mem[332] = storD421[[94midx].field_0
                      mem[364] = unknowna970d378[storD421[[94midx].field_0].field_512
                      mem[396] = storD421[[94midx].field_256
                      require ext_code.size(stor2)
                      call stor2.0x4c36e831 with:
                           gas gas_remaining wei
                          args 1, [94midx, storD421[[94midx].field_0, unknowna970d378[storD421[[94midx].field_0].field_512, storD421[[94midx].field_256
                      mem[264] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[0] = 1
                      mem[32] = 12
                      if bool(ext_call.return_data[0]) != 1:
                          [94midx = [94midx
                          continue 
                      [94midx = [94midx + 1
                      continue 
                  stor3 = 1
  log 0xcdbf3cba: stor3


# hash = 0x289a9202
# getter = None
# const = None
# payable = False
def unknown289a9202(): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  return addr(stor1.length), stor2, bool(stor1.length.field_160), stor4, stor3, stor9, stor13


# hash = 0x33cd5dc9
# getter = None
# const = None
# payable = False
def unknown33cd5dc9(): # not payable
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  stor16 += (100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18
  stor17 += (100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18
  if eth.balance(this.address) > ((100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18) + stor17:
      stor16 = eth.balance(this.address) - stor17 + stor16
      stor17 = eth.balance(this.address)
  [94midx = 1
  while [94midx <= stor18 - (100000 * stor18 / 100000):
      if not stor19[[94midx].field_256:
          if 0 < unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
              if stor14 > 0:
                  if stor15 < 0:
                      revert with 0, 'SafeMath add failed'
              require unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
              [94ms = 0
              [94ms = 1
              while [94ms <= unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_768:
                  if not 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                      if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 < 0:
                          revert with 0, 'SafeMath add failed'
                  else:
                      if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 / 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 != unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256:
                          revert with 0, 'SafeMath mul failed'
                      if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 + (unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512) < unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                          revert with 0, 'SafeMath add failed'
                      unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 += unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                      if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 0 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 > 0:
                          revert with 0, 'SafeMath sub failed'
                  mem[0] = stor10[stor19[[94midx].field_0]
                  mem[32] = 12
                  [94ms = unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_0
                  [94ms = [94ms + 1
                  continue 
          if stor15 < 0:
              revert with 0, 'SafeMath add failed'
      else:
          if 10^18 * stor19[[94midx].field_256 / stor19[[94midx].field_256 != 10^18:
              revert with 0, 'SafeMath mul failed'
          if 0 >= unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
              if stor15 + (10^18 * stor19[[94midx].field_256) < 10^18 * stor19[[94midx].field_256:
                  revert with 0, 'SafeMath add failed'
              stor15 += 10^18 * stor19[[94midx].field_256
          else:
              if stor14 <= 0:
                  require unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                  [94ms = 0
                  [94ms = 1
                  while [94ms <= unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_768:
                      if not 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                          if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 < 0:
                              revert with 0, 'SafeMath add failed'
                          if 0 > 10^18 * stor19[[94midx].field_256:
                              revert with 0, 'SafeMath sub failed'
                      else:
                          if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 / 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 != unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256:
                              revert with 0, 'SafeMath mul failed'
                          if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 + (unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512) < unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                              revert with 0, 'SafeMath add failed'
                          unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 += unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                          if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 > 10^18 * stor19[[94midx].field_256:
                              revert with 0, 'SafeMath sub failed'
                      mem[0] = stor10[stor19[[94midx].field_0]
                      mem[32] = 12
                      [94ms = unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_0
                      [94ms = [94ms + 1
                      continue 
                  if stor15 + (10^18 * stor19[[94midx].field_256) < 10^18 * stor19[[94midx].field_256:
                      revert with 0, 'SafeMath add failed'
                  stor15 += 10^18 * stor19[[94midx].field_256
              else:
                  if not 10^18 * stor19[[94midx].field_256:
                      if stor15 < 0:
                          revert with 0, 'SafeMath add failed'
                      if 0 > 10^18 * stor19[[94midx].field_256:
                          revert with 0, 'SafeMath sub failed'
                      require unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                      [94ms = 0
                      [94ms = 1
                      while [94ms <= unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_768:
                          if not 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                              if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 < 0:
                                  revert with 0, 'SafeMath add failed'
                              if 0 > 10^18 * stor19[[94midx].field_256:
                                  revert with 0, 'SafeMath sub failed'
                          else:
                              if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 / 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 != unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256:
                                  revert with 0, 'SafeMath mul failed'
                              if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 + (unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512) < unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                                  revert with 0, 'SafeMath add failed'
                              unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 += unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                              if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * 10^18 * stor19[[94midx].field_256 / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 > 10^18 * stor19[[94midx].field_256:
                                  revert with 0, 'SafeMath sub failed'
                          mem[0] = stor10[stor19[[94midx].field_0]
                          mem[32] = 12
                          [94ms = unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_0
                          [94ms = [94ms + 1
                          continue 
                      if stor15 + (10^18 * stor19[[94midx].field_256) < 10^18 * stor19[[94midx].field_256:
                          revert with 0, 'SafeMath add failed'
                      stor15 += 10^18 * stor19[[94midx].field_256
                  else:
                      if 10^18 * stor14 * stor19[[94midx].field_256 / 10^18 * stor19[[94midx].field_256 != stor14:
                          revert with 0, 'SafeMath mul failed'
                      if stor15 + (10^18 * stor14 * stor19[[94midx].field_256 / 100) < 10^18 * stor14 * stor19[[94midx].field_256 / 100:
                          revert with 0, 'SafeMath add failed'
                      stor15 += 10^18 * stor14 * stor19[[94midx].field_256 / 100
                      if 10^18 * stor14 * stor19[[94midx].field_256 / 100 > 10^18 * stor19[[94midx].field_256:
                          revert with 0, 'SafeMath sub failed'
                      require unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                      [94ms = 0
                      [94ms = 1
                      while [94ms <= unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_768:
                          if not (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                              if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 < 0:
                                  revert with 0, 'SafeMath add failed'
                              if 0 > (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100):
                                  revert with 0, 'SafeMath sub failed'
                          else:
                              if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 / (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 != unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256:
                                  revert with 0, 'SafeMath mul failed'
                              if unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 + (unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512) < unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512:
                                  revert with 0, 'SafeMath add failed'
                              unknowna970d378[stor12[stor10[stor19[[94midx].field_0]][5][[94ms].field_0].field_768 += unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512
                              if unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_256 * (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100) / unknown8d6f4091[stor10[stor19[[94midx].field_0]].field_512 > (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100):
                                  revert with 0, 'SafeMath sub failed'
                          mem[0] = stor10[stor19[[94midx].field_0]
                          mem[32] = 12
                          [94ms = unknown8d6f4091[stor10[stor19[[94midx].field_0]][5][[94ms].field_0
                          [94ms = [94ms + 1
                          continue 
                      if stor15 < 0:
                          revert with 0, 'SafeMath add failed'
                      stor15 = stor15 + (10^18 * stor19[[94midx].field_256) - (10^18 * stor14 * stor19[[94midx].field_256 / 100)
      stor20[stor19[[94midx].field_0] = 0
      mem[0] = [94midx
      mem[32] = 19
      stor19[[94midx].field_256 = 0
      [94midx = [94midx + 1
      continue 
  stor18 = 0
  log 0xafb42f19: stor15 / 10^18, stor16


# hash = 0x40c6f852
# getter = None
# const = None
# payable = False
def unknown40c6f852(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require stor11[_param1]
  require stor7[_param2]
  if _param3 > unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256:
      revert with 0, 'SafeMath sub failed'
  require unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 - _param3 >= 0
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['removeShares'][this.address].field_256:
      stor0['removeShares'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['removeShares'][this.address][2][caller].field_0 = 1
      stor0['removeShares'][this.address][3][stor0['removeShares'][this.address].field_256].field_0 = caller
      stor0['removeShares'][this.address].field_256++
      if ext_call.return_data[0] == stor0['removeShares'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['removeShares'][this.address].field_256:
              stor0['removeShares'][this.address][2][stor0['removeShares'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['removeShares'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('removeShares', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['removeShares'][this.address][3][[94midx].field_0
              continue 
          stor0['removeShares'][this.address].field_0 = 0
          stor0['removeShares'][this.address].field_256 = 0
          if _param3 > unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256:
              revert with 0, 'SafeMath sub failed'
          unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 -= _param3
          if _param3 > unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256:
              revert with 0, 'SafeMath sub failed'
          unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 -= _param3
          if _param3 > unknown8d6f4091[stor11[_param1]].field_512:
              revert with 0, 'SafeMath sub failed'
          unknown8d6f4091[stor11[_param1]].field_512 -= _param3
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['removeShares'][this.address].field_0:
          if not stor0['removeShares'][this.address][2][caller].field_0:
              stor0['removeShares'][this.address][2][caller].field_0 = 1
              stor0['removeShares'][this.address][3][stor0['removeShares'][this.address].field_256].field_0 = caller
              stor0['removeShares'][this.address].field_256++
          if ext_call.return_data[0] == stor0['removeShares'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['removeShares'][this.address].field_256:
                  stor0['removeShares'][this.address][2][stor0['removeShares'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['removeShares'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('removeShares', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['removeShares'][this.address][3][[94midx].field_0
                  continue 
              stor0['removeShares'][this.address].field_0 = 0
              stor0['removeShares'][this.address].field_256 = 0
              if _param3 > unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256:
                  revert with 0, 'SafeMath sub failed'
              unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 -= _param3
              if _param3 > unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256:
                  revert with 0, 'SafeMath sub failed'
              unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 -= _param3
              if _param3 > unknown8d6f4091[stor11[_param1]].field_512:
                  revert with 0, 'SafeMath sub failed'
              unknown8d6f4091[stor11[_param1]].field_512 -= _param3
  log 0xd2d69e99 


# hash = 0x4c36e831
# getter = None
# const = None
# payable = False
def unknown4c36e831(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  unknown8d6f4091[_param1][5][_param2].field_0 = _param3
  unknown8d6f4091[_param1][5][_param2].field_256 = _param5
  unknown8d6f4091[_param1][4][_param4].field_0 = _param2
  return 1


# hash = 0x4f5a7c66
# getter = None
# const = None
# payable = False
def unknown4f5a7c66(): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return stor14, 
         (100000 * stor18 / 100000) - (100 * 10^18 * stor18 / 100 * 10^18) / 100000,
         (100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18,
         stor18 - (100000 * stor18 / 100000),
         stor16,
         stor15 / 10^18


# hash = 0x556c5ff3
# getter = None
# const = None
# payable = False
def unknown556c5ff3(bool _param1, uint256 _param2, addr _param3): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  if _param1 == 1:
      require _param2
      require not stor1.length.field_160
      require ext_code.size(_param3)
      call _param3.migrationReceiver_setup() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require 1 == bool(ext_call.return_data[0])
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['migrate1_setup'][this.address].field_256:
      stor0['migrate1_setup'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['migrate1_setup'][this.address][2][caller].field_0 = 1
      stor0['migrate1_setup'][this.address][3][stor0['migrate1_setup'][this.address].field_256].field_0 = caller
      stor0['migrate1_setup'][this.address].field_256++
      if ext_call.return_data[0] == stor0['migrate1_setup'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['migrate1_setup'][this.address].field_256:
              stor0['migrate1_setup'][this.address][2][stor0['migrate1_setup'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['migrate1_setup'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('migrate1_setup', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['migrate1_setup'][this.address][3][[94midx].field_0
              continue 
          stor0['migrate1_setup'][this.address].field_0 = 0
          stor0['migrate1_setup'][this.address].field_256 = 0
          if _param1:
              stor5 = _param2
              require ext_code.size(0xe752b7d837a6969a5986467b0109bdf052e45bdb)
              call 0xe752b7d837a6969a5986467b0109bdf052e45bdb.startMigration(address newCorpBank) with:
                   gas gas_remaining wei
                  args _param3
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require 1 == bool(ext_call.return_data[0])
              stor2 = _param3
          else:
              require ext_code.size(0xe752b7d837a6969a5986467b0109bdf052e45bdb)
              call 0xe752b7d837a6969a5986467b0109bdf052e45bdb.cancelMigration() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require 1 == bool(ext_call.return_data[0])
              stor5 = 0
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['migrate2_members'][this.address].field_256:
                  stor0['migrate2_members'][this.address][2][stor0['migrate2_members'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['migrate2_members'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('migrate2_members', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['migrate2_members'][this.address][3][[94midx].field_0
                  continue 
              stor0['migrate2_members'][this.address].field_0 = 0
              stor0['migrate2_members'][this.address].field_256 = 0
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['migrate4_dapps'][this.address].field_256:
                  stor0['migrate4_dapps'][this.address][2][stor0['migrate4_dapps'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['migrate4_dapps'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('migrate4_dapps', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['migrate4_dapps'][this.address][3][[94midx].field_0
                  continue 
              stor0['migrate4_dapps'][this.address].field_0 = 0
              stor0['migrate4_dapps'][this.address].field_256 = 0
              stor2 = 0
          stor1.length.field_160 = Mask(96, 0, _param1)
          stor3 = 0
          stor4 = 0
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['migrate1_setup'][this.address].field_0:
          if not stor0['migrate1_setup'][this.address][2][caller].field_0:
              stor0['migrate1_setup'][this.address][2][caller].field_0 = 1
              stor0['migrate1_setup'][this.address][3][stor0['migrate1_setup'][this.address].field_256].field_0 = caller
              stor0['migrate1_setup'][this.address].field_256++
          if ext_call.return_data[0] == stor0['migrate1_setup'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['migrate1_setup'][this.address].field_256:
                  stor0['migrate1_setup'][this.address][2][stor0['migrate1_setup'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['migrate1_setup'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('migrate1_setup', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['migrate1_setup'][this.address][3][[94midx].field_0
                  continue 
              stor0['migrate1_setup'][this.address].field_0 = 0
              stor0['migrate1_setup'][this.address].field_256 = 0
              if _param1:
                  stor5 = _param2
                  require ext_code.size(0xe752b7d837a6969a5986467b0109bdf052e45bdb)
                  call 0xe752b7d837a6969a5986467b0109bdf052e45bdb.startMigration(address newCorpBank) with:
                       gas gas_remaining wei
                      args _param3
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 1 == bool(ext_call.return_data[0])
                  stor2 = _param3
              else:
                  require ext_code.size(0xe752b7d837a6969a5986467b0109bdf052e45bdb)
                  call 0xe752b7d837a6969a5986467b0109bdf052e45bdb.cancelMigration() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 1 == bool(ext_call.return_data[0])
                  stor5 = 0
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor0['migrate2_members'][this.address].field_256:
                      stor0['migrate2_members'][this.address][2][stor0['migrate2_members'][this.address][3][[94midx].field_0].field_0 = 0
                      stor0['migrate2_members'][this.address][3][[94midx].field_0 = 0
                      mem[0] = sha3('migrate2_members', this.address)
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0['migrate2_members'][this.address][3][[94midx].field_0
                      continue 
                  stor0['migrate2_members'][this.address].field_0 = 0
                  stor0['migrate2_members'][this.address].field_256 = 0
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor0['migrate4_dapps'][this.address].field_256:
                      stor0['migrate4_dapps'][this.address][2][stor0['migrate4_dapps'][this.address][3][[94midx].field_0].field_0 = 0
                      stor0['migrate4_dapps'][this.address][3][[94midx].field_0 = 0
                      mem[0] = sha3('migrate4_dapps', this.address)
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0['migrate4_dapps'][this.address][3][[94midx].field_0
                      continue 
                  stor0['migrate4_dapps'][this.address].field_0 = 0
                  stor0['migrate4_dapps'][this.address].field_256 = 0
                  stor2 = 0
              stor1.length.field_160 = Mask(96, 0, _param1)
              stor3 = 0
              stor4 = 0
  log 0x7f983c2c: bool(stor1.length.field_160)


# hash = 0x5d976d1a
# getter = None
# const = None
# payable = False
def unknown5d976d1a(addr _param1, array _param2): # not payable
  mem[64] = ceil32(_param2.length) + 128
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  if stor1.length.field_160:
      revert with 0, 'cannot execute while in migratin'
  mem[ceil32(_param2.length) + 132] = caller
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  mem[ceil32(_param2.length) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  mem[0] = _param1
  mem[32] = 10
  require stor10[addr(_param1)]
  if _param2.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _param2.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _param2.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _param2.length - 1 < _param2.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param2.length + -ceil32(_param2.length) + 31) + 248, mem[_param2.length + 127 len ceil32(_param2.length) + -_param2.length + 1]) << 8 * _param2.length + -ceil32(_param2.length) + 31:
      revert with 0, 'string cannot start or end with space'
  require 0 < _param2.length
  if Mask(8, 248, mem[128]) != 0x3000000000000000000000000000000000000000000000000000000000000000:
      [94midx = 0
      [94ms = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94midx < _param2.length
          require [94midx < _param2.length
          if Mask(8, 248, mem[[94midx + 128]) <= '@':
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _param2.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) < '[':
                  mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < _param2.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_714 = mem[128]
      mem[32] = 11
      require not stor11[mem[128]]
      mem[0] = mem[128]
      require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
      call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_772 = mem[64]
      mem[mem[64] + 32] = 'updateDapp'
      mem[mem[64] + 64] = addr(this.address)
      [94m_773 = mem[64]
      mem[mem[64]] = 52
      mem[64] = mem[64] + 84
      [94m_774 = mem[[94m_773]
      mem[[94m_772 + 84 len floor32(mem[[94m_773])] = mem[[94m_773 + 32 len floor32(mem[[94m_773])]
      mem[[94m_772 + floor32(mem[[94m_773]) + 84] = mem[[94m_772 + floor32(mem[[94m_773]) + 84] and 256^(-(mem[[94m_773] % 32) + 32) - 1 or mem[[94m_773 + floor32(mem[[94m_773]) + 32] and !(256^(-(mem[[94m_773] % 32) + 32) - 1)
      [94m_1387 = sha3(mem[mem[64] len [94m_772 + [94m_774 + -mem[64] + 84])
      mem[0] = sha3(mem[mem[64] len [94m_772 + [94m_774 + -mem[64] + 84])
      mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
      if not stor0[mem[0]].field_256:
          stor0[[94m_1387].field_0 = sha3(call.data[0 len calldata.size])
          stor0[[94m_1387][2][caller].field_0 = 1
          stor0[[94m_1387][3][stor0[mem[0]].field_256].field_0 = caller
          mem[0] = [94m_1387
          mem[32] = 0
          stor0[[94m_1387].field_256++
          if ext_call.return_data[0] == stor0[[94m_1387].field_256 + 1:
              [94m_1446 = mem[64]
              mem[mem[64] + 32] = 'updateDapp'
              mem[mem[64] + 64] = addr(this.address)
              [94m_1447 = mem[64]
              mem[mem[64]] = 52
              mem[64] = mem[64] + 84
              [94m_1448 = mem[[94m_1447]
              mem[[94m_1446 + 84 len floor32(mem[[94m_1447])] = mem[[94m_1447 + 32 len floor32(mem[[94m_1447])]
              mem[[94m_1446 + floor32(mem[[94m_1447]) + 84] = mem[[94m_1446 + floor32(mem[[94m_1447]) + 84] and 256^(-(mem[[94m_1447] % 32) + 32) - 1 or mem[[94m_1447 + floor32(mem[[94m_1447]) + 32] and !(256^(-(mem[[94m_1447] % 32) + 32) - 1)
              [94m_1737 = sha3(mem[mem[64] len [94m_1446 + [94m_1448 + -mem[64] + 84])
              mem[0] = sha3(mem[mem[64] len [94m_1446 + [94m_1448 + -mem[64] + 84])
              [94m_1934 = sha3(mem[0], 0)
              [94midx = 0
              [94ms = 0
              while [94midx < stor1[[94m_1934].field_0:
                  stor0[[94m_1737][2][stor0[[94m_1737][3][[94midx].field_0].field_0 = 0
                  stor0[[94m_1737][3][[94midx].field_0 = 0
                  mem[0] = [94m_1737
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0[[94m_1737][3][[94midx].field_0
                  continue 
              stor0[[94m_1737].field_0 = 0
              stor0[[94m_1737].field_256 = 0
              stor11[stor12[stor10[addr(_param1)]].field_256] = 0
              stor11[[94m_714] = stor10[addr(_param1)]
              unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_714
      else:
          if sha3(call.data[0 len calldata.size]) == stor0[[94m_1387].field_0:
              if stor0[[94m_1387][2][caller].field_0:
                  mem[0] = [94m_1387
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1387].field_256:
                      [94m_1472 = mem[64]
                      mem[mem[64] + 32] = 'updateDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1473 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1474 = mem[[94m_1473]
                      mem[[94m_1472 + 84 len floor32(mem[[94m_1473])] = mem[[94m_1473 + 32 len floor32(mem[[94m_1473])]
                      mem[[94m_1472 + floor32(mem[[94m_1473]) + 84] = mem[[94m_1472 + floor32(mem[[94m_1473]) + 84] and 256^(-(mem[[94m_1473] % 32) + 32) - 1 or mem[[94m_1473 + floor32(mem[[94m_1473]) + 32] and !(256^(-(mem[[94m_1473] % 32) + 32) - 1)
                      [94m_1717 = sha3(mem[mem[64] len [94m_1472 + [94m_1474 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1472 + [94m_1474 + -mem[64] + 84])
                      [94m_1930 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_1930].field_0:
                          stor0[[94m_1717][2][stor0[[94m_1717][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1717][3][[94midx].field_0 = 0
                          mem[0] = [94m_1717
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1717][3][[94midx].field_0
                          continue 
                      stor0[[94m_1717].field_0 = 0
                      stor0[[94m_1717].field_256 = 0
                      stor11[stor12[stor10[addr(_param1)]].field_256] = 0
                      stor11[[94m_714] = stor10[addr(_param1)]
                      unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_714
              else:
                  stor0[[94m_1387][2][caller].field_0 = 1
                  stor0[[94m_1387][3][stor0[mem[0]].field_256].field_0 = caller
                  stor0[[94m_1387].field_256++
                  mem[0] = [94m_1387
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1387].field_256:
                      [94m_1510 = mem[64]
                      mem[mem[64] + 32] = 'updateDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1511 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1512 = mem[[94m_1511]
                      mem[[94m_1510 + 84 len floor32(mem[[94m_1511])] = mem[[94m_1511 + 32 len floor32(mem[[94m_1511])]
                      mem[[94m_1510 + floor32(mem[[94m_1511]) + 84] = mem[[94m_1510 + floor32(mem[[94m_1511]) + 84] and 256^(-(mem[[94m_1511] % 32) + 32) - 1 or mem[[94m_1511 + floor32(mem[[94m_1511]) + 32] and !(256^(-(mem[[94m_1511] % 32) + 32) - 1)
                      [94m_1727 = sha3(mem[mem[64] len [94m_1510 + [94m_1512 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1510 + [94m_1512 + -mem[64] + 84])
                      [94m_1932 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_1932].field_0:
                          stor0[[94m_1727][2][stor0[[94m_1727][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1727][3][[94midx].field_0 = 0
                          mem[0] = [94m_1727
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1727][3][[94midx].field_0
                          continue 
                      stor0[[94m_1727].field_0 = 0
                      stor0[[94m_1727].field_256 = 0
                      stor11[stor12[stor10[addr(_param1)]].field_256] = 0
                      stor11[[94m_714] = stor10[addr(_param1)]
                      unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_714
  else:
      require 1 < _param2.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _param2.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
      [94midx = 0
      [94ms = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94midx < _param2.length
          require [94midx < _param2.length
          if Mask(8, 248, mem[[94midx + 128]) <= '@':
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _param2.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) < '[':
                  mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < _param2.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_718 = mem[128]
      mem[32] = 11
      require not stor11[mem[128]]
      mem[0] = mem[128]
      require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
      call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_779 = mem[64]
      mem[mem[64] + 32] = 'updateDapp'
      mem[mem[64] + 64] = addr(this.address)
      [94m_780 = mem[64]
      mem[mem[64]] = 52
      mem[64] = mem[64] + 84
      [94m_781 = mem[[94m_780]
      mem[[94m_779 + 84 len floor32(mem[[94m_780])] = mem[[94m_780 + 32 len floor32(mem[[94m_780])]
      mem[[94m_779 + floor32(mem[[94m_780]) + 84] = mem[[94m_779 + floor32(mem[[94m_780]) + 84] and 256^(-(mem[[94m_780] % 32) + 32) - 1 or mem[[94m_780 + floor32(mem[[94m_780]) + 32] and !(256^(-(mem[[94m_780] % 32) + 32) - 1)
      [94m_1392 = sha3(mem[mem[64] len [94m_779 + [94m_781 + -mem[64] + 84])
      mem[0] = sha3(mem[mem[64] len [94m_779 + [94m_781 + -mem[64] + 84])
      mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
      if not stor0[mem[0]].field_256:
          stor0[[94m_1392].field_0 = sha3(call.data[0 len calldata.size])
          stor0[[94m_1392][2][caller].field_0 = 1
          stor0[[94m_1392][3][stor0[mem[0]].field_256].field_0 = caller
          mem[0] = [94m_1392
          mem[32] = 0
          stor0[[94m_1392].field_256++
          if ext_call.return_data[0] == stor0[[94m_1392].field_256 + 1:
              [94m_1453 = mem[64]
              mem[mem[64] + 32] = 'updateDapp'
              mem[mem[64] + 64] = addr(this.address)
              [94m_1454 = mem[64]
              mem[mem[64]] = 52
              mem[64] = mem[64] + 84
              [94m_1455 = mem[[94m_1454]
              mem[[94m_1453 + 84 len floor32(mem[[94m_1454])] = mem[[94m_1454 + 32 len floor32(mem[[94m_1454])]
              mem[[94m_1453 + floor32(mem[[94m_1454]) + 84] = mem[[94m_1453 + floor32(mem[[94m_1454]) + 84] and 256^(-(mem[[94m_1454] % 32) + 32) - 1 or mem[[94m_1454 + floor32(mem[[94m_1454]) + 32] and !(256^(-(mem[[94m_1454] % 32) + 32) - 1)
              [94m_1772 = sha3(mem[mem[64] len [94m_1453 + [94m_1455 + -mem[64] + 84])
              mem[0] = sha3(mem[mem[64] len [94m_1453 + [94m_1455 + -mem[64] + 84])
              [94m_1941 = sha3(mem[0], 0)
              [94midx = 0
              [94ms = 0
              while [94midx < stor1[[94m_1941].field_0:
                  stor0[[94m_1772][2][stor0[[94m_1772][3][[94midx].field_0].field_0 = 0
                  stor0[[94m_1772][3][[94midx].field_0 = 0
                  mem[0] = [94m_1772
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0[[94m_1772][3][[94midx].field_0
                  continue 
              stor0[[94m_1772].field_0 = 0
              stor0[[94m_1772].field_256 = 0
              stor11[stor12[stor10[addr(_param1)]].field_256] = 0
              stor11[[94m_718] = stor10[addr(_param1)]
              unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_718
      else:
          if sha3(call.data[0 len calldata.size]) == stor0[[94m_1392].field_0:
              if stor0[[94m_1392][2][caller].field_0:
                  mem[0] = [94m_1392
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1392].field_256:
                      [94m_1488 = mem[64]
                      mem[mem[64] + 32] = 'updateDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1489 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1490 = mem[[94m_1489]
                      mem[[94m_1488 + 84 len floor32(mem[[94m_1489])] = mem[[94m_1489 + 32 len floor32(mem[[94m_1489])]
                      mem[[94m_1488 + floor32(mem[[94m_1489]) + 84] = mem[[94m_1488 + floor32(mem[[94m_1489]) + 84] and 256^(-(mem[[94m_1489] % 32) + 32) - 1 or mem[[94m_1489 + floor32(mem[[94m_1489]) + 32] and !(256^(-(mem[[94m_1489] % 32) + 32) - 1)
                      [94m_1752 = sha3(mem[mem[64] len [94m_1488 + [94m_1490 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1488 + [94m_1490 + -mem[64] + 84])
                      [94m_1937 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_1937].field_0:
                          stor0[[94m_1752][2][stor0[[94m_1752][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1752][3][[94midx].field_0 = 0
                          mem[0] = [94m_1752
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1752][3][[94midx].field_0
                          continue 
                      stor0[[94m_1752].field_0 = 0
                      stor0[[94m_1752].field_256 = 0
                      stor11[stor12[stor10[addr(_param1)]].field_256] = 0
                      stor11[[94m_718] = stor10[addr(_param1)]
                      unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_718
              else:
                  stor0[[94m_1392][2][caller].field_0 = 1
                  stor0[[94m_1392][3][stor0[mem[0]].field_256].field_0 = caller
                  stor0[[94m_1392].field_256++
                  mem[0] = [94m_1392
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1392].field_256:
                      [94m_1519 = mem[64]
                      mem[mem[64] + 32] = 'updateDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1520 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1521 = mem[[94m_1520]
                      mem[[94m_1519 + 84 len floor32(mem[[94m_1520])] = mem[[94m_1520 + 32 len floor32(mem[[94m_1520])]
                      mem[[94m_1519 + floor32(mem[[94m_1520]) + 84] = mem[[94m_1519 + floor32(mem[[94m_1520]) + 84] and 256^(-(mem[[94m_1520] % 32) + 32) - 1 or mem[[94m_1520 + floor32(mem[[94m_1520]) + 32] and !(256^(-(mem[[94m_1520] % 32) + 32) - 1)
                      [94m_1762 = sha3(mem[mem[64] len [94m_1519 + [94m_1521 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1519 + [94m_1521 + -mem[64] + 84])
                      [94m_1939 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_1939].field_0:
                          stor0[[94m_1762][2][stor0[[94m_1762][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1762][3][[94midx].field_0 = 0
                          mem[0] = [94m_1762
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1762][3][[94midx].field_0
                          continue 
                      stor0[[94m_1762].field_0 = 0
                      stor0[[94m_1762].field_256 = 0
                      stor11[stor12[stor10[addr(_param1)]].field_256] = 0
                      stor11[[94m_718] = stor10[addr(_param1)]
                      unknown8d6f4091[stor10[addr(_param1)]].field_256 = [94m_718
  log 0x751d9667 


# hash = 0x6f8d4b3a
# getter = None
# const = None
# payable = False
def unknown6f8d4b3a(addr _param1, uint256 _param2): # not payable
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  stor18 = (100 * 10^18 * _param2) + stor18 + 1
  stor20[addr(_param1)] = (100 * 10^18 * _param2) + stor18 + (-100000 * (100 * 10^18 * _param2) + stor18 + 1 / 100000) + 1
  stor19[(100 * 10^18 * _param2) + stor18 + (-100000 * (100 * 10^18 * _param2) + stor18 + 1 / 100000) + 1].field_0 = _param1
  if stor19[(100 * 10^18 * _param2) + stor18 + (-100000 * (100 * 10^18 * _param2) + stor18 + 1 / 100000) + 1].field_256 + _param2 < _param2:
      revert with 0, 'SafeMath add failed'
  stor19[(100 * 10^18 * _param2) + stor18 + (-100000 * (100 * 10^18 * _param2) + stor18 + 1 / 100000) + 1].field_256 += _param2
  return 1


# hash = 0x768f930d
# getter = None
# const = None
# payable = False
def checkSignersByAddress(bytes32 _whatFunction, uint256 _signerA, uint256 _signerB, uint256 _signerC): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  if _signerA <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'MSFun checkSigner failed - 0 not allowed'
  if _signerB <= 0:
      revert with 0, 'MSFun checkSigner failed - 0 not allowed'
  if _signerC <= 0:
      revert with 0, 'MSFun checkSigner failed - 0 not allowed'
  return stor0[_whatFunction][this.address][3][_signerA - 1].field_0, 
         stor0[_whatFunction][this.address][3][_signerB - 1].field_0,
         stor0[_whatFunction][this.address][3][_signerC - 1].field_0


# hash = 0x76c19546
# getter = None
# const = None
# payable = False
def unknown76c19546(addr _param1, array _param2, array _param3): # not payable
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  mem[64] = ceil32(_param2.length) + ceil32(_param3.length) + 160
  mem[ceil32(_param2.length) + 128] = _param3.length
  mem[ceil32(_param2.length) + 160 len _param3.length] = _param3[all]
  if stor1.length.field_160:
      revert with 0, 'cannot execute while in migratin'
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 164] = caller
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 160] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require not stor6[addr(_param1)]
  if _param3.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _param3.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _param3.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + 160]):
      revert with 0, 'string cannot start or end with space'
  require _param3.length - 1 < _param3.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param3.length + -ceil32(_param3.length) + 31) + 248, mem[ceil32(_param2.length) + _param3.length + 159 len ceil32(_param3.length) + -_param3.length + 1]) << 8 * _param3.length + -ceil32(_param3.length) + 31:
      revert with 0, 'string cannot start or end with space'
  require 0 < _param3.length
  if Mask(8, 248, mem[ceil32(_param2.length) + 160]) != 0x3000000000000000000000000000000000000000000000000000000000000000:
      [94midx = 0
      [94ms = 0
      while [94midx < _param3.length:
          require [94midx < _param3.length
          require [94midx < _param3.length
          require [94midx < _param3.length
          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '@':
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '`':
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '{':
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]):
                  require [94midx + 1 < _param3.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 161]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param3.length
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '0':
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param3.length
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) < '[':
                  mem[ceil32(_param2.length) + [94midx + 160 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '`':
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '{':
                              require [94midx < _param3.length
                              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param3.length
                              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]):
                      require [94midx + 1 < _param3.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 161]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '0':
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_1875 = mem[ceil32(_param2.length) + 160]
      mem[0] = mem[ceil32(_param2.length) + 160]
      mem[32] = 7
      require not stor7[mem[ceil32(_param2.length) + 160]]
      if _param2.length > 32:
          revert with 0, 'string must be between 1 and 32 characters'
      if _param2.length <= 0:
          revert with 0, 'string must be between 1 and 32 characters'
      require 0 < _param2.length
      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
          revert with 0, 'string cannot start or end with space'
      require _param2.length - 1 < _param2.length
      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param2.length + -ceil32(_param2.length) + 31) + 248, mem[_param2.length + 127 len ceil32(_param2.length) + -_param2.length + 1]) << 8 * _param2.length + -ceil32(_param2.length) + 31:
          revert with 0, 'string cannot start or end with space'
      require 0 < _param2.length
      if Mask(8, 248, mem[128]) != 0x3000000000000000000000000000000000000000000000000000000000000000:
          [94midx = 0
          [94ms = 0
          while [94midx < mem[96]:
              require [94midx < mem[96]
              require [94midx < mem[96]
              require [94midx < mem[96]
              if Mask(8, 248, mem[[94midx + 128]) <= '@':
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < mem[96]
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
              else:
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) < '[':
                      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '`':
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                          else:
                              if Mask(8, 248, mem[[94midx + 128]) >= '{':
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                      revert with 0, 'string contains invalid characters'
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                      revert with 0, 'string contains invalid characters'
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                          require [94midx + 1 < mem[96]
                          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                              revert with 0, 'string cannot contain consecutive spaces'
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) >= '0':
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '9':
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
              [94midx = [94midx + 1
              [94ms = 1
              continue 
          if bool([94ms) != 1:
              revert with 0, 'string cannot be only numbers'
          [94m_3709 = mem[128]
          require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
          call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_3805 = mem[64]
          mem[mem[64] + 32] = 'addMember'
          mem[mem[64] + 64] = addr(this.address)
          [94m_3806 = mem[64]
          mem[mem[64]] = 52
          mem[64] = mem[64] + 84
          [94m_3807 = mem[[94m_3806]
          mem[[94m_3805 + 84 len floor32(mem[[94m_3806])] = mem[[94m_3806 + 32 len floor32(mem[[94m_3806])]
          mem[[94m_3805 + floor32(mem[[94m_3806]) + 84] = mem[[94m_3805 + floor32(mem[[94m_3806]) + 84] and 256^(-(mem[[94m_3806] % 32) + 32) - 1 or mem[[94m_3806 + floor32(mem[[94m_3806]) + 32] and !(256^(-(mem[[94m_3806] % 32) + 32) - 1)
          [94m_5160 = sha3(mem[mem[64] len [94m_3805 + [94m_3807 + -mem[64] + 84])
          mem[0] = sha3(mem[mem[64] len [94m_3805 + [94m_3807 + -mem[64] + 84])
          mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
          if not stor0[mem[0]].field_256:
              stor0[[94m_5160].field_0 = sha3(call.data[0 len calldata.size])
              stor0[[94m_5160][2][caller].field_0 = 1
              stor0[[94m_5160][3][stor0[mem[0]].field_256].field_0 = caller
              mem[0] = [94m_5160
              mem[32] = 0
              stor0[[94m_5160].field_256++
              if ext_call.return_data[0] == stor0[[94m_5160].field_256 + 1:
                  [94m_5302 = mem[64]
                  mem[mem[64] + 32] = 'addMember'
                  mem[mem[64] + 64] = addr(this.address)
                  [94m_5303 = mem[64]
                  mem[mem[64]] = 52
                  mem[64] = mem[64] + 84
                  [94m_5304 = mem[[94m_5303]
                  mem[[94m_5302 + 84 len floor32(mem[[94m_5303])] = mem[[94m_5303 + 32 len floor32(mem[[94m_5303])]
                  mem[[94m_5302 + floor32(mem[[94m_5303]) + 84] = mem[[94m_5302 + floor32(mem[[94m_5303]) + 84] and 256^(-(mem[[94m_5303] % 32) + 32) - 1 or mem[[94m_5303 + floor32(mem[[94m_5303]) + 32] and !(256^(-(mem[[94m_5303] % 32) + 32) - 1)
                  [94m_5942 = sha3(mem[mem[64] len [94m_5302 + [94m_5304 + -mem[64] + 84])
                  mem[0] = sha3(mem[mem[64] len [94m_5302 + [94m_5304 + -mem[64] + 84])
                  [94m_6447 = sha3(mem[0], 0)
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor1[[94m_6447].field_0:
                      stor0[[94m_5942][2][stor0[[94m_5942][3][[94midx].field_0].field_0 = 0
                      stor0[[94m_5942][3][[94midx].field_0 = 0
                      mem[0] = [94m_5942
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0[[94m_5942][3][[94midx].field_0
                      continue 
                  stor0[[94m_5942].field_0 = 0
                  stor0[[94m_5942].field_256 = 0
                  if stor9 + 1 < stor9:
                      revert with 0, 'SafeMath add failed'
                  stor9++
                  stor6[addr(_param1)] = stor9 + 1
                  stor7[[94m_1875] = stor9 + 1
                  unknowna970d378[stor9 + 1].field_0 = _param1
                  unknowna970d378[stor9].field_256 = [94m_3709
                  unknowna970d378[stor9].field_512 = [94m_1875
          else:
              if sha3(call.data[0 len calldata.size]) == stor0[[94m_5160].field_0:
                  if stor0[[94m_5160][2][caller].field_0:
                      mem[0] = [94m_5160
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5160].field_256:
                          [94m_5361 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5362 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5363 = mem[[94m_5362]
                          mem[[94m_5361 + 84 len floor32(mem[[94m_5362])] = mem[[94m_5362 + 32 len floor32(mem[[94m_5362])]
                          mem[[94m_5361 + floor32(mem[[94m_5362]) + 84] = mem[[94m_5361 + floor32(mem[[94m_5362]) + 84] and 256^(-(mem[[94m_5362] % 32) + 32) - 1 or mem[[94m_5362 + floor32(mem[[94m_5362]) + 32] and !(256^(-(mem[[94m_5362] % 32) + 32) - 1)
                          [94m_5922 = sha3(mem[mem[64] len [94m_5361 + [94m_5363 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5361 + [94m_5363 + -mem[64] + 84])
                          [94m_6443 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6443].field_0:
                              stor0[[94m_5922][2][stor0[[94m_5922][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_5922][3][[94midx].field_0 = 0
                              mem[0] = [94m_5922
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_5922][3][[94midx].field_0
                              continue 
                          stor0[[94m_5922].field_0 = 0
                          stor0[[94m_5922].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1875] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3709
                          unknowna970d378[stor9].field_512 = [94m_1875
                  else:
                      stor0[[94m_5160][2][caller].field_0 = 1
                      stor0[[94m_5160][3][stor0[mem[0]].field_256].field_0 = caller
                      stor0[[94m_5160].field_256++
                      mem[0] = [94m_5160
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5160].field_256:
                          [94m_5431 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5432 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5433 = mem[[94m_5432]
                          mem[[94m_5431 + 84 len floor32(mem[[94m_5432])] = mem[[94m_5432 + 32 len floor32(mem[[94m_5432])]
                          mem[[94m_5431 + floor32(mem[[94m_5432]) + 84] = mem[[94m_5431 + floor32(mem[[94m_5432]) + 84] and 256^(-(mem[[94m_5432] % 32) + 32) - 1 or mem[[94m_5432 + floor32(mem[[94m_5432]) + 32] and !(256^(-(mem[[94m_5432] % 32) + 32) - 1)
                          [94m_5932 = sha3(mem[mem[64] len [94m_5431 + [94m_5433 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5431 + [94m_5433 + -mem[64] + 84])
                          [94m_6445 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6445].field_0:
                              stor0[[94m_5932][2][stor0[[94m_5932][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_5932][3][[94midx].field_0 = 0
                              mem[0] = [94m_5932
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_5932][3][[94midx].field_0
                              continue 
                          stor0[[94m_5932].field_0 = 0
                          stor0[[94m_5932].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1875] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3709
                          unknowna970d378[stor9].field_512 = [94m_1875
      else:
          require 1 < _param2.length
          if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
              revert with 0, 'string cannot start with 0x'
          require 1 < _param2.length
          if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
              revert with 0, 'string cannot start with 0X'
          [94midx = 0
          [94ms = 0
          while [94midx < mem[96]:
              require [94midx < mem[96]
              require [94midx < mem[96]
              require [94midx < mem[96]
              if Mask(8, 248, mem[[94midx + 128]) <= '@':
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < mem[96]
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
              else:
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) < '[':
                      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '`':
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                          else:
                              if Mask(8, 248, mem[[94midx + 128]) >= '{':
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                      revert with 0, 'string contains invalid characters'
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                      revert with 0, 'string contains invalid characters'
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                          require [94midx + 1 < mem[96]
                          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                              revert with 0, 'string cannot contain consecutive spaces'
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) >= '0':
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '9':
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
              [94midx = [94midx + 1
              [94ms = 1
              continue 
          if bool([94ms) != 1:
              revert with 0, 'string cannot be only numbers'
          [94m_3713 = mem[128]
          require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
          call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_3812 = mem[64]
          mem[mem[64] + 32] = 'addMember'
          mem[mem[64] + 64] = addr(this.address)
          [94m_3813 = mem[64]
          mem[mem[64]] = 52
          mem[64] = mem[64] + 84
          [94m_3814 = mem[[94m_3813]
          mem[[94m_3812 + 84 len floor32(mem[[94m_3813])] = mem[[94m_3813 + 32 len floor32(mem[[94m_3813])]
          mem[[94m_3812 + floor32(mem[[94m_3813]) + 84] = mem[[94m_3812 + floor32(mem[[94m_3813]) + 84] and 256^(-(mem[[94m_3813] % 32) + 32) - 1 or mem[[94m_3813 + floor32(mem[[94m_3813]) + 32] and !(256^(-(mem[[94m_3813] % 32) + 32) - 1)
          [94m_5165 = sha3(mem[mem[64] len [94m_3812 + [94m_3814 + -mem[64] + 84])
          mem[0] = sha3(mem[mem[64] len [94m_3812 + [94m_3814 + -mem[64] + 84])
          mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
          if not stor0[mem[0]].field_256:
              stor0[[94m_5165].field_0 = sha3(call.data[0 len calldata.size])
              stor0[[94m_5165][2][caller].field_0 = 1
              stor0[[94m_5165][3][stor0[mem[0]].field_256].field_0 = caller
              mem[0] = [94m_5165
              mem[32] = 0
              stor0[[94m_5165].field_256++
              if ext_call.return_data[0] == stor0[[94m_5165].field_256 + 1:
                  [94m_5310 = mem[64]
                  mem[mem[64] + 32] = 'addMember'
                  mem[mem[64] + 64] = addr(this.address)
                  [94m_5311 = mem[64]
                  mem[mem[64]] = 52
                  mem[64] = mem[64] + 84
                  [94m_5312 = mem[[94m_5311]
                  mem[[94m_5310 + 84 len floor32(mem[[94m_5311])] = mem[[94m_5311 + 32 len floor32(mem[[94m_5311])]
                  mem[[94m_5310 + floor32(mem[[94m_5311]) + 84] = mem[[94m_5310 + floor32(mem[[94m_5311]) + 84] and 256^(-(mem[[94m_5311] % 32) + 32) - 1 or mem[[94m_5311 + floor32(mem[[94m_5311]) + 32] and !(256^(-(mem[[94m_5311] % 32) + 32) - 1)
                  [94m_5977 = sha3(mem[mem[64] len [94m_5310 + [94m_5312 + -mem[64] + 84])
                  mem[0] = sha3(mem[mem[64] len [94m_5310 + [94m_5312 + -mem[64] + 84])
                  [94m_6454 = sha3(mem[0], 0)
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor1[[94m_6454].field_0:
                      stor0[[94m_5977][2][stor0[[94m_5977][3][[94midx].field_0].field_0 = 0
                      stor0[[94m_5977][3][[94midx].field_0 = 0
                      mem[0] = [94m_5977
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0[[94m_5977][3][[94midx].field_0
                      continue 
                  stor0[[94m_5977].field_0 = 0
                  stor0[[94m_5977].field_256 = 0
                  if stor9 + 1 < stor9:
                      revert with 0, 'SafeMath add failed'
                  stor9++
                  stor6[addr(_param1)] = stor9 + 1
                  stor7[[94m_1875] = stor9 + 1
                  unknowna970d378[stor9 + 1].field_0 = _param1
                  unknowna970d378[stor9].field_256 = [94m_3713
                  unknowna970d378[stor9].field_512 = [94m_1875
          else:
              if sha3(call.data[0 len calldata.size]) == stor0[[94m_5165].field_0:
                  if stor0[[94m_5165][2][caller].field_0:
                      mem[0] = [94m_5165
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5165].field_256:
                          [94m_5377 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5378 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5379 = mem[[94m_5378]
                          mem[[94m_5377 + 84 len floor32(mem[[94m_5378])] = mem[[94m_5378 + 32 len floor32(mem[[94m_5378])]
                          mem[[94m_5377 + floor32(mem[[94m_5378]) + 84] = mem[[94m_5377 + floor32(mem[[94m_5378]) + 84] and 256^(-(mem[[94m_5378] % 32) + 32) - 1 or mem[[94m_5378 + floor32(mem[[94m_5378]) + 32] and !(256^(-(mem[[94m_5378] % 32) + 32) - 1)
                          [94m_5957 = sha3(mem[mem[64] len [94m_5377 + [94m_5379 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5377 + [94m_5379 + -mem[64] + 84])
                          [94m_6450 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6450].field_0:
                              stor0[[94m_5957][2][stor0[[94m_5957][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_5957][3][[94midx].field_0 = 0
                              mem[0] = [94m_5957
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_5957][3][[94midx].field_0
                              continue 
                          stor0[[94m_5957].field_0 = 0
                          stor0[[94m_5957].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1875] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3713
                          unknowna970d378[stor9].field_512 = [94m_1875
                  else:
                      stor0[[94m_5165][2][caller].field_0 = 1
                      stor0[[94m_5165][3][stor0[mem[0]].field_256].field_0 = caller
                      stor0[[94m_5165].field_256++
                      mem[0] = [94m_5165
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5165].field_256:
                          [94m_5440 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5441 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5442 = mem[[94m_5441]
                          mem[[94m_5440 + 84 len floor32(mem[[94m_5441])] = mem[[94m_5441 + 32 len floor32(mem[[94m_5441])]
                          mem[[94m_5440 + floor32(mem[[94m_5441]) + 84] = mem[[94m_5440 + floor32(mem[[94m_5441]) + 84] and 256^(-(mem[[94m_5441] % 32) + 32) - 1 or mem[[94m_5441 + floor32(mem[[94m_5441]) + 32] and !(256^(-(mem[[94m_5441] % 32) + 32) - 1)
                          [94m_5967 = sha3(mem[mem[64] len [94m_5440 + [94m_5442 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5440 + [94m_5442 + -mem[64] + 84])
                          [94m_6452 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6452].field_0:
                              stor0[[94m_5967][2][stor0[[94m_5967][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_5967][3][[94midx].field_0 = 0
                              mem[0] = [94m_5967
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_5967][3][[94midx].field_0
                              continue 
                          stor0[[94m_5967].field_0 = 0
                          stor0[[94m_5967].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1875] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3713
                          unknowna970d378[stor9].field_512 = [94m_1875
  else:
      require 1 < _param3.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + 161]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _param3.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + 161]):
          revert with 0, 'string cannot start with 0X'
      [94midx = 0
      [94ms = 0
      while [94midx < _param3.length:
          require [94midx < _param3.length
          require [94midx < _param3.length
          require [94midx < _param3.length
          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '@':
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '`':
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '{':
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]):
                  require [94midx + 1 < _param3.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 161]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param3.length
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '0':
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param3.length
              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) < '[':
                  mem[ceil32(_param2.length) + [94midx + 160 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '`':
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param3.length
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '{':
                              require [94midx < _param3.length
                              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param3.length
                              if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]):
                      require [94midx + 1 < _param3.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 161]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param3.length
                  if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) >= '0':
                      require [94midx < _param3.length
                      if Mask(8, 248, mem[ceil32(_param2.length) + [94midx + 160]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_1879 = mem[ceil32(_param2.length) + 160]
      mem[0] = mem[ceil32(_param2.length) + 160]
      mem[32] = 7
      require not stor7[mem[ceil32(_param2.length) + 160]]
      if _param2.length > 32:
          revert with 0, 'string must be between 1 and 32 characters'
      if _param2.length <= 0:
          revert with 0, 'string must be between 1 and 32 characters'
      require 0 < _param2.length
      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
          revert with 0, 'string cannot start or end with space'
      require _param2.length - 1 < _param2.length
      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param2.length + -ceil32(_param2.length) + 31) + 248, mem[_param2.length + 127 len ceil32(_param2.length) + -_param2.length + 1]) << 8 * _param2.length + -ceil32(_param2.length) + 31:
          revert with 0, 'string cannot start or end with space'
      require 0 < _param2.length
      if Mask(8, 248, mem[128]) != 0x3000000000000000000000000000000000000000000000000000000000000000:
          [94midx = 0
          [94ms = 0
          while [94midx < mem[96]:
              require [94midx < mem[96]
              require [94midx < mem[96]
              require [94midx < mem[96]
              if Mask(8, 248, mem[[94midx + 128]) <= '@':
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < mem[96]
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
              else:
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) < '[':
                      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '`':
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                          else:
                              if Mask(8, 248, mem[[94midx + 128]) >= '{':
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                      revert with 0, 'string contains invalid characters'
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                      revert with 0, 'string contains invalid characters'
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                          require [94midx + 1 < mem[96]
                          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                              revert with 0, 'string cannot contain consecutive spaces'
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) >= '0':
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '9':
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
              [94midx = [94midx + 1
              [94ms = 1
              continue 
          if bool([94ms) != 1:
              revert with 0, 'string cannot be only numbers'
          [94m_3717 = mem[128]
          require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
          call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_3819 = mem[64]
          mem[mem[64] + 32] = 'addMember'
          mem[mem[64] + 64] = addr(this.address)
          [94m_3820 = mem[64]
          mem[mem[64]] = 52
          mem[64] = mem[64] + 84
          [94m_3821 = mem[[94m_3820]
          mem[[94m_3819 + 84 len floor32(mem[[94m_3820])] = mem[[94m_3820 + 32 len floor32(mem[[94m_3820])]
          mem[[94m_3819 + floor32(mem[[94m_3820]) + 84] = mem[[94m_3819 + floor32(mem[[94m_3820]) + 84] and 256^(-(mem[[94m_3820] % 32) + 32) - 1 or mem[[94m_3820 + floor32(mem[[94m_3820]) + 32] and !(256^(-(mem[[94m_3820] % 32) + 32) - 1)
          [94m_5170 = sha3(mem[mem[64] len [94m_3819 + [94m_3821 + -mem[64] + 84])
          mem[0] = sha3(mem[mem[64] len [94m_3819 + [94m_3821 + -mem[64] + 84])
          mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
          if not stor0[mem[0]].field_256:
              stor0[[94m_5170].field_0 = sha3(call.data[0 len calldata.size])
              stor0[[94m_5170][2][caller].field_0 = 1
              stor0[[94m_5170][3][stor0[mem[0]].field_256].field_0 = caller
              mem[0] = [94m_5170
              mem[32] = 0
              stor0[[94m_5170].field_256++
              if ext_call.return_data[0] == stor0[[94m_5170].field_256 + 1:
                  [94m_5318 = mem[64]
                  mem[mem[64] + 32] = 'addMember'
                  mem[mem[64] + 64] = addr(this.address)
                  [94m_5319 = mem[64]
                  mem[mem[64]] = 52
                  mem[64] = mem[64] + 84
                  [94m_5320 = mem[[94m_5319]
                  mem[[94m_5318 + 84 len floor32(mem[[94m_5319])] = mem[[94m_5319 + 32 len floor32(mem[[94m_5319])]
                  mem[[94m_5318 + floor32(mem[[94m_5319]) + 84] = mem[[94m_5318 + floor32(mem[[94m_5319]) + 84] and 256^(-(mem[[94m_5319] % 32) + 32) - 1 or mem[[94m_5319 + floor32(mem[[94m_5319]) + 32] and !(256^(-(mem[[94m_5319] % 32) + 32) - 1)
                  [94m_6012 = sha3(mem[mem[64] len [94m_5318 + [94m_5320 + -mem[64] + 84])
                  mem[0] = sha3(mem[mem[64] len [94m_5318 + [94m_5320 + -mem[64] + 84])
                  [94m_6461 = sha3(mem[0], 0)
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor1[[94m_6461].field_0:
                      stor0[[94m_6012][2][stor0[[94m_6012][3][[94midx].field_0].field_0 = 0
                      stor0[[94m_6012][3][[94midx].field_0 = 0
                      mem[0] = [94m_6012
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0[[94m_6012][3][[94midx].field_0
                      continue 
                  stor0[[94m_6012].field_0 = 0
                  stor0[[94m_6012].field_256 = 0
                  if stor9 + 1 < stor9:
                      revert with 0, 'SafeMath add failed'
                  stor9++
                  stor6[addr(_param1)] = stor9 + 1
                  stor7[[94m_1879] = stor9 + 1
                  unknowna970d378[stor9 + 1].field_0 = _param1
                  unknowna970d378[stor9].field_256 = [94m_3717
                  unknowna970d378[stor9].field_512 = [94m_1879
          else:
              if sha3(call.data[0 len calldata.size]) == stor0[[94m_5170].field_0:
                  if stor0[[94m_5170][2][caller].field_0:
                      mem[0] = [94m_5170
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5170].field_256:
                          [94m_5393 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5394 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5395 = mem[[94m_5394]
                          mem[[94m_5393 + 84 len floor32(mem[[94m_5394])] = mem[[94m_5394 + 32 len floor32(mem[[94m_5394])]
                          mem[[94m_5393 + floor32(mem[[94m_5394]) + 84] = mem[[94m_5393 + floor32(mem[[94m_5394]) + 84] and 256^(-(mem[[94m_5394] % 32) + 32) - 1 or mem[[94m_5394 + floor32(mem[[94m_5394]) + 32] and !(256^(-(mem[[94m_5394] % 32) + 32) - 1)
                          [94m_5992 = sha3(mem[mem[64] len [94m_5393 + [94m_5395 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5393 + [94m_5395 + -mem[64] + 84])
                          [94m_6457 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6457].field_0:
                              stor0[[94m_5992][2][stor0[[94m_5992][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_5992][3][[94midx].field_0 = 0
                              mem[0] = [94m_5992
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_5992][3][[94midx].field_0
                              continue 
                          stor0[[94m_5992].field_0 = 0
                          stor0[[94m_5992].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1879] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3717
                          unknowna970d378[stor9].field_512 = [94m_1879
                  else:
                      stor0[[94m_5170][2][caller].field_0 = 1
                      stor0[[94m_5170][3][stor0[mem[0]].field_256].field_0 = caller
                      stor0[[94m_5170].field_256++
                      mem[0] = [94m_5170
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5170].field_256:
                          [94m_5449 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5450 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5451 = mem[[94m_5450]
                          mem[[94m_5449 + 84 len floor32(mem[[94m_5450])] = mem[[94m_5450 + 32 len floor32(mem[[94m_5450])]
                          mem[[94m_5449 + floor32(mem[[94m_5450]) + 84] = mem[[94m_5449 + floor32(mem[[94m_5450]) + 84] and 256^(-(mem[[94m_5450] % 32) + 32) - 1 or mem[[94m_5450 + floor32(mem[[94m_5450]) + 32] and !(256^(-(mem[[94m_5450] % 32) + 32) - 1)
                          [94m_6002 = sha3(mem[mem[64] len [94m_5449 + [94m_5451 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5449 + [94m_5451 + -mem[64] + 84])
                          [94m_6459 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6459].field_0:
                              stor0[[94m_6002][2][stor0[[94m_6002][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_6002][3][[94midx].field_0 = 0
                              mem[0] = [94m_6002
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_6002][3][[94midx].field_0
                              continue 
                          stor0[[94m_6002].field_0 = 0
                          stor0[[94m_6002].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1879] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3717
                          unknowna970d378[stor9].field_512 = [94m_1879
      else:
          require 1 < _param2.length
          if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
              revert with 0, 'string cannot start with 0x'
          require 1 < _param2.length
          if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
              revert with 0, 'string cannot start with 0X'
          [94midx = 0
          [94ms = 0
          while [94midx < mem[96]:
              require [94midx < mem[96]
              require [94midx < mem[96]
              require [94midx < mem[96]
              if Mask(8, 248, mem[[94midx + 128]) <= '@':
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < mem[96]
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
              else:
                  require [94midx < mem[96]
                  if Mask(8, 248, mem[[94midx + 128]) < '[':
                      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '`':
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < mem[96]
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                          else:
                              if Mask(8, 248, mem[[94midx + 128]) >= '{':
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                      revert with 0, 'string contains invalid characters'
                                  require [94midx < mem[96]
                                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                      revert with 0, 'string contains invalid characters'
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                          require [94midx + 1 < mem[96]
                          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                              revert with 0, 'string cannot contain consecutive spaces'
                      if [94ms:
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
                      require [94midx < mem[96]
                      if Mask(8, 248, mem[[94midx + 128]) >= '0':
                          require [94midx < mem[96]
                          if Mask(8, 248, mem[[94midx + 128]) <= '9':
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
              [94midx = [94midx + 1
              [94ms = 1
              continue 
          if bool([94ms) != 1:
              revert with 0, 'string cannot be only numbers'
          [94m_3721 = mem[128]
          require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
          call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          [94m_3826 = mem[64]
          mem[mem[64] + 32] = 'addMember'
          mem[mem[64] + 64] = addr(this.address)
          [94m_3827 = mem[64]
          mem[mem[64]] = 52
          mem[64] = mem[64] + 84
          [94m_3828 = mem[[94m_3827]
          mem[[94m_3826 + 84 len floor32(mem[[94m_3827])] = mem[[94m_3827 + 32 len floor32(mem[[94m_3827])]
          mem[[94m_3826 + floor32(mem[[94m_3827]) + 84] = mem[[94m_3826 + floor32(mem[[94m_3827]) + 84] and 256^(-(mem[[94m_3827] % 32) + 32) - 1 or mem[[94m_3827 + floor32(mem[[94m_3827]) + 32] and !(256^(-(mem[[94m_3827] % 32) + 32) - 1)
          [94m_5175 = sha3(mem[mem[64] len [94m_3826 + [94m_3828 + -mem[64] + 84])
          mem[0] = sha3(mem[mem[64] len [94m_3826 + [94m_3828 + -mem[64] + 84])
          mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
          if not stor0[mem[0]].field_256:
              stor0[[94m_5175].field_0 = sha3(call.data[0 len calldata.size])
              stor0[[94m_5175][2][caller].field_0 = 1
              stor0[[94m_5175][3][stor0[mem[0]].field_256].field_0 = caller
              mem[0] = [94m_5175
              mem[32] = 0
              stor0[[94m_5175].field_256++
              if ext_call.return_data[0] == stor0[[94m_5175].field_256 + 1:
                  [94m_5326 = mem[64]
                  mem[mem[64] + 32] = 'addMember'
                  mem[mem[64] + 64] = addr(this.address)
                  [94m_5327 = mem[64]
                  mem[mem[64]] = 52
                  mem[64] = mem[64] + 84
                  [94m_5328 = mem[[94m_5327]
                  mem[[94m_5326 + 84 len floor32(mem[[94m_5327])] = mem[[94m_5327 + 32 len floor32(mem[[94m_5327])]
                  mem[[94m_5326 + floor32(mem[[94m_5327]) + 84] = mem[[94m_5326 + floor32(mem[[94m_5327]) + 84] and 256^(-(mem[[94m_5327] % 32) + 32) - 1 or mem[[94m_5327 + floor32(mem[[94m_5327]) + 32] and !(256^(-(mem[[94m_5327] % 32) + 32) - 1)
                  [94m_6047 = sha3(mem[mem[64] len [94m_5326 + [94m_5328 + -mem[64] + 84])
                  mem[0] = sha3(mem[mem[64] len [94m_5326 + [94m_5328 + -mem[64] + 84])
                  [94m_6468 = sha3(mem[0], 0)
                  [94midx = 0
                  [94ms = 0
                  while [94midx < stor1[[94m_6468].field_0:
                      stor0[[94m_6047][2][stor0[[94m_6047][3][[94midx].field_0].field_0 = 0
                      stor0[[94m_6047][3][[94midx].field_0 = 0
                      mem[0] = [94m_6047
                      mem[32] = 0
                      [94midx = [94midx + 1
                      [94ms = stor0[[94m_6047][3][[94midx].field_0
                      continue 
                  stor0[[94m_6047].field_0 = 0
                  stor0[[94m_6047].field_256 = 0
                  if stor9 + 1 < stor9:
                      revert with 0, 'SafeMath add failed'
                  stor9++
                  stor6[addr(_param1)] = stor9 + 1
                  stor7[[94m_1879] = stor9 + 1
                  unknowna970d378[stor9 + 1].field_0 = _param1
                  unknowna970d378[stor9].field_256 = [94m_3721
                  unknowna970d378[stor9].field_512 = [94m_1879
          else:
              if sha3(call.data[0 len calldata.size]) == stor0[[94m_5175].field_0:
                  if stor0[[94m_5175][2][caller].field_0:
                      mem[0] = [94m_5175
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5175].field_256:
                          [94m_5409 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5410 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5411 = mem[[94m_5410]
                          mem[[94m_5409 + 84 len floor32(mem[[94m_5410])] = mem[[94m_5410 + 32 len floor32(mem[[94m_5410])]
                          mem[[94m_5409 + floor32(mem[[94m_5410]) + 84] = mem[[94m_5409 + floor32(mem[[94m_5410]) + 84] and 256^(-(mem[[94m_5410] % 32) + 32) - 1 or mem[[94m_5410 + floor32(mem[[94m_5410]) + 32] and !(256^(-(mem[[94m_5410] % 32) + 32) - 1)
                          [94m_6027 = sha3(mem[mem[64] len [94m_5409 + [94m_5411 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5409 + [94m_5411 + -mem[64] + 84])
                          [94m_6464 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6464].field_0:
                              stor0[[94m_6027][2][stor0[[94m_6027][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_6027][3][[94midx].field_0 = 0
                              mem[0] = [94m_6027
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_6027][3][[94midx].field_0
                              continue 
                          stor0[[94m_6027].field_0 = 0
                          stor0[[94m_6027].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1879] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3721
                          unknowna970d378[stor9].field_512 = [94m_1879
                  else:
                      stor0[[94m_5175][2][caller].field_0 = 1
                      stor0[[94m_5175][3][stor0[mem[0]].field_256].field_0 = caller
                      stor0[[94m_5175].field_256++
                      mem[0] = [94m_5175
                      mem[32] = 0
                      if ext_call.return_data[0] == stor0[[94m_5175].field_256:
                          [94m_5458 = mem[64]
                          mem[mem[64] + 32] = 'addMember'
                          mem[mem[64] + 64] = addr(this.address)
                          [94m_5459 = mem[64]
                          mem[mem[64]] = 52
                          mem[64] = mem[64] + 84
                          [94m_5460 = mem[[94m_5459]
                          mem[[94m_5458 + 84 len floor32(mem[[94m_5459])] = mem[[94m_5459 + 32 len floor32(mem[[94m_5459])]
                          mem[[94m_5458 + floor32(mem[[94m_5459]) + 84] = mem[[94m_5458 + floor32(mem[[94m_5459]) + 84] and 256^(-(mem[[94m_5459] % 32) + 32) - 1 or mem[[94m_5459 + floor32(mem[[94m_5459]) + 32] and !(256^(-(mem[[94m_5459] % 32) + 32) - 1)
                          [94m_6037 = sha3(mem[mem[64] len [94m_5458 + [94m_5460 + -mem[64] + 84])
                          mem[0] = sha3(mem[mem[64] len [94m_5458 + [94m_5460 + -mem[64] + 84])
                          [94m_6466 = sha3(mem[0], 0)
                          [94midx = 0
                          [94ms = 0
                          while [94midx < stor1[[94m_6466].field_0:
                              stor0[[94m_6037][2][stor0[[94m_6037][3][[94midx].field_0].field_0 = 0
                              stor0[[94m_6037][3][[94midx].field_0 = 0
                              mem[0] = [94m_6037
                              mem[32] = 0
                              [94midx = [94midx + 1
                              [94ms = stor0[[94m_6037][3][[94midx].field_0
                              continue 
                          stor0[[94m_6037].field_0 = 0
                          stor0[[94m_6037].field_256 = 0
                          if stor9 + 1 < stor9:
                              revert with 0, 'SafeMath add failed'
                          stor9++
                          stor6[addr(_param1)] = stor9 + 1
                          stor7[[94m_1879] = stor9 + 1
                          unknowna970d378[stor9 + 1].field_0 = _param1
                          unknowna970d378[stor9].field_256 = [94m_3721
                          unknowna970d378[stor9].field_512 = [94m_1879
  log 0xe07c6f79: stor9


# hash = 0x8a27de08
# getter = ['struct', ['loc', 12]]
# const = None
# payable = False
def unknown8a27de08(uint256 _param1): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknown8d6f4091[stor11[_param1]].field_0, 
         unknown8d6f4091[stor11[_param1]].field_512,
         unknown8d6f4091[stor11[_param1]].field_768


# hash = 0x8b2fd39e
# getter = None
# const = None
# payable = True
def unknown8b2fd39e(uint256 _param1, bool _param2) payable: 
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  if not _param2:
      require _param1 > 0
      require stor15 / 10^18 >= _param1
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['companyWithdraw'][this.address].field_256:
      stor0['companyWithdraw'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['companyWithdraw'][this.address][2][caller].field_0 = 1
      stor0['companyWithdraw'][this.address][3][stor0['companyWithdraw'][this.address].field_256].field_0 = caller
      stor0['companyWithdraw'][this.address].field_256++
      if ext_call.return_data[0] == stor0['companyWithdraw'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['companyWithdraw'][this.address].field_256:
              stor0['companyWithdraw'][this.address][2][stor0['companyWithdraw'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['companyWithdraw'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('companyWithdraw', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['companyWithdraw'][this.address][3][[94midx].field_0
              continue 
          stor0['companyWithdraw'][this.address].field_0 = 0
          stor0['companyWithdraw'][this.address].field_256 = 0
          if _param2 != 1:
              if _param1 > stor17:
                  revert with 0, 'SafeMath sub failed'
              stor17 -= _param1
              if not _param1:
                  if 0 > stor15:
                      revert with 0, 'SafeMath sub failed'
              else:
                  if 10^18 * _param1 / _param1 != 10^18:
                      revert with 0, 'SafeMath mul failed'
                  if 10^18 * _param1 > stor15:
                      revert with 0, 'SafeMath sub failed'
                  stor15 += -1 * 10^18 * _param1
              call stor0['companyWithdraw'][this.address][3][0].field_0 with:
                 value _param1 wei
                   gas 2300 * is_zero(value) wei
          else:
              if stor15 / 10^18 > stor17:
                  revert with 0, 'SafeMath sub failed'
              stor17 -= stor15 / 10^18
              if not stor15 / 10^18:
                  if 0 > stor15:
                      revert with 0, 'SafeMath sub failed'
              else:
                  if 10^18 * stor15 / 10^18 / stor15 / 10^18 != 10^18:
                      revert with 0, 'SafeMath mul failed'
                  if 10^18 * stor15 / 10^18 > stor15:
                      revert with 0, 'SafeMath sub failed'
                  stor15 += -1 * 10^18 * stor15 / 10^18
              call stor0['companyWithdraw'][this.address][3][0].field_0 with:
                 value stor15 / 10^18 wei
                   gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['companyWithdraw'][this.address].field_0:
          if not stor0['companyWithdraw'][this.address][2][caller].field_0:
              stor0['companyWithdraw'][this.address][2][caller].field_0 = 1
              stor0['companyWithdraw'][this.address][3][stor0['companyWithdraw'][this.address].field_256].field_0 = caller
              stor0['companyWithdraw'][this.address].field_256++
          if ext_call.return_data[0] == stor0['companyWithdraw'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['companyWithdraw'][this.address].field_256:
                  stor0['companyWithdraw'][this.address][2][stor0['companyWithdraw'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['companyWithdraw'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('companyWithdraw', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['companyWithdraw'][this.address][3][[94midx].field_0
                  continue 
              stor0['companyWithdraw'][this.address].field_0 = 0
              stor0['companyWithdraw'][this.address].field_256 = 0
              if _param2 != 1:
                  if _param1 > stor17:
                      revert with 0, 'SafeMath sub failed'
                  stor17 -= _param1
                  if not _param1:
                      if 0 > stor15:
                          revert with 0, 'SafeMath sub failed'
                  else:
                      if 10^18 * _param1 / _param1 != 10^18:
                          revert with 0, 'SafeMath mul failed'
                      if 10^18 * _param1 > stor15:
                          revert with 0, 'SafeMath sub failed'
                      stor15 += -1 * 10^18 * _param1
                  call stor0['companyWithdraw'][this.address][3][0].field_0 with:
                     value _param1 wei
                       gas 2300 * is_zero(value) wei
              else:
                  if stor15 / 10^18 > stor17:
                      revert with 0, 'SafeMath sub failed'
                  stor17 -= stor15 / 10^18
                  if not stor15 / 10^18:
                      if 0 > stor15:
                          revert with 0, 'SafeMath sub failed'
                  else:
                      if 10^18 * stor15 / 10^18 / stor15 / 10^18 != 10^18:
                          revert with 0, 'SafeMath mul failed'
                      if 10^18 * stor15 / 10^18 > stor15:
                          revert with 0, 'SafeMath sub failed'
                      stor15 += -1 * 10^18 * stor15 / 10^18
                  call stor0['companyWithdraw'][this.address][3][0].field_0 with:
                     value stor15 / 10^18 wei
                       gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
  log 0x2c009d3d: (stor15 / 10^18)


# hash = 0x8d4abb0c
# getter = None
# const = None
# payable = True
def unknown8d4abb0c(uint256 _param1, bool _param2) payable: 
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  if _param2:
      if unknowna970d378[stor6[caller]].field_768 / 10^18 > stor17:
          revert with 0, 'SafeMath sub failed'
      stor17 -= unknowna970d378[stor6[caller]].field_768 / 10^18
      if not unknowna970d378[stor6[caller]].field_768 / 10^18:
          if 0 > unknowna970d378[stor6[caller]].field_768:
              revert with 0, 'SafeMath sub failed'
      else:
          if 10^18 * unknowna970d378[stor6[caller]].field_768 / 10^18 / unknowna970d378[stor6[caller]].field_768 / 10^18 != 10^18:
              revert with 0, 'SafeMath mul failed'
          if 10^18 * unknowna970d378[stor6[caller]].field_768 / 10^18 > unknowna970d378[stor6[caller]].field_768:
              revert with 0, 'SafeMath sub failed'
          unknowna970d378[stor6[caller]].field_768 += -1 * 10^18 * unknowna970d378[stor6[caller]].field_768 / 10^18
      call caller with:
         value unknowna970d378[stor6[caller]].field_768 / 10^18 wei
           gas 2300 * is_zero(value) wei
  else:
      require _param1 > 0
      require unknowna970d378[stor6[caller]].field_768 / 10^18 >= _param1
      if _param1 > stor17:
          revert with 0, 'SafeMath sub failed'
      stor17 -= _param1
      if not _param1:
          if 0 > unknowna970d378[stor6[caller]].field_768:
              revert with 0, 'SafeMath sub failed'
      else:
          if 10^18 * _param1 / _param1 != 10^18:
              revert with 0, 'SafeMath mul failed'
          if 10^18 * _param1 > unknowna970d378[stor6[caller]].field_768:
              revert with 0, 'SafeMath sub failed'
          unknowna970d378[stor6[caller]].field_768 += -1 * 10^18 * _param1
      call caller with:
         value _param1 wei
           gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x5e6dfc75: unknowna970d378[stor6[caller]].field_768 / 10^18, caller


# hash = 0x8d6f4091
# getter = ['struct', ['loc', 12]]
# const = None
# payable = False
def unknown8d6f4091(addr _param1): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknown8d6f4091[stor10[addr(_param1)]].field_256, 
         unknown8d6f4091[stor10[addr(_param1)]].field_512,
         unknown8d6f4091[stor10[addr(_param1)]].field_768


# hash = 0x905f72e1
# getter = None
# const = None
# payable = False
def unknown905f72e1(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require stor11[_param1]
  require stor7[_param2]
  require unknown8d6f4091[stor11[_param1]][4][_param2].field_0
  require _param3 >= 1
  require _param3 <= 100000
  if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
      revert with 0, 'SafeMath add failed'
  require unknown8d6f4091[stor11[_param1]].field_512 + _param3 <= 100000
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['addShares'][this.address].field_256:
      stor0['addShares'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['addShares'][this.address][2][caller].field_0 = 1
      stor0['addShares'][this.address][3][stor0['addShares'][this.address].field_256].field_0 = caller
      stor0['addShares'][this.address].field_256++
      if ext_call.return_data[0] == stor0['addShares'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['addShares'][this.address].field_256:
              stor0['addShares'][this.address][2][stor0['addShares'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['addShares'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('addShares', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['addShares'][this.address][3][[94midx].field_0
              continue 
          stor0['addShares'][this.address].field_0 = 0
          stor0['addShares'][this.address].field_256 = 0
          if unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 + _param3 < _param3:
              revert with 0, 'SafeMath add failed'
          unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 += _param3
          if unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 + _param3 < _param3:
              revert with 0, 'SafeMath add failed'
          unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 += _param3
          if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
              revert with 0, 'SafeMath add failed'
          unknown8d6f4091[stor11[_param1]].field_512 += _param3
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['addShares'][this.address].field_0:
          if not stor0['addShares'][this.address][2][caller].field_0:
              stor0['addShares'][this.address][2][caller].field_0 = 1
              stor0['addShares'][this.address][3][stor0['addShares'][this.address].field_256].field_0 = caller
              stor0['addShares'][this.address].field_256++
          if ext_call.return_data[0] == stor0['addShares'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['addShares'][this.address].field_256:
                  stor0['addShares'][this.address][2][stor0['addShares'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['addShares'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('addShares', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['addShares'][this.address][3][[94midx].field_0
                  continue 
              stor0['addShares'][this.address].field_0 = 0
              stor0['addShares'][this.address].field_256 = 0
              if unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 + _param3 < _param3:
                  revert with 0, 'SafeMath add failed'
              unknowna970d378[stor7[_param2]][6][unknowna970d378[stor7[_param2]][5][_param1].field_0].field_256 += _param3
              if unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 + _param3 < _param3:
                  revert with 0, 'SafeMath add failed'
              unknown8d6f4091[stor11[_param1]][5][unknown8d6f4091[stor11[_param1]][4][_param2].field_0].field_256 += _param3
              if unknown8d6f4091[stor11[_param1]].field_512 + _param3 < _param3:
                  revert with 0, 'SafeMath add failed'
              unknown8d6f4091[stor11[_param1]].field_512 += _param3
  log 0x6b830882 


# hash = 0x926d48f0
# getter = None
# const = None
# payable = False
def unknown926d48f0(addr _param1, uint256 _param2): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknowna970d378[stor12[stor10[addr(_param1)]][5][_param2].field_0].field_512, 
         unknown8d6f4091[stor10[addr(_param1)]][5][_param2].field_256


# hash = 0x99128677
# getter = None
# const = None
# payable = False
def unknown99128677(): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return stor9, stor13


# hash = 0x9a13f799
# getter = None
# const = None
# payable = False
def unknown9a13f799(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  if stor9 + 1 < stor9:
      revert with 0, 'SafeMath add failed'
  stor9++
  stor6[addr(_param1)] = stor9 + 1
  stor7[_param3] = stor9 + 1
  unknowna970d378[stor9 + 1].field_0 = _param1
  unknowna970d378[stor9].field_256 = _param2
  unknowna970d378[stor9].field_512 = _param3
  unknowna970d378[stor9].field_768 = _param4
  unknowna970d378[stor9].field_1024 = _param5
  return 1


# hash = 0x9bf04bae
# getter = None
# const = None
# payable = False
def unknown9bf04bae(array _param1, array _param2): # not payable
  mem[96] = _param1.length
  mem[128 len _param1.length] = _param1[all]
  mem[64] = ceil32(_param1.length) + ceil32(_param2.length) + 160
  mem[ceil32(_param1.length) + 128] = _param2.length
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  if stor1.length.field_160:
      revert with 0, 'cannot execute while in migratin'
  mem[0] = caller
  mem[32] = 6
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  if _param1.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _param1.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _param1.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _param1.length - 1 < _param1.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param1.length + -ceil32(_param1.length) + 31) + 248, mem[_param1.length + 127 len ceil32(_param1.length) + -_param1.length + 1]) << 8 * _param1.length + -ceil32(_param1.length) + 31:
      revert with 0, 'string cannot start or end with space'
  require 0 < _param1.length
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      require 1 < _param1.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _param1.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require [94midx < _param1.length
      require [94midx < _param1.length
      if Mask(8, 248, mem[[94midx + 128]) <= '@':
          if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < _param1.length
              if Mask(8, 248, mem[[94midx + 128]) <= '`':
                  if Mask(8, 248, mem[[94midx + 128]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < _param1.length
                  if Mask(8, 248, mem[[94midx + 128]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[[94midx + 128]) >= '{':
                      require [94midx < _param1.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param1.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
              require [94midx + 1 < _param1.length
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < _param1.length
          if Mask(8, 248, mem[[94midx + 128]) >= '0':
              require [94midx < _param1.length
              if Mask(8, 248, mem[[94midx + 128]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < _param1.length
          if Mask(8, 248, mem[[94midx + 128]) < '[':
              mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param1.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param1.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _param1.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param1.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _param1.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param1.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _param1.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if mem[ceil32(_param1.length) + 128] > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if mem[ceil32(_param1.length) + 128] <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < mem[ceil32(_param1.length) + 128]
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + 160]):
      revert with 0, 'string cannot start or end with space'
  require mem[ceil32(_param1.length) + 128] - 1 < mem[ceil32(_param1.length) + 128]
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + mem[ceil32(_param1.length) + 128] + 159]):
      revert with 0, 'string cannot start or end with space'
  require 0 < mem[ceil32(_param1.length) + 128]
  if 0x3000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + 160]):
      require 1 < mem[ceil32(_param1.length) + 128]
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + 161]):
          revert with 0, 'string cannot start with 0x'
      require 1 < mem[ceil32(_param1.length) + 128]
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + 161]):
          revert with 0, 'string cannot start with 0X'
  [94midx = 0
  [94ms = 0
  while [94midx < mem[ceil32(_param1.length) + 128]:
      require [94midx < mem[ceil32(_param1.length) + 128]
      require [94midx < mem[ceil32(_param1.length) + 128]
      require [94midx < mem[ceil32(_param1.length) + 128]
      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '@':
          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
              require [94midx < mem[ceil32(_param1.length) + 128]
              if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '`':
                  if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '/':
                      revert with 0, 'string contains invalid characters'
                  require [94midx < mem[ceil32(_param1.length) + 128]
                  if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= ':':
                      revert with 0, 'string contains invalid characters'
              else:
                  if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= '{':
                      require [94midx < mem[ceil32(_param1.length) + 128]
                      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < mem[ceil32(_param1.length) + 128]
                      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= ':':
                          revert with 0, 'string contains invalid characters'
          if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]):
              require [94midx + 1 < mem[ceil32(_param1.length) + 128]
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 161]):
                  revert with 0, 'string cannot contain consecutive spaces'
          if [94ms:
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < mem[ceil32(_param1.length) + 128]
          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= '0':
              require [94midx < mem[ceil32(_param1.length) + 128]
              if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '9':
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
      else:
          require [94midx < mem[ceil32(_param1.length) + 128]
          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) < '[':
              mem[ceil32(_param1.length) + [94midx + 160 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 1)))), 0) - 256
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < mem[ceil32(_param1.length) + 128]
                  if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '`':
                      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < mem[ceil32(_param1.length) + 128]
                      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= '{':
                          require [94midx < mem[ceil32(_param1.length) + 128]
                          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < mem[ceil32(_param1.length) + 128]
                          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]):
                  require [94midx + 1 < mem[ceil32(_param1.length) + 128]
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 161]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < mem[ceil32(_param1.length) + 128]
              if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= '0':
                  require [94midx < mem[ceil32(_param1.length) + 128]
                  if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if bool([94ms) != 1:
      revert with 0, 'string cannot be only numbers'
  if mem[ceil32(_param1.length) + 160] != unknowna970d378[stor6[caller]].field_512:
      require not stor7[mem[ceil32(_param1.length) + 160]]
      stor7[stor8[stor6[caller]].field_512] = 0
      stor7[mem[ceil32(_param1.length) + 160]] = stor6[caller]
  unknowna970d378[stor6[caller]].field_256 = mem[128]
  unknowna970d378[stor6[caller]].field_512 = mem[ceil32(_param1.length) + 160]
  log 0x8f9b506c 


# hash = 0xa31828b4
# getter = None
# const = None
# payable = False
def unknowna31828b4(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  unknowna970d378[_param1][6][_param2].field_0 = _param3
  unknowna970d378[_param1][6][_param2].field_256 = _param5
  unknowna970d378[_param1][5][_param4].field_0 = _param2
  return 1


# hash = 0xa553506e
# getter = None
# const = None
# payable = False
def checkData(bytes32 _whatFunction): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  return stor0[_whatFunction][this.address].field_0, stor0[_whatFunction][this.address].field_256


# hash = 0xa970d378
# getter = ['struct', ['loc', 8]]
# const = None
# payable = False
def unknowna970d378(addr _param1): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknowna970d378[stor6[addr(_param1)]].field_512, 
         unknowna970d378[stor6[addr(_param1)]].field_256,
         unknowna970d378[stor6[addr(_param1)]].field_1024,
         unknowna970d378[stor6[addr(_param1)]].field_768 / 10^18


# hash = 0xba3c623d
# getter = None
# const = None
# payable = False
def unknownba3c623d(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  if stor13 + 1 < stor13:
      revert with 0, 'SafeMath add failed'
  stor13++
  stor10[addr(_param1)] = stor13 + 1
  stor11[_param2] = stor13 + 1
  unknown8d6f4091[stor13 + 1].field_0 = _param1
  unknown8d6f4091[stor13].field_256 = _param2
  unknown8d6f4091[stor13].field_512 = _param3
  unknown8d6f4091[stor13].field_768 = _param4
  return 1


# hash = 0xd021bff5
# getter = None
# const = None
# payable = False
def unknownd021bff5(): # not payable
  require caller == 0xd3049b671c9818e0896f34ec4ad0bb58fe1248e5
  [93mselfdestruct([91mcaller[93m)


# hash = 0xd3fd1356
# getter = None
# const = None
# payable = True
def unknownd3fd1356(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4) payable: 
  if addr(stor1.length) != caller:
      revert with 0, 'Gmsg sender is not last bank'
  require ext_code.size(0xe752b7d837a6969a5986467b0109bdf052e45bdb)
  call 0xe752b7d837a6969a5986467b0109bdf052e45bdb.finishMigration() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 1 == bool(ext_call.return_data[0])
  Mask(168, 0, stor1.length) = 0
  stor14 = _param1
  if _param2 + stor15 < stor15:
      revert with 0, 'SafeMath add failed'
  stor15 += _param2
  if _param3 + stor16 < stor16:
      revert with 0, 'SafeMath add failed'
  stor16 += _param3
  stor18 += 100000 * _param4
  return 1


# hash = 0xd923385e
# getter = None
# const = None
# payable = False
def unknownd923385e(addr _param1, uint256 _param2): # not payable
  if not stor6[caller]:
      revert with 0, 'msg sender is not a member'
  return unknown8d6f4091[stor8[stor6[addr(_param1)]][6][_param2].field_0].field_256, 
         unknowna970d378[stor6[addr(_param1)]][6][_param2].field_256


# hash = 0xdb1c7b9b
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknowndb1c7b9b(): # not payable
  return unknowndb1c7b9b


# hash = 0xe184c878
# getter = None
# const = None
# payable = False
def unknowne184c878(uint256 _param1): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require bool(stor1.length.field_160) == 1
  require _param1 == stor5
  require stor3 == stor13
  require stor4 == stor9
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['migrate5_kill'][this.address].field_256:
      stor0['migrate5_kill'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['migrate5_kill'][this.address][2][caller].field_0 = 1
      stor0['migrate5_kill'][this.address][3][stor0['migrate5_kill'][this.address].field_256].field_0 = caller
      stor0['migrate5_kill'][this.address].field_256++
      if ext_call.return_data[0] != stor0['migrate5_kill'][this.address].field_256 + 1:
          log 0x1bcb34ca: 0
          stop
  else:
      if sha3(call.data[0 len calldata.size]) != stor0['migrate5_kill'][this.address].field_0:
          log 0x1bcb34ca: 0
          stop
      if not stor0['migrate5_kill'][this.address][2][caller].field_0:
          stor0['migrate5_kill'][this.address][2][caller].field_0 = 1
          stor0['migrate5_kill'][this.address][3][stor0['migrate5_kill'][this.address].field_256].field_0 = caller
          stor0['migrate5_kill'][this.address].field_256++
      if ext_call.return_data[0] != stor0['migrate5_kill'][this.address].field_256:
          log 0x1bcb34ca: 0
          stop
  [94midx = 0
  [94ms = 0
  while [94midx < stor0['migrate5_kill'][this.address].field_256:
      stor0['migrate5_kill'][this.address][2][stor0['migrate5_kill'][this.address][3][[94midx].field_0].field_0 = 0
      stor0['migrate5_kill'][this.address][3][[94midx].field_0 = 0
      mem[0] = sha3('migrate5_kill', this.address)
      mem[32] = 0
      [94midx = [94midx + 1
      [94ms = stor0['migrate5_kill'][this.address][3][[94midx].field_0
      continue 
  stor0['migrate5_kill'][this.address].field_0 = 0
  stor0['migrate5_kill'][this.address].field_256 = 0
  [94midx = 1
  while [94midx <= stor18 - (100000 * stor18 / 100000):
      mem[0] = [94midx
      mem[32] = 19
      mem[268] = stor19[[94midx].field_0
      mem[300] = stor19[[94midx].field_256
      require ext_code.size(stor2)
      call stor2.0x6f8d4b3a with:
           gas gas_remaining wei
          args stor19[[94midx].field_0, stor19[[94midx].field_256
      mem[264] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if bool(ext_call.return_data[0]) != 1:
          [94midx = [94midx
          continue 
      [94midx = [94midx + 1
      continue 
  require ext_code.size(stor2)
  call stor2.0xd3fd1356 with:
     value eth.balance(this.address) wei
       gas gas_remaining wei
      args stor14, stor15, stor16, (100000 * stor18 / 100000) - (100 * 10^18 * stor18 / 100 * 10^18) / 100000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      log 0x1bcb34ca: 0
      stop
  log 0x1bcb34ca: 1
  [93mselfdestruct([91mcaller[93m)


# hash = 0xe9e574e6
# getter = None
# const = None
# payable = False
def unknowne9e574e6(uint256 _param1): # not payable
  if stor1.length.field_160:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'cannot execute while in migratin'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  require _param1 >= 0
  require _param1 <= 25
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not stor0['setCompanyReserve'][this.address].field_256:
      stor0['setCompanyReserve'][this.address].field_0 = sha3(call.data[0 len calldata.size])
      stor0['setCompanyReserve'][this.address][2][caller].field_0 = 1
      stor0['setCompanyReserve'][this.address][3][stor0['setCompanyReserve'][this.address].field_256].field_0 = caller
      stor0['setCompanyReserve'][this.address].field_256++
      if ext_call.return_data[0] == stor0['setCompanyReserve'][this.address].field_256 + 1:
          [94midx = 0
          [94ms = 0
          while [94midx < stor0['setCompanyReserve'][this.address].field_256:
              stor0['setCompanyReserve'][this.address][2][stor0['setCompanyReserve'][this.address][3][[94midx].field_0].field_0 = 0
              stor0['setCompanyReserve'][this.address][3][[94midx].field_0 = 0
              mem[0] = sha3('setCompanyReserve', this.address)
              mem[32] = 0
              [94midx = [94midx + 1
              [94ms = stor0['setCompanyReserve'][this.address][3][[94midx].field_0
              continue 
          stor0['setCompanyReserve'][this.address].field_0 = 0
          stor0['setCompanyReserve'][this.address].field_256 = 0
          stor14 = _param1
  else:
      if sha3(call.data[0 len calldata.size]) == stor0['setCompanyReserve'][this.address].field_0:
          if not stor0['setCompanyReserve'][this.address][2][caller].field_0:
              stor0['setCompanyReserve'][this.address][2][caller].field_0 = 1
              stor0['setCompanyReserve'][this.address][3][stor0['setCompanyReserve'][this.address].field_256].field_0 = caller
              stor0['setCompanyReserve'][this.address].field_256++
          if ext_call.return_data[0] == stor0['setCompanyReserve'][this.address].field_256:
              [94midx = 0
              [94ms = 0
              while [94midx < stor0['setCompanyReserve'][this.address].field_256:
                  stor0['setCompanyReserve'][this.address][2][stor0['setCompanyReserve'][this.address][3][[94midx].field_0].field_0 = 0
                  stor0['setCompanyReserve'][this.address][3][[94midx].field_0 = 0
                  mem[0] = sha3('setCompanyReserve', this.address)
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0['setCompanyReserve'][this.address][3][[94midx].field_0
                  continue 
              stor0['setCompanyReserve'][this.address].field_0 = 0
              stor0['setCompanyReserve'][this.address].field_256 = 0
              stor14 = _param1
  log 0x7cea3ecf: stor14


# hash = 0xed3643d6
# getter = None
# const = None
# payable = False
def checkSignersByName(bytes32 _whatFunction, uint256 _signerA, uint256 _signerB, uint256 _signerC): # not payable
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  if _signerA <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'MSFun checkSigner failed - 0 not allowed'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.adminName(address who) with:
       gas gas_remaining wei
      args stor0[_whatFunction][this.address][3][_signerA - 1].field_0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _signerB <= 0:
      revert with 0, 'MSFun checkSigner failed - 0 not allowed'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.adminName(address who) with:
       gas gas_remaining wei
      args stor0[_whatFunction][this.address][3][_signerB - 1].field_0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _signerC <= 0:
      revert with 0, 'MSFun checkSigner failed - 0 not allowed'
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.adminName(address who) with:
       gas gas_remaining wei
      args stor0[_whatFunction][this.address][3][_signerC - 1].field_0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0], ext_call.return_data[0], ext_call.return_data[0]


# hash = 0xf340fa01
# getter = None
# const = None
# payable = True
def deposit(address _payee) payable: 
  if 0xd3049b671c9818e0896f34ec4ad0bb58fe1248e5 != tx.origin:
      call 0xe752b7d837a6969a5986467b0109bdf052e45bdb with:
         funct Mask(32, 224, sha3('deposit()')) >> 224
         value call.value wei
           gas gas_remaining wei
  require 0xe752b7d837a6969a5986467b0109bdf052e45bdb == caller
  require stor10[addr(_payee)]
  require (100000 * stor18 / 100000) - (100 * 10^18 * stor18 / 100 * 10^18) / 100000 < 10^15
  if stor20[addr(_payee)]:
      stor19[stor20[addr(_payee)]].field_256 += call.value
      stor18 = (100 * 10^18 * call.value) + stor18 + 100000
      log 0x3d5ef7f1: (100000 * (100 * 10^18 * call.value) + stor18 + 100000 / 100000) - (100 * 10^18 * (100 * 10^18 * call.value) + stor18 + 100000 / 100 * 10^18) / 100000, (100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18, stor18 - (100000 * stor18 / 100000)
  else:
      stor20[addr(_payee)] = stor18 + (-100000 * stor18 / 100000) + 1
      stor19[stor18 + (-100000 * stor18 / 100000) + 1].field_0 = _payee
      stor19[stor18 + (-100000 * stor18 / 100000) + 1].field_256 += call.value
      stor18 = (100 * 10^18 * call.value) + stor18 + 100001
      log 0x3d5ef7f1: (100000 * (100 * 10^18 * call.value) + stor18 + 100001 / 100000) - (100 * 10^18 * (100 * 10^18 * call.value) + stor18 + 100001 / 100 * 10^18) / 100000, (100 * 10^18 * stor18 / 100 * 10^18) - (0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000 * stor18 / 0x97edd871cfda3a5697758bf0e3cbb5ac5741c640000000000000000) / 100 * 10^18, stor18 - (100000 * stor18 / 100000)
  return 1


# hash = 0xf745963d
# getter = None
# const = None
# payable = False
def unknownf745963d(addr _param1, array _param2): # not payable
  mem[64] = ceil32(_param2.length) + 128
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  if stor1.length.field_160:
      revert with 0, 'cannot execute while in migratin'
  mem[ceil32(_param2.length) + 132] = caller
  require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
  call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.isDev(address who) with:
       gas gas_remaining wei
      args caller
  mem[ceil32(_param2.length) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      revert with 0, 'omsg sender is not a dev'
  mem[0] = _param1
  mem[32] = 10
  require not stor10[addr(_param1)]
  if _param2.length > 32:
      revert with 0, 'string must be between 1 and 32 characters'
  if _param2.length <= 0:
      revert with 0, 'string must be between 1 and 32 characters'
  require 0 < _param2.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[128]):
      revert with 0, 'string cannot start or end with space'
  require _param2.length - 1 < _param2.length
  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, -(8 * _param2.length + -ceil32(_param2.length) + 31) + 248, mem[_param2.length + 127 len ceil32(_param2.length) + -_param2.length + 1]) << 8 * _param2.length + -ceil32(_param2.length) + 31:
      revert with 0, 'string cannot start or end with space'
  require 0 < _param2.length
  if Mask(8, 248, mem[128]) != 0x3000000000000000000000000000000000000000000000000000000000000000:
      [94midx = 0
      [94ms = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94midx < _param2.length
          require [94midx < _param2.length
          if Mask(8, 248, mem[[94midx + 128]) <= '@':
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _param2.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) < '[':
                  mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < _param2.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_756 = mem[128]
      mem[32] = 11
      require not stor11[mem[128]]
      require _param1
      mem[0] = mem[128]
      require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
      call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_822 = mem[64]
      mem[mem[64] + 32] = 'addDapp'
      mem[mem[64] + 64] = addr(this.address)
      [94m_823 = mem[64]
      mem[mem[64]] = 52
      mem[64] = mem[64] + 84
      [94m_824 = mem[[94m_823]
      mem[[94m_822 + 84 len floor32(mem[[94m_823])] = mem[[94m_823 + 32 len floor32(mem[[94m_823])]
      mem[[94m_822 + floor32(mem[[94m_823]) + 84] = mem[[94m_822 + floor32(mem[[94m_823]) + 84] and 256^(-(mem[[94m_823] % 32) + 32) - 1 or mem[[94m_823 + floor32(mem[[94m_823]) + 32] and !(256^(-(mem[[94m_823] % 32) + 32) - 1)
      [94m_1471 = sha3(mem[mem[64] len [94m_822 + [94m_824 + -mem[64] + 84])
      mem[0] = sha3(mem[mem[64] len [94m_822 + [94m_824 + -mem[64] + 84])
      mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
      if not stor0[mem[0]].field_256:
          stor0[[94m_1471].field_0 = sha3(call.data[0 len calldata.size])
          stor0[[94m_1471][2][caller].field_0 = 1
          stor0[[94m_1471][3][stor0[mem[0]].field_256].field_0 = caller
          mem[0] = [94m_1471
          mem[32] = 0
          stor0[[94m_1471].field_256++
          if ext_call.return_data[0] == stor0[[94m_1471].field_256 + 1:
              [94m_1543 = mem[64]
              mem[mem[64] + 32] = 'addDapp'
              mem[mem[64] + 64] = addr(this.address)
              [94m_1544 = mem[64]
              mem[mem[64]] = 52
              mem[64] = mem[64] + 84
              [94m_1545 = mem[[94m_1544]
              mem[[94m_1543 + 84 len floor32(mem[[94m_1544])] = mem[[94m_1544 + 32 len floor32(mem[[94m_1544])]
              mem[[94m_1543 + floor32(mem[[94m_1544]) + 84] = mem[[94m_1543 + floor32(mem[[94m_1544]) + 84] and 256^(-(mem[[94m_1544] % 32) + 32) - 1 or mem[[94m_1544 + floor32(mem[[94m_1544]) + 32] and !(256^(-(mem[[94m_1544] % 32) + 32) - 1)
              [94m_1863 = sha3(mem[mem[64] len [94m_1543 + [94m_1545 + -mem[64] + 84])
              mem[0] = sha3(mem[mem[64] len [94m_1543 + [94m_1545 + -mem[64] + 84])
              [94m_2088 = sha3(mem[0], 0)
              [94midx = 0
              [94ms = 0
              while [94midx < stor1[[94m_2088].field_0:
                  stor0[[94m_1863][2][stor0[[94m_1863][3][[94midx].field_0].field_0 = 0
                  stor0[[94m_1863][3][[94midx].field_0 = 0
                  mem[0] = [94m_1863
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0[[94m_1863][3][[94midx].field_0
                  continue 
              stor0[[94m_1863].field_0 = 0
              stor0[[94m_1863].field_256 = 0
              if stor13 + 1 < stor13:
                  revert with 0, 'SafeMath add failed'
              stor13++
              stor10[addr(_param1)] = stor13 + 1
              stor11[[94m_756] = stor13 + 1
              unknown8d6f4091[stor13 + 1].field_0 = _param1
              unknown8d6f4091[stor13].field_256 = [94m_756
      else:
          if sha3(call.data[0 len calldata.size]) == stor0[[94m_1471].field_0:
              if stor0[[94m_1471][2][caller].field_0:
                  mem[0] = [94m_1471
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1471].field_256:
                      [94m_1570 = mem[64]
                      mem[mem[64] + 32] = 'addDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1571 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1572 = mem[[94m_1571]
                      mem[[94m_1570 + 84 len floor32(mem[[94m_1571])] = mem[[94m_1571 + 32 len floor32(mem[[94m_1571])]
                      mem[[94m_1570 + floor32(mem[[94m_1571]) + 84] = mem[[94m_1570 + floor32(mem[[94m_1571]) + 84] and 256^(-(mem[[94m_1571] % 32) + 32) - 1 or mem[[94m_1571 + floor32(mem[[94m_1571]) + 32] and !(256^(-(mem[[94m_1571] % 32) + 32) - 1)
                      [94m_1843 = sha3(mem[mem[64] len [94m_1570 + [94m_1572 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1570 + [94m_1572 + -mem[64] + 84])
                      [94m_2084 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_2084].field_0:
                          stor0[[94m_1843][2][stor0[[94m_1843][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1843][3][[94midx].field_0 = 0
                          mem[0] = [94m_1843
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1843][3][[94midx].field_0
                          continue 
                      stor0[[94m_1843].field_0 = 0
                      stor0[[94m_1843].field_256 = 0
                      if stor13 + 1 < stor13:
                          revert with 0, 'SafeMath add failed'
                      stor13++
                      stor10[addr(_param1)] = stor13 + 1
                      stor11[[94m_756] = stor13 + 1
                      unknown8d6f4091[stor13 + 1].field_0 = _param1
                      unknown8d6f4091[stor13].field_256 = [94m_756
              else:
                  stor0[[94m_1471][2][caller].field_0 = 1
                  stor0[[94m_1471][3][stor0[mem[0]].field_256].field_0 = caller
                  stor0[[94m_1471].field_256++
                  mem[0] = [94m_1471
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1471].field_256:
                      [94m_1608 = mem[64]
                      mem[mem[64] + 32] = 'addDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1609 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1610 = mem[[94m_1609]
                      mem[[94m_1608 + 84 len floor32(mem[[94m_1609])] = mem[[94m_1609 + 32 len floor32(mem[[94m_1609])]
                      mem[[94m_1608 + floor32(mem[[94m_1609]) + 84] = mem[[94m_1608 + floor32(mem[[94m_1609]) + 84] and 256^(-(mem[[94m_1609] % 32) + 32) - 1 or mem[[94m_1609 + floor32(mem[[94m_1609]) + 32] and !(256^(-(mem[[94m_1609] % 32) + 32) - 1)
                      [94m_1853 = sha3(mem[mem[64] len [94m_1608 + [94m_1610 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1608 + [94m_1610 + -mem[64] + 84])
                      [94m_2086 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_2086].field_0:
                          stor0[[94m_1853][2][stor0[[94m_1853][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1853][3][[94midx].field_0 = 0
                          mem[0] = [94m_1853
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1853][3][[94midx].field_0
                          continue 
                      stor0[[94m_1853].field_0 = 0
                      stor0[[94m_1853].field_256 = 0
                      if stor13 + 1 < stor13:
                          revert with 0, 'SafeMath add failed'
                      stor13++
                      stor10[addr(_param1)] = stor13 + 1
                      stor11[[94m_756] = stor13 + 1
                      unknown8d6f4091[stor13 + 1].field_0 = _param1
                      unknown8d6f4091[stor13].field_256 = [94m_756
  else:
      require 1 < _param2.length
      if 0x7800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0x'
      require 1 < _param2.length
      if 0x5800000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[129]):
          revert with 0, 'string cannot start with 0X'
      [94midx = 0
      [94ms = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94midx < _param2.length
          require [94midx < _param2.length
          if Mask(8, 248, mem[[94midx + 128]) <= '@':
              if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '`':
                      if Mask(8, 248, mem[[94midx + 128]) <= '/':
                          revert with 0, 'string contains invalid characters'
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) >= ':':
                          revert with 0, 'string contains invalid characters'
                  else:
                      if Mask(8, 248, mem[[94midx + 128]) >= '{':
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
              if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                  require [94midx + 1 < _param2.length
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                      revert with 0, 'string cannot contain consecutive spaces'
              if [94ms:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) >= '0':
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) <= '9':
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
          else:
              require [94midx < _param2.length
              if Mask(8, 248, mem[[94midx + 128]) < '[':
                  mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
              else:
                  if Mask(8, 248, mem[[94midx + 128]) != 0x2000000000000000000000000000000000000000000000000000000000000000:
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '`':
                          if Mask(8, 248, mem[[94midx + 128]) <= '/':
                              revert with 0, 'string contains invalid characters'
                          require [94midx < _param2.length
                          if Mask(8, 248, mem[[94midx + 128]) >= ':':
                              revert with 0, 'string contains invalid characters'
                      else:
                          if Mask(8, 248, mem[[94midx + 128]) >= '{':
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) <= '/':
                                  revert with 0, 'string contains invalid characters'
                              require [94midx < _param2.length
                              if Mask(8, 248, mem[[94midx + 128]) >= ':':
                                  revert with 0, 'string contains invalid characters'
                  if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 128]):
                      require [94midx + 1 < _param2.length
                      if 0x2000000000000000000000000000000000000000000000000000000000000000 == Mask(8, 248, mem[[94midx + 129]):
                          revert with 0, 'string cannot contain consecutive spaces'
                  if [94ms:
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      continue 
                  require [94midx < _param2.length
                  if Mask(8, 248, mem[[94midx + 128]) >= '0':
                      require [94midx < _param2.length
                      if Mask(8, 248, mem[[94midx + 128]) <= '9':
                          [94midx = [94midx + 1
                          [94ms = [94ms
                          continue 
          [94midx = [94midx + 1
          [94ms = 1
          continue 
      if bool([94ms) != 1:
          revert with 0, 'string cannot be only numbers'
      [94m_760 = mem[128]
      mem[32] = 11
      require not stor11[mem[128]]
      require _param1
      mem[0] = mem[128]
      require ext_code.size(0xeba1dd62472853aca00d43f53cce9e95e5a054)
      call 0x00eba1dd62472853aca00d43f53cce9e95e5a054.requiredDevSignatures() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_832 = mem[64]
      mem[mem[64] + 32] = 'addDapp'
      mem[mem[64] + 64] = addr(this.address)
      [94m_833 = mem[64]
      mem[mem[64]] = 52
      mem[64] = mem[64] + 84
      [94m_834 = mem[[94m_833]
      mem[[94m_832 + 84 len floor32(mem[[94m_833])] = mem[[94m_833 + 32 len floor32(mem[[94m_833])]
      mem[[94m_832 + floor32(mem[[94m_833]) + 84] = mem[[94m_832 + floor32(mem[[94m_833]) + 84] and 256^(-(mem[[94m_833] % 32) + 32) - 1 or mem[[94m_833 + floor32(mem[[94m_833]) + 32] and !(256^(-(mem[[94m_833] % 32) + 32) - 1)
      [94m_1476 = sha3(mem[mem[64] len [94m_832 + [94m_834 + -mem[64] + 84])
      mem[0] = sha3(mem[mem[64] len [94m_832 + [94m_834 + -mem[64] + 84])
      mem[mem[64] len calldata.size] = call.data[0 len calldata.size]
      if not stor0[mem[0]].field_256:
          stor0[[94m_1476].field_0 = sha3(call.data[0 len calldata.size])
          stor0[[94m_1476][2][caller].field_0 = 1
          stor0[[94m_1476][3][stor0[mem[0]].field_256].field_0 = caller
          mem[0] = [94m_1476
          mem[32] = 0
          stor0[[94m_1476].field_256++
          if ext_call.return_data[0] == stor0[[94m_1476].field_256 + 1:
              [94m_1551 = mem[64]
              mem[mem[64] + 32] = 'addDapp'
              mem[mem[64] + 64] = addr(this.address)
              [94m_1552 = mem[64]
              mem[mem[64]] = 52
              mem[64] = mem[64] + 84
              [94m_1553 = mem[[94m_1552]
              mem[[94m_1551 + 84 len floor32(mem[[94m_1552])] = mem[[94m_1552 + 32 len floor32(mem[[94m_1552])]
              mem[[94m_1551 + floor32(mem[[94m_1552]) + 84] = mem[[94m_1551 + floor32(mem[[94m_1552]) + 84] and 256^(-(mem[[94m_1552] % 32) + 32) - 1 or mem[[94m_1552 + floor32(mem[[94m_1552]) + 32] and !(256^(-(mem[[94m_1552] % 32) + 32) - 1)
              [94m_1898 = sha3(mem[mem[64] len [94m_1551 + [94m_1553 + -mem[64] + 84])
              mem[0] = sha3(mem[mem[64] len [94m_1551 + [94m_1553 + -mem[64] + 84])
              [94m_2095 = sha3(mem[0], 0)
              [94midx = 0
              [94ms = 0
              while [94midx < stor1[[94m_2095].field_0:
                  stor0[[94m_1898][2][stor0[[94m_1898][3][[94midx].field_0].field_0 = 0
                  stor0[[94m_1898][3][[94midx].field_0 = 0
                  mem[0] = [94m_1898
                  mem[32] = 0
                  [94midx = [94midx + 1
                  [94ms = stor0[[94m_1898][3][[94midx].field_0
                  continue 
              stor0[[94m_1898].field_0 = 0
              stor0[[94m_1898].field_256 = 0
              if stor13 + 1 < stor13:
                  revert with 0, 'SafeMath add failed'
              stor13++
              stor10[addr(_param1)] = stor13 + 1
              stor11[[94m_760] = stor13 + 1
              unknown8d6f4091[stor13 + 1].field_0 = _param1
              unknown8d6f4091[stor13].field_256 = [94m_760
      else:
          if sha3(call.data[0 len calldata.size]) == stor0[[94m_1476].field_0:
              if stor0[[94m_1476][2][caller].field_0:
                  mem[0] = [94m_1476
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1476].field_256:
                      [94m_1586 = mem[64]
                      mem[mem[64] + 32] = 'addDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1587 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1588 = mem[[94m_1587]
                      mem[[94m_1586 + 84 len floor32(mem[[94m_1587])] = mem[[94m_1587 + 32 len floor32(mem[[94m_1587])]
                      mem[[94m_1586 + floor32(mem[[94m_1587]) + 84] = mem[[94m_1586 + floor32(mem[[94m_1587]) + 84] and 256^(-(mem[[94m_1587] % 32) + 32) - 1 or mem[[94m_1587 + floor32(mem[[94m_1587]) + 32] and !(256^(-(mem[[94m_1587] % 32) + 32) - 1)
                      [94m_1878 = sha3(mem[mem[64] len [94m_1586 + [94m_1588 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1586 + [94m_1588 + -mem[64] + 84])
                      [94m_2091 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_2091].field_0:
                          stor0[[94m_1878][2][stor0[[94m_1878][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1878][3][[94midx].field_0 = 0
                          mem[0] = [94m_1878
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1878][3][[94midx].field_0
                          continue 
                      stor0[[94m_1878].field_0 = 0
                      stor0[[94m_1878].field_256 = 0
                      if stor13 + 1 < stor13:
                          revert with 0, 'SafeMath add failed'
                      stor13++
                      stor10[addr(_param1)] = stor13 + 1
                      stor11[[94m_760] = stor13 + 1
                      unknown8d6f4091[stor13 + 1].field_0 = _param1
                      unknown8d6f4091[stor13].field_256 = [94m_760
              else:
                  stor0[[94m_1476][2][caller].field_0 = 1
                  stor0[[94m_1476][3][stor0[mem[0]].field_256].field_0 = caller
                  stor0[[94m_1476].field_256++
                  mem[0] = [94m_1476
                  mem[32] = 0
                  if ext_call.return_data[0] == stor0[[94m_1476].field_256:
                      [94m_1617 = mem[64]
                      mem[mem[64] + 32] = 'addDapp'
                      mem[mem[64] + 64] = addr(this.address)
                      [94m_1618 = mem[64]
                      mem[mem[64]] = 52
                      mem[64] = mem[64] + 84
                      [94m_1619 = mem[[94m_1618]
                      mem[[94m_1617 + 84 len floor32(mem[[94m_1618])] = mem[[94m_1618 + 32 len floor32(mem[[94m_1618])]
                      mem[[94m_1617 + floor32(mem[[94m_1618]) + 84] = mem[[94m_1617 + floor32(mem[[94m_1618]) + 84] and 256^(-(mem[[94m_1618] % 32) + 32) - 1 or mem[[94m_1618 + floor32(mem[[94m_1618]) + 32] and !(256^(-(mem[[94m_1618] % 32) + 32) - 1)
                      [94m_1888 = sha3(mem[mem[64] len [94m_1617 + [94m_1619 + -mem[64] + 84])
                      mem[0] = sha3(mem[mem[64] len [94m_1617 + [94m_1619 + -mem[64] + 84])
                      [94m_2093 = sha3(mem[0], 0)
                      [94midx = 0
                      [94ms = 0
                      while [94midx < stor1[[94m_2093].field_0:
                          stor0[[94m_1888][2][stor0[[94m_1888][3][[94midx].field_0].field_0 = 0
                          stor0[[94m_1888][3][[94midx].field_0 = 0
                          mem[0] = [94m_1888
                          mem[32] = 0
                          [94midx = [94midx + 1
                          [94ms = stor0[[94m_1888][3][[94midx].field_0
                          continue 
                      stor0[[94m_1888].field_0 = 0
                      stor0[[94m_1888].field_256 = 0
                      if stor13 + 1 < stor13:
                          revert with 0, 'SafeMath add failed'
                      stor13++
                      stor10[addr(_param1)] = stor13 + 1
                      stor11[[94m_760] = stor13 + 1
                      unknown8d6f4091[stor13 + 1].field_0 = _param1
                      unknown8d6f4091[stor13].field_256 = [94m_760
  log 0x8fefea4c: stor13


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  revert


