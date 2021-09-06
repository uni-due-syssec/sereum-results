# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xEcabad8118960F930B11777A89a2401483353F45 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address -12
    stor-12
    # storage address -11
    stor-11
    # storage address -10
    stor-10
    # storage address -9
    stor-9
    # storage address -8
    stor-8
    # storage address -7
    stor-7
    # storage address -6
    stor-6
    # storage address -5
    stor-5
    # storage address -4
    stor-4
    # storage address -3
    stor-3
    # storage address -2
    stor-2
    # storage address -1
    stor-1
    # storage address 0
    stor0
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    stor6
    # storage address 7
    stor7
    # storage address 8
    stor8
    # storage address 9
    stor9
    # storage address 10
    stor10
    # storage address 11
    stor11
    # storage address 12
    stor12
    # storage address 13
    stor13
    # storage address 14
    stor14
    # storage address 15
    stor15
    # storage address 16
    stor16
    # storage address 17
    stor17
    # storage address 18
    stor18
    # storage address 15003
    stor3A9B # mask: a s
    # storage address 15004
    unknowndae1a089 # mask: a s
# hash = 0x29e59770
# getter = None
# const = None
# payable = True
def unknown29e59770(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if m_param1 <= 6:
      [94midx = 0
      [94ms = mstor3A9B
      mwhile [94midx < m_param1m:
          require [94ms + 15 >= [94ms
          if [94ms + 15 > 15000:
              mstor3A9B = [94ms
              stop
          require [94ms < 15000
          mstor3m[[94msm] = 1
          require [94ms + 1 < 15000
          mstor4m[[94msm] = 1
          require [94ms + 2 < 15000
          mstor5m[[94msm] = 1
          require [94ms + 3 < 15000
          mstor6m[[94msm] = 1
          require [94ms + 4 < 15000
          mstor7m[[94msm] = 1
          require [94ms + 5 < 15000
          mstor8m[[94msm] = 1
          require [94ms + 6 < 15000
          mstor9m[[94msm] = 1
          require [94ms + 7 < 15000
          mstor10m[[94msm] = 1
          require [94ms + 8 < 15000
          mstor11m[[94msm] = 1
          require [94ms + 9 < 15000
          mstor12m[[94msm] = 1
          require [94ms + 10 < 15000
          mstor13m[[94msm] = 1
          require [94ms + 11 < 15000
          mstor14m[[94msm] = 1
          require [94ms + 12 < 15000
          mstor15m[[94msm] = 1
          require [94ms + 13 < 15000
          mstor16m[[94msm] = 1
          require [94ms + 14 < 15000
          mstor17m[[94msm] = 1
          require [94ms + 15 < 15000
          mstor18m[[94msm] = 1
          [94midx = [94midx + 1
          [94ms = [94ms + 16
          mcontinue 
      mstor3A9B += 16 * m_param1
  else:
      [94midx = 0
      [94ms = mstor3A9B
      mwhile [94midx < 6m:
          require [94ms + 15 >= [94ms
          if [94ms + 15 > 15000:
              mstor3A9B = [94ms
              stop
          require [94ms < 15000
          mstor3m[[94msm] = 1
          require [94ms + 1 < 15000
          mstor4m[[94msm] = 1
          require [94ms + 2 < 15000
          mstor5m[[94msm] = 1
          require [94ms + 3 < 15000
          mstor6m[[94msm] = 1
          require [94ms + 4 < 15000
          mstor7m[[94msm] = 1
          require [94ms + 5 < 15000
          mstor8m[[94msm] = 1
          require [94ms + 6 < 15000
          mstor9m[[94msm] = 1
          require [94ms + 7 < 15000
          mstor10m[[94msm] = 1
          require [94ms + 8 < 15000
          mstor11m[[94msm] = 1
          require [94ms + 9 < 15000
          mstor12m[[94msm] = 1
          require [94ms + 10 < 15000
          mstor13m[[94msm] = 1
          require [94ms + 11 < 15000
          mstor14m[[94msm] = 1
          require [94ms + 12 < 15000
          mstor15m[[94msm] = 1
          require [94ms + 13 < 15000
          mstor16m[[94msm] = 1
          require [94ms + 14 < 15000
          mstor17m[[94msm] = 1
          require [94ms + 15 < 15000
          mstor18m[[94msm] = 1
          [94midx = [94midx + 1
          [94ms = [94ms + 16
          mcontinue 
      mstor3A9B += 96


# hash = 0x680709f9
# getter = None
# const = None
# payable = True
def unknown680709f9() payable: 
  require mstor3A9B <= 15000
  return (-mstor3A9B + 15000 / 15)


# hash = 0x9041a74e
# getter = None
# const = None
# payable = True
def unknown9041a74e(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  [94midx = 0
  [94ms = mstor3A9B
  mwhile [94midx < m_param1m:
      if [94ms < 14:
          mstor3A9B = [94ms
          stop
      require [94ms < 15000
      mstor3m[[94msm] = 0
      require [94ms - 1 < 15000
      mstor2m[[94msm] = 0
      require [94ms - 2 < 15000
      uint256(mstor1m[[94msm]) = 0
      require [94ms - 3 < 15000
      mstor[[94msm] = 0
      require [94ms - 4 < 15000
      mstor-1m[[94msm] = 0
      require [94ms - 5 < 15000
      mstor-2m[[94msm] = 0
      require [94ms - 6 < 15000
      mstor-3m[[94msm] = 0
      require [94ms - 7 < 15000
      mstor-4m[[94msm] = 0
      require [94ms - 8 < 15000
      mstor-5m[[94msm] = 0
      require [94ms - 9 < 15000
      mstor-6m[[94msm] = 0
      require [94ms - 10 < 15000
      mstor-7m[[94msm] = 0
      require [94ms - 11 < 15000
      mstor-8m[[94msm] = 0
      require [94ms - 12 < 15000
      mstor-9m[[94msm] = 0
      require [94ms - 13 < 15000
      mstor-10m[[94msm] = 0
      require [94ms - 14 < 15000
      mstor-11m[[94msm] = 0
      require [94ms - 15 < 15000
      mstor-12m[[94msm] = 0
      [94midx = [94midx + 1
      [94ms = [94ms - 16
      mcontinue 
  mstor3A9B += -16 * m_param1


# hash = 0xb8b3dbc6
# getter = None
# const = None
# payable = True
def unknownb8b3dbc6() payable: 
  if addr(mstor1m.length) != caller:
      revert with 0, 'Must be the commander.'
  [93mselfdestruct([91maddr(stor1.length)[93m)


# hash = 0xdae1a089
# getter = ['storage', 256, 0, 15004]
# const = None
# payable = True
def unknowndae1a089() payable: 
  return munknowndae1a089


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


