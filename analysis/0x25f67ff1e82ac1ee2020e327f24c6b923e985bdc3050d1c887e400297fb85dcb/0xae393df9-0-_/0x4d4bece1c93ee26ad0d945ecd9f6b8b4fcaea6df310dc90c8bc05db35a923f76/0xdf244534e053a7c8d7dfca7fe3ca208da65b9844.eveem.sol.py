# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xdF244534e053a7C8d7dfCA7fe3ca208da65B9844 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x0386a016': 'closeProposal(uint256 _proposalId)', '0x16fdc34e': 'unknown16fdc34e(?)', '0x174e31c4': 'unknown174e31c4(?)', '0x4c15676b': 'unknown4c15676b(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknowna0b2d57fAddress # mask: a s
    # storage address 1
    unknownf17a3becAddress # mask: a s
    # storage address 2
    stor2
    # storage address 3
    unknownbb73c562
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    stor6
    # storage address 7
    stor7
    # storage address 8
    unknown060225f6
    # storage address 9
    unknown787112a6
    # storage address 10
    stor10
    # storage address 11
    stor11
    # storage address 12
    unknown0fec1dec
    # storage address 13
    stor13
    # storage address 14
    unknowne0429d09
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    unknown39bb9607 # mask: a s
    # storage address 17
    unknownaaf86c30 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 20
    stor20 # mask: a s
    # storage address 21
    proposalLength # mask: a s
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 25
    stor25 # mask: a s
    # storage address 25
    stor25 # mask: a s
    # storage address 26
    stor26 # mask: a s
    # storage address 26
    stor26 # mask: a s
    # storage address 29102676481673041902632991033461445430619272659676223336789171408008386403023
    stor29102676481673041902632991033461445430619272659676223336789171408008386403023
    # storage address 29102676481673041902632991033461445430619272659676223336789171408008386403024
    stor29102676481673041902632991033461445430619272659676223336789171408008386403024
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037084
    stor87903029871075914254377627908054574944891091886930582284385770809450030037084
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037085
    stor87903029871075914254377627908054574944891091886930582284385770809450030037085
# hash = 0x060225f6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 8]]]]]
# const = None
# payable = True
def unknown060225f6(addr m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  return munknown060225f6m[m_param1m]m[m_param2m]


# hash = 0x0ea9c984
# getter = None
# const = None
# payable = True
def unknown0ea9c984() payable: 
  if not mstor15:
      mstor2m.length++
      mstor2m[mstor2m.lengthm]m.field_0 = 0
      mstor4057m[mstor2m.lengthm] = 0
      mstor4057m[mstor2m.lengthm] = 0
      mproposalLength = 1
      munknownbb73c562m.length++
      munknownbb73c562m[munknownbb73c562m.lengthm]m.field_0 = 0
      mstorC257m[mstor3m.lengthm] = 0
      mstorC257m[mstor3m.lengthm] = block.timestamp
      munknown39bb9607 = 168 * 24 * 3600
      mstor22 = 336 * 24 * 3600
      mstor18 = 5
      mstor20 = 40
      mstor15 = 1
      munknownaaf86c30 = 1
      mstor19 = 75
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x3a12507f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor25) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor25))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4d52000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor23) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor23))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5043000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor24) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor24))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4d52000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor26) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor26))


