# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x88e1315687AeC48a72786c6B3b3F075208B62713 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x77228659': 'query2(uint256 _timestamp, string _datasource, string _arg1, string _arg2)', '0x7e1c4205': 'query2(uint256 _timestamp, string _datasource, string _arg1, string _arg2, uint256 _gaslimit)', '0x85dee34c': 'query2_withGasLimit(uint256 _timestamp, string _datasource, string _arg1, string _arg2, uint256 _gaslimit)', '0xe839e65e': 'query2(string _datasource, string _arg1, string _arg2)'} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    cbAddress # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6
    # storage address 7
    stor7
    # storage address 8
    baseprice # mask: a s
    # storage address 9
    stor9
    # storage address 10
    stor10
    # storage address 11
    stor11
# hash = 0x0f825673
# getter = None
# const = None
# payable = True
def deleteCoupon(string _code) payable: 
  if stor2 != caller:
      require caller == cbAddress
  stor3[_code[all]] = 0


# hash = 0x23dc42e7
# getter = None
# const = None
# payable = True
def query1(uint256 _timestamp, string _datasource, string _arg) payable: 
  if 0 == stor0[caller]:
      require call.value >= 0
      if call.value > 0:
          call caller with:
             value call.value wei
               gas 0 wei
  else:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require 200000 <= block.gas_limit
  stor0[caller]++
  mem[ceil32(_datasource.length) + ceil32(_arg.length) + 448 len _datasource.length] = _datasource[all]
  if not _datasource.length % 32:
      mem[_datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480] = mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 512 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + _arg.length + 480 len -(_arg.length % 32) + 32],
  else:
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 448] = mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_datasource.length % 32) + 480 len _datasource.length % 32]
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512] = mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 544 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + floor32(_datasource.length) + _arg.length + 512 len -(_arg.length % 32) + 32],
  return sha3(this.address + caller + stor0[caller])


# hash = 0x2ef3accc
# getter = None
# const = None
# payable = True
def getPrice(string _datasource, uint256 _gaslimit) payable: 
  if _gaslimit <= 200000:
      if 0 == stor0[caller]:
          return 0
  if stor4 != 0:
      if 1 == stor3[stor4]:
          return 0
  if stor7[caller] != 0:
      return ((stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]])
  return ((stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]])


# hash = 0x45362978
# getter = None
# const = None
# payable = True
def query1(string _datasource, string _arg) payable: 
  if 0 == stor0[caller]:
      require call.value >= 0
      if call.value > 0:
          call caller with:
             value call.value wei
               gas 0 wei
  else:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  require 0 <= block.timestamp + (1440 * 24 * 3600)
  require 200000 <= block.gas_limit
  stor0[caller]++
  mem[ceil32(_datasource.length) + ceil32(_arg.length) + 448 len _datasource.length] = _datasource[all]
  if not _datasource.length % 32:
      mem[_datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480] = mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 512 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + _arg.length + 480 len -(_arg.length % 32) + 32],
  else:
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 448] = mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_datasource.length % 32) + 480 len _datasource.length % 32]
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512] = mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 544 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + floor32(_datasource.length) + _arg.length + 512 len -(_arg.length % 32) + 32],
  return sha3(this.address + caller + stor0[caller])


# hash = 0x480a434d
# getter = ['storage', 256, 0, 8]
# const = None
# payable = True
def baseprice() payable: 
  return baseprice


# hash = 0x524f3889
# getter = None
# const = None
# payable = True
def getPrice(string _datasource) payable: 
  if 0 == stor0[caller]:
      return 0
  if stor4 != 0:
      if 1 == stor3[stor4]:
          return 0
  if stor7[caller] != 0:
      return ((200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]])
  return ((200000 * stor5) + stor9[_datasource[all]][stor6[caller]])


# hash = 0x5c242c59
# getter = None
# const = None
# payable = True
def query1(uint256 _timestamp, string _datasource, string _arg, uint256 _gaslimit) payable: 
  if _gaslimit > 200000:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  else:
      if 0 == stor0[caller]:
          require call.value >= 0
          if call.value > 0:
              call caller with:
                 value call.value wei
                   gas 0 wei
      else:
          if 0 == stor4:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
          else:
              if 1 == stor3[stor4]:
                  require call.value >= 0
                  if call.value > 0:
                      call caller with:
                         value call.value wei
                           gas 0 wei
              else:
                  if stor7[caller] != 0:
                      require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
                  else:
                      require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require _gaslimit <= block.gas_limit
  stor0[caller]++
  log Log1(
        address sender=caller,
        bytes32 cid=sha3(this.address + caller + stor0[caller]),
        uint256 timestamp=_timestamp,
        string datasource=Array(len=_datasource.length, data=_datasource[all]),
        string arg=_datasource.length + 288,
        uint256 gaslimit=_gaslimit,
        bytes1 proofType=stor6[caller],
        uint256 gasPrice=stor7[caller])
  return sha3(this.address + caller + stor0[caller])


