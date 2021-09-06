# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAb7B362C76D2785bB3a3c368fe27dA93D579BB64 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 4
    name
    # storage address 5
    symbol
    # storage address 6
    decimals # mask: a s
    # storage address 7
    chainStartTime # mask: a s
    # storage address 8
    chainStartBlockNumber # mask: a s
    # storage address 9
    stakeStartTime # mask: a s
    # storage address 10
    stakeMinAge # mask: a s
    # storage address 11
    stakeMaxAge # mask: a s
    # storage address 12
    maxMintProofOfStake # mask: a s
    # storage address 13
    totalSupply # mask: a s
    # storage address 14
    maxTotalSupply # mask: a s
    # storage address 15
    totalInitialSupply # mask: a s
    # storage address 16
    balanceOf
    # storage address 17
    stor17
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x1249c58b
# getter = None
# const = None
# payable = False
def mint(): # not payable
  require mtotalSupply < mmaxTotalSupply
  if uint256(mbalanceOfm[callerm]) > 0:
      if mstor17m[callerm]m.field_0 > 0:
          require block.timestamp >= mstakeStartTime
          require mstakeStartTime > 0
          if mstor17m[callerm]m.field_0 > 0:
              [94midx = 0
              mwhile [94midx < mstor17m[callerm]m.field_0m:
                  require [94midx < mstor17m[callerm]m.field_0
                  require mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[callerm]m[[94midxm]m.field_128
                  if block.timestamp >= mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge:
                      require [94midx < mstor17m[callerm]m.field_0
                      require mstor17m[callerm]m[[94midxm]m.field_128 <= block.timestamp
                      require [94midx < mstor17m[callerm]m.field_0
                      if block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 <= mstakeMaxAge:
                          require mstor17m[callerm]m[[94midxm]m.field_0 * block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 / 24 * 3600 >= 0
                      else:
                          require mstor17m[callerm]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
                  mem[0] = caller
                  mem[32] = 17
                  [94midx = [94midx + 1
                  mcontinue 
              return 0
          else:
              return 0
      else:
          return 0
  else:
      return 0


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x2ab4d052
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def maxTotalSupply(): # not payable
  return mmaxTotalSupply


# hash = 0x313ce567
# getter = ['storage', 8, 0, 6]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x42cbb15c
# getter = None
# const = None
# payable = False
def getBlockNumber(): # not payable
  require mchainStartBlockNumber <= block.number
  return (block.number - mchainStartBlockNumber)


# hash = 0x5b054f9b
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def chainStartTime(): # not payable
  return mchainStartTime


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 16]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return uint256(mbalanceOfm[addr(m_owner)m])


# hash = 0x7419f190
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def stakeStartTime(): # not payable
  return mstakeStartTime


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x9fd4da40
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def totalInitialSupply(): # not payable
  return mtotalInitialSupply


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  if ext_code.size(m_to) <= 0:
      if caller == m_to:
          require mtotalSupply < mmaxTotalSupply
          if uint256(mbalanceOfm[callerm]) > 0:
              if mstor17m[callerm]m.field_0 > 0:
                  require block.timestamp >= mstakeStartTime
                  require mstakeStartTime > 0
                  if mstor17m[callerm]m.field_0 > 0:
                      [94midx = 0
                      mwhile [94midx < mstor17m[callerm]m.field_0m:
                          require [94midx < mstor17m[callerm]m.field_0
                          require mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[callerm]m[[94midxm]m.field_128
                          if block.timestamp >= mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge:
                              require [94midx < mstor17m[callerm]m.field_0
                              require mstor17m[callerm]m[[94midxm]m.field_128 <= block.timestamp
                              require [94midx < mstor17m[callerm]m.field_0
                              if block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 <= mstakeMaxAge:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 / 24 * 3600 >= 0
                              else:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
                          mem[0] = caller
                          mem[32] = 17
                          [94midx = [94midx + 1
                          mcontinue 
                      return 0
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      require uint256(mbalanceOfm[callerm]) >= m_value
      require m_value <= uint256(mbalanceOfm[callerm])
      uint256(mbalanceOfm[callerm]) -= m_value
      require uint256(mbalanceOfm[addr(m_to)m]) + m_value >= uint256(mbalanceOfm[addr(m_to)m])
      uint256(mbalanceOfm[addr(m_to)m]) += m_value
      if mstor17m[callerm]m.field_0 <= 0:
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 <= mstor17m[addr(m_to)m]m.field_0 + 1:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
              log Transfer(
                    address from=_value,
                    address to=caller,
                    uint256 value=_to)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar40001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
      else:
          mstor17m[callerm]m.field_0 = 0
          [94midx = 0
          mwhile mstor17m[callerm]m.field_0 > [94midxm:
              mstor17m[callerm]m[[94midxm]m.field_0 = 0
              mstor17m[callerm]m[[94midxm]m.field_128 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar42001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar49001 = 0
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar49001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
  else:
      if caller == m_to:
          require mtotalSupply < mmaxTotalSupply
          if uint256(mbalanceOfm[callerm]) > 0:
              if mstor17m[callerm]m.field_0 > 0:
                  require block.timestamp >= mstakeStartTime
                  require mstakeStartTime > 0
                  if mstor17m[callerm]m.field_0 > 0:
                      [94midx = 0
                      mwhile [94midx < mstor17m[callerm]m.field_0m:
                          require [94midx < mstor17m[callerm]m.field_0
                          require mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[callerm]m[[94midxm]m.field_128
                          if block.timestamp >= mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge:
                              require [94midx < mstor17m[callerm]m.field_0
                              require mstor17m[callerm]m[[94midxm]m.field_128 <= block.timestamp
                              require [94midx < mstor17m[callerm]m.field_0
                              if block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 <= mstakeMaxAge:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 / 24 * 3600 >= 0
                              else:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
                          mem[0] = caller
                          mem[32] = 17
                          [94midx = [94midx + 1
                          mcontinue 
                      return 0
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      require uint256(mbalanceOfm[callerm]) >= m_value
      require m_value <= uint256(mbalanceOfm[callerm])
      uint256(mbalanceOfm[callerm]) -= m_value
      require uint256(mbalanceOfm[addr(m_to)m]) + m_value >= uint256(mbalanceOfm[addr(m_to)m])
      uint256(mbalanceOfm[addr(m_to)m]) += m_value
      require ext_code.size(m_to)
      call m_to.tokenFallback(address from, uint256 value, bytes param3) with:
           gas gas_remaining - 710 wei
          args caller, m_value, 96, 0
      require ext_call.success
      if mstor17m[callerm]m.field_0 <= 0:
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 <= mstor17m[addr(m_to)m]m.field_0 + 1:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
              log Transfer(
                    address from=_value,
                    address to=caller,
                    uint256 value=_to)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar46001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
      else:
          mstor17m[callerm]m.field_0 = 0
          [94midx = 0
          mwhile mstor17m[callerm]m.field_0 > [94midxm:
              mstor17m[callerm]m[[94midxm]m.field_0 = 0
              mstor17m[callerm]m[[94midxm]m.field_128 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar48001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar55001 = 0
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar55001 = 0
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
  log ERC223Transfer(address from, address to, uint256 value, bytes data):
                     _value,
                     64,
                     0,
                     caller,
                     _to,
  return 1


# hash = 0xaa9cdaf4
# getter = None
# const = None
# payable = False
def coinAge(address m_staker): # not payable
  if mstor17m[addr(m_staker)m]m.field_0 > 0:
      [94midx = 0
      mwhile [94midx < mstor17m[addr(m_staker)m]m.field_0m:
          require [94midx < mstor17m[addr(m_staker)m]m.field_0
          require mstor17m[addr(m_staker)m]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[addr(m_staker)m]m[[94midxm]m.field_128
          if block.timestamp >= mstor17m[addr(m_staker)m]m[[94midxm]m.field_128 + mstakeMinAge:
              require [94midx < mstor17m[addr(m_staker)m]m.field_0
              require mstor17m[addr(m_staker)m]m[[94midxm]m.field_128 <= block.timestamp
              require [94midx < mstor17m[addr(m_staker)m]m.field_0
              if block.timestamp - mstor17m[addr(m_staker)m]m[[94midxm]m.field_128 <= mstakeMaxAge:
                  require mstor17m[addr(m_staker)m]m[[94midxm]m.field_0 * block.timestamp - mstor17m[addr(m_staker)m]m[[94midxm]m.field_128 / 24 * 3600 >= 0
              else:
                  require mstor17m[addr(m_staker)m]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
          mem[0] = m_staker
          mem[32] = 17
          [94midx = [94midx + 1
          mcontinue 
      return 0
  else:
      return 0


# hash = 0xb2552fc4
# getter = None
# const = None
# payable = False
def annualInterest(): # not payable
  require mstakeStartTime <= block.timestamp
  if not block.timestamp - mstakeStartTime / 8760 * 24 * 3600:
      return (770 * mmaxMintProofOfStake / 100)
  require mstakeStartTime <= block.timestamp
  if block.timestamp - mstakeStartTime / 8760 * 24 * 3600 != 1:
      return mmaxMintProofOfStake
  return (435 * mmaxMintProofOfStake / 100)


# hash = 0xbe45fd62
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value, bytes m_data): # not payable
  if ext_code.size(m_to) <= 0:
      if caller == m_to:
          require mtotalSupply < mmaxTotalSupply
          if uint256(mbalanceOfm[callerm]) > 0:
              if mstor17m[callerm]m.field_0 > 0:
                  require block.timestamp >= mstakeStartTime
                  require mstakeStartTime > 0
                  if mstor17m[callerm]m.field_0 > 0:
                      [94midx = 0
                      mwhile [94midx < mstor17m[callerm]m.field_0m:
                          require [94midx < mstor17m[callerm]m.field_0
                          require mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[callerm]m[[94midxm]m.field_128
                          if block.timestamp >= mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge:
                              require [94midx < mstor17m[callerm]m.field_0
                              require mstor17m[callerm]m[[94midxm]m.field_128 <= block.timestamp
                              require [94midx < mstor17m[callerm]m.field_0
                              if block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 <= mstakeMaxAge:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 / 24 * 3600 >= 0
                              else:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
                          mem[0] = caller
                          mem[32] = 17
                          [94midx = [94midx + 1
                          mcontinue 
                      return 0
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      require uint256(mbalanceOfm[callerm]) >= m_value
      require m_value <= uint256(mbalanceOfm[callerm])
      uint256(mbalanceOfm[callerm]) -= m_value
      require uint256(mbalanceOfm[addr(m_to)m]) + m_value >= uint256(mbalanceOfm[addr(m_to)m])
      uint256(mbalanceOfm[addr(m_to)m]) += m_value
      if mstor17m[callerm]m.field_0 <= 0:
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 <= mstor17m[addr(m_to)m]m.field_0 + 1:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
              log Transfer(
                    address from=_value,
                    address to=caller,
                    uint256 value=_to)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar38001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
      else:
          mstor17m[callerm]m.field_0 = 0
          [94midx = 0
          mwhile mstor17m[callerm]m.field_0 > [94midxm:
              mstor17m[callerm]m[[94midxm]m.field_0 = 0
              mstor17m[callerm]m[[94midxm]m.field_128 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar40001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar47001 = ceil32(m_data.length)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar47001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
  else:
      if caller == m_to:
          require mtotalSupply < mmaxTotalSupply
          if uint256(mbalanceOfm[callerm]) > 0:
              if mstor17m[callerm]m.field_0 > 0:
                  require block.timestamp >= mstakeStartTime
                  require mstakeStartTime > 0
                  if mstor17m[callerm]m.field_0 > 0:
                      [94midx = 0
                      mwhile [94midx < mstor17m[callerm]m.field_0m:
                          require [94midx < mstor17m[callerm]m.field_0
                          require mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge >= mstor17m[callerm]m[[94midxm]m.field_128
                          if block.timestamp >= mstor17m[callerm]m[[94midxm]m.field_128 + mstakeMinAge:
                              require [94midx < mstor17m[callerm]m.field_0
                              require mstor17m[callerm]m[[94midxm]m.field_128 <= block.timestamp
                              require [94midx < mstor17m[callerm]m.field_0
                              if block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 <= mstakeMaxAge:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * block.timestamp - mstor17m[callerm]m[[94midxm]m.field_128 / 24 * 3600 >= 0
                              else:
                                  require mstor17m[callerm]m[[94midxm]m.field_0 * mstakeMaxAge / 24 * 3600 >= 0
                          mem[0] = caller
                          mem[32] = 17
                          [94midx = [94midx + 1
                          mcontinue 
                      return 0
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      require uint256(mbalanceOfm[callerm]) >= m_value
      require m_value <= uint256(mbalanceOfm[callerm])
      uint256(mbalanceOfm[callerm]) -= m_value
      require uint256(mbalanceOfm[addr(m_to)m]) + m_value >= uint256(mbalanceOfm[addr(m_to)m])
      uint256(mbalanceOfm[addr(m_to)m]) += m_value
      require ext_code.size(m_to)
      call m_to.tokenFallback(address from, uint256 value, bytes param3) with:
           gas gas_remaining - 710 wei
          args caller, m_value, Array(len=m_data.length, data=m_data[allm])
      require ext_call.success
      if mstor17m[callerm]m.field_0 <= 0:
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 <= mstor17m[addr(m_to)m]m.field_0 + 1:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
              mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
              log Transfer(
                    address from=_value,
                    address to=caller,
                    uint256 value=_to)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar44001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
      else:
          mstor17m[callerm]m.field_0 = 0
          [94midx = 0
          mwhile mstor17m[callerm]m.field_0 > [94midxm:
              mstor17m[callerm]m[[94midxm]m.field_0 = 0
              mstor17m[callerm]m[[94midxm]m.field_128 = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor17m[callerm]m.field_0++
          if not mstor17m[callerm]m.field_0 > mstor17m[callerm]m.field_0 + 1:
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar46001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar53001 = ceil32(m_data.length)
          else:
              [94midx = mstor17m[callerm]m.field_0 + 1
              mwhile mstor17m[callerm]m.field_0 > [94midxm:
                  mstor17m[callerm]m[[94midxm]m.field_0 = 0
                  mstor17m[callerm]m[[94midxm]m.field_128 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_0 = uint128(mbalanceOfm[callerm])
              mstor17m[callerm]m[mstor17m[callerm]m.field_0m]m.field_128 = uint64(block.timestamp)
              mstor17m[addr(m_to)m]m.field_0++
              if not mstor17m[addr(m_to)m]m.field_0 > mstor17m[addr(m_to)m]m.field_0 + 1:
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
                  [94mvar53001 = ceil32(m_data.length)
              else:
                  [94midx = mstor17m[addr(m_to)m]m.field_0 + 1
                  mwhile mstor17m[addr(m_to)m]m.field_0 > [94midxm:
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_0 = 0
                      mstor17m[addr(m_to)m]m[[94midxm]m.field_128 = 0
                      [94midx = [94midx + 1
                      mcontinue 
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_0 = uint128(m_value)
                  mstor17m[addr(m_to)m]m[mstor17m[addr(m_to)m]m.field_0m]m.field_128 = uint64(block.timestamp)
                  log Transfer(
                        address from=_value,
                        address to=caller,
                        uint256 value=_to)
  log ERC223Transfer(
        address from=_value,
        address to=Array(len=_data.length, data=_data[all]),
        uint256 value=caller,
        bytes data=_to)
  return 1


# hash = 0xcbd8877e
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def stakeMinAge(): # not payable
  return mstakeMinAge


# hash = 0xcd474b04
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def chainStartBlockNumber(): # not payable
  return mchainStartBlockNumber


# hash = 0xe1c3bac6
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def stakeMaxAge(): # not payable
  return mstakeMaxAge


# hash = 0xf2bb5ce1
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def maxMintProofOfStake(): # not payable
  return mmaxMintProofOfStake


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


