# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD1cbC66749ba9fe3024Da32407f5C05d72379391 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x85b2824a': 'unknown85b2824a(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    owner # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    unknown7651bc92
# hash = 0x07e00bcb
# getter = None
# const = None
# payable = True
def kissBTCCallback(uint256 _id, uint256 _amount) payable: 
  call 0x6777c314b412f0196aca852632969f63e7971340.balanceOf(address owner) with:
       gas gas_remaining - 25050 wei
      args this.address
  require ext_call.success
  if ext_call.return_data[0] > 0:
      call 0x6777c314b412f0196aca852632969f63e7971340.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args addr(owner), ext_call.return_data[0]
      require ext_call.success


# hash = 0x13af4035
# getter = None
# const = None
# payable = True
def setOwner(address _newOwner) payable: 
  if caller == addr(owner):
      uint256(stor2) = _newOwner or Mask(96, 160, uint256(stor2))


# hash = 0x27dc297e
# getter = None
# const = None
# payable = True
def __callback(bytes32 _myid, string _result) payable: 
  call stor0.getAddress() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  if ext_call.return_data[12 len 20] != 0:
      stor1 = ext_call.return_data[0] or Mask(96, 160, stor1)
      call addr(ext_call.return_data[0]).cbAddress() with:
           gas gas_remaining - 25050 wei
      require ext_call.success
  else:
      if ext_code.size(0x1d3b2638a7cc9f2cb3d298a3da7a90b67e5506ed) > 0:
          stor0 = 0x1d3b2638a7cc9f2cb3d298a3da7a90b67e5506ed
      else:
          if ext_code.size(0x9efbea6358bed926b293d2ce63a730d6d98d43dd) > 0:
              stor0 = 0x9efbea6358bed926b293d2ce63a730d6d98d43dd
          else:
              if ext_code.size(0x20e12a1f859b3feae5fb2a0a32c18f5a65555bbf) > 0:
                  stor0 = 0x20e12a1f859b3feae5fb2a0a32c18f5a65555bbf
      call stor0.getAddress() with:
           gas gas_remaining - 25050 wei
      require ext_call.success
      stor1 = ext_call.return_data[0] or Mask(96, 160, stor1)
      call addr(ext_call.return_data[0]).cbAddress() with:
           gas gas_remaining - 25050 wei
  require caller == ext_call.return_data[12 len 20]
  unknown7651bc92[] = Array(len=_result.length, data=_result[all])


# hash = 0x7651bc92
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
# const = None
# payable = True
def unknown7651bc92() payable: 
  return unknown7651bc92[0 len unknown7651bc92.length]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def owner() payable: 
  return addr(owner)


# hash = 0xa3de4ae1
# getter = None
# const = None
# payable = True
def unknowna3de4ae1(array _param1, array _param2) payable: 
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  if addr(owner) == caller:
      mem[ceil32(_param1.length) + ceil32(_param2.length) + 160] = 0
      [94midx = 0
      [94ms = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94midx < _param2.length
          if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) >= 0x3000000000000000000000000000000000000000000000000000000000000000:
              if Mask(8, 248, mem[ceil32(_param1.length) + [94midx + 160]) <= 0x3900000000000000000000000000000000000000000000000000000000000000:
                  require [94midx < _param2.length
                  [94midx = [94midx + 1
                  [94ms = (10 * [94ms) + mem[[94midx + ceil32(_param1.length) + 160 len 1] - 48
                  continue 
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      call 0x6777c314b412f0196aca852632969f63e7971340.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args addr(owner), addr(this.address), 100 * 10^6 * [94ms
      require ext_call.success
      require ext_call.return_data[0]
      call 0x6777c314b412f0196aca852632969f63e7971340.approve(address spender, uint256 value) with:
           gas gas_remaining - 25050 wei
          args 0x71107a8959f1249920cf87dc8c994b9b483d25ef, 100 * 10^6 * [94ms
      require ext_call.success
      require ext_call.return_data[0]
      call 0x71107a8959f1249920cf87dc8c994b9b483d25ef.sendBitcoin(string address, uint256 amount) with:
           gas gas_remaining - 25050 wei
          args Array(len=_param1.length, data=_param1[all]), 100 * 10^6 * [94ms
      require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if eth.balance(this.address) <= 10 * 10^18:
      call 0x6777c314b412f0196aca852632969f63e7971340.buyKissBTCWithCallback(address callback, uint256 gasLimit) with:
         value eth.balance(this.address) wei
           gas gas_remaining - 34050 wei
          args addr(this.address), 200000
  else:
      call 0x6777c314b412f0196aca852632969f63e7971340.buyKissBTCWithCallback(address callback, uint256 gasLimit) with:
         value 10 * 10^18 wei
           gas gas_remaining - 34050 wei
          args addr(this.address), 200000
  require ext_call.success