# hash = 0x60f66701
# getter = None
# const = None
# payable = True
def useCoupon(string _coupon) payable: 
  stor4 = sha3(_coupon[all])


# hash = 0x62b3b833
# getter = None
# const = None
# payable = True
def createCoupon(string _code) payable: 
  if stor2 != caller:
      require caller == cbAddress
  stor3[_code[all]] = 1


# hash = 0x68742da6
# getter = None
# const = None
# payable = True
def withdrawFunds(address _payee) payable: 
  if stor2 != caller:
      require caller == cbAddress
  call _payee with:
     value eth.balance(this.address) wei
       gas 0 wei


# hash = 0x688dcfd7
# getter = None
# const = None
# payable = True
def setProofType(bytes1 _proofType) payable: 
  stor6[caller] = uint8(_proofType)


# hash = 0x75700437
# getter = None
# const = None
# payable = True
def query1_withGasLimit(uint256 _timestamp, string _datasource, string _arg, uint256 _gaslimit) payable: 
  if _gaslimit > 200000:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  else:
      if 0 == stor0[caller]:
          require call.value >= 0
          if call.value > 0:
              call caller with:
                 value call.value wei
                   gas 0 wei
      else:
          if 0 == stor4:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
          else:
              if 1 == stor3[stor4]:
                  require call.value >= 0
                  if call.value > 0:
                      call caller with:
                         value call.value wei
                           gas 0 wei
              else:
                  if stor7[caller] != 0:
                      require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
                  else:
                      require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require _gaslimit <= block.gas_limit
  stor0[caller]++
  log Log1(
        address sender=caller,
        bytes32 cid=sha3(this.address + caller + stor0[caller]),
        uint256 timestamp=_timestamp,
        string datasource=Array(len=_datasource.length, data=_datasource[all]),
        string arg=_datasource.length + 288,
        uint256 gaslimit=_gaslimit,
        bytes1 proofType=stor6[caller],
        uint256 gasPrice=stor7[caller])
  return sha3(this.address + caller + stor0[caller])


# hash = 0x7d242ae5
# getter = None
# const = None
# payable = True
def setBasePrice(uint256 _new_baseprice, bytes _proofID) payable: 
  if stor2 != caller:
      require caller == cbAddress
  baseprice = _new_baseprice
  [94midx = 0
  while [94midx < stor11.length:
      mem[0] = stor[code.data[6275 len 32] + [94midx]
      mem[32] = 9
      stor9[stor[code.data[6275 len 32] + [94midx]] = _new_baseprice * stor10[stor[[94midx + code.data[6275 len 32]]]
      [94midx = [94midx + 1
      continue 


# hash = 0x81ade307
# getter = None
# const = None
# payable = True
def query(string _datasource, string _arg) payable: 
  if 0 == stor0[caller]:
      require call.value >= 0
      if call.value > 0:
          call caller with:
             value call.value wei
               gas 0 wei
  else:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  require 0 <= block.timestamp + (1440 * 24 * 3600)
  require 200000 <= block.gas_limit
  stor0[caller]++
  mem[ceil32(_datasource.length) + ceil32(_arg.length) + 448 len _datasource.length] = _datasource[all]
  if not _datasource.length % 32:
      mem[_datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480] = mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 512 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + _arg.length + 480 len -(_arg.length % 32) + 32],
  else:
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 448] = mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_datasource.length % 32) + 480 len _datasource.length % 32]
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512] = mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 544 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   0,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + floor32(_datasource.length) + _arg.length + 512 len -(_arg.length % 32) + 32],
  return sha3(this.address + caller + stor0[caller])


# hash = 0xa2ec191a
# getter = None
# const = None
# payable = True
def addDSource(string _dsname, uint256 _multiplier) payable: 
  if stor2 != caller:
      require caller == cbAddress
  stor11.length++
  if not stor11.length <= stor11.length + 1:
      [94midx = stor11.length + 1
      while stor11.length > [94midx:
          stor11[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  require stor11.length < stor11.length
  stor11[stor11.length] = sha3(_dsname[all], 0)
  stor10[('map', ('call.data', ('add', 36, ('param', '_dsname')), ('cd', ('add', 4, ('param', '_dsname')))), ('name', 'stor0', 0))] = _multiplier


# hash = 0xadf59f99
# getter = None
# const = None
# payable = True
def query(uint256 _timestamp, string _datasource, string _arg) payable: 
  if 0 == stor0[caller]:
      require call.value >= 0
      if call.value > 0:
          call caller with:
             value call.value wei
               gas 0 wei
  else:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (200000 * stor7[caller]) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor7[caller]) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (200000 * stor5) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (200000 * stor5) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require 200000 <= block.gas_limit
  stor0[caller]++
  mem[ceil32(_datasource.length) + ceil32(_arg.length) + 448 len _datasource.length] = _datasource[all]
  if not _datasource.length % 32:
      mem[_datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + 480] = mem[floor32(_arg.length) + _datasource.length + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 512 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   _datasource.length + 288,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + _arg.length + 480 len -(_arg.length % 32) + 32],
  else:
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 448] = mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_datasource.length % 32) + 480 len _datasource.length % 32]
      mem[floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512 len _arg.length] = _arg[all]
      if not _arg.length % 32:
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
      else:
          mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + 512] = mem[floor32(_arg.length) + floor32(_datasource.length) + ceil32(_datasource.length) + ceil32(_arg.length) + -(_arg.length % 32) + 544 len _arg.length % 32]
          log Log1(address sender, bytes32 cid, uint256 timestamp, string datasource, string arg, uint256 gaslimit, bytes1 proofType, uint256 gasPrice):
                   caller,
                   sha3(this.address + caller + stor0[caller]),
                   _timestamp,
                   256,
                   floor32(_datasource.length) + 320,
                   200000,
                   stor6[caller],
                   stor7[caller],
                   _datasource.length,
                   _datasource[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + _datasource.length + 448 len -(_datasource.length % 32) + 32],
                   _arg.length,
                   _arg[all],
                   mem[ceil32(_datasource.length) + ceil32(_arg.length) + floor32(_datasource.length) + _arg.length + 512 len -(_arg.length % 32) + 32],
  return sha3(this.address + caller + stor0[caller])


