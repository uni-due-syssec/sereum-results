# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF05E8643B8487Fa97e03619c239f41ED4cF03f1E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    tokenAddress # mask: a s
    # storage address 2
    holderAddress # mask: a s
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    unknown8475fcac
    # storage address 7
    unknown92a8675d
    # storage address 8
    unknown5f54eabbAddress # mask: a s
    # storage address 9
    unknown55e7e714Address # mask: a s
    # storage address 10
    unknown5758b804Address # mask: a s
    # storage address 11
    preSaleAddress # mask: a s
    # storage address 12
    crowdsaleAddress # mask: a s
    # storage address 13
    unknown69997261 # mask: a s
    # storage address 14
    unknown31ef54d9
    # storage address 16
    unknownf4166388 # mask: a s
    # storage address 17
    unknown2955316f # mask: a s
    # storage address 18
    unknownd8e1a97f # mask: a s
    # storage address 19
    totalSold # mask: a s
    # storage address 20
    airdropSpent # mask: a s
    # storage address 21
    crowdsaleFinished # mask: a s
# hash = 0x08d52d46
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknown08d52d46(addr _param1): # not payable
  return bool(stor3[_param1])


# hash = 0x13f44d10
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]]
# const = None
# payable = False
def isAddressWhitelisted(address _addr): # not payable
  return bool(stor3[addr(_addr)])


# hash = 0x195055f1
# getter = None
# const = None
# payable = False
def isTransferable(address _addr): # not payable
  if not crowdsaleFinished:
      if unknown5758b804Address != _addr:
          if preSaleAddress != _addr:
              if crowdsaleAddress != _addr:
                  if not stor4[addr(_addr)]:
                      if _addr != this.address:
                          return 0
  return 1


