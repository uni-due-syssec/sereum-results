# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAAcC2a7ef85F024B31EA0A1335AD799036B8263f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown1ccf8abe # mask: a s
    # storage address 1
    unknown9eed8369 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    unknown101158af # mask: a s
    # storage address 6
    unknown85a38635 # mask: a s
    # storage address 7
    unknownb0cccc84 # mask: a s
    # storage address 8
    closed # mask: a s
    # storage address 9
    unknown5f5300ff # mask: a s
    # storage address 10
    threshold # mask: a s
    # storage address 11
    unknown7ddb5e65 # mask: a s
    # storage address 12
    stor12
    # storage address 13
    unknowne54c495a # mask: a s
    # storage address 14
    unknownd6f5c939 # mask: a s
    # storage address 15
    stor15
# hash = 0x02a251a3
# getter = None
# const = ['return', 604800]
# payable = False
const unknown02a251a3 = (168 * 24 * 3600)


# hash = 0x101158af
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown101158af(): # not payable
  return munknown101158af


# hash = 0x1ccf8abe
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def unknown1ccf8abe(): # not payable
  return munknown1ccf8abe


# hash = 0x42cde4e8
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def threshold(): # not payable
  return mthreshold


# hash = 0x597e1fb5
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def closed(): # not payable
  return bool(mclosed)


# hash = 0x5f5300ff
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown5f5300ff(): # not payable
  return munknown5f5300ff


# hash = 0x73b2e80e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 15]]]]
# const = None
# payable = False
def hasClaimed(address m_param1): # not payable
  return bool(mstor15m[addr(m_param1)m])


# hash = 0x7ddb5e65
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknown7ddb5e65(): # not payable
  return munknown7ddb5e65


# hash = 0x81c65884
# getter = None
# const = None
# payable = True
def unknown81c65884(uint256 m_param1) payable: 
  require munknown101158af <= block.timestamp
  require munknown85a38635 >= block.timestamp
  require not mstor3m[callerm]
  require call.value == 5 * 10^16
  require not mclosed
  if 1 == m_param1:
      munknown1ccf8abe++
  else:
      require 2 == m_param1
      munknown9eed8369++
  mstor3m[callerm] = 1
  mstor4m[callerm] = m_param1
  munknown5f5300ff++
  mstor12m[callerm] = call.value


# hash = 0x85a38635
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown85a38635(): # not payable
  return munknown85a38635


# hash = 0x9eed8369
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def unknown9eed8369(): # not payable
  return munknown9eed8369


