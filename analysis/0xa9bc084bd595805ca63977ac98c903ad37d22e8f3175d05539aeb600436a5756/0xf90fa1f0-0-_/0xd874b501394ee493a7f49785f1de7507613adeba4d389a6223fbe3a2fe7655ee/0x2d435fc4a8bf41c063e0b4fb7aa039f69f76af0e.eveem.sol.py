# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2D435fc4A8bf41c063e0b4fb7aA039f69F76AF0E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    topAddress # mask: a s
    # storage address 1
    ref # mask: a s
    # storage address 2
    second # mask: a s
    # storage address 2
    owner # mask: a s
    # storage address 2
    unknown591710f0 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    first # mask: a s
# hash = 0x17c9a887
# getter = None
# const = None
# payable = False
def unknown17c9a887(bool _param1): # not payable
  require caller == owner
  stor2 = Mask(96, 0, _param1)


# hash = 0x21a78f68
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def ref(): # not payable
  return ref


# hash = 0x3dab5e8b
# getter = None
# const = None
# payable = True
def unknown3dab5e8b(uint256 _param1) payable: 
  unknown591710f0 = 1
  require ext_code.size(topAddress)
  call topAddress.createBet(uint256 referrerID) with:
     value call.value - (10^16 * _param1) wei
       gas gas_remaining wei
      args ref
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94midx = 0
  while [94midx < _param1:
      mem[96] = 0xac793a6000000000000000000000000000000000000000000000000000000000
      mem[100] = ref
      require ext_code.size(topAddress)
      call topAddress.createBet(uint256 referrerID) with:
         value 10^16 wei
           gas gas_remaining wei
          args ref
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  require eth.balance(this.address) < eth.balance(this.address)
  unknown591710f0 = 0


# hash = 0x3df4ddf4
# getter = ['bool', ['storage', 8, 168, 2]]
# const = None
# payable = False
def first(): # not payable
  return bool(first)


# hash = 0x591710f0
# getter = ['bool', ['storage', 8, 160, 2]]
# const = None
# payable = False
def unknown591710f0(): # not payable
  return bool(unknown591710f0)


# hash = 0x5a8ac02d
# getter = ['bool', ['storage', 8, 176, 2]]
# const = None
# payable = False
def second(): # not payable
  return bool(second)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x99f89d8e
# getter = None
# const = None
# payable = False
def unknown99f89d8e(uint256 _param1): # not payable
  unknown591710f0 = 1
  [94midx = 0
  while [94midx < _param1:
      mem[96] = 0xac793a6000000000000000000000000000000000000000000000000000000000
      mem[100] = ref
      require ext_code.size(topAddress)
      call topAddress.createBet(uint256 referrerID) with:
         value 10^16 wei
           gas gas_remaining wei
          args ref
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  require eth.balance(this.address) < eth.balance(this.address)
  unknown591710f0 = 0


# hash = 0xbf8eec20
# getter = None
# const = None
# payable = False
def unknownbf8eec20(): # not payable
  require caller == owner
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xdaaa5f2d
# getter = None
# const = None
# payable = False
def unknowndaaa5f2d(uint256 _param1): # not payable
  unknown591710f0 = 1
  require ext_code.size(topAddress)
  call topAddress.createBet(uint256 referrerID) with:
     value eth.balance(this.address) - (10^16 * _param1) wei
       gas gas_remaining wei
      args ref
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94midx = 0
  while [94midx < _param1:
      mem[96] = 0xac793a6000000000000000000000000000000000000000000000000000000000
      mem[100] = ref
      require ext_code.size(topAddress)
      call topAddress.createBet(uint256 referrerID) with:
         value 10^16 wei
           gas gas_remaining wei
          args ref
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  require eth.balance(this.address) < eth.balance(this.address)
  unknown591710f0 = 0


# hash = 0xf90fa1f0
# getter = None
# const = None
# payable = False
def unknownf90fa1f0(uint256 _param1, uint256 _param2): # not payable
  require block.timestamp > 426864 * 24 * 3600
  if not first:
      if second:
          unknown591710f0 = 1
          [94midx = 0
          while [94midx < _param2:
              mem[96] = 0xac793a6000000000000000000000000000000000000000000000000000000000
              mem[100] = ref
              require ext_code.size(topAddress)
              call topAddress.createBet(uint256 referrerID) with:
                 value 10^16 wei
                   gas gas_remaining wei
                  args ref
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94midx = [94midx + 1
              continue 
          require eth.balance(this.address) < eth.balance(this.address)
          unknown591710f0 = 0
          second = 0
  else:
      unknown591710f0 = 1
      require ext_code.size(topAddress)
      call topAddress.createBet(uint256 referrerID) with:
         value eth.balance(this.address) - (10^16 * _param1) wei
           gas gas_remaining wei
          args ref
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = 0
      while [94midx < _param1:
          mem[96] = 0xac793a6000000000000000000000000000000000000000000000000000000000
          mem[100] = ref
          require ext_code.size(topAddress)
          call topAddress.createBet(uint256 referrerID) with:
             value 10^16 wei
               gas gas_remaining wei
              args ref
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94midx = [94midx + 1
          continue 
      require eth.balance(this.address) < eth.balance(this.address)
      unknown591710f0 = 0
      first = 0


# hash = 0xfe6dcdba
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def top(): # not payable
  return topAddress


# hash = 0xffe7edf6
# getter = None
# const = None
# payable = True
def unknownffe7edf6() payable: 
  stop


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require unknown591710f0