# hash = 0x1cc7c06b
# getter = None
# const = None
# payable = False
def unknown1cc7c06b(array _param1): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  require owner == caller
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require mem[(32 * [94midx) + 140 len 20]
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 4
      stor4[mem[(32 * [94midx) + 140 len 20]] = 1
      [94midx = [94midx + 1
      continue 


# hash = 0x28bc8a04
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def airdropSpent(): # not payable
  return airdropSpent


# hash = 0x2955316f
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown2955316f(): # not payable
  return unknown2955316f


# hash = 0x2ffbbcec
# getter = None
# const = None
# payable = False
def unknown2ffbbcec(): # not payable
  require unknown69997261 < block.timestamp
  unknown92a8675d[caller] = 0
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, unknown92a8675d[caller]
  require ext_call.success


# hash = 0x31ef54d9
# getter = ['storage', 256, 0, ['add', 14, ['cd', 4]]]
# const = None
# payable = False
def unknown31ef54d9(uint256 _param1): # not payable
  require _param1 < 2
  return unknown31ef54d9[_param1]


# hash = 0x33fa9d4b
# getter = None
# const = None
# payable = False
def unknown33fa9d4b(addr _param1, uint256 _param2): # not payable
  require owner == caller
  require unknownd8e1a97f <= 40000000 * 10^18
  require -unknownd8e1a97f + 40000000 * 10^18 >= _param2
  require _param1
  require not crowdsaleFinished
  require _param2 + unknownd8e1a97f >= unknownd8e1a97f
  unknownd8e1a97f += _param2
  require _param2 + unknown92a8675d[addr(_param1)] >= unknown92a8675d[addr(_param1)]
  unknown92a8675d[addr(_param1)] += _param2
  return 1


# hash = 0x353a790b
# getter = None
# const = None
# payable = False
def unknown353a790b(uint256 _param1): # not payable
  require owner == caller
  require unknown5758b804Address
  require ext_code.size(unknown5758b804Address)
  call unknown5758b804Address.0x1d412dcb with:
       gas gas_remaining wei
      args _param1
  require ext_call.success


# hash = 0x35741f95
# getter = None
# const = None
# payable = False
def unknown35741f95(uint256 _param1, uint256 _param2): # not payable
  require owner == caller
  require preSaleAddress
  require not crowdsaleAddress
  require ext_code.size(preSaleAddress)
  call preSaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require _param1 >= block.timestamp
  require _param2 >= _param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b604051610100806109c7833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff199092169190911790556108ed806100da6000396000f3006060604052600436106100e25763ffffffff60e060020a6000350416631d412dcb81146100ed5780632c4e722e146101035780633197cbb61461012857806333b5b62e1461013b5780634042b66f1461014e57806340582f1314610161578063521eb2731461017457806378e97925146101a357806383408d73146101b65780638da5cb5b146101c9578063977b055b146101dc578063c0ee0b8a146101ef578063c2507ac114610268578063ec8ac4d81461027e578063ecb70fb714610292578063eef9d905146102a5578063f2fde38b146102b8578063fc0c546a146102d7575b6100eb336102ea565b005b34156100f857600080fd5b6100eb6004356104ef565b341561010e57600080fd5b61011661051d565b60405190815260200160405180910390f35b341561013357600080fd5b610116610523565b341561014657600080fd5b610116610529565b341561015957600080fd5b61011661052f565b341561016c57600080fd5b610116610535565b341561017f57600080fd5b61018761053b565b604051600160a060020a03909116815260200160405180910390f35b34156101ae57600080fd5b61011661054a565b34156101c157600080fd5b6100eb610550565b34156101d457600080fd5b6101876105bc565b34156101e757600080fd5b6101166105cb565b34156101fa57600080fd5b61025460048035600160a060020a03169060248035919060649060443590810190830135806020601f820181900481020160405190810160405281815292919060208401838380828437509496506105d195505050505050565b604051901515815260200160405180910390f35b341561027357600080fd5b6101166004356105da565b6100eb600160a060020a03600435166102ea565b341561029d57600080fd5b6102546106a4565b34156102b057600080fd5b6102546106ac565b34156102c357600080fd5b6100eb600160a060020a03600435166106b5565b34156102e257600080fd5b610187610750565b60008080600160a060020a038416151561030357600080fd5b61030c8461075f565b151561031757600080fd5b349250610323836105da565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561037657600080fd5b5af1151561038357600080fd5b50505060405180519150508082111561039b57600080fd5b6006546103ae908463ffffffff61082f16565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561040757600080fd5b5af1151561041457600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361047683610849565b600a5460ff1615156104e957600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104d857600080fd5b5af115156104e557600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461050a57600080fd5b600354811161051857600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60025481565b60005433600160a060020a0390811691161461056b57600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105aa57600080fd5b5af115156105b757600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b60008060006105f46005548561087f90919063ffffffff16565b915060009050678ac7230489e8000084101561060f5761068c565b68015af1d78b58c4000084101561064557600a5460ff1615156106405761063d82600a63ffffffff6108aa16565b90505b61068c565b68056bc75e2d631000008410156106785761063d606461066c84600f63ffffffff61087f16565b9063ffffffff6108aa16565b61068982600563ffffffff6108aa16565b90505b61069c828263ffffffff61082f16565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a039081169116146106d057600080fd5b600160a060020a03811615156106e557600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b600080600080600080600254421015801561077c57506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b15156107e657600080fd5b5af115156107f357600080fd5b5050506040518051905090508480156108095750835b80156108125750805b801561081b5750825b80156108245750815b979650505050505050565b60008282018381101561083e57fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f19350505050151561087c57600080fd5b50565b6000808315156108925760009150610842565b508282028284828115156108a257fe5b041461083e57fe5b60008082848115156108b857fe5b049493505050505600a165627a7a72305820ad3f0896d66bb4a9b778fa09310b1d1e918a3981f10324abe722768f7ad18b890000, _param1, _param2, 8500, 0, 200 * 10^18, addr(this.address), tokenAddress, 0
  require create.new_address
  crowdsaleAddress = addr(create.new_address)
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 208250000 * 10^18
  require ext_call.success
  require ext_code.size(preSaleAddress)
  call preSaleAddress.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0x38b69004
# getter = None
# const = None
# payable = False
def unknown38b69004(addr _param1): # not payable
  require owner == caller
  require not unknown5f54eabbAddress
  unknown5f54eabbAddress = _param1


# hash = 0x425c4e6f
# getter = None
# const = None
# payable = False
def unknown425c4e6f(): # not payable
  require owner == caller
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require addr(cd[((32 * [94midx) + cd[4] + 36)])
      require [94midx < ('cd', 4).length
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 3
      stor3[addr(cd[((32 * [94midx) + cd[4] + 36)])] = 1
      [94midx = [94midx + 1
      continue 


# hash = 0x48f4e8bf
# getter = None
# const = ['return', 42000000000000000000000000]
# payable = False
const unknown48f4e8bf = 42000000 * 10^18


# hash = 0x50c1bdf2
# getter = None
# const = None
# payable = False
def unknown50c1bdf2(addr _param1, uint256 _param2): # not payable
  if unknown5758b804Address != caller:
      if preSaleAddress != caller:
          require crowdsaleAddress == caller
  require _param2 + unknown8475fcac[addr(_param1)] >= unknown8475fcac[addr(_param1)]
  unknown8475fcac[addr(_param1)] += _param2


# hash = 0x52b14c87
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown52b14c87(addr _param1): # not payable
  return bool(stor4[_param1])


# hash = 0x55e7e714
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknown55e7e714(): # not payable
  return unknown55e7e714Address


# hash = 0x56ad9f57
# getter = None
# const = ['return', 208250000000000000000000000]
# payable = False
const CROWDSALE_SUPPLY = 208250000 * 10^18


# hash = 0x5758b804
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown5758b804(): # not payable
  return unknown5758b804Address


# hash = 0x58cf77fa
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 5]]]]
# const = None
# payable = False
def unknown58cf77fa(addr _param1): # not payable
  return bool(stor5[_param1])


# hash = 0x590e1ae3
# getter = None
# const = None
# payable = False
def refund(): # not payable
  require crowdsaleAddress
  require ext_code.size(crowdsaleAddress)
  call crowdsaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_call.return_data[0]
  if not totalSold:
      require ext_code.size(crowdsaleAddress)
      call crowdsaleAddress.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require ext_code.size(preSaleAddress)
      call preSaleAddress.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require ext_code.size(unknown5758b804Address)
      call unknown5758b804Address.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require 2 * ext_call.return_data[0] >= ext_call.return_data[0]
      require ext_call.return_data[0] >= 0
      totalSold = 3 * ext_call.return_data[0]
  require totalSold < 10^15
  require unknown8475fcac[caller] > 0
  unknown8475fcac[caller] = 0
  call caller with:
     value unknown8475fcac[caller] wei
       gas 2300 * is_zero(value) wei
  require ext_call.success
  return 1


# hash = 0x595a90f2
# getter = None
# const = None
# payable = False
def unknown595a90f2(): # not payable
  require owner == caller
  require ('cd', 36).length == ('cd', 4).length
  [94midx = 0
  while [94midx < ('cd', 36).length:
      require [94midx < ('cd', 4).length
      require [94midx < ('cd', 36).length
      require owner == caller
      require unknownd8e1a97f <= 40000000 * 10^18
      require -unknownd8e1a97f + 40000000 * 10^18 >= cd[((32 * [94midx) + cd[36] + 36)]
      require addr(cd[((32 * [94midx) + cd[4] + 36)])
      require not crowdsaleFinished
      require cd[((32 * [94midx) + cd[36] + 36)] + unknownd8e1a97f >= unknownd8e1a97f
      unknownd8e1a97f += cd[((32 * [94midx) + cd[36] + 36)]
      require cd[((32 * [94midx) + cd[36] + 36)] + unknown92a8675d[addr(cd[((32 * [94midx) + cd[4] + 36)])] >= unknown92a8675d[addr(cd[((32 * [94midx) + cd[4] + 36)])]
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 7
      unknown92a8675d[addr(cd[((32 * [94midx) + cd[4] + 36)])] += cd[((32 * [94midx) + cd[36] + 36)]
      [94midx = [94midx + 1
      continue 
  return 1


# hash = 0x5a01d2ed
# getter = None
# const = None
# payable = False
def unknown5a01d2ed(uint256 _param1, uint256 _param2, addr _param3): # not payable
  require owner == caller
  require not unknown5758b804Address
  require _param3
  require _param1 >= block.timestamp
  require _param2 >= _param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b604051610100806109c7833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff199092169190911790556108ed806100da6000396000f3006060604052600436106100e25763ffffffff60e060020a6000350416631d412dcb81146100ed5780632c4e722e146101035780633197cbb61461012857806333b5b62e1461013b5780634042b66f1461014e57806340582f1314610161578063521eb2731461017457806378e97925146101a357806383408d73146101b65780638da5cb5b146101c9578063977b055b146101dc578063c0ee0b8a146101ef578063c2507ac114610268578063ec8ac4d81461027e578063ecb70fb714610292578063eef9d905146102a5578063f2fde38b146102b8578063fc0c546a146102d7575b6100eb336102ea565b005b34156100f857600080fd5b6100eb6004356104ef565b341561010e57600080fd5b61011661051d565b60405190815260200160405180910390f35b341561013357600080fd5b610116610523565b341561014657600080fd5b610116610529565b341561015957600080fd5b61011661052f565b341561016c57600080fd5b610116610535565b341561017f57600080fd5b61018761053b565b604051600160a060020a03909116815260200160405180910390f35b34156101ae57600080fd5b61011661054a565b34156101c157600080fd5b6100eb610550565b34156101d457600080fd5b6101876105bc565b34156101e757600080fd5b6101166105cb565b34156101fa57600080fd5b61025460048035600160a060020a03169060248035919060649060443590810190830135806020601f820181900481020160405190810160405281815292919060208401838380828437509496506105d195505050505050565b604051901515815260200160405180910390f35b341561027357600080fd5b6101166004356105da565b6100eb600160a060020a03600435166102ea565b341561029d57600080fd5b6102546106a4565b34156102b057600080fd5b6102546106ac565b34156102c357600080fd5b6100eb600160a060020a03600435166106b5565b34156102e257600080fd5b610187610750565b60008080600160a060020a038416151561030357600080fd5b61030c8461075f565b151561031757600080fd5b349250610323836105da565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561037657600080fd5b5af1151561038357600080fd5b50505060405180519150508082111561039b57600080fd5b6006546103ae908463ffffffff61082f16565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561040757600080fd5b5af1151561041457600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361047683610849565b600a5460ff1615156104e957600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104d857600080fd5b5af115156104e557600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461050a57600080fd5b600354811161051857600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60025481565b60005433600160a060020a0390811691161461056b57600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105aa57600080fd5b5af115156105b757600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b60008060006105f46005548561087f90919063ffffffff16565b915060009050678ac7230489e8000084101561060f5761068c565b68015af1d78b58c4000084101561064557600a5460ff1615156106405761063d82600a63ffffffff6108aa16565b90505b61068c565b68056bc75e2d631000008410156106785761063d606461066c84600f63ffffffff61087f16565b9063ffffffff6108aa16565b61068982600563ffffffff6108aa16565b90505b61069c828263ffffffff61082f16565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a039081169116146106d057600080fd5b600160a060020a03811615156106e557600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b600080600080600080600254421015801561077c57506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b15156107e657600080fd5b5af115156107f357600080fd5b5050506040518051905090508480156108095750835b80156108125750805b801561081b5750825b80156108245750815b979650505050505050565b60008282018381101561083e57fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f19350505050151561087c57600080fd5b50565b6000808315156108925760009150610842565b508282028284828115156108a257fe5b041461083e57fe5b60008082848115156108b857fe5b049493505050505600a165627a7a72305820ad3f0896d66bb4a9b778fa09310b1d1e918a3981f10324abe722768f7ad18b890000, _param1, _param2, 12000, 0, 200 * 10^18, addr(_param3), tokenAddress, 1
  require create.new_address
  unknown5758b804Address = addr(create.new_address)
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 42000000 * 10^18
  require ext_call.success


# hash = 0x5a7adf7f
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def preSale(): # not payable
  return preSaleAddress


# hash = 0x5f54eabb
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def unknown5f54eabb(): # not payable
  return unknown5f54eabbAddress


# hash = 0x65712339
# getter = None
# const = ['return', 1000000000000000]
# payable = False
const unknown65712339 = 10^15


# hash = 0x69997261
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown69997261(): # not payable
  return unknown69997261


# hash = 0x7bf2b2df
# getter = None
# const = None
# payable = False
def unknown7bf2b2df(addr _param1): # not payable
  if unknown5758b804Address == _param1:
      return True
  if preSaleAddress == _param1:
      return True
  return (crowdsaleAddress == _param1)


# hash = 0x8475fcac
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknown8475fcac(addr _param1): # not payable
  return unknown8475fcac[_param1]


# hash = 0x8a857bc1
# getter = None
# const = ['return', 5000000000000000000000000]
# payable = False
const unknown8a857bc1 = 5000000 * 10^18


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8e0c09b2
# getter = None
# const = ['return', 50750000000000000000000000]
# payable = False
const unknown8e0c09b2 = 50750000 * 10^18


# hash = 0x9106d7ba
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def totalSold(): # not payable
  return totalSold


# hash = 0x92a8675d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown92a8675d(addr _param1): # not payable
  return unknown92a8675d[_param1]


# hash = 0x98b3f7e2
# getter = None
# const = None
# payable = False
def unknown98b3f7e2(): # not payable
  require owner == caller
  [94midx = 0
  while [94midx < ('cd', 4).length:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 3
      stor3[addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x9c1e03a0
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def crowdsale(): # not payable
  return crowdsaleAddress


# hash = 0xa6ceb1f3
# getter = None
# const = None
# payable = False
def sendAirdrop(address[] _to, uint256[] _value): # not payable
  require owner == caller
  require _value.length == _to.length
  [94midx = 0
  while [94midx < _to.length:
      require [94midx < _value.length
      require cd[((32 * [94midx) + _value + 36)] + airdropSpent >= airdropSpent
      airdropSpent += cd[((32 * [94midx) + _value + 36)]
      require 5000000 * 10^18 >= cd[((32 * [94midx) + _value + 36)] + airdropSpent
      require [94midx < _to.length
      require addr(cd[((32 * [94midx) + _to + 36)])
      require [94midx < _to.length
      require [94midx < _value.length
      mem[100] = addr(cd[((32 * [94midx) + _to + 36)])
      mem[132] = cd[((32 * [94midx) + _value + 36)]
      require ext_code.size(tokenAddress)
      call tokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(cd[((32 * [94midx) + _to + 36)]), cd[((32 * [94midx) + _value + 36)]
      mem[96] = ext_call.return_data[0]
      require ext_call.success
      [94midx = [94midx + 1
      continue 


# hash = 0xa818e816
# getter = None
# const = ['return', 40000000000000000000000000]
# payable = False
const unknowna818e816 = 40000000 * 10^18


# hash = 0xb1905c5d
# getter = None
# const = None
# payable = False
def unknownb1905c5d(array _param1): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  require owner == caller
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require mem[(32 * [94midx) + 140 len 20]
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 4
      stor4[mem[(32 * [94midx) + 140 len 20]] = 0
      [94midx = [94midx + 1
      continue 


# hash = 0xb80cdcf6
# getter = None
# const = None
# payable = False
def finishCrowdsale(): # not payable
  require owner == caller
  require crowdsaleAddress
  require ext_code.size(crowdsaleAddress)
  call crowdsaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require not crowdsaleFinished
  require unknown5f54eabbAddress
  require ext_code.size(crowdsaleAddress)
  call crowdsaleAddress.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_code.size(crowdsaleAddress)
  call crowdsaleAddress.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_code.size(preSaleAddress)
  call preSaleAddress.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require 2 * ext_call.return_data[0] >= ext_call.return_data[0]
  require ext_code.size(unknown5758b804Address)
  call unknown5758b804Address.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require 3 * ext_call.return_data[0] >= ext_call.return_data[0]
  totalSold = 3 * ext_call.return_data[0]
  if 3 * ext_call.return_data[0] >= 10^15:
      require ext_code.size(tokenAddress)
      call tokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args unknown5f54eabbAddress, 75000000 * 10^18
      require ext_call.success
      require bool(ext_call.return_data[0]) == 1
      call unknown55e7e714Address with:
         value eth.balance(this.address) / 2 wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
      call holderAddress with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
  crowdsaleFinished = 1


# hash = 0xbb0a4c2d
# getter = None
# const = ['return', 1585699200]
# payable = False
const unknownbb0a4c2d = (440472 * 24 * 3600)


# hash = 0xc1417fb9
# getter = None
# const = None
# payable = False
def unknownc1417fb9(uint256 _param1, uint256 _param2): # not payable
  require owner == caller
  require unknown5758b804Address
  require not preSaleAddress
  require ext_code.size(unknown5758b804Address)
  call unknown5758b804Address.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require _param1 >= block.timestamp
  require _param2 >= _param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b604051610100806109c7833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff199092169190911790556108ed806100da6000396000f3006060604052600436106100e25763ffffffff60e060020a6000350416631d412dcb81146100ed5780632c4e722e146101035780633197cbb61461012857806333b5b62e1461013b5780634042b66f1461014e57806340582f1314610161578063521eb2731461017457806378e97925146101a357806383408d73146101b65780638da5cb5b146101c9578063977b055b146101dc578063c0ee0b8a146101ef578063c2507ac114610268578063ec8ac4d81461027e578063ecb70fb714610292578063eef9d905146102a5578063f2fde38b146102b8578063fc0c546a146102d7575b6100eb336102ea565b005b34156100f857600080fd5b6100eb6004356104ef565b341561010e57600080fd5b61011661051d565b60405190815260200160405180910390f35b341561013357600080fd5b610116610523565b341561014657600080fd5b610116610529565b341561015957600080fd5b61011661052f565b341561016c57600080fd5b610116610535565b341561017f57600080fd5b61018761053b565b604051600160a060020a03909116815260200160405180910390f35b34156101ae57600080fd5b61011661054a565b34156101c157600080fd5b6100eb610550565b34156101d457600080fd5b6101876105bc565b34156101e757600080fd5b6101166105cb565b34156101fa57600080fd5b61025460048035600160a060020a03169060248035919060649060443590810190830135806020601f820181900481020160405190810160405281815292919060208401838380828437509496506105d195505050505050565b604051901515815260200160405180910390f35b341561027357600080fd5b6101166004356105da565b6100eb600160a060020a03600435166102ea565b341561029d57600080fd5b6102546106a4565b34156102b057600080fd5b6102546106ac565b34156102c357600080fd5b6100eb600160a060020a03600435166106b5565b34156102e257600080fd5b610187610750565b60008080600160a060020a038416151561030357600080fd5b61030c8461075f565b151561031757600080fd5b349250610323836105da565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561037657600080fd5b5af1151561038357600080fd5b50505060405180519150508082111561039b57600080fd5b6006546103ae908463ffffffff61082f16565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561040757600080fd5b5af1151561041457600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361047683610849565b600a5460ff1615156104e957600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104d857600080fd5b5af115156104e557600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461050a57600080fd5b600354811161051857600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60025481565b60005433600160a060020a0390811691161461056b57600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105aa57600080fd5b5af115156105b757600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b60008060006105f46005548561087f90919063ffffffff16565b915060009050678ac7230489e8000084101561060f5761068c565b68015af1d78b58c4000084101561064557600a5460ff1615156106405761063d82600a63ffffffff6108aa16565b90505b61068c565b68056bc75e2d631000008410156106785761063d606461066c84600f63ffffffff61087f16565b9063ffffffff6108aa16565b61068982600563ffffffff6108aa16565b90505b61069c828263ffffffff61082f16565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a039081169116146106d057600080fd5b600160a060020a03811615156106e557600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b600080600080600080600254421015801561077c57506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b15156107e657600080fd5b5af115156107f357600080fd5b5050506040518051905090508480156108095750835b80156108125750805b801561081b5750825b80156108245750815b979650505050505050565b60008282018381101561083e57fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f19350505050151561087c57600080fd5b50565b6000808315156108925760009150610842565b508282028284828115156108a257fe5b041461083e57fe5b60008082848115156108b857fe5b049493505050505600a165627a7a72305820ad3f0896d66bb4a9b778fa09310b1d1e918a3981f10324abe722768f7ad18b890000, _param1, _param2, 10150, 0, 200 * 10^18, addr(this.address), tokenAddress, 0
  require create.new_address
  preSaleAddress = addr(create.new_address)
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 50750000 * 10^18
  require ext_call.success
  require ext_code.size(unknown5758b804Address)
  call unknown5758b804Address.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0xc4290fd1
# getter = None
# const = None
# payable = False
def unknownc4290fd1(): # not payable
  require owner == caller
  require 1 == bool(crowdsaleFinished)
  require unknownd8e1a97f <= 40000000 * 10^18
  require ext_code.size(tokenAddress)
  call tokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require 100000000 * 10^18 <= ext_call.return_data[0]
  if not -unknownd8e1a97f + 40000000 * 10^18:
      require airdropSpent <= 5000000 * 10^18
      if -airdropSpent + 5000000 * 10^18:
          if ext_call.return_data[0] - 100000000 * 10^18 >= -airdropSpent + 5000000 * 10^18:
              require ext_code.size(tokenAddress)
              call tokenAddress.burn(uint256 value) with:
                   gas gas_remaining wei
                  args (-airdropSpent + 5000000 * 10^18)
              require ext_call.success
  else:
      if ext_call.return_data[0] - 100000000 * 10^18 < -unknownd8e1a97f + 40000000 * 10^18:
          require airdropSpent <= 5000000 * 10^18
          if -airdropSpent + 5000000 * 10^18:
              if ext_call.return_data[0] - 100000000 * 10^18 >= -airdropSpent + 5000000 * 10^18:
                  require ext_code.size(tokenAddress)
                  call tokenAddress.burn(uint256 value) with:
                       gas gas_remaining wei
                      args (-airdropSpent + 5000000 * 10^18)
                  require ext_call.success
      else:
          require ext_code.size(tokenAddress)
          call tokenAddress.burn(uint256 value) with:
               gas gas_remaining wei
              args (-unknownd8e1a97f + 40000000 * 10^18)
          require ext_call.success
          require -unknownd8e1a97f + 40000000 * 10^18 <= ext_call.return_data[0] - 100000000 * 10^18
          require airdropSpent <= 5000000 * 10^18
          if -airdropSpent + 5000000 * 10^18:
              if ext_call.return_data[0] + unknownd8e1a97f - 140000000 * 10^18 >= -airdropSpent + 5000000 * 10^18:
                  require ext_code.size(tokenAddress)
                  call tokenAddress.burn(uint256 value) with:
                       gas gas_remaining wei
                      args (-airdropSpent + 5000000 * 10^18)
                  require ext_call.success


# hash = 0xccb887bc
# getter = None
# const = ['return', 1554076800]
# payable = False
const unknownccb887bc = (431688 * 24 * 3600)


# hash = 0xd1ef3063
# getter = None
# const = None
# payable = False
def unknownd1ef3063(): # not payable
  require owner == caller
  require unknownf4166388 < 2
  require unknown31ef54d9[stor16] < block.timestamp
  unknown2955316f = 0
  require ext_code.size(tokenAddress)
  call tokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args owner, unknown2955316f
  require ext_call.success
  unknownf4166388++


# hash = 0xd8e1a97f
# getter = ['storage', 256, 0, 18]
# const = None
# payable = False
def unknownd8e1a97f(): # not payable
  return unknownd8e1a97f


# hash = 0xe534155d
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def holder(): # not payable
  return holderAddress


# hash = 0xe647e19f
# getter = None
# const = ['return', 100000000000000000000000000]
# payable = False
const unknowne647e19f = 100000000 * 10^18


# hash = 0xece84fd5
# getter = ['bool', ['storage', 8, 0, 21]]
# const = None
# payable = False
def crowdsaleFinished(): # not payable
  return bool(crowdsaleFinished)


# hash = 0xedba3df2
# getter = None
# const = ['return', 1530403200]
# payable = False
const unknownedba3df2 = (425112 * 24 * 3600)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require owner == caller
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf4166388
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknownf4166388(): # not payable
  return unknownf4166388


# hash = 0xf6700481
# getter = None
# const = ['return', 75000000000000000000000000]
# payable = False
const unknownf6700481 = 75000000 * 10^18


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def token(): # not payable
  return tokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