# hash = 0xae815843
# getter = None
# const = None
# payable = True
def query(uint256 _timestamp, string _datasource, string _arg, uint256 _gaslimit) payable: 
  if _gaslimit > 200000:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  else:
      if 0 == stor0[caller]:
          require call.value >= 0
          if call.value > 0:
              call caller with:
                 value call.value wei
                   gas 0 wei
      else:
          if 0 == stor4:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
          else:
              if 1 == stor3[stor4]:
                  require call.value >= 0
                  if call.value > 0:
                      call caller with:
                         value call.value wei
                           gas 0 wei
              else:
                  if stor7[caller] != 0:
                      require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
                  else:
                      require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require _gaslimit <= block.gas_limit
  stor0[caller]++
  log Log1(
        address sender=caller,
        bytes32 cid=sha3(this.address + caller + stor0[caller]),
        uint256 timestamp=_timestamp,
        string datasource=Array(len=_datasource.length, data=_datasource[all]),
        string arg=_datasource.length + 288,
        uint256 gaslimit=_gaslimit,
        bytes1 proofType=stor6[caller],
        uint256 gasPrice=stor7[caller])
  return sha3(this.address + caller + stor0[caller])


# hash = 0xb5bfdd73
# getter = None
# const = None
# payable = True
def addDSource(string _dsname, bytes1 _proofType, uint256 _multiplier) payable: 
  if stor2 != caller:
      require caller == cbAddress
  stor11.length++
  if not stor11.length <= stor11.length + 1:
      [94midx = stor11.length + 1
      while stor11.length > [94midx:
          stor11[[94midx] = 0
          [94midx = [94midx + 1
          continue 
  require stor11.length < stor11.length
  stor11[stor11.length] = sha3(_dsname[all], uint8(_proofType))
  stor10[_dsname[all]][uint8(_proofType)] = _multiplier


# hash = 0xbf1fe420
# getter = None
# const = None
# payable = True
def setGasPrice(uint256 _newgasprice) payable: 
  if stor2 != caller:
      require caller == cbAddress
  stor5 = _newgasprice


# hash = 0xc281d19e
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def cbAddress() payable: 
  return cbAddress


# hash = 0xc51be90f
# getter = None
# const = None
# payable = True
def query_withGasLimit(uint256 _timestamp, string _datasource, string _arg, uint256 _gaslimit) payable: 
  if _gaslimit > 200000:
      if 0 == stor4:
          if stor7[caller] != 0:
              require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
          else:
              require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
              if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                  call caller with:
                     value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                       gas 0 wei
      else:
          if 1 == stor3[stor4]:
              require call.value >= 0
              if call.value > 0:
                  call caller with:
                     value call.value wei
                       gas 0 wei
          else:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
  else:
      if 0 == stor0[caller]:
          require call.value >= 0
          if call.value > 0:
              call caller with:
                 value call.value wei
                   gas 0 wei
      else:
          if 0 == stor4:
              if stor7[caller] != 0:
                  require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
              else:
                  require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                  if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                      call caller with:
                         value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                           gas 0 wei
          else:
              if 1 == stor3[stor4]:
                  require call.value >= 0
                  if call.value > 0:
                      call caller with:
                         value call.value wei
                           gas 0 wei
              else:
                  if stor7[caller] != 0:
                      require call.value >= (stor7[caller] * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor7[caller] * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
                  else:
                      require call.value >= (stor5 * _gaslimit) + stor9[_datasource[all]][stor6[caller]]
                      if call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] > 0:
                          call caller with:
                             value call.value - (stor5 * _gaslimit) - stor9[_datasource[all]][stor6[caller]] wei
                               gas 0 wei
  require _timestamp <= block.timestamp + (1440 * 24 * 3600)
  require _gaslimit <= block.gas_limit
  stor0[caller]++
  log Log1(
        address sender=caller,
        bytes32 cid=sha3(this.address + caller + stor0[caller]),
        uint256 timestamp=_timestamp,
        string datasource=Array(len=_datasource.length, data=_datasource[all]),
        string arg=_datasource.length + 288,
        uint256 gaslimit=_gaslimit,
        bytes1 proofType=stor6[caller],
        uint256 gasPrice=stor7[caller])
  return sha3(this.address + caller + stor0[caller])


# hash = 0xca6ad1e4
# getter = None
# const = None
# payable = True
def setCustomGasPrice(uint256 _gasPrice) payable: 
  stor7[caller] = _gasPrice


# hash = 0xd9597016
# getter = None
# const = None
# payable = True
def multisetCustomGasPrice(uint256[] _gasPrice, address[] _addr) payable: 
  mem[128 len 32 * _gasPrice.length] = call.data[_gasPrice + 36 len 32 * _gasPrice.length]
  mem[(32 * _gasPrice.length) + 128] = _addr.length
  mem[(32 * _gasPrice.length) + 160 len 32 * _addr.length] = call.data[_addr + 36 len 32 * _addr.length]
  if stor2 != caller:
      require caller == cbAddress
  [94midx = 0
  while [94midx < _addr.length:
      require [94midx < _gasPrice.length
      require [94midx < _addr.length
      mem[0] = mem[(32 * _gasPrice.length) + (32 * [94midx) + 172 len 20]
      mem[32] = 7
      stor7[mem[(32 * _gasPrice.length) + (32 * [94midx) + 172 len 20]] = mem[(32 * [94midx) + 128]
      [94midx = [94midx + 1
      continue 


# hash = 0xdb37e42f
# getter = None
# const = None
# payable = True
def multisetProofType(uint256[] _proofType, address[] _addr) payable: 
  mem[128 len 32 * _proofType.length] = call.data[_proofType + 36 len 32 * _proofType.length]
  mem[(32 * _proofType.length) + 128] = _addr.length
  mem[(32 * _proofType.length) + 160 len 32 * _addr.length] = call.data[_addr + 36 len 32 * _addr.length]
  if stor2 != caller:
      require caller == cbAddress
  [94midx = 0
  while [94midx < _addr.length:
      require [94midx < _proofType.length
      require [94midx < _addr.length
      mem[0] = mem[(32 * _proofType.length) + (32 * [94midx) + 172 len 20]
      mem[32] = 6
      stor6[mem[(32 * _proofType.length) + (32 * [94midx) + 172 len 20]] = mem[(32 * [94midx) + 159 len 1]
      [94midx = [94midx + 1
      continue 


# hash = 0xde4b3262
# getter = None
# const = None
# payable = True
def setBasePrice(uint256 _new_baseprice) payable: 
  if stor2 != caller:
      require caller == cbAddress
  baseprice = _new_baseprice
  [94midx = 0
  while [94midx < stor11.length:
      mem[0] = stor[code.data[6275 len 32] + [94midx]
      mem[32] = 9
      stor9[stor[code.data[6275 len 32] + [94midx]] = _new_baseprice * stor10[stor[code.data[6275 len 32] + [94midx]]
      [94midx = [94midx + 1
      continue 


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if stor2 == caller:
      stop
  require caller == cbAddress


