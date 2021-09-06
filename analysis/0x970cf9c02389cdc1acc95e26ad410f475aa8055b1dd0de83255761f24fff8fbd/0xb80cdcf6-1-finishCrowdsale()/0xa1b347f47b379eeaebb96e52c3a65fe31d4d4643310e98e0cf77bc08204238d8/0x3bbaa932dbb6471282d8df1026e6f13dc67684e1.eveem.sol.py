# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3BBaA932dbb6471282d8dF1026e6f13dc67684e1 
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
def unknown08d52d46(addr m_param1): # not payable
  return bool(mstor3m[m_param1m])


# hash = 0x13f44d10
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]]
# const = None
# payable = False
def isAddressWhitelisted(address m_addr): # not payable
  return bool(mstor3m[addr(m_addr)m])


# hash = 0x195055f1
# getter = None
# const = None
# payable = False
def isTransferable(address m_addr): # not payable
  if not mcrowdsaleFinished:
      if munknown5758b804Address != m_addr:
          if mpreSaleAddress != m_addr:
              if mcrowdsaleAddress != m_addr:
                  if not mstor4m[addr(m_addr)m]:
                      if m_addr != this.address:
                          return 0
  return 1


# hash = 0x1cc7c06b
# getter = None
# const = None
# payable = False
def unknown1cc7c06b(array m_param1): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require mowner == caller
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require mem[(32 * [94midx) + 140 len 20]
      require [94midx < m_param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 4
      mstor4m[mem[(32 * [94midx) + 140 len 20]m] = 1
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x28bc8a04
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def airdropSpent(): # not payable
  return mairdropSpent


# hash = 0x2955316f
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown2955316f(): # not payable
  return munknown2955316f


# hash = 0x2ffbbcec
# getter = None
# const = None
# payable = False
def unknown2ffbbcec(): # not payable
  require munknown69997261 < block.timestamp
  munknown92a8675dm[callerm] = 0
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, munknown92a8675dm[callerm]
  require ext_call.success


# hash = 0x31ef54d9
# getter = ['storage', 256, 0, ['add', 14, ['cd', 4]]]
# const = None
# payable = False
def unknown31ef54d9(uint256 m_param1): # not payable
  require m_param1 < 2
  return munknown31ef54d9m[m_param1m]


# hash = 0x33fa9d4b
# getter = None
# const = None
# payable = False
def unknown33fa9d4b(addr m_param1, uint256 m_param2): # not payable
  require mowner == caller
  require munknownd8e1a97f <= 0
  require -munknownd8e1a97f >= m_param2
  require m_param1
  require not mcrowdsaleFinished
  require m_param2 + munknownd8e1a97f >= munknownd8e1a97f
  munknownd8e1a97f += m_param2
  require m_param2 + munknown92a8675dm[addr(m_param1)m] >= munknown92a8675dm[addr(m_param1)m]
  munknown92a8675dm[addr(m_param1)m] += m_param2
  return 1


# hash = 0x35741f95
# getter = None
# const = None
# payable = False
def unknown35741f95(uint256 m_param1, uint256 m_param2): # not payable
  require mowner == caller
  require mpreSaleAddress
  require not mcrowdsaleAddress
  require ext_code.size(mpreSaleAddress)
  call mpreSaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require m_param1 >= block.timestamp
  require m_param2 >= m_param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b60405161010080610a0f833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff19909216919091179055610935806100da6000396000f3006060604052600436106100ed5763ffffffff60e060020a6000350416631d412dcb81146100f85780632c4e722e1461010e5780633197cbb61461013357806333b5b62e146101465780634042b66f1461015957806340582f131461016c578063521eb2731461017f5780637555e80a146101ae57806378e97925146101c457806383408d73146101d75780638da5cb5b146101ea578063977b055b146101fd578063c0ee0b8a14610210578063c2507ac114610289578063ec8ac4d81461029f578063ecb70fb7146102b3578063eef9d905146102c6578063f2fde38b146102d9578063fc0c546a146102f8575b6100f63361030b565b005b341561010357600080fd5b6100f6600435610510565b341561011957600080fd5b61012161053e565b60405190815260200160405180910390f35b341561013e57600080fd5b610121610544565b341561015157600080fd5b61012161054a565b341561016457600080fd5b610121610550565b341561017757600080fd5b610121610556565b341561018a57600080fd5b61019261055c565b604051600160a060020a03909116815260200160405180910390f35b34156101b957600080fd5b6100f660043561056b565b34156101cf57600080fd5b610121610592565b34156101e257600080fd5b6100f6610598565b34156101f557600080fd5b610192610604565b341561020857600080fd5b610121610613565b341561021b57600080fd5b61027560048035600160a060020a03169060248035919060649060443590810190830135806020601f8201819004810201604051908101604052818152929190602084018383808284375094965061061995505050505050565b604051901515815260200160405180910390f35b341561029457600080fd5b610121600435610622565b6100f6600160a060020a036004351661030b565b34156102be57600080fd5b6102756106ec565b34156102d157600080fd5b6102756106f4565b34156102e457600080fd5b6100f6600160a060020a03600435166106fd565b341561030357600080fd5b610192610798565b60008080600160a060020a038416151561032457600080fd5b61032d846107a7565b151561033857600080fd5b34925061034483610622565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561039757600080fd5b5af115156103a457600080fd5b5050506040518051915050808211156103bc57600080fd5b6006546103cf908463ffffffff61087716565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561042857600080fd5b5af1151561043557600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361049783610891565b600a5460ff16151561050a57600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104f957600080fd5b5af1151561050657600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461052b57600080fd5b600354811161053957600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60005433600160a060020a0390811691161461058657600080fd5b42811161053957600080fd5b60025481565b60005433600160a060020a039081169116146105b357600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105f257600080fd5b5af115156105ff57600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b600080600061063c600554856108c790919063ffffffff16565b915060009050678ac7230489e80000841015610657576106d4565b68015af1d78b58c4000084101561068d57600a5460ff1615156106885761068582600a63ffffffff6108f216565b90505b6106d4565b68056bc75e2d631000008410156106c05761068560646106b484600f63ffffffff6108c716565b9063ffffffff6108f216565b6106d182600563ffffffff6108f216565b90505b6106e4828263ffffffff61087716565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a0390811691161461071857600080fd5b600160a060020a038116151561072d57600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b60008060008060008060025442101580156107c457506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561082e57600080fd5b5af1151561083b57600080fd5b5050506040518051905090508480156108515750835b801561085a5750805b80156108635750825b801561086c5750815b979650505050505050565b60008282018381101561088657fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f1935050505015156108c457600080fd5b50565b6000808315156108da576000915061088a565b508282028284828115156108ea57fe5b041461088657fe5b600080828481151561090057fe5b049493505050505600a165627a7a723058202c989f017a9fd91a3accb97188fd011c279487b41112c465e60c908980aae83b0000, _param1, _param2, 8500, 10^17, 200 * 10^18, addr(this.address), tokenAddress, 0
  require create.new_address
  mcrowdsaleAddress = addr(create.new_address)
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 208250000 * 10^18
  require ext_call.success
  require ext_code.size(mpreSaleAddress)
  call mpreSaleAddress.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0x38b69004
# getter = None
# const = None
# payable = False
def unknown38b69004(addr m_param1): # not payable
  require mowner == caller
  require not munknown5f54eabbAddress
  munknown5f54eabbAddress = m_param1


# hash = 0x425c4e6f
# getter = None
# const = None
# payable = False
def unknown425c4e6f(): # not payable
  require mowner == caller
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require addr(cd[((32 * [94midx) + cd[4] + 36)])
      require [94midx < m('cd', 4).length
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 3
      mstor3m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 1
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x48f4e8bf
# getter = None
# const = ['return', 42000000000000000000000000]
# payable = False
const unknown48f4e8bf = 42000000 * 10^18


# hash = 0x50c1bdf2
# getter = None
# const = None
# payable = False
def unknown50c1bdf2(addr m_param1, uint256 m_param2): # not payable
  if munknown5758b804Address != caller:
      if mpreSaleAddress != caller:
          require mcrowdsaleAddress == caller
  require m_param2 + munknown8475fcacm[addr(m_param1)m] >= munknown8475fcacm[addr(m_param1)m]
  munknown8475fcacm[addr(m_param1)m] += m_param2


# hash = 0x52b14c87
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown52b14c87(addr m_param1): # not payable
  return bool(mstor4m[m_param1m])


# hash = 0x55e7e714
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknown55e7e714(): # not payable
  return munknown55e7e714Address


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
  return munknown5758b804Address


# hash = 0x58cf77fa
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 5]]]]
# const = None
# payable = False
def unknown58cf77fa(addr m_param1): # not payable
  return bool(mstor5m[m_param1m])


# hash = 0x590e1ae3
# getter = None
# const = None
# payable = False
def refund(): # not payable
  require mcrowdsaleAddress
  require ext_code.size(mcrowdsaleAddress)
  call mcrowdsaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_call.return_data[0]
  if not mtotalSold:
      require ext_code.size(mcrowdsaleAddress)
      call mcrowdsaleAddress.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require ext_code.size(mpreSaleAddress)
      call mpreSaleAddress.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require ext_code.size(munknown5758b804Address)
      call munknown5758b804Address.getWeiRaised() with:
           gas gas_remaining wei
      require ext_call.success
      require 2 * ext_call.return_data[0] >= ext_call.return_data[0]
      require ext_call.return_data[0] >= 0
      mtotalSold = 3 * ext_call.return_data[0]
  require mtotalSold < 2500 * 10^18
  require munknown8475fcacm[callerm] > 0
  munknown8475fcacm[callerm] = 0
  call caller with:
     value munknown8475fcacm[callerm] wei
       gas 2300 * is_zero(value) wei
  require ext_call.success
  return 1


# hash = 0x595a90f2
# getter = None
# const = None
# payable = False
def unknown595a90f2(): # not payable
  require mowner == caller
  require m('cd', 36).length == m('cd', 4).length
  [94midx = 0
  mwhile [94midx < m('cd', 36).lengthm:
      require [94midx < m('cd', 4).length
      require [94midx < m('cd', 36).length
      require mowner == caller
      require munknownd8e1a97f <= 0
      require -munknownd8e1a97f >= cd[((32 * [94midx) + cd[36] + 36)]
      require addr(cd[((32 * [94midx) + cd[4] + 36)])
      require not mcrowdsaleFinished
      require cd[((32 * [94midx) + cd[36] + 36)] + munknownd8e1a97f >= munknownd8e1a97f
      munknownd8e1a97f += cd[((32 * [94midx) + cd[36] + 36)]
      require cd[((32 * [94midx) + cd[36] + 36)] + munknown92a8675dm[addr(cd[((32 * [94midx) + cd[4] + 36)])m] >= munknown92a8675dm[addr(cd[((32 * [94midx) + cd[4] + 36)])m]
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 7
      munknown92a8675dm[addr(cd[((32 * [94midx) + cd[4] + 36)])m] += cd[((32 * [94midx) + cd[36] + 36)]
      [94midx = [94midx + 1
      mcontinue 
  return 1


# hash = 0x5a01d2ed
# getter = None
# const = None
# payable = False
def unknown5a01d2ed(uint256 m_param1, uint256 m_param2, addr m_param3): # not payable
  require mowner == caller
  require not munknown5758b804Address
  require m_param3
  require m_param1 >= block.timestamp
  require m_param2 >= m_param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b60405161010080610a0f833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff19909216919091179055610935806100da6000396000f3006060604052600436106100ed5763ffffffff60e060020a6000350416631d412dcb81146100f85780632c4e722e1461010e5780633197cbb61461013357806333b5b62e146101465780634042b66f1461015957806340582f131461016c578063521eb2731461017f5780637555e80a146101ae57806378e97925146101c457806383408d73146101d75780638da5cb5b146101ea578063977b055b146101fd578063c0ee0b8a14610210578063c2507ac114610289578063ec8ac4d81461029f578063ecb70fb7146102b3578063eef9d905146102c6578063f2fde38b146102d9578063fc0c546a146102f8575b6100f63361030b565b005b341561010357600080fd5b6100f6600435610510565b341561011957600080fd5b61012161053e565b60405190815260200160405180910390f35b341561013e57600080fd5b610121610544565b341561015157600080fd5b61012161054a565b341561016457600080fd5b610121610550565b341561017757600080fd5b610121610556565b341561018a57600080fd5b61019261055c565b604051600160a060020a03909116815260200160405180910390f35b34156101b957600080fd5b6100f660043561056b565b34156101cf57600080fd5b610121610592565b34156101e257600080fd5b6100f6610598565b34156101f557600080fd5b610192610604565b341561020857600080fd5b610121610613565b341561021b57600080fd5b61027560048035600160a060020a03169060248035919060649060443590810190830135806020601f8201819004810201604051908101604052818152929190602084018383808284375094965061061995505050505050565b604051901515815260200160405180910390f35b341561029457600080fd5b610121600435610622565b6100f6600160a060020a036004351661030b565b34156102be57600080fd5b6102756106ec565b34156102d157600080fd5b6102756106f4565b34156102e457600080fd5b6100f6600160a060020a03600435166106fd565b341561030357600080fd5b610192610798565b60008080600160a060020a038416151561032457600080fd5b61032d846107a7565b151561033857600080fd5b34925061034483610622565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561039757600080fd5b5af115156103a457600080fd5b5050506040518051915050808211156103bc57600080fd5b6006546103cf908463ffffffff61087716565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561042857600080fd5b5af1151561043557600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361049783610891565b600a5460ff16151561050a57600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104f957600080fd5b5af1151561050657600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461052b57600080fd5b600354811161053957600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60005433600160a060020a0390811691161461058657600080fd5b42811161053957600080fd5b60025481565b60005433600160a060020a039081169116146105b357600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105f257600080fd5b5af115156105ff57600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b600080600061063c600554856108c790919063ffffffff16565b915060009050678ac7230489e80000841015610657576106d4565b68015af1d78b58c4000084101561068d57600a5460ff1615156106885761068582600a63ffffffff6108f216565b90505b6106d4565b68056bc75e2d631000008410156106c05761068560646106b484600f63ffffffff6108c716565b9063ffffffff6108f216565b6106d182600563ffffffff6108f216565b90505b6106e4828263ffffffff61087716565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a0390811691161461071857600080fd5b600160a060020a038116151561072d57600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b60008060008060008060025442101580156107c457506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561082e57600080fd5b5af1151561083b57600080fd5b5050506040518051905090508480156108515750835b801561085a5750805b80156108635750825b801561086c5750815b979650505050505050565b60008282018381101561088657fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f1935050505015156108c457600080fd5b50565b6000808315156108da576000915061088a565b508282028284828115156108ea57fe5b041461088657fe5b600080828481151561090057fe5b049493505050505600a165627a7a723058202c989f017a9fd91a3accb97188fd011c279487b41112c465e60c908980aae83b0000, _param1, _param2, 12000, 10 * 10^18, 200 * 10^18, addr(_param3), tokenAddress, 1
  require create.new_address
  munknown5758b804Address = addr(create.new_address)
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 42000000 * 10^18
  require ext_call.success


# hash = 0x5a7adf7f
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def preSale(): # not payable
  return mpreSaleAddress


# hash = 0x5f54eabb
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def unknown5f54eabb(): # not payable
  return munknown5f54eabbAddress


# hash = 0x65712339
# getter = None
# const = ['return', 2500000000000000000000]
# payable = False
const unknown65712339 = 2500 * 10^18


# hash = 0x69997261
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown69997261(): # not payable
  return munknown69997261


# hash = 0x6a45c4bc
# getter = None
# const = None
# payable = False
def unknown6a45c4bc(uint256 m_param1): # not payable
  require mowner == caller
  if mcrowdsaleAddress:
      require ext_code.size(mcrowdsaleAddress)
      call mcrowdsaleAddress.0x1d412dcb with:
           gas gas_remaining wei
          args m_param1
      require ext_call.success
  else:
      if mpreSaleAddress:
          require ext_code.size(mpreSaleAddress)
          call mpreSaleAddress.0x1d412dcb with:
               gas gas_remaining wei
              args m_param1
          require ext_call.success
      else:
          if munknown5758b804Address:
              require ext_code.size(munknown5758b804Address)
              call munknown5758b804Address.0x1d412dcb with:
                   gas gas_remaining wei
                  args m_param1
              require ext_call.success


# hash = 0x7bf2b2df
# getter = None
# const = None
# payable = False
def unknown7bf2b2df(addr m_param1): # not payable
  if munknown5758b804Address == m_param1:
      return True
  if mpreSaleAddress == m_param1:
      return True
  return (mcrowdsaleAddress == m_param1)


# hash = 0x7caed168
# getter = None
# const = None
# payable = False
def unknown7caed168(uint256 m_param1, uint256 m_param2, addr m_param3): # not payable
  require mowner == caller
  require munknown5758b804Address
  require m_param3
  require not mpreSaleAddress
  require ext_code.size(munknown5758b804Address)
  call munknown5758b804Address.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require m_param1 >= block.timestamp
  require m_param2 >= m_param1
  create contract with 0 wei
                  code: 0x6060604052341561000f57600080fd5b60405161010080610a0f833981016040528080519190602001805191906020018051919060200180519190602001805191906020018051919060200180519190602001805160008054600160a060020a03338116600160a060020a0319928316811790935560029c909c5560039a909a5560059890985560048054958b16958a1695909517909455505060018054919097169086161790955560085560095560078054909216179055600a805491151560ff19909216919091179055610935806100da6000396000f3006060604052600436106100ed5763ffffffff60e060020a6000350416631d412dcb81146100f85780632c4e722e1461010e5780633197cbb61461013357806333b5b62e146101465780634042b66f1461015957806340582f131461016c578063521eb2731461017f5780637555e80a146101ae57806378e97925146101c457806383408d73146101d75780638da5cb5b146101ea578063977b055b146101fd578063c0ee0b8a14610210578063c2507ac114610289578063ec8ac4d81461029f578063ecb70fb7146102b3578063eef9d905146102c6578063f2fde38b146102d9578063fc0c546a146102f8575b6100f63361030b565b005b341561010357600080fd5b6100f6600435610510565b341561011957600080fd5b61012161053e565b60405190815260200160405180910390f35b341561013e57600080fd5b610121610544565b341561015157600080fd5b61012161054a565b341561016457600080fd5b610121610550565b341561017757600080fd5b610121610556565b341561018a57600080fd5b61019261055c565b604051600160a060020a03909116815260200160405180910390f35b34156101b957600080fd5b6100f660043561056b565b34156101cf57600080fd5b610121610592565b34156101e257600080fd5b6100f6610598565b34156101f557600080fd5b610192610604565b341561020857600080fd5b610121610613565b341561021b57600080fd5b61027560048035600160a060020a03169060248035919060649060443590810190830135806020601f8201819004810201604051908101604052818152929190602084018383808284375094965061061995505050505050565b604051901515815260200160405180910390f35b341561029457600080fd5b610121600435610622565b6100f6600160a060020a036004351661030b565b34156102be57600080fd5b6102756106ec565b34156102d157600080fd5b6102756106f4565b34156102e457600080fd5b6100f6600160a060020a03600435166106fd565b341561030357600080fd5b610192610798565b60008080600160a060020a038416151561032457600080fd5b61032d846107a7565b151561033857600080fd5b34925061034483610622565b600154909250600160a060020a03166370a082313060405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561039757600080fd5b5af115156103a457600080fd5b5050506040518051915050808211156103bc57600080fd5b6006546103cf908463ffffffff61087716565b600655600154600160a060020a031663a9059cbb858460405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401602060405180830381600087803b151561042857600080fd5b5af1151561043557600080fd5b505050604051805190505083600160a060020a031633600160a060020a03167f623b3804fa71d67900d064613da8f94b9617215ee90799290593e1745087ad18858560405191825260208201526040908101905180910390a361049783610891565b600a5460ff16151561050a57600754600160a060020a03166350c1bdf2338560405160e060020a63ffffffff8516028152600160a060020a0390921660048301526024820152604401600060405180830381600087803b15156104f957600080fd5b5af1151561050657600080fd5b5050505b50505050565b60005433600160a060020a0390811691161461052b57600080fd5b600354811161053957600080fd5b600355565b60055481565b60035481565b60095481565b60065481565b60065490565b600454600160a060020a031681565b60005433600160a060020a0390811691161461058657600080fd5b42811161053957600080fd5b60025481565b60005433600160a060020a039081169116146105b357600080fd5b600154600160a060020a0316639975038c6040518163ffffffff1660e060020a028152600401600060405180830381600087803b15156105f257600080fd5b5af115156105ff57600080fd5b505050565b600054600160a060020a031681565b60085481565b60019392505050565b600080600061063c600554856108c790919063ffffffff16565b915060009050678ac7230489e80000841015610657576106d4565b68015af1d78b58c4000084101561068d57600a5460ff1615156106885761068582600a63ffffffff6108f216565b90505b6106d4565b68056bc75e2d631000008410156106c05761068560646106b484600f63ffffffff6108c716565b9063ffffffff6108f216565b6106d182600563ffffffff6108f216565b90505b6106e4828263ffffffff61087716565b949350505050565b600354421190565b600a5460ff1681565b60005433600160a060020a0390811691161461071857600080fd5b600160a060020a038116151561072d57600080fd5b600054600160a060020a0380831691167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a36000805473ffffffffffffffffffffffffffffffffffffffff1916600160a060020a0392909216919091179055565b600154600160a060020a031681565b60008060008060008060025442101580156107c457506003544211155b6008546009546007549297503480151597509182111595509010159250600160a060020a03166313f44d108860405160e060020a63ffffffff8416028152600160a060020a039091166004820152602401602060405180830381600087803b151561082e57600080fd5b5af1151561083b57600080fd5b5050506040518051905090508480156108515750835b801561085a5750805b80156108635750825b801561086c5750815b979650505050505050565b60008282018381101561088657fe5b8091505b5092915050565b600454600160a060020a031681156108fc0282604051600060405180830381858888f1935050505015156108c457600080fd5b50565b6000808315156108da576000915061088a565b508282028284828115156108ea57fe5b041461088657fe5b600080828481151561090057fe5b049493505050505600a165627a7a723058202c989f017a9fd91a3accb97188fd011c279487b41112c465e60c908980aae83b0000, _param1, _param2, 10150, 5 * 10^18, 200 * 10^18, addr(_param3), tokenAddress, 1
  require create.new_address
  mpreSaleAddress = addr(create.new_address)
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(create.new_address), 50750000 * 10^18
  require ext_call.success
  require ext_code.size(munknown5758b804Address)
  call munknown5758b804Address.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success


# hash = 0x8475fcac
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknown8475fcac(addr m_param1): # not payable
  return munknown8475fcacm[m_param1m]


# hash = 0x8a857bc1
# getter = None
# const = ['return', 220000000000000000000000000]
# payable = False
const unknown8a857bc1 = 220000000 * 10^18


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


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
  return mtotalSold


# hash = 0x92a8675d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown92a8675d(addr m_param1): # not payable
  return munknown92a8675dm[m_param1m]


# hash = 0x98b3f7e2
# getter = None
# const = None
# payable = False
def unknown98b3f7e2(): # not payable
  require mowner == caller
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = 3
      mstor3m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x9c1e03a0
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def crowdsale(): # not payable
  return mcrowdsaleAddress


# hash = 0xa6ceb1f3
# getter = None
# const = None
# payable = False
def sendAirdrop(address[] m_to, uint256[] m_value): # not payable
  require mowner == caller
  require not mcrowdsaleFinished
  require m_value.length == m_to.length
  [94midx = 0
  mwhile [94midx < m_to.lengthm:
      require [94midx < m_value.length
      require cd[((32 * [94midx) + m_value + 36)] + mairdropSpent >= mairdropSpent
      mairdropSpent += cd[((32 * [94midx) + m_value + 36)]
      require 220000000 * 10^18 >= cd[((32 * [94midx) + m_value + 36)] + mairdropSpent
      require [94midx < m_to.length
      require addr(cd[((32 * [94midx) + m_to + 36)])
      require [94midx < m_to.length
      require [94midx < m_value.length
      mem[100] = addr(cd[((32 * [94midx) + m_to + 36)])
      mem[132] = cd[((32 * [94midx) + m_value + 36)]
      require ext_code.size(mtokenAddress)
      call mtokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(cd[((32 * [94midx) + m_to + 36)]), cd[((32 * [94midx) + m_value + 36)]
      mem[96] = ext_call.return_data[0]
      require ext_call.success
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xa818e816
# getter = None
# const = ['return', 0]
# payable = False
const unknowna818e816 = 0


# hash = 0xb1905c5d
# getter = None
# const = None
# payable = False
def unknownb1905c5d(array m_param1): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require mowner == caller
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require mem[(32 * [94midx) + 140 len 20]
      require [94midx < m_param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 4
      mstor4m[mem[(32 * [94midx) + 140 len 20]m] = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xb80cdcf6
# getter = None
# const = None
# payable = False
def finishCrowdsale(): # not payable
  require mowner == caller
  require mcrowdsaleAddress
  require ext_code.size(mcrowdsaleAddress)
  call mcrowdsaleAddress.hasEnded() with:
       gas gas_remaining wei
  require ext_call.success
  require 1 == bool(ext_call.return_data[0])
  require not mcrowdsaleFinished
  require munknown5f54eabbAddress
  require ext_code.size(mcrowdsaleAddress)
  call mcrowdsaleAddress.burnRemainingTokens() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_code.size(mcrowdsaleAddress)
  call mcrowdsaleAddress.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require ext_code.size(mpreSaleAddress)
  call mpreSaleAddress.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require 2 * ext_call.return_data[0] >= ext_call.return_data[0]
  require ext_code.size(munknown5758b804Address)
  call munknown5758b804Address.getWeiRaised() with:
       gas gas_remaining wei
  require ext_call.success
  require 3 * ext_call.return_data[0] >= ext_call.return_data[0]
  mtotalSold = 3 * ext_call.return_data[0]
  if 3 * ext_call.return_data[0] >= 2500 * 10^18:
      require ext_code.size(mtokenAddress)
      call mtokenAddress.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args munknown5f54eabbAddress, 0
      require ext_call.success
      require bool(ext_call.return_data[0]) == 1
      call munknown55e7e714Address with:
         value eth.balance(this.address) / 2 wei
           gas 2300 * is_zero(value) wei
      require ext_call.success
      call mholderAddress with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
  mcrowdsaleFinished = 1


# hash = 0xbb0a4c2d
# getter = None
# const = ['return', 1585699200]
# payable = False
const unknownbb0a4c2d = (440472 * 24 * 3600)


# hash = 0xc4290fd1
# getter = None
# const = None
# payable = False
def unknownc4290fd1(): # not payable
  require mowner == caller
  require 1 == bool(mcrowdsaleFinished)
  require munknownd8e1a97f <= 0
  require ext_code.size(mtokenAddress)
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  require ext_call.success
  require 0 <= ext_call.return_data[0]
  if not -munknownd8e1a97f:
      require mairdropSpent <= 220000000 * 10^18
      if -mairdropSpent + 220000000 * 10^18:
          if ext_call.return_data[0] >= -mairdropSpent + 220000000 * 10^18:
              require ext_code.size(mtokenAddress)
              call mtokenAddress.burn(uint256 value) with:
                   gas gas_remaining wei
                  args (-mairdropSpent + 220000000 * 10^18)
              require ext_call.success
  else:
      if ext_call.return_data[0] < -munknownd8e1a97f:
          require mairdropSpent <= 220000000 * 10^18
          if -mairdropSpent + 220000000 * 10^18:
              if ext_call.return_data[0] >= -mairdropSpent + 220000000 * 10^18:
                  require ext_code.size(mtokenAddress)
                  call mtokenAddress.burn(uint256 value) with:
                       gas gas_remaining wei
                      args (-mairdropSpent + 220000000 * 10^18)
                  require ext_call.success
      else:
          require ext_code.size(mtokenAddress)
          call mtokenAddress.burn(uint256 value) with:
               gas gas_remaining wei
              args -munknownd8e1a97f
          require ext_call.success
          require -munknownd8e1a97f <= ext_call.return_data[0]
          require mairdropSpent <= 220000000 * 10^18
          if -mairdropSpent + 220000000 * 10^18:
              if ext_call.return_data[0] + munknownd8e1a97f >= -mairdropSpent + 220000000 * 10^18:
                  require ext_code.size(mtokenAddress)
                  call mtokenAddress.burn(uint256 value) with:
                       gas gas_remaining wei
                      args (-mairdropSpent + 220000000 * 10^18)
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
  require mowner == caller
  require munknownf4166388 < 2
  require munknown31ef54d9m[mstor16m] < block.timestamp
  munknown2955316f = 0
  require ext_code.size(mtokenAddress)
  call mtokenAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mowner, munknown2955316f
  require ext_call.success
  munknownf4166388++


# hash = 0xd8e1a97f
# getter = ['storage', 256, 0, 18]
# const = None
# payable = False
def unknownd8e1a97f(): # not payable
  return munknownd8e1a97f


# hash = 0xe534155d
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def holder(): # not payable
  return mholderAddress


# hash = 0xe647e19f
# getter = None
# const = ['return', 0]
# payable = False
const unknowne647e19f = 0


# hash = 0xece84fd5
# getter = ['bool', ['storage', 8, 0, 21]]
# const = None
# payable = False
def crowdsaleFinished(): # not payable
  return bool(mcrowdsaleFinished)


# hash = 0xedba3df2
# getter = None
# const = ['return', 1530403200]
# payable = False
const unknownedba3df2 = (425112 * 24 * 3600)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require mowner == caller
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf4166388
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknownf4166388(): # not payable
  return munknownf4166388


# hash = 0xf6700481
# getter = None
# const = ['return', 0]
# payable = False
const unknownf6700481 = 0


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def token(): # not payable
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