# hash = 0x0fec1dec
# getter = ['struct', ['loc', 12]]
# const = None
# payable = True
def unknown0fec1dec(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  return munknown0fec1decm[m_param1m]m[m_param2m]m.field_0, 
         munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0,
         munknown0fec1decm[m_param1m]m.field_512


# hash = 0x11a1ef3e
# getter = None
# const = None
# payable = True
def unknown11a1ef3e() payable: 
  require calldata.size - 4 >= 32


# hash = 0x16e9eaec
# getter = None
# const = None
# payable = True
def unknown16e9eaec(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return m_param1, mstor5m[m_param1m]m.field_0, munknown0fec1decm[m_param1m]m.field_512


# hash = 0x1eef225c
# getter = None
# const = None
# payable = True
def unknown1eef225c() payable: 
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 1 == bool(ext_call.return_data[0])
  if not munknown787112a6m[callerm]:
      [94midx = munknowne0429d09m[callerm]
      [94ms = 0
      [94mt = 0
      mwhile [94midx < mstor6m[callerm]m:
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
              if caller != caller:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
          require [94midx < mstor6m[callerm]
          if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = [94ms
              [94mt = [94mt
              mcontinue 
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
          mem[0] = caller
          mem[32] = 6
          [94midx = [94midx + 1
          [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
          [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
          mcontinue 
  else:
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      if not munknownbb73c562m[mstor9m[callerm]m]m.field_256:
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[callerm]m:
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
                  if caller != caller:
                      mem[0] = caller
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[callerm]
              if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
      else:
          require munknown787112a6m[callerm] < munknownbb73c562m.length
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m:
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_512 <= munknownbb73c562m[mstor9m[callerm]m]m.field_512 + munknown39bb9607:
                  if munknownbb73c562m[mstor9m[callerm]m]m.field_256 != caller:
                      mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              if mstor7m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m[callerm]:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
  if [94mt:
      revert with 0, 'Claim pending rewards'
  if munknown787112a6m[callerm]:
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      mstor10m[mstor3m[mstor9m[callerm]m]m.field_256m]--
      munknownbb73c562m[mstor9m[callerm]m]m.field_256 = 0
      munknownbb73c562m[mstor9m[callerm]m]m.field_512 = block.timestamp
      munknowne0429d09m[callerm] = mstor6m[callerm]


# hash = 0x207008f6
# getter = None
# const = None
# payable = True
def unknown207008f6(bool m_param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 1 == bool(ext_call.return_data[0])
  if not munknown787112a6m[callerm]:
      [94midx = munknowne0429d09m[callerm]
      [94ms = 0
      [94mt = 0
      mwhile [94midx < mstor6m[callerm]m:
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
              if caller != caller:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
          require [94midx < mstor6m[callerm]
          if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = [94ms
              [94mt = [94mt
              mcontinue 
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
          mem[0] = caller
          mem[32] = 6
          [94midx = [94midx + 1
          [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
          [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
          mcontinue 
  else:
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      if not munknownbb73c562m[mstor9m[callerm]m]m.field_256:
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[callerm]m:
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
                  if caller != caller:
                      mem[0] = caller
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[callerm]
              if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
      else:
          require munknown787112a6m[callerm] < munknownbb73c562m.length
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m:
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_512 <= munknownbb73c562m[mstor9m[callerm]m]m.field_512 + munknown39bb9607:
                  if munknownbb73c562m[mstor9m[callerm]m]m.field_256 != caller:
                      mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              if mstor7m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m[callerm]:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
  if [94mt:
      revert with 0, 'Claim pending rewards'
  mstor13m[callerm] = uint8(m_param1)


# hash = 0x2f54243a
# getter = None
# const = None
# payable = True
def unknown2f54243a(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 < mstor5m[m_param1m]m.field_0
  mem[128] = mstor5m[m_param1m]m[m_param2m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor5m[m_param1m]m[m_param2m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor5m[m_param1m]m[m_param2 + [94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return m_param2, Array(len=mstor5m[m_param1m]m[m_param2m]m.length, data=mem[128 len mstor5m[m_param1m]m[m_param2m]m.length])


# hash = 0x30326c17
# getter = None
# const = None
# payable = True
def proposal(uint256 m_proposalId) payable: 
  require calldata.size - 4 >= 32
  return m_proposalId, 
         mstor4m[m_proposalIdm]m.field_512,
         mstor4m[m_proposalIdm]m.field_0,
         mstor4m[m_proposalIdm]m.field_256,
         mstor4m[m_proposalIdm]m.field_768


# hash = 0x39bb9607
# getter = ['storage', 256, 0, 16]
# const = None
# payable = True
def unknown39bb9607() payable: 
  return munknown39bb9607


# hash = 0x4df9d6ba
# getter = None
# const = None
# payable = True
def unknown4df9d6ba(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknown787112a6m[addr(m_param1)m]:
      [94midx = munknowne0429d09m[addr(m_param1)m]
      [94ms = 0
      [94mt = 0
      mwhile [94midx < mstor6m[addr(m_param1)m]m:
          require [94midx < mstor6m[addr(m_param1)m]
          require mstor6m[addr(m_param1)m]m[[94midxm] < mstor2m.length
          if mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_512 <= munknown39bb9607:
              if m_param1 != m_param1:
                  mem[0] = m_param1
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
          require [94midx < mstor6m[addr(m_param1)m]
          if mstor7m[mstor6m[addr(m_param1)m]m[[94midxm]m]m[addr(m_param1)m]:
              mem[0] = m_param1
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = [94ms
              [94mt = [94mt
              mcontinue 
          require [94midx < mstor6m[addr(m_param1)m]
          require mstor6m[addr(m_param1)m]m[[94midxm] < mstor2m.length
          if munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
              mem[0] = m_param1
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          if mstor4m[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
              mem[0] = m_param1
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          require munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512
          mem[0] = m_param1
          mem[32] = 6
          [94midx = [94midx + 1
          [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
          [94mt = [94mt + (mstor4m[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512)
          mcontinue 
  else:
      require munknown787112a6m[addr(m_param1)m] < munknownbb73c562m.length
      if not munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256:
          [94midx = munknowne0429d09m[addr(m_param1)m]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[addr(m_param1)m]m:
              require [94midx < mstor6m[addr(m_param1)m]
              require mstor6m[addr(m_param1)m]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_512 <= munknown39bb9607:
                  if m_param1 != m_param1:
                      mem[0] = m_param1
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[addr(m_param1)m]
              if mstor7m[mstor6m[addr(m_param1)m]m[[94midxm]m]m[addr(m_param1)m]:
                  mem[0] = m_param1
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[addr(m_param1)m]
              require mstor6m[addr(m_param1)m]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = m_param1
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = m_param1
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = m_param1
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[addr(m_param1)m]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
      else:
          require munknown787112a6m[addr(m_param1)m] < munknownbb73c562m.length
          [94midx = munknowne0429d09m[addr(m_param1)m]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m:
              require [94midx < mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_512 <= munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_512 + munknown39bb9607:
                  if munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256 != m_param1:
                      mem[0] = munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]
              if mstor7m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m[addr(m_param1)m]:
                  mem[0] = munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
  return [94mt


# hash = 0x53fb6c5c
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 7]]]]]]
# const = None
# payable = True
def unknown53fb6c5c(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  return bool(mstor7m[m_param1m]m[m_param2m])


# hash = 0x5d128f73
# getter = None
# const = None
# payable = True
def unknown5d128f73(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 96
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + m_param1.length + 36 <= calldata.size
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size


# hash = 0x6122f840
# getter = None
# const = None
# payable = True
def unknown6122f840(uint64 m_param1) payable: 
  require calldata.size - 4 >= 32
  if Mask(64, 192, m_param1) == 0x474f56484f4c4400000000000000000000000000000000000000000000000000:
      return Mask(64, 192, m_param1), munknown39bb9607 / 24 * 3600
  if Mask(64, 192, m_param1) == 0x4d4158464f4c0000000000000000000000000000000000000000000000000000:
      return Mask(64, 192, m_param1), mstor20
  if Mask(64, 192, m_param1) == 0x4d41584452465400000000000000000000000000000000000000000000000000:
      return Mask(64, 192, m_param1), mstor22 / 24 * 3600
  if Mask(64, 192, m_param1) == 0x4d41584142000000000000000000000000000000000000000000000000000000:
      require ext_code.size(addr(mstor26))
      static call addr(mstor26).0x37f15a58 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return Mask(64, 192, m_param1), ext_call.return_data[0]
  if Mask(64, 192, m_param1) != 0x455054494d450000000000000000000000000000000000000000000000000000:
      return Mask(64, 192, m_param1), 0
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x15cb3ff with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return Mask(64, 192, m_param1), ext_call.return_data[0] / 24 * 3600


# hash = 0x6edde0bd
# getter = None
# const = None
# payable = True
def unknown6edde0bd(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  require mstor4m[m_param1m]m.field_0 < 2
  require ext_code.size(addr(mstor23))
  static call addr(mstor23).0x505ef22f with:
          gas gas_remaining wei
         args caller, munknownaaf86c30
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Not authorized'
  if m_param2 <= 0:
      revert with 0, 'Invalid category'
  require ext_code.size(addr(mstor24))
  static call addr(mstor24).0x39275b0a with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_param2 >= ext_call.return_data[0]:
      revert with 0, 'Invalid category'
  mstor4m[m_param1m]m.field_512 = m_param2
  mstor4m[m_param1m]m.field_768 = m_param3
  mstor4m[m_param1m]m.field_0 = 1
  log 0x5c0ed408: _param2, _param1, caller


# hash = 0x6f93bfb7
# getter = None
# const = None
# payable = True
def unknown6f93bfb7(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mstor4m[m_param1m]m.field_0 != 2:
      revert with 0, 'Not allowed'
  if m_param2 > mstor5m[m_param1m]m.field_0:
      revert with 0, 'Solution doesn't exist'
  mem[96] = 0x253eca1f00000000000000000000000000000000000000000000000000000000
  mem[100] = mstor4m[m_param1m]m.field_512
  require ext_code.size(addr(mstor24))
  static call addr(mstor24).0x253eca1f with:
          gas gas_remaining wei
         args mstor4m[m_param1m]m.field_512
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 224
  require mem[224] <= 4294967296
  require mem[224] + 32 <= return_data.size
  require mem[mem[224] + 96] <= 4294967296 and mem[224] + (32 * mem[mem[224] + 96]) + 32 <= return_data.size
  require mem[256] + mstor4m[m_param1m]m.field_1024 >= mstor4m[m_param1m]m.field_1024
  if mem[256] + mstor4m[m_param1m]m.field_1024 <= block.timestamp:
      revert with 0, 'Closed'
  if munknown060225f6m[callerm]m[m_param1m]:
      revert with 0, 'Voted'
  if munknown787112a6m[callerm]:
      require munknown787112a6m[callerm] > 0
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      require not munknownbb73c562m[mstor9m[callerm]m]m.field_256
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      require block.timestamp - munknownbb73c562m[mstor9m[callerm]m]m.field_512 > munknown39bb9607
  require ext_code.size(addr(mstor23))
  static call addr(mstor23).0x505ef22f with:
          gas gas_remaining wei
         args caller, mstor4m[m_param1m]m.field_512, mem[132 len 28]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Not Authorized'
  mstor6m[callerm]++
  mstor6m[callerm]m[mstor6m[callerm]m] = mstor2m.length
  munknown060225f6m[callerm]m[m_param1m] = mstor2m.length
  mstor2m.length++
  mstor2m[mstor2m.lengthm]m.field_0 = caller
  mstor4057m[mstor2m.lengthm] = m_param1
  mstor4057m[mstor2m.lengthm] = block.timestamp
  log 0x89eb0be5: block.timestamp, _param2, caller, _param1, stor2.length
  if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
      if m_param2 != 1:
          mstor4m[m_param1m]m.field_1024 = block.timestamp
          mstor4m[m_param1m]m.field_0 = 4
      else:
          mstor4m[m_param1m]m.field_256 = 1
          require ext_code.size(addr(mstor24))
          static call addr(mstor24).0x674aa712 with:
                  gas gas_remaining wei
                 args mstor4m[m_param1m]m.field_512
          mem[ceil32(return_data.size) + 192 len 128] = ext_call.return_data[0 len 128]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 128
          mstor4m[m_param1m]m.field_1024 = block.timestamp
          mstor4m[m_param1m]m.field_0 = 3
          if Mask(16, 240, ext_call.return_data[64]) == 0x4d53000000000000000000000000000000000000000000000000000000000000:
              require 1 < mstor5m[m_param1m]m.field_0
              mem[ceil32(return_data.size) + 192] = mstor5m[m_param1m]m[1m]m.field_0
              [94midx = ceil32(return_data.size) + 192
              [94ms = 0
              mwhile ceil32(return_data.size) + mstor5m[m_param1m]m[1m]m.length + 192 > [94midx + 32m:
                  mem[[94midx + 32] = mstor5m[m_param1m]m[[94ms + 1m]m.field_256
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
              call munknowna0b2d57fAddress.mem[ceil32(return_data.size) + 192 len 4] with:
                   gas gas_remaining wei
                  args mem[ceil32(return_data.size) + 196 len mstor5m[m_param1m]m[1m]m.length - 4]
          else:
              if Mask(16, 240, ext_call.return_data[64]) == 0x4558000000000000000000000000000000000000000000000000000000000000:
                  require 1 < mstor5m[m_param1m]m.field_0
                  mem[ceil32(return_data.size) + 192] = mstor5m[m_param1m]m[1m]m.field_0
                  [94midx = ceil32(return_data.size) + 192
                  [94ms = 0
                  mwhile ceil32(return_data.size) + mstor5m[m_param1m]m[1m]m.length + 192 > [94midx + 32m:
                      mem[[94midx + 32] = mstor5m[m_param1m]m[[94ms + 1m]m.field_256
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
                  call addr(ext_call.return_data[32]).mem[ceil32(return_data.size) + 192 len 4] with:
                       gas gas_remaining wei
                      args mem[ceil32(return_data.size) + 196 len mstor5m[m_param1m]m[1m]m.length - 4]
              else:
                  mem[ceil32(return_data.size) + 196] = Mask(16, 240, ext_call.return_data[64])
                  require ext_code.size(munknowna0b2d57fAddress)
                  static call munknowna0b2d57fAddress.0x1382858 with:
                          gas gas_remaining wei
                         args Mask(16, 240, ext_call.return_data[64])
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 1 < mstor5m[m_param1m]m.field_0
                  mem[ceil32(return_data.size) + 192] = mstor5m[m_param1m]m[1m]m.field_0
                  [94midx = ceil32(return_data.size) + 192
                  [94ms = 0
                  mwhile ceil32(return_data.size) + mstor5m[m_param1m]m[1m]m.length + 192 > [94midx + 32m:
                      mem[[94midx + 32] = mstor5m[m_param1m]m[[94ms + 1m]m.field_256
                      [94midx = [94midx + 32
                      [94ms = [94ms + 1
                      mcontinue 
                  call addr(ext_call.return_data[0]).mem[ceil32(return_data.size) + 192 len 4] with:
                       gas gas_remaining wei
                      args mem[ceil32(return_data.size) + 196 len mstor5m[m_param1m]m[1m]m.length - 4]
          if ext_call.success:
              log 0x6535f242: _param1
          log ProposalAccepted(uint256 ProposalID=_param1)
  else:
      require ext_code.size(addr(mstor23))
      static call addr(mstor23).0xdc6f847 with:
              gas gas_remaining wei
             args mstor4m[m_param1m]m.field_512, mem[132 len 28]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(mstor24))
      static call addr(mstor24).0x86957731 with:
              gas gas_remaining wei
             args mstor4m[m_param1m]m.field_512
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(mstor25))
      static call addr(mstor25).totalBalanceOf(address of) with:
              gas gas_remaining wei
             args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(mstor25))
      static call addr(mstor25).totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] == 1:
          require ext_code.size(addr(mstor23))
          static call addr(mstor23).0x505ef22f with:
                  gas gas_remaining wei
                 args caller, 1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(addr(mstor25))
              call addr(mstor25).0x4c47e71d with:
                   gas gas_remaining wei
                  args caller, munknown39bb9607
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94midx = 0
              [94ms = 0
              [94ms = ext_call.return_data[0]
              [94mt = 1
              [94mu = ext_call.return_data[0] + 10^18
              mwhile [94midx < mstor11m[callerm]m.field_0m:
                  require [94midx < mstor11m[callerm]m.field_0
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                  require ext_code.size(addr(mstor23))
                  static call addr(mstor23).0x505ef22f with:
                          gas gas_remaining wei
                         args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                  mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  require ext_code.size(addr(mstor25))
                  static call addr(mstor25).totalBalanceOf(address of) with:
                          gas gas_remaining wei
                         args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                  mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  mem[ceil32(return_data.size) + 228] = munknown39bb9607
                  require ext_code.size(addr(mstor25))
                  call addr(mstor25).0x4c47e71d with:
                       gas gas_remaining wei
                      args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if ext_call.return_data[0] == 1:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = ext_call.return_data[0] + [94mu + 10^18
                      mcontinue 
                  if not mstor18:
                      mem[0] = caller
                      mem[32] = 11
                      if ext_call.return_data[0] <= 0:
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + ext_call.return_data[0] + 10^18
                          mcontinue 
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = [94mu + 10^18
                      mcontinue 
                  require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                  mem[0] = caller
                  mem[32] = 11
                  if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = [94mu + ext_call.return_data[0] + 10^18
                      mcontinue 
                  [94midx = [94midx + 1
                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                  [94ms = ext_call.return_data[0]
                  [94mt = [94mt + 1
                  [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                  mcontinue 
              if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                  munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                  munknown0fec1decm[m_param1m]m.field_512 += [94mt
              else:
                  if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                      munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                      munknown0fec1decm[m_param1m]m.field_512 += [94mt
              if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
              else:
                  munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
          else:
              require ext_code.size(addr(mstor24))
              static call addr(mstor24).0x78005297 with:
                      gas gas_remaining wei
                     args mstor4m[m_param1m]m.field_512
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(mstor25))
              call addr(mstor25).0x4c47e71d with:
                   gas gas_remaining wei
                  args caller, munknown39bb9607
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94midx = 0
              [94ms = 0
              [94ms = ext_call.return_data[0]
              [94mt = 1
              [94mu = ext_call.return_data[0] + 10^18
              mwhile [94midx < mstor11m[callerm]m.field_0m:
                  require [94midx < mstor11m[callerm]m.field_0
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                  require ext_code.size(addr(mstor23))
                  static call addr(mstor23).0x505ef22f with:
                          gas gas_remaining wei
                         args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                  mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = [94ms
                      [94mt = [94mt
                      [94mu = [94mu
                      mcontinue 
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  require ext_code.size(addr(mstor25))
                  static call addr(mstor25).totalBalanceOf(address of) with:
                          gas gas_remaining wei
                         args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                  mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                  mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                  mem[ceil32(return_data.size) + 228] = munknown39bb9607
                  require ext_code.size(addr(mstor25))
                  call addr(mstor25).0x4c47e71d with:
                       gas gas_remaining wei
                      args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if ext_call.return_data[0] == 1:
                      mem[0] = caller
                      mem[32] = 11
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = ext_call.return_data[0] + [94mu + 10^18
                      mcontinue 
                  if not mstor18:
                      mem[0] = caller
                      mem[32] = 11
                      if ext_call.return_data[0] <= 0:
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + ext_call.return_data[0] + 10^18
                          mcontinue 
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = [94mu + 10^18
                      mcontinue 
                  require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                  mem[0] = caller
                  mem[32] = 11
                  if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                      [94midx = [94midx + 1
                      [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94mt = [94mt + 1
                      [94mu = [94mu + ext_call.return_data[0] + 10^18
                      mcontinue 
                  [94midx = [94midx + 1
                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                  [94ms = ext_call.return_data[0]
                  [94mt = [94mt + 1
                  [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                  mcontinue 
              if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                  munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                  munknown0fec1decm[m_param1m]m.field_512 += [94mt
              else:
                  if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                      munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                      munknown0fec1decm[m_param1m]m.field_512 += [94mt
              if ext_call.return_data[0] > 0:
                  munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
              else:
                  if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                  else:
                      munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
      else:
          if not mstor18:
              require ext_code.size(addr(mstor23))
              static call addr(mstor23).0x505ef22f with:
                      gas gas_remaining wei
                     args caller, 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] <= 0:
                  if not ext_call.return_data[0]:
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = ext_call.return_data[0] + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                      else:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                  else:
                      require ext_code.size(addr(mstor24))
                      static call addr(mstor24).0x78005297 with:
                              gas gas_remaining wei
                             args mstor4m[m_param1m]m.field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = ext_call.return_data[0] + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if ext_call.return_data[0] > 0:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                          else:
                              munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
              else:
                  if not ext_call.return_data[0]:
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                      else:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                  else:
                      require ext_code.size(addr(mstor24))
                      static call addr(mstor24).0x78005297 with:
                              gas gas_remaining wei
                             args mstor4m[m_param1m]m.field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if ext_call.return_data[0] > 0:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                          else:
                              munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
          else:
              require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
              require ext_code.size(addr(mstor23))
              static call addr(mstor23).0x505ef22f with:
                      gas gas_remaining wei
                     args caller, 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                  if not ext_call.return_data[0]:
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = ext_call.return_data[0] + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                      else:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                  else:
                      require ext_code.size(addr(mstor24))
                      static call addr(mstor24).0x78005297 with:
                              gas gas_remaining wei
                             args mstor4m[m_param1m]m.field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = ext_call.return_data[0] + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if ext_call.return_data[0] > 0:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                          else:
                              munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
              else:
                  if not ext_call.return_data[0]:
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = (ext_call.return_data[0] * mstor18 / 100) + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                      else:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                  else:
                      require ext_code.size(addr(mstor24))
                      static call addr(mstor24).0x78005297 with:
                              gas gas_remaining wei
                             args mstor4m[m_param1m]m.field_512
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(addr(mstor25))
                      call addr(mstor25).0x4c47e71d with:
                           gas gas_remaining wei
                          args caller, munknown39bb9607
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94midx = 0
                      [94ms = 0
                      [94ms = ext_call.return_data[0]
                      [94mt = 1
                      [94mu = (ext_call.return_data[0] * mstor18 / 100) + 10^18
                      mwhile [94midx < mstor11m[callerm]m.field_0m:
                          require [94midx < mstor11m[callerm]m.field_0
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 != caller:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          if block.timestamp - munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_512 <= munknown39bb9607:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          require ext_code.size(addr(mstor23))
                          static call addr(mstor23).0x505ef22f with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, mstor4m[m_param1m]m.field_512, mem[132 len 28]
                          mem[ceil32(return_data.size) + 192] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if not ext_call.return_data[0]:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = [94ms
                              [94mt = [94mt
                              [94mu = [94mu
                              mcontinue 
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          require ext_code.size(addr(mstor25))
                          static call addr(mstor25).totalBalanceOf(address of) with:
                                  gas gas_remaining wei
                                 args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
                          mem[ceil32(return_data.size) + 192] = 0x4c47e71d00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 196] = munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0
                          mem[ceil32(return_data.size) + 228] = munknown39bb9607
                          require ext_code.size(addr(mstor25))
                          call addr(mstor25).0x4c47e71d with:
                               gas gas_remaining wei
                              args munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_0, munknown39bb9607
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0] == 1:
                              mem[0] = caller
                              mem[32] = 11
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = ext_call.return_data[0] + [94mu + 10^18
                              mcontinue 
                          if not mstor18:
                              mem[0] = caller
                              mem[32] = 11
                              if ext_call.return_data[0] <= 0:
                                  [94midx = [94midx + 1
                                  [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                                  [94ms = ext_call.return_data[0]
                                  [94mt = [94mt + 1
                                  [94mu = [94mu + ext_call.return_data[0] + 10^18
                                  mcontinue 
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + 10^18
                              mcontinue 
                          require ext_call.return_data[0] * mstor18 / mstor18 == ext_call.return_data[0]
                          mem[0] = caller
                          mem[32] = 11
                          if ext_call.return_data[0] <= ext_call.return_data[0] * mstor18 / 100:
                              [94midx = [94midx + 1
                              [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                              [94ms = ext_call.return_data[0]
                              [94mt = [94mt + 1
                              [94mu = [94mu + ext_call.return_data[0] + 10^18
                              mcontinue 
                          [94midx = [94midx + 1
                          [94ms = mstor11m[callerm]m[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94mt = [94mt + 1
                          [94mu = [94mu + (ext_call.return_data[0] * mstor18 / 100) + 10^18
                          mcontinue 
                      if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 2:
                          munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                          munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] == 3:
                              munknown0fec1decm[m_param1m]m[m_param2m]m.field_0 += [94mu
                              munknown0fec1decm[m_param1m]m.field_512 += [94mt
                      if ext_call.return_data[0] > 0:
                          munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
                      else:
                          if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
                          else:
                              munknown0fec1decm[m_param1m]m[1m]m[m_param2m]m.field_0++
      if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
          if ext_call.return_data[0] == munknown0fec1decm[m_param1m]m.field_512:
              log VoteCast(uint256 candidateId=_param1)
      else:
          if not munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0:
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if 0 / ext_call.return_data[0] >= mem[160]:
                  log VoteCast(uint256 candidateId=_param1)
              else:
                  if munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 + munknown0fec1decm[m_param1m]m[1m]m[0m]m.field_0 == ext_call.return_data[0]:
                      log VoteCast(uint256 candidateId=_param1)
          else:
              require 100 * munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 / munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 == 100
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if 100 * munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 / ext_call.return_data[0] >= mem[160]:
                  log VoteCast(uint256 candidateId=_param1)
              else:
                  if munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 + munknown0fec1decm[m_param1m]m[1m]m[0m]m.field_0 == ext_call.return_data[0]:
                      log VoteCast(uint256 candidateId=_param1)


# hash = 0x72870786
# getter = None
# const = None
# payable = True
def unknown72870786(uint256 m_param1, array m_param2, array m_param3) payable: 
  require calldata.size - 4 >= 96
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  if mstor4m[m_param1m]m.field_1280 != caller:
      revert with 0, 'Not authorized'
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  mem[ceil32(m_param2.length) + 128] = m_param3.length
  mem[ceil32(m_param2.length) + 160 len m_param3.length] = m_param3[allm]
  mem[ceil32(m_param2.length) + m_param3.length + 160] = 0
  mstor5m[m_param1m]m.field_0++
  mstor5m[m_param1m]m[mstor5m[m_param1m]m.field_0m]m[m]m.field_0 = Array(len=m_param3.length, data=m_param3[allm])
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 192] = block.timestamp
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160] = 64
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 224] = m_param2.length
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 256 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
  if not m_param2.length % 32:
      log 0x28aed3fd: Mask(8 * -ceil32(_param3.length) + _param3.length + 32, 0, 0), mem[ceil32(_param2.length) + _param3.length + 192 len ceil32(_param3.length) + -_param3.length + 32], _param2.length, Mask(8 * _param2.length, -(8 * _param2.length) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * _param2.length) - 256, _param1, caller, stor5[_param1].field_0 - 1
  else:
      mem[floor32(m_param2.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256] = mem[floor32(m_param2.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + -(m_param2.length % 32) + 288 len m_param2.length % 32]
      log 0x28aed3fd: Mask(8 * -ceil32(_param3.length) + _param3.length + 32, 0, 0), mem[ceil32(_param2.length) + _param3.length + 192 len ceil32(_param3.length) + -_param3.length + 32], _param2.length, Mask(8 * ceil32(_param2.length), -(8 * ceil32(_param2.length)) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * ceil32(_param2.length)) - 256, mem[(2 * ceil32(_param2.length)) + ceil32(_param3.length) + 256 len floor32(_param2.length) + -ceil32(_param2.length) + 32], _param1, caller, stor5[_param1].field_0 - 1
  if not mstor4m[m_param1m]m.field_512:
      revert with 0, 'Proposal not categorized'
  mstor4m[m_param1m]m.field_1024 = block.timestamp
  mstor4m[m_param1m]m.field_0 = 2
  mem[0] = m_param1
  mem[32] = 4
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160] = 0x253eca1f00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 164] = mstor4m[m_param1m]m.field_512
  require ext_code.size(addr(mstor24))
  static call addr(mstor24).0x253eca1f with:
          gas gas_remaining wei
         args mstor4m[m_param1m]m.field_512
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(m_param2.length) + ceil32(m_param3.length) + ceil32(return_data.size) + 160
  require return_data.size >= 224
  require mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] <= 4294967296
  require mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] + 32 <= return_data.size
  require mem[ceil32(m_param2.length) + ceil32(m_param3.length) + mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] + 160] <= 4294967296 and mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] + (32 * mem[ceil32(m_param2.length) + ceil32(m_param3.length) + mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] + 160]) + 32 <= return_data.size
  require block.timestamp + mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 320] >= mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 320]
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + ceil32(return_data.size) + 160] = block.timestamp + mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 320]
  log 0xc5be51db: mem[ceil32(_param2.length) + ceil32(_param3.length) + ceil32(return_data.size) + 160], _param1


# hash = 0x787112a6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = True
def unknown787112a6(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown787112a6m[m_param1m]


# hash = 0x8263a938
# getter = ['storage', 256, 0, 21]
# const = None
# payable = True
def getProposalLength() payable: 
  return mproposalLength


# hash = 0x9dd86e0f
# getter = None
# const = None
# payable = True
def unknown9dd86e0f(uint64 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x5834e67a with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if Mask(64, 192, m_param1) == 0x474f56484f4c4400000000000000000000000000000000000000000000000000:
      munknown39bb9607 = 24 * 3600 * m_param2
  else:
      if Mask(64, 192, m_param1) == 0x4d4158464f4c0000000000000000000000000000000000000000000000000000:
          mstor20 = m_param2
      else:
          if Mask(64, 192, m_param1) == 0x4d41584452465400000000000000000000000000000000000000000000000000:
              mstor22 = 24 * 3600 * m_param2
          else:
              if Mask(64, 192, m_param1) == 0x4d41584142000000000000000000000000000000000000000000000000000000:
                  require ext_code.size(addr(mstor26))
                  call addr(mstor26).0x8f8c0094 with:
                       gas gas_remaining wei
                      args m_param2
              else:
                  if Mask(64, 192, m_param1) != 0x455054494d450000000000000000000000000000000000000000000000000000:
                      revert with 0, 'Invalid code'
                  require ext_code.size(munknowna0b2d57fAddress)
                  call munknowna0b2d57fAddress.0x78ddbed4 with:
                       gas gas_remaining wei
                      args (24 * 3600 * m_param2)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]


# hash = 0x9ed1c7db
# getter = None
# const = None
# payable = True
def unknown9ed1c7db(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if not m_param1:
      return 1
  mem[96] = 0x253eca1f00000000000000000000000000000000000000000000000000000000
  mem[100] = m_param1
  require ext_code.size(addr(mstor24))
  static call addr(mstor24).0x253eca1f with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 224
  [94m_10 = mem[224]
  require mem[224] <= 4294967296
  require mem[224] + 32 <= return_data.size
  require mem[mem[224] + 96] <= 4294967296 and mem[224] + (32 * mem[mem[224] + 96]) + 32 <= return_data.size
  [94m_27 = mem[mem[224] + 96]
  [94midx = 0
  mwhile [94midx < [94m_27m:
      require [94midx < mem[[94m_10 + 96]
      if mem[(32 * [94midx) + [94m_10 + 128] != 0:
          require [94midx < mem[[94m_10 + 96]
          [94m_33 = mem[(32 * [94midx) + [94m_10 + 128]
          mem[ceil32(return_data.size) + 100] = caller
          mem[ceil32(return_data.size) + 132] = [94m_33
          require ext_code.size(addr(mstor23))
          static call addr(mstor23).0x505ef22f with:
                  gas gas_remaining wei
                 args caller, [94m_33
          mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              mcontinue 
      return 1
  return 0


# hash = 0xa0b2d57f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def unknowna0b2d57f() payable: 
  return munknowna0b2d57fAddress


# hash = 0xaaf86c30
# getter = ['storage', 256, 0, 17]
# const = None
# payable = True
def unknownaaf86c30() payable: 
  return munknownaaf86c30


# hash = 0xb31e1d4d
# getter = None
# const = None
# payable = True
def delegateVote(address m_to) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 1 == bool(ext_call.return_data[0])
  if not munknown787112a6m[callerm]:
      [94midx = munknowne0429d09m[callerm]
      [94ms = 0
      [94mt = 0
      mwhile [94midx < mstor6m[callerm]m:
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
              if caller != caller:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
          require [94midx < mstor6m[callerm]
          if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = [94ms
              [94mt = [94mt
              mcontinue 
          require [94midx < mstor6m[callerm]
          require mstor6m[callerm]m[[94midxm] < mstor2m.length
          if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt
              mcontinue 
          require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
          mem[0] = caller
          mem[32] = 6
          [94midx = [94midx + 1
          [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
          [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
          mcontinue 
  else:
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      if not munknownbb73c562m[mstor9m[callerm]m]m.field_256:
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[callerm]m:
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_512 <= munknown39bb9607:
                  if caller != caller:
                      mem[0] = caller
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[callerm]
              if mstor7m[mstor6m[callerm]m[[94midxm]m]m[callerm]:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[callerm]
              require mstor6m[callerm]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = caller
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = caller
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[callerm]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
      else:
          require munknown787112a6m[callerm] < munknownbb73c562m.length
          [94midx = munknowne0429d09m[callerm]
          [94ms = 0
          [94mt = 0
          mwhile [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m:
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_512 <= munknownbb73c562m[mstor9m[callerm]m]m.field_512 + munknown39bb9607:
                  if munknownbb73c562m[mstor9m[callerm]m]m.field_256 != caller:
                      mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                      mem[32] = 6
                      [94midx = [94midx + 1
                      [94ms = [94ms
                      [94mt = [94mt
                      mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              if mstor7m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m[callerm]:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  [94mt = [94mt
                  mcontinue 
              require [94midx < mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]
              require mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm] < mstor2m.length
              if munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512 <= 0:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              if mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_0 <= 2:
                  mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
                  mem[32] = 6
                  [94midx = [94midx + 1
                  [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
                  [94mt = [94mt
                  mcontinue 
              require munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512
              mem[0] = munknownbb73c562m[mstor9m[callerm]m]m.field_256
              mem[32] = 6
              [94midx = [94midx + 1
              [94ms = mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256
              [94mt = [94mt + (mstor4m[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_768 / munknown0fec1decm[mstor2m[mstor6m[mstor3m[mstor9m[callerm]m]m.field_256m]m[[94midxm]m]m.field_256m]m.field_512)
              mcontinue 
  if [94mt:
      revert with 0, 'Claim pending rewards'
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require munknown787112a6m[addr(m_to)m] < munknownbb73c562m.length
  require not munknownbb73c562m[mstor9m[addr(m_to)m]m]m.field_256
  if munknown787112a6m[callerm]:
      require munknown787112a6m[callerm] < munknownbb73c562m.length
      require munknown39bb9607 + munknownbb73c562m[mstor9m[callerm]m]m.field_512 >= munknownbb73c562m[mstor9m[callerm]m]m.field_512
      require munknown39bb9607 + munknownbb73c562m[mstor9m[callerm]m]m.field_512 < block.timestamp
  [94midx = 0
  mwhile [94midx < mstor11m[callerm]m.field_0m:
      require [94midx < mstor11m[callerm]m.field_0
      require mstor11m[callerm]m[[94midxm]m.field_0 < munknownbb73c562m.length
      if munknownbb73c562m[mstor11m[callerm]m[[94midxm]m.field_0m]m.field_256 == caller:
          revert with 0, 'Already a leader'
      mem[0] = caller
      mem[32] = 11
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(addr(mstor23))
  static call addr(mstor23).0x505ef22f with:
          gas gas_remaining wei
         args caller, 3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(mstor23))
  static call addr(mstor23).0x505ef22f with:
          gas gas_remaining wei
         args caller, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require mstor10m[addr(m_to)m] < mstor20
  if mstor6m[callerm]:
      require 1 <= mstor6m[callerm]
      require mstor6m[callerm] - 1 < mstor6m[callerm]
      require mstor6m[callerm]m[mstor6m[callerm]m] < mstor2m.length
      require munknown39bb9607 + mstor2m[mstor6m[callerm]m[mstor6m[callerm]m]m]m.field_512 >= mstor2m[mstor6m[callerm]m[mstor6m[callerm]m]m]m.field_512
      require munknown39bb9607 + mstor2m[mstor6m[callerm]m[mstor6m[callerm]m]m]m.field_512 < block.timestamp
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args m_to
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require mstor13m[addr(m_to)m]
  munknownbb73c562m.length++
  munknownbb73c562m[munknownbb73c562m.lengthm]m.field_0 = caller
  mstorC257m[mstor3m.lengthm] = m_to
  mstorC257m[mstor3m.lengthm] = block.timestamp
  munknown787112a6m[callerm] = munknownbb73c562m.length - 1
  mstor11m[addr(m_to)m]m.field_0++
  mstor11m[addr(m_to)m]m[mstor11m[addr(m_to)m]m.field_0m]m.field_0 = munknownbb73c562m.length - 1
  mstor10m[addr(m_to)m]++
  munknowne0429d09m[callerm] = mstor6m[addr(m_to)m]


# hash = 0xbb73c562
# getter = ['struct', ['loc', 3]]
# const = None
# payable = True
def unknownbb73c562(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1 < munknownbb73c562m.length
  return munknownbb73c562m[m_param1m]m.field_0, munknownbb73c562m[m_param1m]m.field_256, munknownbb73c562m[m_param1m]m.field_512


# hash = 0xbcc81c0c
# getter = None
# const = None
# payable = True
def unknownbcc81c0c(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  mem[96] = 0x253eca1f00000000000000000000000000000000000000000000000000000000
  mem[100] = mstor4m[m_param1m]m.field_512
  require ext_code.size(addr(mstor24))
  static call addr(mstor24).0x253eca1f with:
          gas gas_remaining wei
         args mstor4m[m_param1m]m.field_512
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 224
  require mem[224] <= 4294967296
  require mem[224] + 32 <= return_data.size
  require mem[mem[224] + 96] <= 4294967296 and mem[224] + (32 * mem[mem[224] + 96]) + 32 <= return_data.size
  if mstor4m[m_param1m]m.field_0 != 2:
      if mstor4m[m_param1m]m.field_0 <= 2:
          return 0
      return 2
  require ext_code.size(addr(mstor23))
  static call addr(mstor23).0xdc6f847 with:
          gas gas_remaining wei
         args mstor4m[m_param1m]m.field_512, mem[132 len 28]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor4m[m_param1m]m.field_512, mem[132 len 28] != 1:
      if ext_call.return_data[0] != munknown0fec1decm[m_param1m]m.field_512:
          require mem[256] + mstor4m[m_param1m]m.field_1024 >= mstor4m[m_param1m]m.field_1024
          if mem[256] + mstor4m[m_param1m]m.field_1024 > block.timestamp:
              return 0
  else:
      if not munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0:
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if 0 / ext_call.return_data[0] < mem[160]:
              if munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 + munknown0fec1decm[m_param1m]m[1m]m[0m]m.field_0 != ext_call.return_data[0]:
                  require mem[256] + mstor4m[m_param1m]m.field_1024 >= mstor4m[m_param1m]m.field_1024
                  if mem[256] + mstor4m[m_param1m]m.field_1024 > block.timestamp:
                      return 0
      else:
          require 100 * munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 / munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 == 100
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if 100 * munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 / ext_call.return_data[0] < mem[160]:
              if munknown0fec1decm[m_param1m]m[1m]m[1m]m.field_0 + munknown0fec1decm[m_param1m]m[1m]m[0m]m.field_0 != ext_call.return_data[0]:
                  require mem[256] + mstor4m[m_param1m]m.field_1024 >= mstor4m[m_param1m]m.field_1024
                  if mem[256] + mstor4m[m_param1m]m.field_1024 > block.timestamp:
                      return 0
  return 1


# hash = 0xc1457fa0
# getter = None
# const = None
# payable = True
def unknownc1457fa0() payable: 
  require calldata.size - 4 >= 32


# hash = 0xc2fe2022
# getter = None
# const = None
# payable = True
def getFollowers(address m_user) payable: 
  require calldata.size - 4 >= 32
  if not mstor11m[addr(m_user)m]m.field_0:
      mem[(32 * mstor11m[addr(m_user)m]m.field_0) + 128] = 32
      mem[(32 * mstor11m[addr(m_user)m]m.field_0) + 160] = mstor11m[addr(m_user)m]m.field_0
      mem[(32 * mstor11m[addr(m_user)m]m.field_0) + 192 len floor32(mstor11m[addr(m_user)m]m.field_0)] = mem[128 len floor32(mstor11m[addr(m_user)m]m.field_0)]
      return memory
        from (32 * mstor11m[addr(m_user)m]m.field_0) + 128
         [93mlen (96 * mstor11m[addr(m_user)m]m.field_0) + 64
  mem[128] = mstor11m[addr(m_user)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor11m[addr(m_user)m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = mstor11m[addr(m_user)m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor11m[addr(m_user)m]m.field_0) + 192 len floor32(mstor11m[addr(m_user)m]m.field_0)] = mem[128 len floor32(mstor11m[addr(m_user)m]m.field_0)]
  return Array(len=mstor11m[addr(m_user)m]m.field_0, data=mem[128 len floor32(mstor11m[addr(m_user)m]m.field_0)], mem[(32 * mstor11m[addr(m_user)m]m.field_0) + floor32(mstor11m[addr(m_user)m]m.field_0) + 192 len (32 * mstor11m[addr(m_user)m]m.field_0) - floor32(mstor11m[addr(m_user)m]m.field_0)]), 


# hash = 0xd46655f4
# getter = None
# const = None
# payable = True
def unknownd46655f4(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if munknowna0b2d57fAddress:
      if munknowna0b2d57fAddress != caller:
          revert with 0, 'Not master'
  munknowna0b2d57fAddress = m_param1
  munknownf17a3becAddress = m_param1


# hash = 0xd5950ad1
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 13]]]]
# const = None
# payable = True
def unknownd5950ad1(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return bool(mstor13m[m_param1m])


# hash = 0xe0429d09
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = True
def unknowne0429d09(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknowne0429d09m[m_param1m]


# hash = 0xe3b34c88
# getter = None
# const = None
# payable = True
def unknowne3b34c88(uint256 m_param1, array m_param2, array m_param3, array m_param4) payable: 
  require calldata.size - 4 >= 128
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  if mstor4m[m_param1m]m.field_1280 != caller:
      revert with 0, 'Not authorized'
  if 2 <= mstor5m[m_param1m]m.field_0:
      revert with 0, 'Solution submitted'
  mstor4m[m_param1m]m.field_0 = 0
  mstor4m[m_param1m]m.field_512 = 0
  mstor4m[m_param1m]m.field_768 = 0
  mem[ceil32(m_param2.length) + 256] = m_param3.length
  mem[ceil32(m_param2.length) + 288 len m_param3.length] = m_param3[allm]
  mem[m_param3.length + ceil32(m_param2.length) + 288] = 0
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 288] = m_param4.length
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 320 len m_param4.length] = m_param4[allm]
  mem[m_param4.length + ceil32(m_param2.length) + ceil32(m_param3.length) + 320] = 0
  log 0x47010640: block.timestamp, 128, ceil32(_param2.length) + 160, ceil32(_param2.length) + ceil32(_param3.length) + 192, _param2.length, _param2[all], 0, mem[_param2.length + 288 len ceil32(_param2.length) + ceil32(_param3.length) + -_param2.length + 32], _param4[all], mem[ceil32(_param2.length) + ceil32(_param3.length) + _param4.length + 320 len ceil32(_param4.length) - _param4.length], stor4[_param1].field_1280, _param1


# hash = 0xeeff9188
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 12]]]]
# const = None
# payable = True
def unknowneeff9188(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown0fec1decm[m_param1m]m.field_512


# hash = 0xf0466c73
# getter = None
# const = None
# payable = True
def unknownf0466c73(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if munknown787112a6m[addr(m_param1)m]:
      require munknown787112a6m[addr(m_param1)m] < munknownbb73c562m.length
      mstor10m[mstor3m[mstor9m[addr(m_param1)m]m]m.field_256m]--
      munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_256 = 0
      munknownbb73c562m[mstor9m[addr(m_param1)m]m]m.field_512 = block.timestamp
      munknowne0429d09m[callerm] = mstor6m[callerm]


# hash = 0xf17a3bec
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def unknownf17a3bec() payable: 
  return munknownf17a3becAddress


# hash = 0xf213d00c
# getter = None
# const = None
# payable = True
def unknownf213d00c() payable: 
  require calldata.size - 4 >= 32


# hash = 0xfa17e84d
# getter = None
# const = None
# payable = True
def unknownfa17e84d(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  [94midx = 0
  mwhile [94midx < mstor11m[addr(m_param1)m]m.field_0m:
      require [94midx < mstor11m[addr(m_param1)m]m.field_0
      require mstor11m[addr(m_param1)m]m[[94midxm]m.field_0 < munknownbb73c562m.length
      if munknownbb73c562m[mstor11m[addr(m_param1)m]m[[94midxm]m.field_0m]m.field_256 == m_param1:
          return 1
      mem[0] = m_param1
      mem[32] = 11
      [94midx = [94midx + 1
      mcontinue 
  return 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


