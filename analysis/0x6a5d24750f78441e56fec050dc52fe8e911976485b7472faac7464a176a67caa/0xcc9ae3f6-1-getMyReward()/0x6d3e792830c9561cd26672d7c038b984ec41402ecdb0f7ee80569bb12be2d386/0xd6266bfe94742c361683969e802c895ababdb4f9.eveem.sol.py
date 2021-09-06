# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD6266BfE94742c361683969E802C895ABABDb4f9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown3b0c03b1Address # mask: a s
    # storage address 1
    daoAddress # mask: a s
    # storage address 2
    collectorAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
# hash = 0x3b0c03b1
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def unknown3b0c03b1() payable: 
  return unknown3b0c03b1Address


# hash = 0x4162169f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def dao() payable: 
  return daoAddress


# hash = 0x42966c68
# getter = None
# const = None
# payable = True
def burn(uint256 _value) payable: 
  if unknown3b0c03b1Address == caller:
      stor3 = _value
      call daoAddress.getMyReward() with:
           gas gas_remaining - 25050 wei
      require ext_call.success
      call daoAddress.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      call daoAddress.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args collectorAddress, ext_call.return_data[0]
      call unknown3b0c03b1Address.sendEther() with:
         value eth.balance(this.address) wei
           gas gas_remaining - 34050 wei


# hash = 0x913e77ad
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def collector() payable: 
  return collectorAddress


# hash = 0xb61d27f6
# getter = None
# const = None
# payable = True
def execute(address _to, uint256 _value, bytes _data) payable: 
  mem[128 len _data.length] = _data[all]
  if unknown3b0c03b1Address == caller:
      mem[ceil32(_data.length) + 128 len _data.length] = _data[all]
      if not _data.length % 32:
          call _to with:
             value _value wei
               gas gas_remaining - 34050 wei
              args _data[all]
      else:
          mem[floor32(_data.length) + ceil32(_data.length) + 128] = mem[floor32(_data.length) + ceil32(_data.length) + -(_data.length % 32) + 160 len _data.length % 32]
          call _to.mem[ceil32(_data.length) + 128 len 4] with:
             value _value wei
               gas gas_remaining - 34050 wei
              args mem[ceil32(_data.length) + 132 len floor32(_data.length) + 28]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if stor3 <= 0:
      call daoAddress.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      call daoAddress.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args unknown3b0c03b1Address, ext_call.return_data[0] - 10^6
  else:
      stor3--
      call daoAddress.getMyReward() with:
           gas gas_remaining - 25050 wei
      require ext_call.success
  return 1


