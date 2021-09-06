# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xd8002e06Ca22eF22Ac648b9cC16C6363f17A5ae8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    adminAddress # mask: a s
    # storage address 1
    pendingAdminAddress # mask: a s
    # storage address 2
    unknownbb82aa5eAddress # mask: a s
    # storage address 3
    unknowndcfbc0c7Address # mask: a s
    # storage address 4
    oracleAddress # mask: a s
    # storage address 5
    unknowne8755446 # mask: a s
    # storage address 6
    unknown4ada90af # mask: a s
    # storage address 7
    unknown94b2294b # mask: a s
    # storage address 8
    unknowndce15449
    # storage address 9
    markets
# hash = 0x007e3dd2
# getter = None
# const = ['return', 1]
# payable = True
const unknown007e3dd2 = 1


# hash = 0x1ededc91
# getter = None
# const = None
# payable = True
def unknown1ededc91() payable: 
  require calldata.size - 4 >= 160


# hash = 0x24008a62
# getter = None
# const = None
# payable = True
def unknown24008a62(addr _param1) payable: 
  require calldata.size - 4 >= 128
  if uint8(markets[addr(_param1)].field_0):
      return 0
  return 9


# hash = 0x26782247
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def pendingAdmin() payable: 
  return pendingAdminAddress