# hash = 0xa97b8b4d
# getter = None
# const = None
# payable = False
def unknowna97b8b4d(): # not payable
  require not mclosed
  require block.timestamp > munknown85a38635
  if not munknown9eed8369:
      require munknown5f5300ff
      if not munknown1ccf8abe:
          require munknown5f5300ff
          if 0 / munknown5f5300ff == 0 / munknown5f5300ff:
              if 50000 == mthreshold:
                  munknownb0cccc84 = 9
                  mclosed = 1
                  munknownd6f5c939 = 1
                  return 9
      else:
          require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
          require munknown5f5300ff
          if 100000 * munknown1ccf8abe / munknown5f5300ff == 0 / munknown5f5300ff:
              if 50000 == mthreshold:
                  munknownb0cccc84 = 9
                  mclosed = 1
                  munknownd6f5c939 = 1
                  return 9
  else:
      require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
      require munknown5f5300ff
      if not munknown1ccf8abe:
          require munknown5f5300ff
          if 0 / munknown5f5300ff == 100000 * munknown9eed8369 / munknown5f5300ff:
              if 50000 == mthreshold:
                  munknownb0cccc84 = 9
                  mclosed = 1
                  munknownd6f5c939 = 1
                  return 9
      else:
          require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
          require munknown5f5300ff
          if 100000 * munknown1ccf8abe / munknown5f5300ff == 100000 * munknown9eed8369 / munknown5f5300ff:
              if 50000 == mthreshold:
                  munknownb0cccc84 = 9
                  mclosed = 1
                  munknownd6f5c939 = 1
                  return 9
  if not munknown1ccf8abe:
      require munknown5f5300ff
      if 0 / munknown5f5300ff >= mthreshold:
          munknownb0cccc84 = 1
          require ext_code.size(mstor2)
          call mstor2.getLosersOnePercent(uint256 loser) with:
               gas gas_remaining - 710 wei
              args 2
          require ext_call.success
          munknown7ddb5e65 = ext_call.return_data[0]
          require ext_call.return_data[0] + (5 * 10^16 * munknown9eed8369) >= 5 * 10^16 * munknown9eed8369
          require munknown1ccf8abe
          munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown9eed8369) / munknown1ccf8abe
      else:
          if not munknown9eed8369:
              require munknown5f5300ff
              if 0 / munknown5f5300ff >= mthreshold:
                  munknownb0cccc84 = 2
                  require ext_code.size(mstor2)
                  call mstor2.getLosersOnePercent(uint256 loser) with:
                       gas gas_remaining - 710 wei
                      args 3
                  require ext_call.success
                  munknown7ddb5e65 = ext_call.return_data[0]
                  require ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) >= 5 * 10^16 * munknown1ccf8abe
                  require munknown9eed8369
                  munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) / munknown9eed8369
              else:
                  if not munknown9eed8369:
                      require munknown5f5300ff
                      if 0 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  else:
                      require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
                      require munknown5f5300ff
                      if 100000 * munknown9eed8369 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  munknownb0cccc84 = 0
          else:
              require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
              require munknown5f5300ff
              if 100000 * munknown9eed8369 / munknown5f5300ff >= mthreshold:
                  munknownb0cccc84 = 2
                  require ext_code.size(mstor2)
                  call mstor2.getLosersOnePercent(uint256 loser) with:
                       gas gas_remaining - 710 wei
                      args 3
                  require ext_call.success
                  munknown7ddb5e65 = ext_call.return_data[0]
                  require ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) >= 5 * 10^16 * munknown1ccf8abe
                  require munknown9eed8369
                  munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) / munknown9eed8369
              else:
                  if not munknown9eed8369:
                      require munknown5f5300ff
                      if 0 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  else:
                      require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
                      require munknown5f5300ff
                      if 100000 * munknown9eed8369 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  munknownb0cccc84 = 0
  else:
      require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
      require munknown5f5300ff
      if 100000 * munknown1ccf8abe / munknown5f5300ff >= mthreshold:
          munknownb0cccc84 = 1
          require ext_code.size(mstor2)
          call mstor2.getLosersOnePercent(uint256 loser) with:
               gas gas_remaining - 710 wei
              args 2
          require ext_call.success
          munknown7ddb5e65 = ext_call.return_data[0]
          require ext_call.return_data[0] + (5 * 10^16 * munknown9eed8369) >= 5 * 10^16 * munknown9eed8369
          require munknown1ccf8abe
          munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown9eed8369) / munknown1ccf8abe
      else:
          if not munknown9eed8369:
              require munknown5f5300ff
              if 0 / munknown5f5300ff >= mthreshold:
                  munknownb0cccc84 = 2
                  require ext_code.size(mstor2)
                  call mstor2.getLosersOnePercent(uint256 loser) with:
                       gas gas_remaining - 710 wei
                      args 3
                  require ext_call.success
                  munknown7ddb5e65 = ext_call.return_data[0]
                  require ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) >= 5 * 10^16 * munknown1ccf8abe
                  require munknown9eed8369
                  munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) / munknown9eed8369
              else:
                  if not munknown9eed8369:
                      require munknown5f5300ff
                      if 0 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  else:
                      require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
                      require munknown5f5300ff
                      if 100000 * munknown9eed8369 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  munknownb0cccc84 = 0
          else:
              require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
              require munknown5f5300ff
              if 100000 * munknown9eed8369 / munknown5f5300ff >= mthreshold:
                  munknownb0cccc84 = 2
                  require ext_code.size(mstor2)
                  call mstor2.getLosersOnePercent(uint256 loser) with:
                       gas gas_remaining - 710 wei
                      args 3
                  require ext_call.success
                  munknown7ddb5e65 = ext_call.return_data[0]
                  require ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) >= 5 * 10^16 * munknown1ccf8abe
                  require munknown9eed8369
                  munknowne54c495a = ext_call.return_data[0] + (5 * 10^16 * munknown1ccf8abe) / munknown9eed8369
              else:
                  if not munknown9eed8369:
                      require munknown5f5300ff
                      if 0 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  else:
                      require 100000 * munknown9eed8369 / munknown9eed8369 == 100000
                      require munknown5f5300ff
                      if 100000 * munknown9eed8369 / munknown5f5300ff > 50000:
                          require munknown9eed8369
                          munknowne54c495a = 5 * 10^16 * munknown1ccf8abe / munknown9eed8369
                      else:
                          if not munknown1ccf8abe:
                              require munknown5f5300ff
                              if 0 / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                          else:
                              require 100000 * munknown1ccf8abe / munknown1ccf8abe == 100000
                              require munknown5f5300ff
                              if 100000 * munknown1ccf8abe / munknown5f5300ff <= 50000:
                                  munknownd6f5c939 = 1
                                  munknowne54c495a = 0
                              else:
                                  require munknown1ccf8abe
                                  munknowne54c495a = 5 * 10^16 * munknown9eed8369 / munknown1ccf8abe
                  munknownb0cccc84 = 0
  mclosed = 1
  return munknownb0cccc84


# hash = 0xb0cccc84
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknownb0cccc84(): # not payable
  return munknownb0cccc84


# hash = 0xc00007b0
# getter = None
# const = None
# payable = False
def getReward(address m_a): # not payable
  require mclosed
  require mstor3m[addr(m_a)m]
  require not mstor15m[addr(m_a)m]
  if munknownd6f5c939:
      call m_a with:
         value mstor12m[addr(m_a)m] wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
  if mstor4m[addr(m_a)m] == munknownb0cccc84:
      call m_a with:
         value munknowne54c495a + mstor12m[addr(m_a)m] wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
  mstor15m[addr(m_a)m] = 1


# hash = 0xd6f5c939
# getter = ['bool', ['storage', 8, 0, 14]]
# const = None
# payable = False
def unknownd6f5c939(): # not payable
  return bool(munknownd6f5c939)


# hash = 0xe54c495a
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknowne54c495a(): # not payable
  return munknowne54c495a


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