# hash = 0x317b0b77
# getter = None
# const = None
# payable = True
def unknown317b0b77(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if unknownbb82aa5eAddress != caller:
      if adminAddress != caller:
          if unknownbb82aa5eAddress != caller:
              log Failure(
                    uint256 error=1,
                    uint256 info=4,
                    uint256 detail=0)
              return 1
  else:
      if adminAddress != caller:
          if adminAddress != tx.origin:
              log Failure(
                    uint256 error=1,
                    uint256 info=4,
                    uint256 detail=0)
              return 1
  if _param1 <= 5 * 10^16:
      log Failure(
            uint256 error=5,
            uint256 info=5,
            uint256 detail=0)
      return 5
  if 25 * 10^13 * 3600 < _param1:
      log Failure(
            uint256 error=5,
            uint256 info=5,
            uint256 detail=0)
      return 5
  unknowne8755446 = _param1
  log 0x3b9670cf: unknowne8755446, _param1
  return 0


# hash = 0x32000e00
# getter = None
# const = None
# payable = True
def unknown32000e00(addr _param1, addr _param2, uint256 _param3, uint256 _param4, bool _param5) payable: 
  require calldata.size - 4 >= 160
  require ext_code.size(_param1)
  static call _param1.admin() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0x646f6e6c7920756e6974726f6c6c65722061646d696e2063616e206368616e676520627261696e,
                  mem[203 len 25]
  require ext_code.size(_param1)
  call _param1.0xc1e80334 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      revert with 0, 'change not authorized'
  if not _param5:
      require ext_code.size(_param1)
      call _param1.0x55ee1fe1 with:
           gas gas_remaining wei
          args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          revert with 0, 'set price oracle error'
      require ext_code.size(_param1)
      call _param1.0x317b0b77 with:
           gas gas_remaining wei
          args _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          revert with 0, 'set close factor error'
      require ext_code.size(_param1)
      call _param1.0xd9226ced with:
           gas gas_remaining wei
          args _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          revert with 0, 'set max asssets error'
      require ext_code.size(_param1)
      call _param1.0x4fd42e17 with:
           gas gas_remaining wei
          args 10^18
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          revert with 0, 'set liquidation incentive error'


# hash = 0x41c728b9
# getter = None
# const = None
# payable = True
def unknown41c728b9() payable: 
  require calldata.size - 4 >= 128


# hash = 0x47ef3b3b
# getter = None
# const = None
# payable = True
def unknown47ef3b3b() payable: 
  require calldata.size - 4 >= 192


# hash = 0x4ada90af
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def unknown4ada90af() payable: 
  return unknown4ada90af


# hash = 0x4ef4c3e1
# getter = None
# const = None
# payable = True
def unknown4ef4c3e1(addr _param1) payable: 
  require calldata.size - 4 >= 96
  if uint8(markets[addr(_param1)].field_0):
      return 0
  return 9


# hash = 0x4fd42e17
# getter = None
# const = None
# payable = True
def unknown4fd42e17(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if unknownbb82aa5eAddress != caller:
      if adminAddress != caller:
          if unknownbb82aa5eAddress != caller:
              log Failure(
                    uint256 error=1,
                    uint256 info=11,
                    uint256 detail=0)
              return 1
  else:
      if adminAddress != caller:
          if adminAddress != tx.origin:
              log Failure(
                    uint256 error=1,
                    uint256 info=11,
                    uint256 detail=0)
              return 1
  if _param1 < 10^18:
      log Failure(
            uint256 error=7,
            uint256 info=12,
            uint256 detail=0)
      return 7
  if 15 * 10^17 < _param1:
      log Failure(
            uint256 error=7,
            uint256 info=12,
            uint256 detail=0)
      return 7
  unknown4ada90af = _param1
  log 0xaeba5a6c: unknown4ada90af, _param1
  return 0


# hash = 0x501ec9b4
# getter = None
# const = None
# payable = True
def unknown501ec9b4(addr _param1, bool _param2) payable: 
  require calldata.size - 4 >= 64
  if adminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=6,
            uint256 detail=0)
      return 1
  if not uint8(markets[addr(_param1)].field_0):
      log Failure(
            uint256 error=9,
            uint256 info=7,
            uint256 detail=0)
      return 9
  if _param2 != bool(uint8(markets[addr(_param1)].field_8)):
      Mask(248, 0, markets[addr(_param1)].field_8) = Mask(248, 0, _param2)
      log 0xd7ae9572: addr(_param1), _param2
      return 0
  else:
      return 0


# hash = 0x51dff989
# getter = None
# const = None
# payable = True
def unknown51dff989(uint256 _param1, bool _param2) payable: 
  require calldata.size - 4 >= 128
  if not _param2:
      if _param1 > 0:
          revert with 0, 'redeemTokens zero'


# hash = 0x55ee1fe1
# getter = None
# const = None
# payable = True
def unknown55ee1fe1(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if unknownbb82aa5eAddress != caller:
      if adminAddress != caller:
          if unknownbb82aa5eAddress != caller:
              log Failure(
                    uint256 error=1,
                    uint256 info=16,
                    uint256 detail=0)
              return 1
  else:
      if adminAddress != caller:
          if adminAddress != tx.origin:
              log Failure(
                    uint256 error=1,
                    uint256 info=16,
                    uint256 detail=0)
              return 1
  oracleAddress = _param1
  log 0xd52b2b9b: oracleAddress, _param1
  return 0


# hash = 0x5c778605
# getter = None
# const = None
# payable = True
def unknown5c778605() payable: 
  require calldata.size - 4 >= 96


# hash = 0x5ec88c79
# getter = None
# const = None
# payable = True
def getAccountLiquidity(address _account) payable: 
  require calldata.size - 4 >= 32
  mem[96] = 0
  mem[128] = 0
  mem[64] = (32 * unknowndce15449[addr(_account)].field_0) + 576
  mem[544] = unknowndce15449[addr(_account)].field_0
  if not unknowndce15449[addr(_account)].field_0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_account)].field_0:
          require [94midx < mem[544]
          [94m_1060 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_account)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if not ext_call.return_data[0]:
                  [94m_1072 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[0] = addr([94m_1060)
                  mem[32] = 9
                  mem[[94m_1072] = markets[addr([94m_1060)].field_256
                  mem[288] = [94m_1072
                  [94m_1074 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1074] = ext_call.return_data[96]
                  mem[320] = [94m_1074
                  mem[mem[64] + 4] = addr([94m_1060)
                  require ext_code.size(oracleAddress)
                  static call oracleAddress.0xfc57d4df with:
                          gas gas_remaining wei
                         args addr([94m_1060)
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      mem[256] = ext_call.return_data[0]
                      if ext_call.return_data[0]:
                          [94m_1080 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1080] = ext_call.return_data[0]
                          mem[352] = [94m_1080
                          [94m_1086 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1086] = 0
                          [94m_1087 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1087] = 0
                          [94m_1090 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1090] = 0
                          if markets[addr([94m_1060)].field_256:
                              if ext_call.return_data[96] * markets[addr([94m_1060)].field_256 / markets[addr([94m_1060)].field_256 == ext_call.return_data[96]:
                                  if (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 < 5 * 10^17:
                                      return 12, 0, 0
                                  else:
                                      [94m_1096 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1096] = (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18
                                      [94m_1102 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1102] = 0
                                      if (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18:
                                          if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18 == ext_call.return_data[0]:
                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                  return 12, 0, 0
                                              else:
                                                  [94m_1118 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1118] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                  mem[384] = [94m_1118
                                                  [94m_1135 = mem[96]
                                                  [94m_1139 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1139] = 0
                                                  [94m_1145 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1145] = 0
                                                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 == ext_call.return_data[32]:
                                                          [94m_1158 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1158] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                          if [94m_1135 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[96] = [94m_1135 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                                                              [94m_1203 = mem[128]
                                                              [94m_1219 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1219] = 0
                                                              [94m_1237 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1237] = 0
                                                              if ext_call.return_data[0]:
                                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                      [94m_1266 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1266] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                          if addr([94m_1060):
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                          else:
                                                                              [94m_1388 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1388] = 0
                                                                              [94m_1406 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1406] = 0
                                                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                      [94m_1469 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1469] = 0
                                                                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          [94m_1708 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1708] = 0
                                                                                          [94m_1749 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1749] = 0
                                                                                          if ext_call.return_data[0]:
                                                                                              if not 0 / ext_call.return_data[0]:
                                                                                                  [94m_1879 = mem[64]
                                                                                                  mem[64] = mem[64] + 32
                                                                                                  mem[[94m_1879] = 0
                                                                                                  if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                      return 12, 0, 0
                                                                                                  else:
                                                                                                      mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                      [94midx = [94midx + 1
                                                                                                      [94ms = ext_call.return_data[0]
                                                                                                      continue 
                                                                                              else:
                                                                                                  return 12, 0, 0
                                                                                          else:
                                                                                              [94m_1848 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1848] = 0
                                                                                              if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                  else:
                                                                                      return 12, 0, 0
                                                                              else:
                                                                                  [94m_1450 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1450] = 0
                                                                                  if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1663 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1663] = 0
                                                                                      [94m_1730 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1730] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1849 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1849] = 0
                                                                                              if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_1808 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1808] = 0
                                                                                          if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                  else:
                                                                      return 12, 0, 0
                                                              else:
                                                                  [94m_1255 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1255] = 0
                                                                  if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_1203 + (0 / 10^18)
                                                                      if addr([94m_1060):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_1366 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1366] = 0
                                                                          [94m_1397 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1397] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_1451 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1451] = 0
                                                                                  if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1664 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1664] = 0
                                                                                      [94m_1731 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1731] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1851 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1851] = 0
                                                                                              if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_1203 + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_1809 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1809] = 0
                                                                                          if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1203 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12, 0, 0
                                                                          else:
                                                                              [94m_1429 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1429] = 0
                                                                              if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_1602 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1602] = 0
                                                                                  [94m_1698 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1698] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1810 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1810] = 0
                                                                                          if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1203 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1772 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1772] = 0
                                                                                      if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_1203 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                      else:
                                                          return 12, 0, 0
                                                  else:
                                                      [94m_1152 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1152] = 0
                                                      if [94m_1135 + (0 / 10^18) < 0 / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[96] = [94m_1135 + (0 / 10^18)
                                                          [94m_1184 = mem[128]
                                                          [94m_1206 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1206] = 0
                                                          [94m_1229 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1229] = 0
                                                          if ext_call.return_data[0]:
                                                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                  [94m_1256 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1256] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                  if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                      if addr([94m_1060):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_1367 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1367] = 0
                                                                          [94m_1398 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1398] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_1453 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1453] = 0
                                                                                  if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1667 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1667] = 0
                                                                                      [94m_1732 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1732] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1854 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1854] = 0
                                                                                              if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_1812 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1812] = 0
                                                                                          if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12, 0, 0
                                                                          else:
                                                                              [94m_1430 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1430] = 0
                                                                              if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_1607 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1607] = 0
                                                                                  [94m_1699 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1699] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1813 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1813] = 0
                                                                                          if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1773 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1773] = 0
                                                                                      if [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_1184 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                              else:
                                                                  return 12, 0, 0
                                                          else:
                                                              [94m_1245 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1245] = 0
                                                              if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  mem[128] = [94m_1184 + (0 / 10^18)
                                                                  if addr([94m_1060):
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                                                                  else:
                                                                      [94m_1335 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1335] = 0
                                                                      [94m_1378 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1378] = 0
                                                                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                          if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1060)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              [94m_1431 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1431] = 0
                                                                              if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_1608 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1608] = 0
                                                                                  [94m_1700 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1700] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1815 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1815] = 0
                                                                                          if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_1184 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_1774 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1774] = 0
                                                                                      if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_1184 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                          else:
                                                                              return 12, 0, 0
                                                                      else:
                                                                          [94m_1414 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1414] = 0
                                                                          if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                              return 12, 0, 0
                                                                          else:
                                                                              [94m_1546 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1546] = 0
                                                                              [94m_1649 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1649] = 0
                                                                              if ext_call.return_data[0]:
                                                                                  if not 0 / ext_call.return_data[0]:
                                                                                      [94m_1775 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1775] = 0
                                                                                      if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_1184 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                                  else:
                                                                                      return 12, 0, 0
                                                                              else:
                                                                                  [94m_1751 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1751] = 0
                                                                                  if [94m_1184 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      mem[128] = [94m_1184 + (0 / 10^18)
                                                                                      [94midx = [94midx + 1
                                                                                      [94ms = ext_call.return_data[0]
                                                                                      continue 
                                          else:
                                              return 12, 0, 0
                                      else:
                                          [94m_1116 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1116] = 0
                                          mem[384] = [94m_1116
                                          [94m_1126 = mem[96]
                                          [94m_1136 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1136] = 0
                                          [94m_1141 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1141] = 0
                                          [94m_1148 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1148] = 0
                                          if [94m_1126 + (0 / 10^18) < 0 / 10^18:
                                              return 12, 0, 0
                                          else:
                                              mem[96] = [94m_1126 + (0 / 10^18)
                                              [94m_1172 = mem[128]
                                              [94m_1190 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1190] = 0
                                              [94m_1216 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1216] = 0
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                      [94m_1247 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1247] = ext_call.return_data[64] * ext_call.return_data[0]
                                                      if [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[128] = [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                          if addr([94m_1060):
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                          else:
                                                              [94m_1339 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1339] = 0
                                                              [94m_1382 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1382] = 0
                                                              [94m_1416 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1416] = 0
                                                              if [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  [94m_1558 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1558] = 0
                                                                  [94m_1651 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1651] = 0
                                                                  if ext_call.return_data[0]:
                                                                      if not 0 / ext_call.return_data[0]:
                                                                          [94m_1782 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1782] = 0
                                                                          if [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                              return 12, 0, 0
                                                                          else:
                                                                              mem[128] = [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                      else:
                                                                          return 12, 0, 0
                                                                  else:
                                                                      [94m_1753 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1753] = 0
                                                                      if [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_1172 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                  else:
                                                      return 12, 0, 0
                                              else:
                                                  [94m_1240 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1240] = 0
                                                  if [94m_1172 + (0 / 10^18) < 0 / 10^18:
                                                      return 12, 0, 0
                                                  else:
                                                      mem[128] = [94m_1172 + (0 / 10^18)
                                                      if addr([94m_1060):
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          [94m_1306 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1306] = 0
                                                          [94m_1354 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1354] = 0
                                                          [94m_1408 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1408] = 0
                                                          if [94m_1172 + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              [94m_1512 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1512] = 0
                                                              [94m_1591 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1591] = 0
                                                              if ext_call.return_data[0]:
                                                                  if not 0 / ext_call.return_data[0]:
                                                                      [94m_1755 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1755] = 0
                                                                      if [94m_1172 + (0 / 10^18) < 0 / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_1172 + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                  else:
                                                                      return 12, 0, 0
                                                              else:
                                                                  [94m_1741 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1741] = 0
                                                                  if [94m_1172 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_1172 + (0 / 10^18)
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                              else:
                                  return 12, 0, 0
                          else:
                              [94m_1095 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1095] = 0
                              [94m_1099 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1099] = 0
                              [94m_1113 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1113] = 0
                              mem[384] = [94m_1113
                              [94m_1121 = mem[96]
                              [94m_1130 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1130] = 0
                              [94m_1138 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1138] = 0
                              [94m_1147 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1147] = 0
                              if [94m_1121 + (0 / 10^18) < 0 / 10^18:
                                  return 12, 0, 0
                              else:
                                  mem[96] = [94m_1121 + (0 / 10^18)
                                  [94m_1169 = mem[128]
                                  [94m_1181 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1181] = 0
                                  [94m_1200 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1200] = 0
                                  if ext_call.return_data[0]:
                                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                          [94m_1243 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1243] = ext_call.return_data[64] * ext_call.return_data[0]
                                          if [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                              return 12, 0, 0
                                          else:
                                              mem[128] = [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                              if addr([94m_1060):
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                              else:
                                                  [94m_1315 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1315] = 0
                                                  [94m_1363 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1363] = 0
                                                  [94m_1411 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1411] = 0
                                                  if [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                      return 12, 0, 0
                                                  else:
                                                      [94m_1533 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1533] = 0
                                                      [94m_1594 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1594] = 0
                                                      if ext_call.return_data[0]:
                                                          if not 0 / ext_call.return_data[0]:
                                                              [94m_1767 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1767] = 0
                                                              if [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  mem[128] = [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                  [94midx = [94midx + 1
                                                                  [94ms = ext_call.return_data[0]
                                                                  continue 
                                                          else:
                                                              return 12, 0, 0
                                                      else:
                                                          [94m_1745 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1745] = 0
                                                          if [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[128] = [94m_1169 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                      else:
                                          return 12, 0, 0
                                  else:
                                      [94m_1239 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1239] = 0
                                      if [94m_1169 + (0 / 10^18) < 0 / 10^18:
                                          return 12, 0, 0
                                      else:
                                          mem[128] = [94m_1169 + (0 / 10^18)
                                          if addr([94m_1060):
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              continue 
                                          else:
                                              [94m_1291 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1291] = 0
                                              [94m_1330 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1330] = 0
                                              [94m_1405 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1405] = 0
                                              if [94m_1169 + (0 / 10^18) < 0 / 10^18:
                                                  return 12, 0, 0
                                              else:
                                                  [94m_1501 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1501] = 0
                                                  [94m_1537 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1537] = 0
                                                  if ext_call.return_data[0]:
                                                      if not 0 / ext_call.return_data[0]:
                                                          [94m_1747 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1747] = 0
                                                          if [94m_1169 + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[128] = [94m_1169 + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                      else:
                                                          return 12, 0, 0
                                                  else:
                                                      [94m_1729 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1729] = 0
                                                      if [94m_1169 + (0 / 10^18) < 0 / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[128] = [94m_1169 + (0 / 10^18)
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                      else:
                          return 14, 0, 0
              else:
                  return 16, 0, 0
  else:
      mem[576] = addr(unknowndce15449[addr(_account)].field_0)
      [94midx = 576
      [94ms = 0
      while (32 * unknowndce15449[addr(_account)].field_0) + 544 > [94midx:
          mem[[94midx + 32] = addr(unknowndce15449[addr(_account)][[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_account)].field_0:
          require [94midx < mem[544]
          [94m_3146 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_account)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if not ext_call.return_data[0]:
                  [94m_3158 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[0] = addr([94m_3146)
                  mem[32] = 9
                  mem[[94m_3158] = markets[addr([94m_3146)].field_256
                  mem[288] = [94m_3158
                  [94m_3160 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3160] = ext_call.return_data[96]
                  mem[320] = [94m_3160
                  mem[mem[64] + 4] = addr([94m_3146)
                  require ext_code.size(oracleAddress)
                  static call oracleAddress.0xfc57d4df with:
                          gas gas_remaining wei
                         args addr([94m_3146)
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      mem[256] = ext_call.return_data[0]
                      if ext_call.return_data[0]:
                          [94m_3166 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3166] = ext_call.return_data[0]
                          mem[352] = [94m_3166
                          [94m_3172 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3172] = 0
                          [94m_3173 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3173] = 0
                          [94m_3176 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3176] = 0
                          if markets[addr([94m_3146)].field_256:
                              if ext_call.return_data[96] * markets[addr([94m_3146)].field_256 / markets[addr([94m_3146)].field_256 == ext_call.return_data[96]:
                                  if (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 < 5 * 10^17:
                                      return 12, 0, 0
                                  else:
                                      [94m_3182 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3182] = (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18
                                      [94m_3188 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3188] = 0
                                      if (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18:
                                          if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18 == ext_call.return_data[0]:
                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                  return 12, 0, 0
                                              else:
                                                  [94m_3204 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3204] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                  mem[384] = [94m_3204
                                                  [94m_3221 = mem[96]
                                                  [94m_3225 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3225] = 0
                                                  [94m_3231 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3231] = 0
                                                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 == ext_call.return_data[32]:
                                                          [94m_3244 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3244] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                          if [94m_3221 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[96] = [94m_3221 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                                                              [94m_3289 = mem[128]
                                                              [94m_3305 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3305] = 0
                                                              [94m_3323 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3323] = 0
                                                              if ext_call.return_data[0]:
                                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                      [94m_3352 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3352] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                      if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                          if addr([94m_3146):
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                          else:
                                                                              [94m_3474 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3474] = 0
                                                                              [94m_3492 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3492] = 0
                                                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                      [94m_3555 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3555] = 0
                                                                                      if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          [94m_3794 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3794] = 0
                                                                                          [94m_3835 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3835] = 0
                                                                                          if ext_call.return_data[0]:
                                                                                              if not 0 / ext_call.return_data[0]:
                                                                                                  [94m_3965 = mem[64]
                                                                                                  mem[64] = mem[64] + 32
                                                                                                  mem[[94m_3965] = 0
                                                                                                  if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                      return 12, 0, 0
                                                                                                  else:
                                                                                                      mem[128] = [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                      [94midx = [94midx + 1
                                                                                                      [94ms = ext_call.return_data[0]
                                                                                                      continue 
                                                                                              else:
                                                                                                  return 12, 0, 0
                                                                                          else:
                                                                                              [94m_3934 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_3934] = 0
                                                                                              if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                  else:
                                                                                      return 12, 0, 0
                                                                              else:
                                                                                  [94m_3536 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3536] = 0
                                                                                  if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3749 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3749] = 0
                                                                                      [94m_3816 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3816] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_3935 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_3935] = 0
                                                                                              if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_3894 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3894] = 0
                                                                                          if [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3289 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                  else:
                                                                      return 12, 0, 0
                                                              else:
                                                                  [94m_3341 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3341] = 0
                                                                  if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_3289 + (0 / 10^18)
                                                                      if addr([94m_3146):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_3452 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3452] = 0
                                                                          [94m_3483 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3483] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_3537 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3537] = 0
                                                                                  if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3750 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3750] = 0
                                                                                      [94m_3817 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3817] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_3937 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_3937] = 0
                                                                                              if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_3289 + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_3895 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3895] = 0
                                                                                          if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3289 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12, 0, 0
                                                                          else:
                                                                              [94m_3515 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3515] = 0
                                                                              if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_3688 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3688] = 0
                                                                                  [94m_3784 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3784] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3896 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3896] = 0
                                                                                          if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3289 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3858 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3858] = 0
                                                                                      if [94m_3289 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_3289 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                      else:
                                                          return 12, 0, 0
                                                  else:
                                                      [94m_3238 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3238] = 0
                                                      if [94m_3221 + (0 / 10^18) < 0 / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[96] = [94m_3221 + (0 / 10^18)
                                                          [94m_3270 = mem[128]
                                                          [94m_3292 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3292] = 0
                                                          [94m_3315 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3315] = 0
                                                          if ext_call.return_data[0]:
                                                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                  [94m_3342 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3342] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                  if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                      if addr([94m_3146):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_3453 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3453] = 0
                                                                          [94m_3484 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3484] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_3539 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3539] = 0
                                                                                  if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3753 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3753] = 0
                                                                                      [94m_3818 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3818] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_3940 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_3940] = 0
                                                                                              if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12, 0, 0
                                                                                              else:
                                                                                                  mem[128] = [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12, 0, 0
                                                                                      else:
                                                                                          [94m_3898 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3898] = 0
                                                                                          if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12, 0, 0
                                                                          else:
                                                                              [94m_3516 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3516] = 0
                                                                              if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_3693 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3693] = 0
                                                                                  [94m_3785 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3785] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3899 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3899] = 0
                                                                                          if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3859 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3859] = 0
                                                                                      if [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_3270 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                              else:
                                                                  return 12, 0, 0
                                                          else:
                                                              [94m_3331 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3331] = 0
                                                              if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  mem[128] = [94m_3270 + (0 / 10^18)
                                                                  if addr([94m_3146):
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                                                                  else:
                                                                      [94m_3421 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3421] = 0
                                                                      [94m_3464 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3464] = 0
                                                                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                          if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3146)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              [94m_3517 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3517] = 0
                                                                              if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12, 0, 0
                                                                              else:
                                                                                  [94m_3694 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3694] = 0
                                                                                  [94m_3786 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3786] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3901 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3901] = 0
                                                                                          if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12, 0, 0
                                                                                          else:
                                                                                              mem[128] = [94m_3270 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12, 0, 0
                                                                                  else:
                                                                                      [94m_3860 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3860] = 0
                                                                                      if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_3270 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                          else:
                                                                              return 12, 0, 0
                                                                      else:
                                                                          [94m_3500 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3500] = 0
                                                                          if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                              return 12, 0, 0
                                                                          else:
                                                                              [94m_3632 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3632] = 0
                                                                              [94m_3735 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3735] = 0
                                                                              if ext_call.return_data[0]:
                                                                                  if not 0 / ext_call.return_data[0]:
                                                                                      [94m_3861 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3861] = 0
                                                                                      if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12, 0, 0
                                                                                      else:
                                                                                          mem[128] = [94m_3270 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                                  else:
                                                                                      return 12, 0, 0
                                                                              else:
                                                                                  [94m_3837 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3837] = 0
                                                                                  if [94m_3270 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12, 0, 0
                                                                                  else:
                                                                                      mem[128] = [94m_3270 + (0 / 10^18)
                                                                                      [94midx = [94midx + 1
                                                                                      [94ms = ext_call.return_data[0]
                                                                                      continue 
                                          else:
                                              return 12, 0, 0
                                      else:
                                          [94m_3202 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3202] = 0
                                          mem[384] = [94m_3202
                                          [94m_3212 = mem[96]
                                          [94m_3222 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3222] = 0
                                          [94m_3227 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3227] = 0
                                          [94m_3234 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3234] = 0
                                          if [94m_3212 + (0 / 10^18) < 0 / 10^18:
                                              return 12, 0, 0
                                          else:
                                              mem[96] = [94m_3212 + (0 / 10^18)
                                              [94m_3258 = mem[128]
                                              [94m_3276 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3276] = 0
                                              [94m_3302 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3302] = 0
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                      [94m_3333 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3333] = ext_call.return_data[64] * ext_call.return_data[0]
                                                      if [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[128] = [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                          if addr([94m_3146):
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                          else:
                                                              [94m_3425 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3425] = 0
                                                              [94m_3468 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3468] = 0
                                                              [94m_3502 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3502] = 0
                                                              if [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  [94m_3644 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3644] = 0
                                                                  [94m_3737 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3737] = 0
                                                                  if ext_call.return_data[0]:
                                                                      if not 0 / ext_call.return_data[0]:
                                                                          [94m_3868 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3868] = 0
                                                                          if [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                              return 12, 0, 0
                                                                          else:
                                                                              mem[128] = [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                      else:
                                                                          return 12, 0, 0
                                                                  else:
                                                                      [94m_3839 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3839] = 0
                                                                      if [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_3258 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                  else:
                                                      return 12, 0, 0
                                              else:
                                                  [94m_3326 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3326] = 0
                                                  if [94m_3258 + (0 / 10^18) < 0 / 10^18:
                                                      return 12, 0, 0
                                                  else:
                                                      mem[128] = [94m_3258 + (0 / 10^18)
                                                      if addr([94m_3146):
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          [94m_3392 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3392] = 0
                                                          [94m_3440 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3440] = 0
                                                          [94m_3494 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3494] = 0
                                                          if [94m_3258 + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              [94m_3598 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3598] = 0
                                                              [94m_3677 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3677] = 0
                                                              if ext_call.return_data[0]:
                                                                  if not 0 / ext_call.return_data[0]:
                                                                      [94m_3841 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3841] = 0
                                                                      if [94m_3258 + (0 / 10^18) < 0 / 10^18:
                                                                          return 12, 0, 0
                                                                      else:
                                                                          mem[128] = [94m_3258 + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                  else:
                                                                      return 12, 0, 0
                                                              else:
                                                                  [94m_3827 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3827] = 0
                                                                  if [94m_3258 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12, 0, 0
                                                                  else:
                                                                      mem[128] = [94m_3258 + (0 / 10^18)
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                              else:
                                  return 12, 0, 0
                          else:
                              [94m_3181 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3181] = 0
                              [94m_3185 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3185] = 0
                              [94m_3199 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3199] = 0
                              mem[384] = [94m_3199
                              [94m_3207 = mem[96]
                              [94m_3216 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3216] = 0
                              [94m_3224 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3224] = 0
                              [94m_3233 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3233] = 0
                              if [94m_3207 + (0 / 10^18) < 0 / 10^18:
                                  return 12, 0, 0
                              else:
                                  mem[96] = [94m_3207 + (0 / 10^18)
                                  [94m_3255 = mem[128]
                                  [94m_3267 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3267] = 0
                                  [94m_3286 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3286] = 0
                                  if ext_call.return_data[0]:
                                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                          [94m_3329 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3329] = ext_call.return_data[64] * ext_call.return_data[0]
                                          if [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                              return 12, 0, 0
                                          else:
                                              mem[128] = [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                              if addr([94m_3146):
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                              else:
                                                  [94m_3401 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3401] = 0
                                                  [94m_3449 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3449] = 0
                                                  [94m_3497 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3497] = 0
                                                  if [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                      return 12, 0, 0
                                                  else:
                                                      [94m_3619 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3619] = 0
                                                      [94m_3680 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3680] = 0
                                                      if ext_call.return_data[0]:
                                                          if not 0 / ext_call.return_data[0]:
                                                              [94m_3853 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3853] = 0
                                                              if [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12, 0, 0
                                                              else:
                                                                  mem[128] = [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                  [94midx = [94midx + 1
                                                                  [94ms = ext_call.return_data[0]
                                                                  continue 
                                                          else:
                                                              return 12, 0, 0
                                                      else:
                                                          [94m_3831 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3831] = 0
                                                          if [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[128] = [94m_3255 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                      else:
                                          return 12, 0, 0
                                  else:
                                      [94m_3325 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3325] = 0
                                      if [94m_3255 + (0 / 10^18) < 0 / 10^18:
                                          return 12, 0, 0
                                      else:
                                          mem[128] = [94m_3255 + (0 / 10^18)
                                          if addr([94m_3146):
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              continue 
                                          else:
                                              [94m_3377 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3377] = 0
                                              [94m_3416 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3416] = 0
                                              [94m_3491 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3491] = 0
                                              if [94m_3255 + (0 / 10^18) < 0 / 10^18:
                                                  return 12, 0, 0
                                              else:
                                                  [94m_3587 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3587] = 0
                                                  [94m_3623 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3623] = 0
                                                  if ext_call.return_data[0]:
                                                      if not 0 / ext_call.return_data[0]:
                                                          [94m_3833 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3833] = 0
                                                          if [94m_3255 + (0 / 10^18) < 0 / 10^18:
                                                              return 12, 0, 0
                                                          else:
                                                              mem[128] = [94m_3255 + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                      else:
                                                          return 12, 0, 0
                                                  else:
                                                      [94m_3815 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3815] = 0
                                                      if [94m_3255 + (0 / 10^18) < 0 / 10^18:
                                                          return 12, 0, 0
                                                      else:
                                                          mem[128] = [94m_3255 + (0 / 10^18)
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                      else:
                          return 14, 0, 0
              else:
                  return 16, 0, 0
  if mem[96] <= mem[128]:
      return 0, 0, mem[128] - mem[96]
  return 0, mem[96] - mem[128], 0


# hash = 0x5fc7e71e
# getter = None
# const = None
# payable = True
def unknown5fc7e71e(addr _param1, addr _param2, addr _param3, uint256 _param4) payable: 
  require calldata.size - 4 >= 160
  if not uint8(markets[addr(_param1)].field_0):
      return 9
  if not uint8(markets[addr(_param2)].field_0):
      return 9
  mem[96] = 0
  mem[128] = 0
  mem[64] = (32 * unknowndce15449[addr(_param3)].field_0) + 576
  mem[544] = unknowndce15449[addr(_param3)].field_0
  if not unknowndce15449[addr(_param3)].field_0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param3)].field_0:
          require [94midx < mem[544]
          [94m_1087 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param3)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if not ext_call.return_data[0]:
                  [94m_1095 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[0] = addr([94m_1087)
                  mem[32] = 9
                  mem[[94m_1095] = markets[addr([94m_1087)].field_256
                  mem[288] = [94m_1095
                  [94m_1097 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1097] = ext_call.return_data[96]
                  mem[320] = [94m_1097
                  mem[mem[64] + 4] = addr([94m_1087)
                  require ext_code.size(oracleAddress)
                  static call oracleAddress.0xfc57d4df with:
                          gas gas_remaining wei
                         args addr([94m_1087)
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      mem[256] = ext_call.return_data[0]
                      if ext_call.return_data[0]:
                          [94m_1106 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1106] = ext_call.return_data[0]
                          mem[352] = [94m_1106
                          [94m_1116 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1116] = 0
                          [94m_1118 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1118] = 0
                          [94m_1123 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1123] = 0
                          if markets[addr([94m_1087)].field_256:
                              if ext_call.return_data[96] * markets[addr([94m_1087)].field_256 / markets[addr([94m_1087)].field_256 == ext_call.return_data[96]:
                                  if (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 < 5 * 10^17:
                                      return 12
                                  else:
                                      [94m_1146 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1146] = (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18
                                      [94m_1152 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1152] = 0
                                      if (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18:
                                          if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18 == ext_call.return_data[0]:
                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                  return 12
                                              else:
                                                  [94m_1166 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1166] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                  mem[384] = [94m_1166
                                                  [94m_1181 = mem[96]
                                                  [94m_1187 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1187] = 0
                                                  [94m_1195 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1195] = 0
                                                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 == ext_call.return_data[32]:
                                                          [94m_1208 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1208] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                          if [94m_1181 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[96] = [94m_1181 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                                                              [94m_1245 = mem[128]
                                                              [94m_1255 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1255] = 0
                                                              [94m_1279 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1279] = 0
                                                              if ext_call.return_data[0]:
                                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                      [94m_1316 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1316] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                      if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                          if addr([94m_1087):
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                          else:
                                                                              [94m_1416 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1416] = 0
                                                                              [94m_1446 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1446] = 0
                                                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                      [94m_1519 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1519] = 0
                                                                                      if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          [94m_1708 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1708] = 0
                                                                                          [94m_1787 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1787] = 0
                                                                                          if ext_call.return_data[0]:
                                                                                              if not 0 / ext_call.return_data[0]:
                                                                                                  [94m_1929 = mem[64]
                                                                                                  mem[64] = mem[64] + 32
                                                                                                  mem[[94m_1929] = 0
                                                                                                  if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                      return 12
                                                                                                  else:
                                                                                                      mem[128] = [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                      [94midx = [94midx + 1
                                                                                                      [94ms = ext_call.return_data[0]
                                                                                                      continue 
                                                                                              else:
                                                                                                  return 12
                                                                                          else:
                                                                                              [94m_1898 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1898] = 0
                                                                                              if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                  else:
                                                                                      return 12
                                                                              else:
                                                                                  [94m_1500 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1500] = 0
                                                                                  if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_1661 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1661] = 0
                                                                                      [94m_1748 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1748] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1899 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1899] = 0
                                                                                              if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_1858 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1858] = 0
                                                                                          if [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1245 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                  else:
                                                                      return 12
                                                              else:
                                                                  [94m_1305 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1305] = 0
                                                                  if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_1245 + (0 / 10^18)
                                                                      if addr([94m_1087):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_1388 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1388] = 0
                                                                          [94m_1425 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1425] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_1501 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1501] = 0
                                                                                  if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_1662 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1662] = 0
                                                                                      [94m_1749 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1749] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1901 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1901] = 0
                                                                                              if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_1245 + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_1859 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1859] = 0
                                                                                          if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1245 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12
                                                                          else:
                                                                              [94m_1479 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1479] = 0
                                                                              if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_1618 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1618] = 0
                                                                                  [94m_1698 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1698] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1860 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1860] = 0
                                                                                          if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1245 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_1822 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1822] = 0
                                                                                      if [94m_1245 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_1245 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                      else:
                                                          return 12
                                                  else:
                                                      [94m_1202 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1202] = 0
                                                      if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                                                          return 12
                                                      else:
                                                          mem[96] = [94m_1181 + (0 / 10^18)
                                                          [94m_1232 = mem[128]
                                                          [94m_1246 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1246] = 0
                                                          [94m_1265 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1265] = 0
                                                          if ext_call.return_data[0]:
                                                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                  [94m_1306 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1306] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                  if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                      if addr([94m_1087):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_1389 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1389] = 0
                                                                          [94m_1426 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1426] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_1503 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1503] = 0
                                                                                  if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_1663 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1663] = 0
                                                                                      [94m_1750 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1750] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_1904 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_1904] = 0
                                                                                              if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_1862 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1862] = 0
                                                                                          if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12
                                                                          else:
                                                                              [94m_1480 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1480] = 0
                                                                              if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_1621 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1621] = 0
                                                                                  [94m_1699 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1699] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1863 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1863] = 0
                                                                                          if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_1823 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1823] = 0
                                                                                      if [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_1232 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                              else:
                                                                  return 12
                                                          else:
                                                              [94m_1295 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1295] = 0
                                                              if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  mem[128] = [94m_1232 + (0 / 10^18)
                                                                  if addr([94m_1087):
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                                                                  else:
                                                                      [94m_1363 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1363] = 0
                                                                      [94m_1398 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1398] = 0
                                                                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                          if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1087)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              [94m_1481 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1481] = 0
                                                                              if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_1622 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1622] = 0
                                                                                  [94m_1700 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1700] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_1865 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_1865] = 0
                                                                                          if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_1232 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_1824 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1824] = 0
                                                                                      if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_1232 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                          else:
                                                                              return 12
                                                                      else:
                                                                          [94m_1464 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1464] = 0
                                                                          if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                              return 12
                                                                          else:
                                                                              [94m_1582 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1582] = 0
                                                                              [94m_1649 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_1649] = 0
                                                                              if ext_call.return_data[0]:
                                                                                  if not 0 / ext_call.return_data[0]:
                                                                                      [94m_1825 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_1825] = 0
                                                                                      if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_1232 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                                  else:
                                                                                      return 12
                                                                              else:
                                                                                  [94m_1795 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_1795] = 0
                                                                                  if [94m_1232 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      mem[128] = [94m_1232 + (0 / 10^18)
                                                                                      [94midx = [94midx + 1
                                                                                      [94ms = ext_call.return_data[0]
                                                                                      continue 
                                          else:
                                              return 12
                                      else:
                                          [94m_1162 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1162] = 0
                                          mem[384] = [94m_1162
                                          [94m_1174 = mem[96]
                                          [94m_1182 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1182] = 0
                                          [94m_1191 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1191] = 0
                                          [94m_1198 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1198] = 0
                                          if [94m_1174 + (0 / 10^18) < 0 / 10^18:
                                              return 12
                                          else:
                                              mem[96] = [94m_1174 + (0 / 10^18)
                                              [94m_1222 = mem[128]
                                              [94m_1236 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1236] = 0
                                              [94m_1252 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1252] = 0
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                      [94m_1297 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1297] = ext_call.return_data[64] * ext_call.return_data[0]
                                                      if [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                          return 12
                                                      else:
                                                          mem[128] = [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                          if addr([94m_1087):
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                          else:
                                                              [94m_1367 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1367] = 0
                                                              [94m_1402 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1402] = 0
                                                              [94m_1466 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1466] = 0
                                                              if [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  [94m_1590 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1590] = 0
                                                                  [94m_1651 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1651] = 0
                                                                  if ext_call.return_data[0]:
                                                                      if not 0 / ext_call.return_data[0]:
                                                                          [94m_1832 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_1832] = 0
                                                                          if [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                              return 12
                                                                          else:
                                                                              mem[128] = [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                      else:
                                                                          return 12
                                                                  else:
                                                                      [94m_1799 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1799] = 0
                                                                      if [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_1222 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                  else:
                                                      return 12
                                              else:
                                                  [94m_1290 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1290] = 0
                                                  if [94m_1222 + (0 / 10^18) < 0 / 10^18:
                                                      return 12
                                                  else:
                                                      mem[128] = [94m_1222 + (0 / 10^18)
                                                      if addr([94m_1087):
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          [94m_1346 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1346] = 0
                                                          [94m_1376 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1376] = 0
                                                          [94m_1456 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1456] = 0
                                                          if [94m_1222 + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              [94m_1558 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1558] = 0
                                                              [94m_1609 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1609] = 0
                                                              if ext_call.return_data[0]:
                                                                  if not 0 / ext_call.return_data[0]:
                                                                      [94m_1801 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_1801] = 0
                                                                      if [94m_1222 + (0 / 10^18) < 0 / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_1222 + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                  else:
                                                                      return 12
                                                              else:
                                                                  [94m_1771 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_1771] = 0
                                                                  if [94m_1222 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_1222 + (0 / 10^18)
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                              else:
                                  return 12
                          else:
                              [94m_1141 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1141] = 0
                              [94m_1147 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1147] = 0
                              [94m_1161 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1161] = 0
                              mem[384] = [94m_1161
                              [94m_1169 = mem[96]
                              [94m_1178 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1178] = 0
                              [94m_1186 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1186] = 0
                              [94m_1197 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1197] = 0
                              if [94m_1169 + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              else:
                                  mem[96] = [94m_1169 + (0 / 10^18)
                                  [94m_1219 = mem[128]
                                  [94m_1229 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1229] = 0
                                  [94m_1242 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1242] = 0
                                  if ext_call.return_data[0]:
                                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                          [94m_1293 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_1293] = ext_call.return_data[64] * ext_call.return_data[0]
                                          if [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                              return 12
                                          else:
                                              mem[128] = [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                              if addr([94m_1087):
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                              else:
                                                  [94m_1355 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1355] = 0
                                                  [94m_1383 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1383] = 0
                                                  [94m_1459 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1459] = 0
                                                  if [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                      return 12
                                                  else:
                                                      [94m_1573 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1573] = 0
                                                      [94m_1612 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1612] = 0
                                                      if ext_call.return_data[0]:
                                                          if not 0 / ext_call.return_data[0]:
                                                              [94m_1815 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_1815] = 0
                                                              if [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  mem[128] = [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                  [94midx = [94midx + 1
                                                                  [94ms = ext_call.return_data[0]
                                                                  continue 
                                                          else:
                                                              return 12
                                                      else:
                                                          [94m_1783 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1783] = 0
                                                          if [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[128] = [94m_1219 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                      else:
                                          return 12
                                  else:
                                      [94m_1287 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1287] = 0
                                      if [94m_1219 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      else:
                                          mem[128] = [94m_1219 + (0 / 10^18)
                                          if addr([94m_1087):
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              continue 
                                          else:
                                              [94m_1339 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1339] = 0
                                              [94m_1358 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1358] = 0
                                              [94m_1445 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_1445] = 0
                                              if [94m_1219 + (0 / 10^18) < 0 / 10^18:
                                                  return 12
                                              else:
                                                  [94m_1549 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1549] = 0
                                                  [94m_1575 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_1575] = 0
                                                  if ext_call.return_data[0]:
                                                      if not 0 / ext_call.return_data[0]:
                                                          [94m_1785 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_1785] = 0
                                                          if [94m_1219 + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[128] = [94m_1219 + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                      else:
                                                          return 12
                                                  else:
                                                      [94m_1747 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_1747] = 0
                                                      if [94m_1219 + (0 / 10^18) < 0 / 10^18:
                                                          return 12
                                                      else:
                                                          mem[128] = [94m_1219 + (0 / 10^18)
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                      else:
                          return 14
              else:
                  return 16
  else:
      mem[576] = addr(unknowndce15449[addr(_param3)].field_0)
      [94midx = 576
      [94ms = 0
      while (32 * unknowndce15449[addr(_param3)].field_0) + 544 > [94midx:
          mem[[94midx + 32] = addr(unknowndce15449[addr(_param3)][[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param3)].field_0:
          require [94midx < mem[544]
          [94m_3219 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param3)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if not ext_call.return_data[0]:
                  [94m_3227 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[0] = addr([94m_3219)
                  mem[32] = 9
                  mem[[94m_3227] = markets[addr([94m_3219)].field_256
                  mem[288] = [94m_3227
                  [94m_3229 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3229] = ext_call.return_data[96]
                  mem[320] = [94m_3229
                  mem[mem[64] + 4] = addr([94m_3219)
                  require ext_code.size(oracleAddress)
                  static call oracleAddress.0xfc57d4df with:
                          gas gas_remaining wei
                         args addr([94m_3219)
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      mem[256] = ext_call.return_data[0]
                      if ext_call.return_data[0]:
                          [94m_3238 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3238] = ext_call.return_data[0]
                          mem[352] = [94m_3238
                          [94m_3248 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3248] = 0
                          [94m_3250 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3250] = 0
                          [94m_3255 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3255] = 0
                          if markets[addr([94m_3219)].field_256:
                              if ext_call.return_data[96] * markets[addr([94m_3219)].field_256 / markets[addr([94m_3219)].field_256 == ext_call.return_data[96]:
                                  if (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 < 5 * 10^17:
                                      return 12
                                  else:
                                      [94m_3278 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3278] = (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18
                                      [94m_3284 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3284] = 0
                                      if (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18:
                                          if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18 == ext_call.return_data[0]:
                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                  return 12
                                              else:
                                                  [94m_3298 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3298] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                  mem[384] = [94m_3298
                                                  [94m_3313 = mem[96]
                                                  [94m_3319 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3319] = 0
                                                  [94m_3327 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3327] = 0
                                                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 == ext_call.return_data[32]:
                                                          [94m_3340 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3340] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                                          if [94m_3313 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[96] = [94m_3313 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                                                              [94m_3377 = mem[128]
                                                              [94m_3387 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3387] = 0
                                                              [94m_3411 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3411] = 0
                                                              if ext_call.return_data[0]:
                                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                      [94m_3448 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3448] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                      if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                          if addr([94m_3219):
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                          else:
                                                                              [94m_3548 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3548] = 0
                                                                              [94m_3578 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3578] = 0
                                                                              if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                      [94m_3651 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3651] = 0
                                                                                      if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          [94m_3840 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3840] = 0
                                                                                          [94m_3919 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3919] = 0
                                                                                          if ext_call.return_data[0]:
                                                                                              if not 0 / ext_call.return_data[0]:
                                                                                                  [94m_4061 = mem[64]
                                                                                                  mem[64] = mem[64] + 32
                                                                                                  mem[[94m_4061] = 0
                                                                                                  if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                      return 12
                                                                                                  else:
                                                                                                      mem[128] = [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                      [94midx = [94midx + 1
                                                                                                      [94ms = ext_call.return_data[0]
                                                                                                      continue 
                                                                                              else:
                                                                                                  return 12
                                                                                          else:
                                                                                              [94m_4030 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_4030] = 0
                                                                                              if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                  else:
                                                                                      return 12
                                                                              else:
                                                                                  [94m_3632 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3632] = 0
                                                                                  if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_3793 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3793] = 0
                                                                                      [94m_3880 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3880] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_4031 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_4031] = 0
                                                                                              if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_3990 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3990] = 0
                                                                                          if [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3377 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                  else:
                                                                      return 12
                                                              else:
                                                                  [94m_3437 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3437] = 0
                                                                  if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_3377 + (0 / 10^18)
                                                                      if addr([94m_3219):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_3520 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3520] = 0
                                                                          [94m_3557 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3557] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_3633 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3633] = 0
                                                                                  if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_3794 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3794] = 0
                                                                                      [94m_3881 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3881] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_4033 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_4033] = 0
                                                                                              if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_3377 + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_3991 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3991] = 0
                                                                                          if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3377 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12
                                                                          else:
                                                                              [94m_3611 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3611] = 0
                                                                              if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_3750 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3750] = 0
                                                                                  [94m_3830 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3830] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3992 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3992] = 0
                                                                                          if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3377 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_3954 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3954] = 0
                                                                                      if [94m_3377 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_3377 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                      else:
                                                          return 12
                                                  else:
                                                      [94m_3334 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3334] = 0
                                                      if [94m_3313 + (0 / 10^18) < 0 / 10^18:
                                                          return 12
                                                      else:
                                                          mem[96] = [94m_3313 + (0 / 10^18)
                                                          [94m_3364 = mem[128]
                                                          [94m_3378 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3378] = 0
                                                          [94m_3397 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3397] = 0
                                                          if ext_call.return_data[0]:
                                                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                                  [94m_3438 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3438] = ext_call.return_data[64] * ext_call.return_data[0]
                                                                  if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                                      if addr([94m_3219):
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                      else:
                                                                          [94m_3521 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3521] = 0
                                                                          [94m_3558 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3558] = 0
                                                                          if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                                  [94m_3635 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3635] = 0
                                                                                  if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      [94m_3795 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3795] = 0
                                                                                      [94m_3882 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3882] = 0
                                                                                      if ext_call.return_data[0]:
                                                                                          if not 0 / ext_call.return_data[0]:
                                                                                              [94m_4036 = mem[64]
                                                                                              mem[64] = mem[64] + 32
                                                                                              mem[[94m_4036] = 0
                                                                                              if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                                  return 12
                                                                                              else:
                                                                                                  mem[128] = [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                                  [94midx = [94midx + 1
                                                                                                  [94ms = ext_call.return_data[0]
                                                                                                  continue 
                                                                                          else:
                                                                                              return 12
                                                                                      else:
                                                                                          [94m_3994 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3994] = 0
                                                                                          if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                              else:
                                                                                  return 12
                                                                          else:
                                                                              [94m_3612 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3612] = 0
                                                                              if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_3753 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3753] = 0
                                                                                  [94m_3831 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3831] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3995 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3995] = 0
                                                                                          if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_3955 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3955] = 0
                                                                                      if [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_3364 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                              else:
                                                                  return 12
                                                          else:
                                                              [94m_3427 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3427] = 0
                                                              if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  mem[128] = [94m_3364 + (0 / 10^18)
                                                                  if addr([94m_3219):
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                                                                  else:
                                                                      [94m_3495 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3495] = 0
                                                                      [94m_3530 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3530] = 0
                                                                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                          if not 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3219)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                                                              [94m_3613 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3613] = 0
                                                                              if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                                  return 12
                                                                              else:
                                                                                  [94m_3754 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3754] = 0
                                                                                  [94m_3832 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3832] = 0
                                                                                  if ext_call.return_data[0]:
                                                                                      if not 0 / ext_call.return_data[0]:
                                                                                          [94m_3997 = mem[64]
                                                                                          mem[64] = mem[64] + 32
                                                                                          mem[[94m_3997] = 0
                                                                                          if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                                              return 12
                                                                                          else:
                                                                                              mem[128] = [94m_3364 + (0 / 10^18)
                                                                                              [94midx = [94midx + 1
                                                                                              [94ms = ext_call.return_data[0]
                                                                                              continue 
                                                                                      else:
                                                                                          return 12
                                                                                  else:
                                                                                      [94m_3956 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3956] = 0
                                                                                      if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_3364 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                          else:
                                                                              return 12
                                                                      else:
                                                                          [94m_3596 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3596] = 0
                                                                          if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                              return 12
                                                                          else:
                                                                              [94m_3714 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3714] = 0
                                                                              [94m_3781 = mem[64]
                                                                              mem[64] = mem[64] + 32
                                                                              mem[[94m_3781] = 0
                                                                              if ext_call.return_data[0]:
                                                                                  if not 0 / ext_call.return_data[0]:
                                                                                      [94m_3957 = mem[64]
                                                                                      mem[64] = mem[64] + 32
                                                                                      mem[[94m_3957] = 0
                                                                                      if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                                          return 12
                                                                                      else:
                                                                                          mem[128] = [94m_3364 + (0 / 10^18)
                                                                                          [94midx = [94midx + 1
                                                                                          [94ms = ext_call.return_data[0]
                                                                                          continue 
                                                                                  else:
                                                                                      return 12
                                                                              else:
                                                                                  [94m_3927 = mem[64]
                                                                                  mem[64] = mem[64] + 32
                                                                                  mem[[94m_3927] = 0
                                                                                  if [94m_3364 + (0 / 10^18) < 0 / 10^18:
                                                                                      return 12
                                                                                  else:
                                                                                      mem[128] = [94m_3364 + (0 / 10^18)
                                                                                      [94midx = [94midx + 1
                                                                                      [94ms = ext_call.return_data[0]
                                                                                      continue 
                                          else:
                                              return 12
                                      else:
                                          [94m_3294 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3294] = 0
                                          mem[384] = [94m_3294
                                          [94m_3306 = mem[96]
                                          [94m_3314 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3314] = 0
                                          [94m_3323 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3323] = 0
                                          [94m_3330 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3330] = 0
                                          if [94m_3306 + (0 / 10^18) < 0 / 10^18:
                                              return 12
                                          else:
                                              mem[96] = [94m_3306 + (0 / 10^18)
                                              [94m_3354 = mem[128]
                                              [94m_3368 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3368] = 0
                                              [94m_3384 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3384] = 0
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                                      [94m_3429 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3429] = ext_call.return_data[64] * ext_call.return_data[0]
                                                      if [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                                          return 12
                                                      else:
                                                          mem[128] = [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                                          if addr([94m_3219):
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                          else:
                                                              [94m_3499 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3499] = 0
                                                              [94m_3534 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3534] = 0
                                                              [94m_3598 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3598] = 0
                                                              if [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  [94m_3722 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3722] = 0
                                                                  [94m_3783 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3783] = 0
                                                                  if ext_call.return_data[0]:
                                                                      if not 0 / ext_call.return_data[0]:
                                                                          [94m_3964 = mem[64]
                                                                          mem[64] = mem[64] + 32
                                                                          mem[[94m_3964] = 0
                                                                          if [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                              return 12
                                                                          else:
                                                                              mem[128] = [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                              [94midx = [94midx + 1
                                                                              [94ms = ext_call.return_data[0]
                                                                              continue 
                                                                      else:
                                                                          return 12
                                                                  else:
                                                                      [94m_3931 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3931] = 0
                                                                      if [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_3354 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                  else:
                                                      return 12
                                              else:
                                                  [94m_3422 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3422] = 0
                                                  if [94m_3354 + (0 / 10^18) < 0 / 10^18:
                                                      return 12
                                                  else:
                                                      mem[128] = [94m_3354 + (0 / 10^18)
                                                      if addr([94m_3219):
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                                                      else:
                                                          [94m_3478 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3478] = 0
                                                          [94m_3508 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3508] = 0
                                                          [94m_3588 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3588] = 0
                                                          if [94m_3354 + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              [94m_3690 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3690] = 0
                                                              [94m_3741 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3741] = 0
                                                              if ext_call.return_data[0]:
                                                                  if not 0 / ext_call.return_data[0]:
                                                                      [94m_3933 = mem[64]
                                                                      mem[64] = mem[64] + 32
                                                                      mem[[94m_3933] = 0
                                                                      if [94m_3354 + (0 / 10^18) < 0 / 10^18:
                                                                          return 12
                                                                      else:
                                                                          mem[128] = [94m_3354 + (0 / 10^18)
                                                                          [94midx = [94midx + 1
                                                                          [94ms = ext_call.return_data[0]
                                                                          continue 
                                                                  else:
                                                                      return 12
                                                              else:
                                                                  [94m_3903 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_3903] = 0
                                                                  if [94m_3354 + (0 / 10^18) < 0 / 10^18:
                                                                      return 12
                                                                  else:
                                                                      mem[128] = [94m_3354 + (0 / 10^18)
                                                                      [94midx = [94midx + 1
                                                                      [94ms = ext_call.return_data[0]
                                                                      continue 
                              else:
                                  return 12
                          else:
                              [94m_3273 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3273] = 0
                              [94m_3279 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3279] = 0
                              [94m_3293 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3293] = 0
                              mem[384] = [94m_3293
                              [94m_3301 = mem[96]
                              [94m_3310 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3310] = 0
                              [94m_3318 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3318] = 0
                              [94m_3329 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3329] = 0
                              if [94m_3301 + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              else:
                                  mem[96] = [94m_3301 + (0 / 10^18)
                                  [94m_3351 = mem[128]
                                  [94m_3361 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3361] = 0
                                  [94m_3374 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3374] = 0
                                  if ext_call.return_data[0]:
                                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[64]:
                                          [94m_3425 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_3425] = ext_call.return_data[64] * ext_call.return_data[0]
                                          if [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                              return 12
                                          else:
                                              mem[128] = [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                                              if addr([94m_3219):
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                              else:
                                                  [94m_3487 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3487] = 0
                                                  [94m_3515 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3515] = 0
                                                  [94m_3591 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3591] = 0
                                                  if [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                      return 12
                                                  else:
                                                      [94m_3705 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3705] = 0
                                                      [94m_3744 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3744] = 0
                                                      if ext_call.return_data[0]:
                                                          if not 0 / ext_call.return_data[0]:
                                                              [94m_3947 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_3947] = 0
                                                              if [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                                  return 12
                                                              else:
                                                                  mem[128] = [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                                  [94midx = [94midx + 1
                                                                  [94ms = ext_call.return_data[0]
                                                                  continue 
                                                          else:
                                                              return 12
                                                      else:
                                                          [94m_3915 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3915] = 0
                                                          if [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[128] = [94m_3351 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                      else:
                                          return 12
                                  else:
                                      [94m_3419 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3419] = 0
                                      if [94m_3351 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      else:
                                          mem[128] = [94m_3351 + (0 / 10^18)
                                          if addr([94m_3219):
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              continue 
                                          else:
                                              [94m_3471 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3471] = 0
                                              [94m_3490 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3490] = 0
                                              [94m_3577 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_3577] = 0
                                              if [94m_3351 + (0 / 10^18) < 0 / 10^18:
                                                  return 12
                                              else:
                                                  [94m_3681 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3681] = 0
                                                  [94m_3707 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_3707] = 0
                                                  if ext_call.return_data[0]:
                                                      if not 0 / ext_call.return_data[0]:
                                                          [94m_3917 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_3917] = 0
                                                          if [94m_3351 + (0 / 10^18) < 0 / 10^18:
                                                              return 12
                                                          else:
                                                              mem[128] = [94m_3351 + (0 / 10^18)
                                                              [94midx = [94midx + 1
                                                              [94ms = ext_call.return_data[0]
                                                              continue 
                                                      else:
                                                          return 12
                                                  else:
                                                      [94m_3879 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_3879] = 0
                                                      if [94m_3351 + (0 / 10^18) < 0 / 10^18:
                                                          return 12
                                                      else:
                                                          mem[128] = [94m_3351 + (0 / 10^18)
                                                          [94midx = [94midx + 1
                                                          [94ms = ext_call.return_data[0]
                                                          continue 
                      else:
                          return 14
              else:
                  return 16
  if mem[96] > mem[128]:
      return 3
  if not mem[128] - mem[96]:
      return 3
  require ext_code.size(_param1)
  static call _param1.0x95dd9193 with:
          gas gas_remaining wei
         args addr(_param3)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknowne8755446:
      if _param4 <= 0 / 10^18:
          return 0
  else:
      if ext_call.return_data[0] * unknowne8755446 / unknowne8755446 != ext_call.return_data[0]:
          return 12
      if _param4 <= ext_call.return_data[0] * unknowne8755446 / 10^18:
          return 0
  return 18


# hash = 0x6a56947e
# getter = None
# const = None
# payable = True
def unknown6a56947e() payable: 
  require calldata.size - 4 >= 128


# hash = 0x6d35bf91
# getter = None
# const = None
# payable = True
def unknown6d35bf91() payable: 
  require calldata.size - 4 >= 160


# hash = 0x7dc0d1d0
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def oracle() payable: 
  return oracleAddress


# hash = 0x8e8f294b
# getter = ['struct', ['loc', 9]]
# const = None
# payable = True
def markets(address _param1) payable: 
  require calldata.size - 4 >= 32
  return bool(uint8(markets[_param1].field_0)), bool(uint8(markets[_param1].field_8)), markets[_param1].field_256


# hash = 0x929fe9a1
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], 9]]]]]]]
# const = None
# payable = True
def unknown929fe9a1(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  return bool(uint8(markets[addr(_param2)][2][addr(_param1)].field_0))


# hash = 0x94b2294b
# getter = ['storage', 256, 0, 7]
# const = None
# payable = True
def unknown94b2294b() payable: 
  return unknown94b2294b


# hash = 0xa76b3fda
# getter = None
# const = None
# payable = True
def unknowna76b3fda(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if adminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=18,
            uint256 detail=0)
      return 1
  if uint8(markets[addr(_param1)].field_0):
      log Failure(
            uint256 error=11,
            uint256 info=17,
            uint256 detail=0)
      return 11
  require ext_code.size(_param1)
  static call _param1.0x9839b52 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint8(markets[addr(_param1)].field_0) = 1
  Mask(248, 0, markets[addr(_param1)].field_8) = 0
  Mask(240, 0, markets[addr(_param1)].field_16) = 0
  markets[addr(_param1)].field_256 = 0
  log 0xcf583bb0: _param1
  return 0


# hash = 0xabfceffc
# getter = None
# const = None
# payable = True
def unknownabfceffc(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if not unknowndce15449[addr(_param1)].field_0:
      mem[(32 * unknowndce15449[addr(_param1)].field_0) + 128] = 32
      mem[(32 * unknowndce15449[addr(_param1)].field_0) + 160] = unknowndce15449[addr(_param1)].field_0
      mem[(32 * unknowndce15449[addr(_param1)].field_0) + 192 len floor32(unknowndce15449[addr(_param1)].field_0)] = mem[128 len floor32(unknowndce15449[addr(_param1)].field_0)]
      return memory
        from (32 * unknowndce15449[addr(_param1)].field_0) + 128
         [93mlen (96 * unknowndce15449[addr(_param1)].field_0) + 64
  mem[128] = addr(unknowndce15449[addr(_param1)].field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknowndce15449[addr(_param1)].field_0) + 96 > [94midx:
      mem[[94midx + 32] = addr(unknowndce15449[addr(_param1)][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknowndce15449[addr(_param1)].field_0) + 192 len floor32(unknowndce15449[addr(_param1)].field_0)] = mem[128 len floor32(unknowndce15449[addr(_param1)].field_0)]
  return Array(len=unknowndce15449[addr(_param1)].field_0, data=mem[128 len floor32(unknowndce15449[addr(_param1)].field_0)], mem[(32 * unknowndce15449[addr(_param1)].field_0) + floor32(unknowndce15449[addr(_param1)].field_0) + 192 len (32 * unknowndce15449[addr(_param1)].field_0) - floor32(unknowndce15449[addr(_param1)].field_0)]), 


# hash = 0xbb82aa5e
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def unknownbb82aa5e() payable: 
  return unknownbb82aa5eAddress


# hash = 0xbdcdc258
# getter = None
# const = None
# payable = True
def unknownbdcdc258(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 128
  if not uint8(markets[addr(_param1)].field_0):
      return 9
  if not uint8(markets[addr(_param1)][2][addr(_param2)].field_0):
      return 0
  mem[96] = 0
  mem[128] = 0
  mem[64] = (32 * unknowndce15449[addr(_param2)].field_0) + 576
  mem[544] = unknowndce15449[addr(_param2)].field_0
  if not unknowndce15449[addr(_param2)].field_0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_1067 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_1075 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_1067)
          mem[32] = 9
          mem[[94m_1075] = markets[addr([94m_1067)].field_256
          mem[288] = [94m_1075
          [94m_1077 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1077] = ext_call.return_data[96]
          mem[320] = [94m_1077
          mem[mem[64] + 4] = addr([94m_1067)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_1067)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_1087 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1087] = ext_call.return_data[0]
          mem[352] = [94m_1087
          [94m_1093 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1093] = 0
          [94m_1094 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1094] = 0
          [94m_1097 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1097] = 0
          if not markets[addr([94m_1067)].field_256:
              [94m_1104 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1104] = 0
              [94m_1106 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1106] = 0
              [94m_1120 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1120] = 0
              mem[384] = [94m_1120
              [94m_1128 = mem[96]
              [94m_1137 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1137] = 0
              [94m_1143 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1143] = 0
              [94m_1156 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1156] = 0
              if [94m_1128 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_1128 + (0 / 10^18)
              [94m_1178 = mem[128]
              [94m_1188 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1188] = 0
              [94m_1201 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1201] = 0
              if not ext_call.return_data[0]:
                  [94m_1240 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1240] = 0
                  if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_1178 + (0 / 10^18)
                  if addr([94m_1067) == _param1:
                      [94m_1298 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1298] = 0
                      [94m_1315 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1315] = 0
                      [94m_1404 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1404] = 0
                      if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1508 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1508] = 0
                      [94m_1534 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1534] = 0
                      if not ext_call.return_data[0]:
                          [94m_1678 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1678] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_1722 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1722] = 0
                      if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (0 / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_1250 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1250] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_1067) == _param1:
                      [94m_1314 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1314] = 0
                      [94m_1336 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1336] = 0
                      [94m_1418 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1418] = 0
                      if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1532 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1532] = 0
                      [94m_1569 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1569] = 0
                      if not ext_call.return_data[0]:
                          [94m_1720 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1720] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_1764 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1764] = 0
                      if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_1067)].field_256 / markets[addr([94m_1067)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_1105 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1105] = (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18
              [94m_1109 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1109] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18:
                  [94m_1121 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1121] = 0
                  mem[384] = [94m_1121
                  [94m_1133 = mem[96]
                  [94m_1141 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1141] = 0
                  [94m_1148 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1148] = 0
                  [94m_1157 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1157] = 0
                  if [94m_1133 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_1133 + (0 / 10^18)
                  [94m_1181 = mem[128]
                  [94m_1195 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1195] = 0
                  [94m_1209 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1209] = 0
                  if not ext_call.return_data[0]:
                      [94m_1247 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1247] = 0
                      if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1181 + (0 / 10^18)
                      if addr([94m_1067) == _param1:
                          [94m_1305 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1305] = 0
                          [94m_1333 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1333] = 0
                          [94m_1413 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1413] = 0
                          if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1517 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1517] = 0
                          [94m_1566 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1566] = 0
                          if not ext_call.return_data[0]:
                              [94m_1716 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1716] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_1752 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1752] = 0
                          if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1181 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_1256 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1256] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_1067) == _param1:
                          [94m_1324 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1324] = 0
                          [94m_1357 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1357] = 0
                          [94m_1425 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1425] = 0
                          if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1549 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1549] = 0
                          [94m_1600 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1600] = 0
                          if not ext_call.return_data[0]:
                              [94m_1750 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1750] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_1789 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1789] = 0
                          if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_1123 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1123] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_1123
                  [94m_1140 = mem[96]
                  [94m_1144 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1144] = 0
                  [94m_1154 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1154] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_1161 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1161] = 0
                      if [94m_1140 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_1140 + (0 / 10^18)
                      [94m_1191 = mem[128]
                      [94m_1205 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1205] = 0
                      [94m_1218 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1218] = 0
                      if not ext_call.return_data[0]:
                          [94m_1254 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1254] = 0
                          if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1191 + (0 / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1320 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1320] = 0
                              [94m_1355 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1355] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1423 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1423] = 0
                                  if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1541 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1541] = 0
                                  [94m_1598 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1598] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1748 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1748] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1782 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1782] = 0
                                  if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1440 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1440] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1581 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1581] = 0
                                  [94m_1637 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1637] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1781 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1781] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1824 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1824] = 0
                                  if [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1265 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1265] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1340 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1340] = 0
                              [94m_1383 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1383] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1439 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1439] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1580 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1580] = 0
                                  [94m_1636 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1636] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1780 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1780] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1822 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1822] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1462 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1462] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1622 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1622] = 0
                                  [94m_1683 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1683] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1821 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1821] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1863 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1863] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_1167 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1167] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_1140 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_1140 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_1204 = mem[128]
                      [94m_1214 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1214] = 0
                      [94m_1230 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1230] = 0
                      if not ext_call.return_data[0]:
                          [94m_1264 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1264] = 0
                          if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1204 + (0 / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1339 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1339] = 0
                              [94m_1382 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1382] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1438 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1438] = 0
                                  if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1577 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1577] = 0
                                  [94m_1635 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1635] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1779 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1779] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1819 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1819] = 0
                                  if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1460 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1460] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1621 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1621] = 0
                                  [94m_1680 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1680] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1818 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1818] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1860 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1860] = 0
                                  if [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1275 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1275] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1361 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1361] = 0
                              [94m_1405 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1405] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1459 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1459] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1620 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1620] = 0
                                  [94m_1679 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1679] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1817 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1817] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1858 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1858] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1478 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1478] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1667 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1667] = 0
                                  [94m_1724 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1724] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1857 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1857] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1888 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1888] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  else:
      mem[576] = addr(unknowndce15449[addr(_param2)].field_0)
      [94midx = 576
      [94ms = 0
      while (32 * unknowndce15449[addr(_param2)].field_0) + 544 > [94midx:
          mem[[94midx + 32] = addr(unknowndce15449[addr(_param2)][[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_3157 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_3165 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_3157)
          mem[32] = 9
          mem[[94m_3165] = markets[addr([94m_3157)].field_256
          mem[288] = [94m_3165
          [94m_3167 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3167] = ext_call.return_data[96]
          mem[320] = [94m_3167
          mem[mem[64] + 4] = addr([94m_3157)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_3157)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_3177 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3177] = ext_call.return_data[0]
          mem[352] = [94m_3177
          [94m_3183 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3183] = 0
          [94m_3184 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3184] = 0
          [94m_3187 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3187] = 0
          if not markets[addr([94m_3157)].field_256:
              [94m_3194 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3194] = 0
              [94m_3196 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3196] = 0
              [94m_3210 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3210] = 0
              mem[384] = [94m_3210
              [94m_3218 = mem[96]
              [94m_3227 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3227] = 0
              [94m_3233 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3233] = 0
              [94m_3246 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3246] = 0
              if [94m_3218 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_3218 + (0 / 10^18)
              [94m_3268 = mem[128]
              [94m_3278 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3278] = 0
              [94m_3291 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3291] = 0
              if not ext_call.return_data[0]:
                  [94m_3330 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3330] = 0
                  if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_3268 + (0 / 10^18)
                  if addr([94m_3157) == _param1:
                      [94m_3388 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3388] = 0
                      [94m_3405 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3405] = 0
                      [94m_3494 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3494] = 0
                      if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3598 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3598] = 0
                      [94m_3624 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3624] = 0
                      if not ext_call.return_data[0]:
                          [94m_3768 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3768] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_3812 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3812] = 0
                      if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (0 / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_3340 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3340] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_3157) == _param1:
                      [94m_3404 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3404] = 0
                      [94m_3426 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3426] = 0
                      [94m_3508 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3508] = 0
                      if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3622 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3622] = 0
                      [94m_3659 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3659] = 0
                      if not ext_call.return_data[0]:
                          [94m_3810 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3810] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_3854 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3854] = 0
                      if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_3157)].field_256 / markets[addr([94m_3157)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_3195 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3195] = (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18
              [94m_3199 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3199] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18:
                  [94m_3211 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3211] = 0
                  mem[384] = [94m_3211
                  [94m_3223 = mem[96]
                  [94m_3231 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3231] = 0
                  [94m_3238 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3238] = 0
                  [94m_3247 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3247] = 0
                  if [94m_3223 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_3223 + (0 / 10^18)
                  [94m_3271 = mem[128]
                  [94m_3285 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3285] = 0
                  [94m_3299 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3299] = 0
                  if not ext_call.return_data[0]:
                      [94m_3337 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3337] = 0
                      if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3271 + (0 / 10^18)
                      if addr([94m_3157) == _param1:
                          [94m_3395 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3395] = 0
                          [94m_3423 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3423] = 0
                          [94m_3503 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3503] = 0
                          if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3607 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3607] = 0
                          [94m_3656 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3656] = 0
                          if not ext_call.return_data[0]:
                              [94m_3806 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3806] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_3842 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3842] = 0
                          if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3271 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_3346 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3346] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_3157) == _param1:
                          [94m_3414 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3414] = 0
                          [94m_3447 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3447] = 0
                          [94m_3515 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3515] = 0
                          if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3639 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3639] = 0
                          [94m_3690 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3690] = 0
                          if not ext_call.return_data[0]:
                              [94m_3840 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3840] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_3879 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3879] = 0
                          if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_3213 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3213] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_3213
                  [94m_3230 = mem[96]
                  [94m_3234 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3234] = 0
                  [94m_3244 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3244] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_3251 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3251] = 0
                      if [94m_3230 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_3230 + (0 / 10^18)
                      [94m_3281 = mem[128]
                      [94m_3295 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3295] = 0
                      [94m_3308 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3308] = 0
                      if not ext_call.return_data[0]:
                          [94m_3344 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3344] = 0
                          if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3281 + (0 / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3410 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3410] = 0
                              [94m_3445 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3445] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3513 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3513] = 0
                                  if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3631 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3631] = 0
                                  [94m_3688 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3688] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3838 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3838] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3872 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3872] = 0
                                  if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3530 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3530] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3671 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3671] = 0
                                  [94m_3727 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3727] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3871 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3871] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3914 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3914] = 0
                                  if [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3355 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3355] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3430 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3430] = 0
                              [94m_3473 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3473] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3529 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3529] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3670 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3670] = 0
                                  [94m_3726 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3726] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3870 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3870] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3912 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3912] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3552 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3552] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3712 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3712] = 0
                                  [94m_3773 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3773] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3911 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3911] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3953 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3953] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_3257 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3257] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_3230 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_3230 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_3294 = mem[128]
                      [94m_3304 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3304] = 0
                      [94m_3320 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3320] = 0
                      if not ext_call.return_data[0]:
                          [94m_3354 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3354] = 0
                          if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3294 + (0 / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3429 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3429] = 0
                              [94m_3472 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3472] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3528 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3528] = 0
                                  if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3667 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3667] = 0
                                  [94m_3725 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3725] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3869 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3869] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3909 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3909] = 0
                                  if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3550 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3550] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3711 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3711] = 0
                                  [94m_3770 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3770] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3908 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3908] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3950 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3950] = 0
                                  if [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3365 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3365] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3451 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3451] = 0
                              [94m_3495 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3495] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3549 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3549] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3710 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3710] = 0
                                  [94m_3769 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3769] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3907 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3907] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3948 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3948] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3568 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3568] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3757 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3757] = 0
                                  [94m_3814 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3814] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3947 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3947] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3978 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3978] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  if mem[96] > mem[128]:
      return 0
  if not mem[128] - mem[96]:
      return 0
  return 4


# hash = 0xc2998238
# getter = None
# const = None
# payable = True
def unknownc2998238(array _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param1.length
  if _param1.length:
      mem[(32 * _param1.length) + 160 len 32 * _param1.length] = code.data[11889 len 32 * _param1.length]
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 9
      if not uint8(markets[mem[(32 * [94midx) + 140 len 20]].field_0):
          require [94midx < mem[(32 * _param1.length) + 128]
          mem[(32 * [94midx) + (32 * _param1.length) + 160] = 9
      else:
          mem[0] = caller
          mem[32] = sha3(mem[(32 * [94midx) + 140 len 20], 9) + 2
          if 1 == bool(uint8(markets[mem[(32 * [94midx) + 140 len 20]][2][caller].field_0)):
              require [94midx < mem[(32 * _param1.length) + 128]
              mem[(32 * [94midx) + (32 * _param1.length) + 160] = 0
          else:
              mem[0] = caller
              mem[32] = 8
              if unknowndce15449[caller].field_0 >= unknown94b2294b:
                  require [94midx < mem[(32 * _param1.length) + 128]
                  mem[(32 * [94midx) + (32 * _param1.length) + 160] = 17
              else:
                  uint8(markets[mem[(32 * [94midx) + 140 len 20]][2][caller].field_0) = 1
                  mem[32] = 8
                  unknowndce15449[caller].field_0++
                  mem[0] = sha3(caller, 8)
                  addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0) = mem[(32 * [94midx) + 140 len 20]
                  mem[(64 * _param1.length) + 160] = mem[(32 * [94midx) + 140 len 20]
                  mem[(64 * _param1.length) + 192] = caller
                  log 0x3ab23ab0: mem[(64 * _param1.length) + 160], caller
                  require [94midx < mem[(32 * _param1.length) + 128]
                  mem[(32 * [94midx) + (32 * _param1.length) + 160] = 0
      [94midx = [94midx + 1
      continue 
  mem[(64 * _param1.length) + 160] = 32
  mem[(64 * _param1.length) + 192] = mem[(32 * _param1.length) + 128]
  mem[(64 * _param1.length) + 224 len floor32(mem[(32 * _param1.length) + 128])] = mem[(32 * _param1.length) + 160 len floor32(mem[(32 * _param1.length) + 128])]
  return 32, mem[(64 * _param1.length) + 192 len (32 * mem[(32 * _param1.length) + 128]) + 32]


# hash = 0xc488847b
# getter = None
# const = None
# payable = True
def unknownc488847b(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(oracleAddress)
  static call oracleAddress.0xfc57d4df with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_code.size(oracleAddress)
      static call oracleAddress.0xfc57d4df with:
              gas gas_remaining wei
             args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              return 14, 0
          else:
              if ext_call.return_data[0]:
                  require ext_code.size(_param2)
                  static call _param2.0x182df0f5 with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if unknown4ada90af:
                          if ext_call.return_data[0] * unknown4ada90af / unknown4ada90af == ext_call.return_data[0]:
                              if (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 < 5 * 10^17:
                                  return 12, 0
                              else:
                                  if ext_call.return_data[0]:
                                      if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                                          if (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 < 5 * 10^17:
                                              return 12, 0
                                          else:
                                              if (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18:
                                                  if 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 == 10^18:
                                                      if (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                                          if 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                                              if _param3 * 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 == _param3:
                                                                  return 0, 
                                                                         _param3 * 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 10^18
                                                              else:
                                                                  return 12, 0
                                                          else:
                                                              return 0
                                                      else:
                                                          return 12, 0
                                                  else:
                                                      return 12, 0
                                              else:
                                                  if (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                                      if 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                                          if _param3 * 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 == _param3:
                                                              return 0, _param3 * 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 10^18
                                                          else:
                                                              return 12, 0
                                                      else:
                                                          return 0
                                                  else:
                                                      return 12, 0
                                      else:
                                          return 12, 0
                                  else:
                                      if (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18:
                                          if 10^18 * (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * unknown4ada90af) + 5 * 10^17 / 10^18 == 10^18:
                                              return 12, 0
                                          else:
                                              return 12, 0
                                      else:
                                          return 12, 0
                          else:
                              return 12, 0
                      else:
                          if ext_call.return_data[0]:
                              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                                  if (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 < 5 * 10^17:
                                      return 12, 0
                                  else:
                                      if (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                          if 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18:
                                              if _param3 * 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 == _param3:
                                                  return 0, _param3 * 0 / (ext_call.return_data[0] * ext_call.return_data[0]) + 5 * 10^17 / 10^18 / 10^18
                                              else:
                                                  return 12, 0
                                          else:
                                              return 0
                                      else:
                                          return 12, 0
                              else:
                                  return 12, 0
                          else:
                              return 12, 0
              else:
                  return 14, 0


# hash = 0xd02f7351
# getter = None
# const = None
# payable = True
def unknownd02f7351(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 160
  if not uint8(markets[addr(_param1)].field_0):
      return 9
  if not uint8(markets[addr(_param2)].field_0):
      return 9
  require ext_code.size(_param2)
  static call _param2.comptroller() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param1)
  static call _param1.comptroller() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] == addr(ext_call.return_data[0]):
      return 0
  return 2


# hash = 0xd9226ced
# getter = None
# const = None
# payable = True
def unknownd9226ced(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  if unknownbb82aa5eAddress != caller:
      if adminAddress != caller:
          if unknownbb82aa5eAddress != caller:
              log Failure(
                    uint256 error=1,
                    uint256 info=13,
                    uint256 detail=0)
              return 1
  else:
      if adminAddress != caller:
          if adminAddress != tx.origin:
              log Failure(
                    uint256 error=1,
                    uint256 info=13,
                    uint256 detail=0)
              return 1
  unknown94b2294b = _param1
  log 0x7093cf1e: unknown94b2294b, _param1
  return 0


# hash = 0xda3d454c
# getter = None
# const = None
# payable = True
def unknownda3d454c(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  if not uint8(markets[addr(_param1)].field_0):
      return 9
  if not uint8(markets[addr(_param1)].field_8):
      return 10
  if not uint8(markets[addr(_param1)][2][addr(_param2)].field_0):
      return 8
  require ext_code.size(oracleAddress)
  static call oracleAddress.0xfc57d4df with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 14
  mem[96] = 0
  mem[128] = 0
  mem[64] = (32 * unknowndce15449[addr(_param2)].field_0) + 576
  mem[544] = unknowndce15449[addr(_param2)].field_0
  if not unknowndce15449[addr(_param2)].field_0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_1064 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_1072 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_1064)
          mem[32] = 9
          mem[[94m_1072] = markets[addr([94m_1064)].field_256
          mem[288] = [94m_1072
          [94m_1074 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1074] = ext_call.return_data[96]
          mem[320] = [94m_1074
          mem[mem[64] + 4] = addr([94m_1064)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_1064)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_1086 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1086] = ext_call.return_data[0]
          mem[352] = [94m_1086
          [94m_1090 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1090] = 0
          [94m_1093 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1093] = 0
          [94m_1094 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1094] = 0
          if not markets[addr([94m_1064)].field_256:
              [94m_1101 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1101] = 0
              [94m_1105 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1105] = 0
              [94m_1117 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1117] = 0
              mem[384] = [94m_1117
              [94m_1127 = mem[96]
              [94m_1134 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1134] = 0
              [94m_1142 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1142] = 0
              [94m_1153 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1153] = 0
              if [94m_1127 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_1127 + (0 / 10^18)
              [94m_1175 = mem[128]
              [94m_1185 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1185] = 0
              [94m_1200 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1200] = 0
              if not ext_call.return_data[0]:
                  [94m_1243 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1243] = 0
                  if [94m_1175 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_1175 + (0 / 10^18)
                  if addr([94m_1064) == _param1:
                      [94m_1295 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1295] = 0
                      [94m_1314 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1314] = 0
                      [94m_1409 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1409] = 0
                      if [94m_1175 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1505 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1505] = 0
                      [94m_1533 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1533] = 0
                      if not ext_call.return_data[0]:
                          [94m_1703 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1703] = 0
                          if [94m_1175 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1175 + (0 / 10^18)
                      else:
                          if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                              return 12
                          [94m_1741 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1741] = _param3 * ext_call.return_data[0]
                          if [94m_1175 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1175 + (_param3 * ext_call.return_data[0] / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_1249 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1249] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_1064) == _param1:
                      [94m_1311 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1311] = 0
                      [94m_1341 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1341] = 0
                      [94m_1417 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1417] = 0
                      if [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1529 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1529] = 0
                      [94m_1576 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1576] = 0
                      if not ext_call.return_data[0]:
                          [94m_1739 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1739] = 0
                          if [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                      else:
                          if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                              return 12
                          [94m_1771 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1771] = _param3 * ext_call.return_data[0]
                          if [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1175 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_1064)].field_256 / markets[addr([94m_1064)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_1102 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1102] = (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18
              [94m_1108 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1108] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18:
                  [94m_1118 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1118] = 0
                  mem[384] = [94m_1118
                  [94m_1130 = mem[96]
                  [94m_1138 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1138] = 0
                  [94m_1147 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1147] = 0
                  [94m_1154 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1154] = 0
                  if [94m_1130 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_1130 + (0 / 10^18)
                  [94m_1178 = mem[128]
                  [94m_1192 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1192] = 0
                  [94m_1210 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1210] = 0
                  if not ext_call.return_data[0]:
                      [94m_1246 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1246] = 0
                      if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (0 / 10^18)
                      if addr([94m_1064) == _param1:
                          [94m_1302 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1302] = 0
                          [94m_1338 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1338] = 0
                          [94m_1414 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1414] = 0
                          if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1514 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1514] = 0
                          [94m_1567 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1567] = 0
                          if not ext_call.return_data[0]:
                              [94m_1735 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1735] = 0
                              if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              mem[128] = [94m_1178 + (0 / 10^18)
                          else:
                              if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                  return 12
                              [94m_1759 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1759] = _param3 * ext_call.return_data[0]
                              if [94m_1178 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                  return 12
                              mem[128] = [94m_1178 + (_param3 * ext_call.return_data[0] / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_1253 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1253] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_1064) == _param1:
                          [94m_1323 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1323] = 0
                          [94m_1368 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1368] = 0
                          [94m_1422 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1422] = 0
                          if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1548 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1548] = 0
                          [94m_1613 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1613] = 0
                          if not ext_call.return_data[0]:
                              [94m_1757 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1757] = 0
                              if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                          else:
                              if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                  return 12
                              [94m_1788 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1788] = _param3 * ext_call.return_data[0]
                              if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                  return 12
                              mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_1122 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1122] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_1122
                  [94m_1137 = mem[96]
                  [94m_1145 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1145] = 0
                  [94m_1151 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1151] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_1158 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1158] = 0
                      if [94m_1137 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_1137 + (0 / 10^18)
                      [94m_1188 = mem[128]
                      [94m_1204 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1204] = 0
                      [94m_1223 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1223] = 0
                      if not ext_call.return_data[0]:
                          [94m_1251 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1251] = 0
                          if [94m_1188 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1188 + (0 / 10^18)
                          if addr([94m_1064) == _param1:
                              [94m_1319 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1319] = 0
                              [94m_1366 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1366] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1420 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1420] = 0
                                  if [94m_1188 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1540 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1540] = 0
                                  [94m_1607 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1607] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1755 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1755] = 0
                                      if [94m_1188 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1781 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1781] = _param3 * ext_call.return_data[0]
                                      if [94m_1188 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_1437 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1437] = 0
                                  if [94m_1188 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1588 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1588] = 0
                                  [94m_1660 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1660] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1780 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1780] = 0
                                      if [94m_1188 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1821 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1821] = _param3 * ext_call.return_data[0]
                                      if [94m_1188 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (_param3 * ext_call.return_data[0] / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1262 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1262] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1064) == _param1:
                              [94m_1345 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1345] = 0
                              [94m_1394 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1394] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1436 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1436] = 0
                                  if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1587 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1587] = 0
                                  [94m_1659 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1659] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1779 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1779] = 0
                                      if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1819 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1819] = _param3 * ext_call.return_data[0]
                                      if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_1459 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1459] = 0
                                  if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1641 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1641] = 0
                                  [94m_1710 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1710] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1818 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1818] = 0
                                      if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1860 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1860] = _param3 * ext_call.return_data[0]
                                      if [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1188 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_1164 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1164] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_1137 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_1137 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_1203 = mem[128]
                      [94m_1217 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1217] = 0
                      [94m_1235 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1235] = 0
                      if not ext_call.return_data[0]:
                          [94m_1261 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1261] = 0
                          if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1203 + (0 / 10^18)
                          if addr([94m_1064) == _param1:
                              [94m_1344 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1344] = 0
                              [94m_1393 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1393] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1435 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1435] = 0
                                  if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1584 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1584] = 0
                                  [94m_1656 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1656] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1778 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1778] = 0
                                      if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1816 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1816] = _param3 * ext_call.return_data[0]
                                      if [94m_1203 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_1457 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1457] = 0
                                  if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1640 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1640] = 0
                                  [94m_1707 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1707] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1815 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1815] = 0
                                      if [94m_1203 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1857 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1857] = _param3 * ext_call.return_data[0]
                                      if [94m_1203 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (_param3 * ext_call.return_data[0] / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1272 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1272] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1064) == _param1:
                              [94m_1372 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1372] = 0
                              [94m_1410 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1410] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1456 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1456] = 0
                                  if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1639 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1639] = 0
                                  [94m_1706 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1706] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1814 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1814] = 0
                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1855 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1855] = _param3 * ext_call.return_data[0]
                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1064)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_1475 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1475] = 0
                                  if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1692 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1692] = 0
                                  [94m_1743 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1743] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1854 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1854] = 0
                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_1885 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1885] = _param3 * ext_call.return_data[0]
                                      if [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_1203 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  else:
      mem[576] = addr(unknowndce15449[addr(_param2)].field_0)
      [94midx = 576
      [94ms = 0
      while (32 * unknowndce15449[addr(_param2)].field_0) + 544 > [94midx:
          mem[[94midx + 32] = addr(unknowndce15449[addr(_param2)][[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_3154 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_3162 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_3154)
          mem[32] = 9
          mem[[94m_3162] = markets[addr([94m_3154)].field_256
          mem[288] = [94m_3162
          [94m_3164 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3164] = ext_call.return_data[96]
          mem[320] = [94m_3164
          mem[mem[64] + 4] = addr([94m_3154)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_3154)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_3176 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3176] = ext_call.return_data[0]
          mem[352] = [94m_3176
          [94m_3180 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3180] = 0
          [94m_3183 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3183] = 0
          [94m_3184 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3184] = 0
          if not markets[addr([94m_3154)].field_256:
              [94m_3191 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3191] = 0
              [94m_3195 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3195] = 0
              [94m_3207 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3207] = 0
              mem[384] = [94m_3207
              [94m_3217 = mem[96]
              [94m_3224 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3224] = 0
              [94m_3232 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3232] = 0
              [94m_3243 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3243] = 0
              if [94m_3217 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_3217 + (0 / 10^18)
              [94m_3265 = mem[128]
              [94m_3275 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3275] = 0
              [94m_3290 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3290] = 0
              if not ext_call.return_data[0]:
                  [94m_3333 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3333] = 0
                  if [94m_3265 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_3265 + (0 / 10^18)
                  if addr([94m_3154) == _param1:
                      [94m_3385 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3385] = 0
                      [94m_3404 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3404] = 0
                      [94m_3499 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3499] = 0
                      if [94m_3265 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3595 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3595] = 0
                      [94m_3623 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3623] = 0
                      if not ext_call.return_data[0]:
                          [94m_3793 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3793] = 0
                          if [94m_3265 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3265 + (0 / 10^18)
                      else:
                          if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                              return 12
                          [94m_3831 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3831] = _param3 * ext_call.return_data[0]
                          if [94m_3265 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3265 + (_param3 * ext_call.return_data[0] / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_3339 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3339] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_3154) == _param1:
                      [94m_3401 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3401] = 0
                      [94m_3431 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3431] = 0
                      [94m_3507 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3507] = 0
                      if [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3619 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3619] = 0
                      [94m_3666 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3666] = 0
                      if not ext_call.return_data[0]:
                          [94m_3829 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3829] = 0
                          if [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                      else:
                          if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                              return 12
                          [94m_3861 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3861] = _param3 * ext_call.return_data[0]
                          if [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3265 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_3154)].field_256 / markets[addr([94m_3154)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_3192 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3192] = (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18
              [94m_3198 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3198] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18:
                  [94m_3208 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3208] = 0
                  mem[384] = [94m_3208
                  [94m_3220 = mem[96]
                  [94m_3228 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3228] = 0
                  [94m_3237 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3237] = 0
                  [94m_3244 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3244] = 0
                  if [94m_3220 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_3220 + (0 / 10^18)
                  [94m_3268 = mem[128]
                  [94m_3282 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3282] = 0
                  [94m_3300 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3300] = 0
                  if not ext_call.return_data[0]:
                      [94m_3336 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3336] = 0
                      if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (0 / 10^18)
                      if addr([94m_3154) == _param1:
                          [94m_3392 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3392] = 0
                          [94m_3428 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3428] = 0
                          [94m_3504 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3504] = 0
                          if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3604 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3604] = 0
                          [94m_3657 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3657] = 0
                          if not ext_call.return_data[0]:
                              [94m_3825 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3825] = 0
                              if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              mem[128] = [94m_3268 + (0 / 10^18)
                          else:
                              if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                  return 12
                              [94m_3849 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3849] = _param3 * ext_call.return_data[0]
                              if [94m_3268 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                  return 12
                              mem[128] = [94m_3268 + (_param3 * ext_call.return_data[0] / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_3343 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3343] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_3154) == _param1:
                          [94m_3413 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3413] = 0
                          [94m_3458 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3458] = 0
                          [94m_3512 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3512] = 0
                          if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3638 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3638] = 0
                          [94m_3703 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3703] = 0
                          if not ext_call.return_data[0]:
                              [94m_3847 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3847] = 0
                              if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  return 12
                              mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                          else:
                              if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                  return 12
                              [94m_3878 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3878] = _param3 * ext_call.return_data[0]
                              if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                  return 12
                              mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_3212 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3212] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_3212
                  [94m_3227 = mem[96]
                  [94m_3235 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3235] = 0
                  [94m_3241 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3241] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_3248 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3248] = 0
                      if [94m_3227 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_3227 + (0 / 10^18)
                      [94m_3278 = mem[128]
                      [94m_3294 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3294] = 0
                      [94m_3313 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3313] = 0
                      if not ext_call.return_data[0]:
                          [94m_3341 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3341] = 0
                          if [94m_3278 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3278 + (0 / 10^18)
                          if addr([94m_3154) == _param1:
                              [94m_3409 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3409] = 0
                              [94m_3456 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3456] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3510 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3510] = 0
                                  if [94m_3278 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3630 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3630] = 0
                                  [94m_3697 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3697] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3845 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3845] = 0
                                      if [94m_3278 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3871 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3871] = _param3 * ext_call.return_data[0]
                                      if [94m_3278 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_3527 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3527] = 0
                                  if [94m_3278 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3678 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3678] = 0
                                  [94m_3750 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3750] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3870 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3870] = 0
                                      if [94m_3278 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3911 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3911] = _param3 * ext_call.return_data[0]
                                      if [94m_3278 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (_param3 * ext_call.return_data[0] / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3352 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3352] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3154) == _param1:
                              [94m_3435 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3435] = 0
                              [94m_3484 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3484] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3526 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3526] = 0
                                  if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3677 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3677] = 0
                                  [94m_3749 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3749] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3869 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3869] = 0
                                      if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3909 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3909] = _param3 * ext_call.return_data[0]
                                      if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_3549 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3549] = 0
                                  if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3731 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3731] = 0
                                  [94m_3800 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3800] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3908 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3908] = 0
                                      if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3950 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3950] = _param3 * ext_call.return_data[0]
                                      if [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3278 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_3254 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3254] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_3227 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_3227 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_3293 = mem[128]
                      [94m_3307 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3307] = 0
                      [94m_3325 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3325] = 0
                      if not ext_call.return_data[0]:
                          [94m_3351 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3351] = 0
                          if [94m_3293 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3293 + (0 / 10^18)
                          if addr([94m_3154) == _param1:
                              [94m_3434 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3434] = 0
                              [94m_3483 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3483] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3525 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3525] = 0
                                  if [94m_3293 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3674 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3674] = 0
                                  [94m_3746 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3746] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3868 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3868] = 0
                                      if [94m_3293 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3906 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3906] = _param3 * ext_call.return_data[0]
                                      if [94m_3293 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_3547 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3547] = 0
                                  if [94m_3293 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3730 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3730] = 0
                                  [94m_3797 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3797] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3905 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3905] = 0
                                      if [94m_3293 + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3947 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3947] = _param3 * ext_call.return_data[0]
                                      if [94m_3293 + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (_param3 * ext_call.return_data[0] / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3362 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3362] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3154) == _param1:
                              [94m_3462 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3462] = 0
                              [94m_3500 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3500] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3546 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3546] = 0
                                  if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3729 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3729] = 0
                                  [94m_3796 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3796] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3904 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3904] = 0
                                      if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3945 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3945] = _param3 * ext_call.return_data[0]
                                      if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
                              else:
                                  if 0 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3154)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      return 12
                                  [94m_3565 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3565] = 0
                                  if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3782 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3782] = 0
                                  [94m_3833 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3833] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3944 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3944] = 0
                                      if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if _param3 * ext_call.return_data[0] / ext_call.return_data[0] != _param3:
                                          return 12
                                      [94m_3975 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3975] = _param3 * ext_call.return_data[0]
                                      if [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18) < _param3 * ext_call.return_data[0] / 10^18:
                                          return 12
                                      mem[128] = [94m_3293 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * ext_call.return_data[0] / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  if mem[96] > mem[128]:
      return 0
  if not mem[128] - mem[96]:
      return 0
  return 4


# hash = 0xdce15449
# getter = ['storage', 160, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 8]]], ['cd', 36]]]
# const = None
# payable = True
def unknowndce15449(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require _param2 < unknowndce15449[_param1].field_0
  return addr(unknowndce15449[_param1][_param2].field_0)


# hash = 0xdcfbc0c7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def unknowndcfbc0c7() payable: 
  return unknowndcfbc0c7Address


# hash = 0xe4028eee
# getter = None
# const = None
# payable = True
def unknowne4028eee(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  if adminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=6,
            uint256 detail=0)
      return 1
  if not uint8(markets[addr(_param1)].field_0):
      log Failure(
            uint256 error=9,
            uint256 info=7,
            uint256 detail=0)
      return 9
  if 25 * 10^13 * 3600 < _param2:
      log Failure(
            uint256 error=6,
            uint256 info=8,
            uint256 detail=0)
      return 6
  if _param2:
      require ext_code.size(oracleAddress)
      static call oracleAddress.0xfc57d4df with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          log Failure(
                uint256 error=14,
                uint256 info=9,
                uint256 detail=0)
          return 14
  markets[addr(_param1)].field_256 = _param2
  log 0x70483e65: addr(_param1), markets[addr(_param1)].field_256, _param2
  return 0


# hash = 0xe8755446
# getter = ['storage', 256, 0, 5]
# const = None
# payable = True
def unknowne8755446() payable: 
  return unknowne8755446


# hash = 0xeabe7d91
# getter = None
# const = None
# payable = True
def unknowneabe7d91(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  if not uint8(markets[addr(_param1)].field_0):
      return 9
  if not uint8(markets[addr(_param1)][2][addr(_param2)].field_0):
      return 0
  mem[96] = 0
  mem[128] = 0
  mem[64] = (32 * unknowndce15449[addr(_param2)].field_0) + 576
  mem[544] = unknowndce15449[addr(_param2)].field_0
  if not unknowndce15449[addr(_param2)].field_0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_1067 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_1075 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_1067)
          mem[32] = 9
          mem[[94m_1075] = markets[addr([94m_1067)].field_256
          mem[288] = [94m_1075
          [94m_1077 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1077] = ext_call.return_data[96]
          mem[320] = [94m_1077
          mem[mem[64] + 4] = addr([94m_1067)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_1067)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_1087 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1087] = ext_call.return_data[0]
          mem[352] = [94m_1087
          [94m_1093 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1093] = 0
          [94m_1094 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1094] = 0
          [94m_1097 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_1097] = 0
          if not markets[addr([94m_1067)].field_256:
              [94m_1104 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1104] = 0
              [94m_1106 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1106] = 0
              [94m_1120 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1120] = 0
              mem[384] = [94m_1120
              [94m_1128 = mem[96]
              [94m_1137 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1137] = 0
              [94m_1143 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1143] = 0
              [94m_1156 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1156] = 0
              if [94m_1128 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_1128 + (0 / 10^18)
              [94m_1178 = mem[128]
              [94m_1188 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1188] = 0
              [94m_1201 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1201] = 0
              if not ext_call.return_data[0]:
                  [94m_1240 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1240] = 0
                  if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_1178 + (0 / 10^18)
                  if addr([94m_1067) == _param1:
                      [94m_1298 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1298] = 0
                      [94m_1315 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1315] = 0
                      [94m_1404 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1404] = 0
                      if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1508 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1508] = 0
                      [94m_1534 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1534] = 0
                      if not ext_call.return_data[0]:
                          [94m_1678 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1678] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_1722 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1722] = 0
                      if [94m_1178 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (0 / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_1250 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1250] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_1067) == _param1:
                      [94m_1314 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1314] = 0
                      [94m_1336 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1336] = 0
                      [94m_1418 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1418] = 0
                      if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_1532 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1532] = 0
                      [94m_1569 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1569] = 0
                      if not ext_call.return_data[0]:
                          [94m_1720 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1720] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_1764 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1764] = 0
                      if [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1178 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_1067)].field_256 / markets[addr([94m_1067)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_1105 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1105] = (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18
              [94m_1109 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1109] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18:
                  [94m_1121 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1121] = 0
                  mem[384] = [94m_1121
                  [94m_1133 = mem[96]
                  [94m_1141 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1141] = 0
                  [94m_1148 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1148] = 0
                  [94m_1157 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1157] = 0
                  if [94m_1133 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_1133 + (0 / 10^18)
                  [94m_1181 = mem[128]
                  [94m_1195 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1195] = 0
                  [94m_1209 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1209] = 0
                  if not ext_call.return_data[0]:
                      [94m_1247 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1247] = 0
                      if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_1181 + (0 / 10^18)
                      if addr([94m_1067) == _param1:
                          [94m_1305 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1305] = 0
                          [94m_1333 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1333] = 0
                          [94m_1413 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1413] = 0
                          if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1517 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1517] = 0
                          [94m_1566 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1566] = 0
                          if not ext_call.return_data[0]:
                              [94m_1716 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1716] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_1752 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1752] = 0
                          if [94m_1181 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1181 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_1256 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1256] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_1067) == _param1:
                          [94m_1324 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1324] = 0
                          [94m_1357 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1357] = 0
                          [94m_1425 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1425] = 0
                          if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_1549 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1549] = 0
                          [94m_1600 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1600] = 0
                          if not ext_call.return_data[0]:
                              [94m_1750 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1750] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_1789 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1789] = 0
                          if [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1181 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_1123 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1123] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_1123
                  [94m_1140 = mem[96]
                  [94m_1144 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1144] = 0
                  [94m_1154 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1154] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_1161 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1161] = 0
                      if [94m_1140 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_1140 + (0 / 10^18)
                      [94m_1191 = mem[128]
                      [94m_1205 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1205] = 0
                      [94m_1218 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1218] = 0
                      if not ext_call.return_data[0]:
                          [94m_1254 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1254] = 0
                          if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1191 + (0 / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1320 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1320] = 0
                              [94m_1355 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1355] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1423 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1423] = 0
                                  if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1541 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1541] = 0
                                  [94m_1598 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1598] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1748 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1748] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1782 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1782] = 0
                                  if [94m_1191 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1440 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1440] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1581 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1581] = 0
                                  [94m_1637 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1637] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1781 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1781] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1824 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1824] = 0
                                  if [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1265 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1265] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1340 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1340] = 0
                              [94m_1383 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1383] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1439 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1439] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1580 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1580] = 0
                                  [94m_1636 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1636] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1780 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1780] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1822 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1822] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1462 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1462] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1622 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1622] = 0
                                  [94m_1683 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1683] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1821 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1821] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1863 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1863] = 0
                                  if [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1191 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_1167 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1167] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_1140 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_1140 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_1204 = mem[128]
                      [94m_1214 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1214] = 0
                      [94m_1230 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1230] = 0
                      if not ext_call.return_data[0]:
                          [94m_1264 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1264] = 0
                          if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_1204 + (0 / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1339 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1339] = 0
                              [94m_1382 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1382] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1438 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1438] = 0
                                  if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1577 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1577] = 0
                                  [94m_1635 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1635] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1779 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1779] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1819 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1819] = 0
                                  if [94m_1204 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1460 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1460] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1621 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1621] = 0
                                  [94m_1680 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1680] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1818 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1818] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1860 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1860] = 0
                                  if [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_1275 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1275] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1067) == _param1:
                              [94m_1361 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1361] = 0
                              [94m_1405 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1405] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_1459 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1459] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_1620 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1620] = 0
                                  [94m_1679 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1679] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1817 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1817] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1858 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1858] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_1478 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1478] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_1667 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1667] = 0
                                  [94m_1724 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1724] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_1857 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1857] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_1888 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1888] = 0
                                  if [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_1204 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1067)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  else:
      mem[576] = addr(unknowndce15449[addr(_param2)].field_0)
      [94midx = 576
      [94ms = 0
      while (32 * unknowndce15449[addr(_param2)].field_0) + 544 > [94midx:
          mem[[94midx + 32] = addr(unknowndce15449[addr(_param2)][[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = 0
      while [94midx < unknowndce15449[addr(_param2)].field_0:
          require [94midx < mem[544]
          [94m_3157 = mem[(32 * [94midx) + 576]
          require ext_code.size(mem[(32 * [94midx) + 588 len 20])
          static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                  gas gas_remaining wei
                 args addr(_param2)
          mem[mem[64] len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mem[224] = ext_call.return_data[96]
          mem[192] = ext_call.return_data[64]
          mem[160] = ext_call.return_data[32]
          if ext_call.return_data[0]:
              return 16
          [94m_3165 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_3157)
          mem[32] = 9
          mem[[94m_3165] = markets[addr([94m_3157)].field_256
          mem[288] = [94m_3165
          [94m_3167 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3167] = ext_call.return_data[96]
          mem[320] = [94m_3167
          mem[mem[64] + 4] = addr([94m_3157)
          require ext_code.size(oracleAddress)
          static call oracleAddress.0xfc57d4df with:
                  gas gas_remaining wei
                 args addr([94m_3157)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[256] = ext_call.return_data[0]
          if not ext_call.return_data[0]:
              return 14
          [94m_3177 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3177] = ext_call.return_data[0]
          mem[352] = [94m_3177
          [94m_3183 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3183] = 0
          [94m_3184 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3184] = 0
          [94m_3187 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_3187] = 0
          if not markets[addr([94m_3157)].field_256:
              [94m_3194 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3194] = 0
              [94m_3196 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3196] = 0
              [94m_3210 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3210] = 0
              mem[384] = [94m_3210
              [94m_3218 = mem[96]
              [94m_3227 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3227] = 0
              [94m_3233 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3233] = 0
              [94m_3246 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3246] = 0
              if [94m_3218 + (0 / 10^18) < 0 / 10^18:
                  return 12
              mem[96] = [94m_3218 + (0 / 10^18)
              [94m_3268 = mem[128]
              [94m_3278 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3278] = 0
              [94m_3291 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3291] = 0
              if not ext_call.return_data[0]:
                  [94m_3330 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3330] = 0
                  if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[128] = [94m_3268 + (0 / 10^18)
                  if addr([94m_3157) == _param1:
                      [94m_3388 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3388] = 0
                      [94m_3405 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3405] = 0
                      [94m_3494 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3494] = 0
                      if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3598 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3598] = 0
                      [94m_3624 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3624] = 0
                      if not ext_call.return_data[0]:
                          [94m_3768 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3768] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_3812 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3812] = 0
                      if [94m_3268 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (0 / 10^18)
              else:
                  if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                      return 12
                  [94m_3340 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3340] = ext_call.return_data[64] * ext_call.return_data[0]
                  if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                      return 12
                  mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                  if addr([94m_3157) == _param1:
                      [94m_3404 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3404] = 0
                      [94m_3426 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3426] = 0
                      [94m_3508 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3508] = 0
                      if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      [94m_3622 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3622] = 0
                      [94m_3659 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3659] = 0
                      if not ext_call.return_data[0]:
                          [94m_3810 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3810] = 0
                      else:
                          if 0 / ext_call.return_data[0]:
                              return 12
                          [94m_3854 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3854] = 0
                      if [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3268 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
          else:
              if ext_call.return_data[96] * markets[addr([94m_3157)].field_256 / markets[addr([94m_3157)].field_256 != ext_call.return_data[96]:
                  return 12
              if (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 < 5 * 10^17:
                  return 12
              [94m_3195 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3195] = (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18
              [94m_3199 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_3199] = 0
              if not (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18:
                  [94m_3211 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3211] = 0
                  mem[384] = [94m_3211
                  [94m_3223 = mem[96]
                  [94m_3231 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3231] = 0
                  [94m_3238 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3238] = 0
                  [94m_3247 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3247] = 0
                  if [94m_3223 + (0 / 10^18) < 0 / 10^18:
                      return 12
                  mem[96] = [94m_3223 + (0 / 10^18)
                  [94m_3271 = mem[128]
                  [94m_3285 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3285] = 0
                  [94m_3299 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3299] = 0
                  if not ext_call.return_data[0]:
                      [94m_3337 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3337] = 0
                      if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[128] = [94m_3271 + (0 / 10^18)
                      if addr([94m_3157) == _param1:
                          [94m_3395 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3395] = 0
                          [94m_3423 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3423] = 0
                          [94m_3503 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3503] = 0
                          if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3607 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3607] = 0
                          [94m_3656 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3656] = 0
                          if not ext_call.return_data[0]:
                              [94m_3806 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3806] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_3842 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3842] = 0
                          if [94m_3271 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3271 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          return 12
                      [94m_3346 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3346] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          return 12
                      mem[128] = [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_3157) == _param1:
                          [94m_3414 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3414] = 0
                          [94m_3447 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3447] = 0
                          [94m_3515 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3515] = 0
                          if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          [94m_3639 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3639] = 0
                          [94m_3690 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3690] = 0
                          if not ext_call.return_data[0]:
                              [94m_3840 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3840] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  return 12
                              [94m_3879 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3879] = 0
                          if [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3271 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                      return 12
                  if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                      return 12
                  [94m_3213 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3213] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                  mem[384] = [94m_3213
                  [94m_3230 = mem[96]
                  [94m_3234 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3234] = 0
                  [94m_3244 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_3244] = 0
                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                      [94m_3251 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3251] = 0
                      if [94m_3230 + (0 / 10^18) < 0 / 10^18:
                          return 12
                      mem[96] = [94m_3230 + (0 / 10^18)
                      [94m_3281 = mem[128]
                      [94m_3295 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3295] = 0
                      [94m_3308 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3308] = 0
                      if not ext_call.return_data[0]:
                          [94m_3344 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3344] = 0
                          if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3281 + (0 / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3410 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3410] = 0
                              [94m_3445 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3445] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3513 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3513] = 0
                                  if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3631 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3631] = 0
                                  [94m_3688 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3688] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3838 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3838] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3872 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3872] = 0
                                  if [94m_3281 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3530 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3530] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3671 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3671] = 0
                                  [94m_3727 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3727] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3871 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3871] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3914 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3914] = 0
                                  if [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3355 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3355] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3430 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3430] = 0
                              [94m_3473 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3473] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3529 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3529] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3670 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3670] = 0
                                  [94m_3726 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3726] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3870 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3870] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3912 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3912] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3552 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3552] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3712 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3712] = 0
                                  [94m_3773 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3773] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3911 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3911] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3953 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3953] = 0
                                  if [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3281 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                          return 12
                      [94m_3257 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3257] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      if [94m_3230 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                          return 12
                      mem[96] = [94m_3230 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                      [94m_3294 = mem[128]
                      [94m_3304 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3304] = 0
                      [94m_3320 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_3320] = 0
                      if not ext_call.return_data[0]:
                          [94m_3354 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3354] = 0
                          if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                              return 12
                          mem[128] = [94m_3294 + (0 / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3429 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3429] = 0
                              [94m_3472 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3472] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3528 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3528] = 0
                                  if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3667 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3667] = 0
                                  [94m_3725 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3725] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3869 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3869] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3909 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3909] = 0
                                  if [94m_3294 + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3550 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3550] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3711 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3711] = 0
                                  [94m_3770 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3770] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3908 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3908] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3950 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3950] = 0
                                  if [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              return 12
                          [94m_3365 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_3365] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              return 12
                          mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_3157) == _param1:
                              [94m_3451 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3451] = 0
                              [94m_3495 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_3495] = 0
                              if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                  [94m_3549 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3549] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  [94m_3710 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3710] = 0
                                  [94m_3769 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3769] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3907 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3907] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3948 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3948] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                              else:
                                  if _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != _param3:
                                      return 12
                                  [94m_3568 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3568] = _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < _param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                      return 12
                                  [94m_3757 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3757] = 0
                                  [94m_3814 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_3814] = 0
                                  if not ext_call.return_data[0]:
                                      [94m_3947 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3947] = 0
                                  else:
                                      if 0 / ext_call.return_data[0]:
                                          return 12
                                      [94m_3978 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_3978] = 0
                                  if [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                      return 12
                                  mem[128] = [94m_3294 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (_param3 * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_3157)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
  if mem[96] > mem[128]:
      return 0
  if not mem[128] - mem[96]:
      return 0
  return 4


# hash = 0xede4edd0
# getter = None
# const = None
# payable = True
def unknownede4edd0(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(_param1)
  static call _param1.0xc37f68e2 with:
          gas gas_remaining wei
         args caller
  mem[96 len 128] = ext_call.return_data[0 len 128]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 128
  if ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  37,
                  0xfe657869744d61726b65743a206765744163636f756e74536e617073686f74206661696c65,
                  ext_call.return_data[105 len 23],
                  mem[224 len 4]
  if ext_call.return_data[64]:
      log Failure(
            uint256 error=13,
            uint256 info=2,
            uint256 detail=0)
      return 13
  if not uint8(markets[addr(_param1)].field_0):
      log Failure(
            uint256 error=15,
            uint256 info=3,
            uint256 detail=9)
      return 15
  if not uint8(markets[addr(_param1)][2][caller].field_0):
      if uint8(markets[addr(_param1)][2][caller].field_0):
          uint8(markets[addr(_param1)][2][caller].field_0) = 0
          if unknowndce15449[caller].field_0:
              mem[128] = addr(unknowndce15449[caller].field_0)
              [94midx = 128
              [94ms = 0
              while (32 * unknowndce15449[caller].field_0) + 96 > [94midx:
                  mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  continue 
          [94midx = 0
          while [94midx < unknowndce15449[caller].field_0:
              require [94midx < unknowndce15449[caller].field_0
              if mem[(32 * [94midx) + 140 len 20] != _param1:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < unknowndce15449[caller].field_0
              require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
              require [94midx < unknowndce15449[caller].field_0
              addr(unknowndce15449[caller][[94midx].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
              unknowndce15449[caller].field_0--
              if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
                  [94midx = unknowndce15449[caller].field_0 + sha3(sha3(caller, 8)) - 1
                  while sha3(sha3(caller, 8)) + unknowndce15449[caller].field_0 > [94midx:
                      stor[[94midx] = 0
                      [94midx = [94midx + 1
                      continue 
              log 0xe699a64c: addr(_param1), caller
              return 0
          require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
          require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
          require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
          addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
          unknowndce15449[caller].field_0--
          if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
              [94midx = unknowndce15449[caller].field_0 - 1
              while unknowndce15449[caller].field_0 > [94midx:
                  unknowndce15449[caller][[94midx].field_0 = 0
                  [94midx = [94midx + 1
                  continue 
              return 0
          else:
              return 0
  else:
      mem[96] = 0
      mem[128] = 0
      mem[160] = 0
      mem[192] = 0
      mem[224] = 0
      mem[256] = 0
      mem[416] = 0
      mem[288] = 416
      mem[448] = 0
      mem[320] = 448
      mem[480] = 0
      mem[352] = 480
      mem[512] = 0
      mem[384] = 512
      mem[64] = (32 * unknowndce15449[caller].field_0) + 576
      mem[544] = unknowndce15449[caller].field_0
      if not unknowndce15449[caller].field_0:
          [94midx = 0
          [94ms = 0
          while [94midx < unknowndce15449[caller].field_0:
              require [94midx < mem[544]
              [94m_1275 = mem[(32 * [94midx) + 576]
              require ext_code.size(mem[(32 * [94midx) + 588 len 20])
              static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                      gas gas_remaining wei
                     args caller
              mem[mem[64] len 128] = ext_call.return_data[0 len 128]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if ext_call.return_data[0]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=16)
                  return 15
              [94m_1288 = mem[64]
              mem[64] = mem[64] + 32
              mem[0] = addr([94m_1275)
              mem[32] = 9
              mem[[94m_1288] = markets[addr([94m_1275)].field_256
              mem[288] = [94m_1288
              [94m_1290 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1290] = ext_call.return_data[96]
              mem[320] = [94m_1290
              mem[mem[64] + 4] = addr([94m_1275)
              require ext_code.size(oracleAddress)
              static call oracleAddress.0xfc57d4df with:
                      gas gas_remaining wei
                     args addr([94m_1275)
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[256] = ext_call.return_data[0]
              if not ext_call.return_data[0]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=14)
                  return 15
              [94m_1314 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1314] = ext_call.return_data[0]
              mem[352] = [94m_1314
              [94m_1330 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1330] = 0
              [94m_1343 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1343] = 0
              [94m_1354 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_1354] = 0
              if not markets[addr([94m_1275)].field_256:
                  [94m_1409 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1409] = 0
                  [94m_1411 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1411] = 0
                  [94m_1429 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1429] = 0
                  mem[384] = [94m_1429
                  [94m_1435 = mem[96]
                  [94m_1444 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1444] = 0
                  [94m_1452 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1452] = 0
                  [94m_1469 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1469] = 0
                  if [94m_1435 + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  mem[96] = [94m_1435 + (0 / 10^18)
                  [94m_1495 = mem[128]
                  [94m_1505 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1505] = 0
                  [94m_1518 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1518] = 0
                  if not ext_call.return_data[0]:
                      [94m_1549 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1549] = 0
                      if [94m_1495 + (0 / 10^18) < 0 / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[128] = [94m_1495 + (0 / 10^18)
                      if addr([94m_1275) == _param1:
                          [94m_1639 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1639] = 0
                          [94m_1656 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1656] = 0
                          [94m_1731 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1731] = 0
                          if [94m_1495 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_1897 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1897] = 0
                          [94m_1923 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1923] = 0
                          if not ext_call.return_data[0]:
                              [94m_2045 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_2045] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_2085 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_2085] = 0
                          if [94m_1495 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_1495 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      [94m_1563 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1563] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_1495 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[128] = [94m_1495 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_1275) == _param1:
                          [94m_1655 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1655] = 0
                          [94m_1675 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1675] = 0
                          [94m_1753 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1753] = 0
                          if [94m_1495 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_1921 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1921] = 0
                          [94m_1958 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1958] = 0
                          if not ext_call.return_data[0]:
                              [94m_2081 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_2081] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_2141 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_2141] = 0
                          if [94m_1495 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_1495 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[96] * markets[addr([94m_1275)].field_256 / markets[addr([94m_1275)].field_256 != ext_call.return_data[96]:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  if (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 < 5 * 10^17:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  [94m_1410 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1410] = (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18
                  [94m_1414 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_1414] = 0
                  if not (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18:
                      [94m_1430 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1430] = 0
                      mem[384] = [94m_1430
                      [94m_1438 = mem[96]
                      [94m_1450 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1450] = 0
                      [94m_1455 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1455] = 0
                      [94m_1472 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1472] = 0
                      if [94m_1438 + (0 / 10^18) < 0 / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[96] = [94m_1438 + (0 / 10^18)
                      [94m_1498 = mem[128]
                      [94m_1512 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1512] = 0
                      [94m_1526 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1526] = 0
                      if not ext_call.return_data[0]:
                          [94m_1558 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1558] = 0
                          if [94m_1498 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_1498 + (0 / 10^18)
                          if addr([94m_1275) == _param1:
                              [94m_1646 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1646] = 0
                              [94m_1672 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1672] = 0
                              [94m_1744 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1744] = 0
                              if [94m_1498 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_1906 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1906] = 0
                              [94m_1955 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1955] = 0
                              if not ext_call.return_data[0]:
                                  [94m_2077 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_2077] = 0
                              else:
                                  if 0 / ext_call.return_data[0]:
                                      log Failure(
                                            uint256 error=15,
                                            uint256 info=3,
                                            uint256 detail=12)
                                      return 15
                                  [94m_2123 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_2123] = 0
                              if [94m_1498 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1498 + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_1575 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1575] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_1498 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_1498 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_1275) == _param1:
                              [94m_1665 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1665] = 0
                              [94m_1690 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1690] = 0
                              [94m_1772 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1772] = 0
                              if [94m_1498 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_1938 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1938] = 0
                              [94m_1987 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1987] = 0
                              if not ext_call.return_data[0]:
                                  [94m_2119 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_2119] = 0
                              else:
                                  if 0 / ext_call.return_data[0]:
                                      log Failure(
                                            uint256 error=15,
                                            uint256 info=3,
                                            uint256 detail=12)
                                      return 15
                                  [94m_2186 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_2186] = 0
                              if [94m_1498 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1498 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      [94m_1432 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1432] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      mem[384] = [94m_1432
                      [94m_1447 = mem[96]
                      [94m_1453 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1453] = 0
                      [94m_1463 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_1463] = 0
                      if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                          [94m_1478 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1478] = 0
                          if [94m_1447 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[96] = [94m_1447 + (0 / 10^18)
                          [94m_1508 = mem[128]
                          [94m_1522 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1522] = 0
                          [94m_1533 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1533] = 0
                          if not ext_call.return_data[0]:
                              [94m_1571 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1571] = 0
                              if [94m_1508 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1508 + (0 / 10^18)
                              if addr([94m_1275) == _param1:
                                  [94m_1661 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1661] = 0
                                  [94m_1688 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1688] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_1768 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1768] = 0
                                      if [94m_1508 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1930 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1930] = 0
                                      [94m_1985 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1985] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2117 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2117] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2175 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2175] = 0
                                      if [94m_1508 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1508 + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1805 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1805] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_1508 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1968 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1968] = 0
                                      [94m_2016 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2016] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2172 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2172] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2249 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2249] = 0
                                      if [94m_1508 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1508 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                          else:
                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_1592 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1592] = ext_call.return_data[64] * ext_call.return_data[0]
                              if [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                              if addr([94m_1275) == _param1:
                                  [94m_1679 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1679] = 0
                                  [94m_1710 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1710] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_1804 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1804] = 0
                                      if [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1967 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1967] = 0
                                      [94m_2015 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2015] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2171 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2171] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2247 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2247] = 0
                                      if [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1841 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1841] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_2001 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2001] = 0
                                      [94m_2048 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2048] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2244 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2244] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2318 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2318] = 0
                                      if [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1508 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_1484 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1484] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                          if [94m_1447 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[96] = [94m_1447 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                          [94m_1521 = mem[128]
                          [94m_1529 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1529] = 0
                          [94m_1541 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_1541] = 0
                          if not ext_call.return_data[0]:
                              [94m_1589 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1589] = 0
                              if [94m_1521 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1521 + (0 / 10^18)
                              if addr([94m_1275) == _param1:
                                  [94m_1678 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1678] = 0
                                  [94m_1709 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1709] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_1803 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1803] = 0
                                      if [94m_1521 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1964 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1964] = 0
                                      [94m_2014 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2014] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2170 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2170] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2242 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2242] = 0
                                      if [94m_1521 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1521 + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1839 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1839] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_1521 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_2000 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2000] = 0
                                      [94m_2047 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2047] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2239 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2239] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2313 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2313] = 0
                                      if [94m_1521 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1521 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                          else:
                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_1608 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_1608] = ext_call.return_data[64] * ext_call.return_data[0]
                              if [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                              if addr([94m_1275) == _param1:
                                  [94m_1694 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1694] = 0
                                  [94m_1732 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_1732] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_1838 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1838] = 0
                                      if [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1999 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1999] = 0
                                      [94m_2046 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2046] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2238 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2238] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2311 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2311] = 0
                                      if [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_1865 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_1865] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_2034 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2034] = 0
                                      [94m_2087 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_2087] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_2308 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2308] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_2361 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_2361] = 0
                                      if [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_1521 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_1275)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          if mem[96] > mem[128]:
              if uint8(markets[addr(_param1)][2][caller].field_0):
                  uint8(markets[addr(_param1)][2][caller].field_0) = 0
                  mem[32] = 8
                  [94m_1313 = mem[64]
                  mem[64] = mem[64] + (32 * unknowndce15449[caller].field_0) + 32
                  if unknowndce15449[caller].field_0:
                      mem[[94m_1313 + 32] = addr(unknowndce15449[caller].field_0)
                      [94midx = [94m_1313 + 32
                      [94ms = 0
                      while [94m_1313 + (32 * unknowndce15449[caller].field_0) > [94midx:
                          mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                  [94midx = 0
                  while [94midx < unknowndce15449[caller].field_0:
                      require [94midx < unknowndce15449[caller].field_0
                      if mem[(32 * [94midx) + [94m_1313 + 44 len 20] != _param1:
                          [94midx = [94midx + 1
                          continue 
                      require [94midx < unknowndce15449[caller].field_0
                      require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                      require [94midx < unknowndce15449[caller].field_0
                      addr(unknowndce15449[caller][[94midx].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
                      unknowndce15449[caller].field_0--
                      if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
                          [94midx = unknowndce15449[caller].field_0 + sha3(sha3(caller, 8)) - 1
                          while sha3(sha3(caller, 8)) + unknowndce15449[caller].field_0 > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                      log 0xe699a64c: addr(_param1), caller
                      return 0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  return 0
          else:
              if mem[128] - mem[96]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=4)
                  return 15
              if uint8(markets[addr(_param1)][2][caller].field_0):
                  uint8(markets[addr(_param1)][2][caller].field_0) = 0
                  mem[32] = 8
                  [94m_1310 = mem[64]
                  mem[64] = mem[64] + (32 * unknowndce15449[caller].field_0) + 32
                  if unknowndce15449[caller].field_0:
                      mem[[94m_1310 + 32] = addr(unknowndce15449[caller].field_0)
                      [94midx = [94m_1310 + 32
                      [94ms = 0
                      while [94m_1310 + (32 * unknowndce15449[caller].field_0) > [94midx:
                          mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                  [94midx = 0
                  while [94midx < unknowndce15449[caller].field_0:
                      require [94midx < unknowndce15449[caller].field_0
                      if mem[(32 * [94midx) + [94m_1310 + 44 len 20] != _param1:
                          [94midx = [94midx + 1
                          continue 
                      require [94midx < unknowndce15449[caller].field_0
                      require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                      require [94midx < unknowndce15449[caller].field_0
                      addr(unknowndce15449[caller][[94midx].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
                      unknowndce15449[caller].field_0--
                      if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
                          [94midx = unknowndce15449[caller].field_0 + sha3(sha3(caller, 8)) - 1
                          while sha3(sha3(caller, 8)) + unknowndce15449[caller].field_0 > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                      log 0xe699a64c: addr(_param1), caller
                      return 0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  return 0
      else:
          mem[576] = addr(unknowndce15449[caller].field_0)
          [94midx = 576
          [94ms = 0
          while (32 * unknowndce15449[caller].field_0) + 544 > [94midx:
              mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
          [94midx = 0
          [94ms = 0
          while [94midx < unknowndce15449[caller].field_0:
              require [94midx < mem[544]
              [94m_4370 = mem[(32 * [94midx) + 576]
              require ext_code.size(mem[(32 * [94midx) + 588 len 20])
              static call mem[(32 * [94midx) + 588 len 20].0xc37f68e2 with:
                      gas gas_remaining wei
                     args caller
              mem[mem[64] len 128] = ext_call.return_data[0 len 128]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 128
              mem[224] = ext_call.return_data[96]
              mem[192] = ext_call.return_data[64]
              mem[160] = ext_call.return_data[32]
              if ext_call.return_data[0]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=16)
                  return 15
              [94m_4409 = mem[64]
              mem[64] = mem[64] + 32
              mem[0] = addr([94m_4370)
              mem[32] = 9
              mem[[94m_4409] = markets[addr([94m_4370)].field_256
              mem[288] = [94m_4409
              [94m_4411 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_4411] = ext_call.return_data[96]
              mem[320] = [94m_4411
              mem[mem[64] + 4] = addr([94m_4370)
              require ext_code.size(oracleAddress)
              static call oracleAddress.0xfc57d4df with:
                      gas gas_remaining wei
                     args addr([94m_4370)
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[256] = ext_call.return_data[0]
              if not ext_call.return_data[0]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=14)
                  return 15
              [94m_4451 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_4451] = ext_call.return_data[0]
              mem[352] = [94m_4451
              [94m_4475 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_4475] = 0
              [94m_4496 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_4496] = 0
              [94m_4515 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_4515] = 0
              if not markets[addr([94m_4370)].field_256:
                  [94m_4570 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4570] = 0
                  [94m_4572 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4572] = 0
                  [94m_4590 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4590] = 0
                  mem[384] = [94m_4590
                  [94m_4596 = mem[96]
                  [94m_4605 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4605] = 0
                  [94m_4613 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4613] = 0
                  [94m_4630 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4630] = 0
                  if [94m_4596 + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  mem[96] = [94m_4596 + (0 / 10^18)
                  [94m_4656 = mem[128]
                  [94m_4666 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4666] = 0
                  [94m_4679 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4679] = 0
                  if not ext_call.return_data[0]:
                      [94m_4710 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4710] = 0
                      if [94m_4656 + (0 / 10^18) < 0 / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[128] = [94m_4656 + (0 / 10^18)
                      if addr([94m_4370) == _param1:
                          [94m_4800 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4800] = 0
                          [94m_4817 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4817] = 0
                          [94m_4892 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4892] = 0
                          if [94m_4656 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_5058 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5058] = 0
                          [94m_5084 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5084] = 0
                          if not ext_call.return_data[0]:
                              [94m_5206 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5206] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_5246 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5246] = 0
                          if [94m_4656 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_4656 + (0 / 10^18)
                  else:
                      if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      [94m_4724 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4724] = ext_call.return_data[64] * ext_call.return_data[0]
                      if [94m_4656 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[128] = [94m_4656 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                      if addr([94m_4370) == _param1:
                          [94m_4816 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4816] = 0
                          [94m_4836 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4836] = 0
                          [94m_4914 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4914] = 0
                          if [94m_4656 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_5082 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5082] = 0
                          [94m_5119 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5119] = 0
                          if not ext_call.return_data[0]:
                              [94m_5242 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5242] = 0
                          else:
                              if 0 / ext_call.return_data[0]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_5302 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5302] = 0
                          if [94m_4656 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_4656 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
              else:
                  if ext_call.return_data[96] * markets[addr([94m_4370)].field_256 / markets[addr([94m_4370)].field_256 != ext_call.return_data[96]:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  if (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 < 5 * 10^17:
                      log Failure(
                            uint256 error=15,
                            uint256 info=3,
                            uint256 detail=12)
                      return 15
                  [94m_4571 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4571] = (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18
                  [94m_4575 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_4575] = 0
                  if not (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18:
                      [94m_4591 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4591] = 0
                      mem[384] = [94m_4591
                      [94m_4599 = mem[96]
                      [94m_4611 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4611] = 0
                      [94m_4616 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4616] = 0
                      [94m_4633 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4633] = 0
                      if [94m_4599 + (0 / 10^18) < 0 / 10^18:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      mem[96] = [94m_4599 + (0 / 10^18)
                      [94m_4659 = mem[128]
                      [94m_4673 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4673] = 0
                      [94m_4687 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4687] = 0
                      if not ext_call.return_data[0]:
                          [94m_4719 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4719] = 0
                          if [94m_4659 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_4659 + (0 / 10^18)
                          if addr([94m_4370) == _param1:
                              [94m_4807 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4807] = 0
                              [94m_4833 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4833] = 0
                              [94m_4905 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4905] = 0
                              if [94m_4659 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_5067 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5067] = 0
                              [94m_5116 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5116] = 0
                              if not ext_call.return_data[0]:
                                  [94m_5238 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5238] = 0
                              else:
                                  if 0 / ext_call.return_data[0]:
                                      log Failure(
                                            uint256 error=15,
                                            uint256 info=3,
                                            uint256 detail=12)
                                      return 15
                                  [94m_5284 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5284] = 0
                              if [94m_4659 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4659 + (0 / 10^18)
                      else:
                          if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_4736 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4736] = ext_call.return_data[64] * ext_call.return_data[0]
                          if [94m_4659 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[128] = [94m_4659 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                          if addr([94m_4370) == _param1:
                              [94m_4826 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4826] = 0
                              [94m_4851 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4851] = 0
                              [94m_4933 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4933] = 0
                              if [94m_4659 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_5099 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5099] = 0
                              [94m_5148 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5148] = 0
                              if not ext_call.return_data[0]:
                                  [94m_5280 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5280] = 0
                              else:
                                  if 0 / ext_call.return_data[0]:
                                      log Failure(
                                            uint256 error=15,
                                            uint256 info=3,
                                            uint256 detail=12)
                                      return 15
                                  [94m_5347 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5347] = 0
                              if [94m_4659 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4659 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                  else:
                      if ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18 / (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18 != ext_call.return_data[0]:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      if (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                          log Failure(
                                uint256 error=15,
                                uint256 info=3,
                                uint256 detail=12)
                          return 15
                      [94m_4593 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4593] = (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                      mem[384] = [94m_4593
                      [94m_4608 = mem[96]
                      [94m_4614 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4614] = 0
                      [94m_4624 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_4624] = 0
                      if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                          [94m_4639 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4639] = 0
                          if [94m_4608 + (0 / 10^18) < 0 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[96] = [94m_4608 + (0 / 10^18)
                          [94m_4669 = mem[128]
                          [94m_4683 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4683] = 0
                          [94m_4694 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4694] = 0
                          if not ext_call.return_data[0]:
                              [94m_4732 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4732] = 0
                              if [94m_4669 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4669 + (0 / 10^18)
                              if addr([94m_4370) == _param1:
                                  [94m_4822 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4822] = 0
                                  [94m_4849 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4849] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_4929 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_4929] = 0
                                      if [94m_4669 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5091 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5091] = 0
                                      [94m_5146 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5146] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5278 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5278] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5336 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5336] = 0
                                      if [94m_4669 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4669 + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_4966 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_4966] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_4669 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5129 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5129] = 0
                                      [94m_5177 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5177] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5333 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5333] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5410 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5410] = 0
                                      if [94m_4669 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4669 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                          else:
                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_4753 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4753] = ext_call.return_data[64] * ext_call.return_data[0]
                              if [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                              if addr([94m_4370) == _param1:
                                  [94m_4840 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4840] = 0
                                  [94m_4871 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4871] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_4965 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_4965] = 0
                                      if [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5128 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5128] = 0
                                      [94m_5176 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5176] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5332 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5332] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5408 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5408] = 0
                                      if [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5002 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5002] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5162 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5162] = 0
                                      [94m_5209 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5209] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5405 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5405] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5479 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5479] = 0
                                      if [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4669 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                      else:
                          if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          [94m_4645 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4645] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                          if [94m_4608 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                              log Failure(
                                    uint256 error=15,
                                    uint256 info=3,
                                    uint256 detail=12)
                              return 15
                          mem[96] = [94m_4608 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18)
                          [94m_4682 = mem[128]
                          [94m_4690 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4690] = 0
                          [94m_4702 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_4702] = 0
                          if not ext_call.return_data[0]:
                              [94m_4750 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4750] = 0
                              if [94m_4682 + (0 / 10^18) < 0 / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4682 + (0 / 10^18)
                              if addr([94m_4370) == _param1:
                                  [94m_4839 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4839] = 0
                                  [94m_4870 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4870] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_4964 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_4964] = 0
                                      if [94m_4682 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5125 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5125] = 0
                                      [94m_5175 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5175] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5331 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5331] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5403 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5403] = 0
                                      if [94m_4682 + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4682 + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5000 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5000] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_4682 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5161 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5161] = 0
                                      [94m_5208 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5208] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5400 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5400] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5474 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5474] = 0
                                      if [94m_4682 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4682 + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
                          else:
                              if ext_call.return_data[64] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[64]:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              [94m_4769 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_4769] = ext_call.return_data[64] * ext_call.return_data[0]
                              if [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) < ext_call.return_data[64] * ext_call.return_data[0] / 10^18:
                                  log Failure(
                                        uint256 error=15,
                                        uint256 info=3,
                                        uint256 detail=12)
                                  return 15
                              mem[128] = [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18)
                              if addr([94m_4370) == _param1:
                                  [94m_4855 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4855] = 0
                                  [94m_4893 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_4893] = 0
                                  if not (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18:
                                      [94m_4999 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_4999] = 0
                                      if [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5160 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5160] = 0
                                      [94m_5207 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5207] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5399 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5399] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5472 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5472] = 0
                                      if [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (0 / 10^18)
                                  else:
                                      if ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 != ext_call.return_data[32]:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5026 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5026] = ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18
                                      if [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) < ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      [94m_5195 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5195] = 0
                                      [94m_5248 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5248] = 0
                                      if not ext_call.return_data[0]:
                                          [94m_5469 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5469] = 0
                                      else:
                                          if 0 / ext_call.return_data[0]:
                                              log Failure(
                                                    uint256 error=15,
                                                    uint256 info=3,
                                                    uint256 detail=12)
                                              return 15
                                          [94m_5522 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_5522] = 0
                                      if [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18) < 0 / 10^18:
                                          log Failure(
                                                uint256 error=15,
                                                uint256 info=3,
                                                uint256 detail=12)
                                          return 15
                                      mem[128] = [94m_4682 + (ext_call.return_data[64] * ext_call.return_data[0] / 10^18) + (ext_call.return_data[32] * (ext_call.return_data[0] * (ext_call.return_data[96] * markets[addr([94m_4370)].field_256) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18 / 10^18) + (0 / 10^18)
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          if mem[96] > mem[128]:
              if uint8(markets[addr(_param1)][2][caller].field_0):
                  uint8(markets[addr(_param1)][2][caller].field_0) = 0
                  mem[32] = 8
                  [94m_4450 = mem[64]
                  mem[64] = mem[64] + (32 * unknowndce15449[caller].field_0) + 32
                  if unknowndce15449[caller].field_0:
                      mem[[94m_4450 + 32] = addr(unknowndce15449[caller].field_0)
                      [94midx = [94m_4450 + 32
                      [94ms = 0
                      while [94m_4450 + (32 * unknowndce15449[caller].field_0) > [94midx:
                          mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                  [94midx = 0
                  while [94midx < unknowndce15449[caller].field_0:
                      require [94midx < unknowndce15449[caller].field_0
                      if mem[(32 * [94midx) + [94m_4450 + 44 len 20] != _param1:
                          [94midx = [94midx + 1
                          continue 
                      require [94midx < unknowndce15449[caller].field_0
                      require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                      require [94midx < unknowndce15449[caller].field_0
                      addr(unknowndce15449[caller][[94midx].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
                      unknowndce15449[caller].field_0--
                      if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
                          [94midx = unknowndce15449[caller].field_0 + sha3(sha3(caller, 8)) - 1
                          while sha3(sha3(caller, 8)) + unknowndce15449[caller].field_0 > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                      log 0xe699a64c: addr(_param1), caller
                      return 0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  return 0
          else:
              if mem[128] - mem[96]:
                  log Failure(
                        uint256 error=15,
                        uint256 info=3,
                        uint256 detail=4)
                  return 15
              if uint8(markets[addr(_param1)][2][caller].field_0):
                  uint8(markets[addr(_param1)][2][caller].field_0) = 0
                  mem[32] = 8
                  [94m_4447 = mem[64]
                  mem[64] = mem[64] + (32 * unknowndce15449[caller].field_0) + 32
                  if unknowndce15449[caller].field_0:
                      mem[[94m_4447 + 32] = addr(unknowndce15449[caller].field_0)
                      [94midx = [94m_4447 + 32
                      [94ms = 0
                      while [94m_4447 + (32 * unknowndce15449[caller].field_0) > [94midx:
                          mem[[94midx + 32] = addr(unknowndce15449[caller][[94ms].field_256)
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                  [94midx = 0
                  while [94midx < unknowndce15449[caller].field_0:
                      require [94midx < unknowndce15449[caller].field_0
                      if mem[(32 * [94midx) + [94m_4447 + 44 len 20] != _param1:
                          [94midx = [94midx + 1
                          continue 
                      require [94midx < unknowndce15449[caller].field_0
                      require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                      require [94midx < unknowndce15449[caller].field_0
                      addr(unknowndce15449[caller][[94midx].field_0) = addr(unknowndce15449[caller][unknowndce15449[caller].field_0].field_0)
                      unknowndce15449[caller].field_0--
                      if unknowndce15449[caller].field_0 > unknowndce15449[caller].field_0 - 1:
                          [94midx = unknowndce15449[caller].field_0 + sha3(sha3(caller, 8)) - 1
                          while sha3(sha3(caller, 8)) + unknowndce15449[caller].field_0 > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                      log 0xe699a64c: addr(_param1), caller
                      return 0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 - 1 < unknowndce15449[caller].field_0
                  require unknowndce15449[caller].field_0 < unknowndce15449[caller].field_0
                  return 0
  return 0


# hash = 0xf851a440
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def admin() payable: 
  return adminAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


