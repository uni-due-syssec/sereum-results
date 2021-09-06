# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xB29d75Ea254f04A1D93f5B765d4080FF21d8d6E9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x63bd1d4a': 'payout()'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    betAmount
    # storage address 2
    stor2
    # storage address 3
    betters
    # storage address 4
    unknown735ea6e2
    # storage address 5
    unknown2d180328
    # storage address 6
    owner # mask: a s
    # storage address 7
    totalBid # mask: a s
    # storage address 8
    unknown1a9b0b7c # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 8
    unknown5005537e # mask: a s
    # storage address 9
    gameId # mask: a s
    # storage address 10
    referralAmount # mask: a s
    # storage address 11
    unknown75024ae5 # mask: a s
    # storage address 12
    unknown2ce5c284 # mask: a s
    # storage address 13
    remaining # mask: a s
    # storage address 14
    totalBalance # mask: a s
    # storage address 15
    unknownbbe7a75bAddress # mask: a s
# hash = 0x0df71602
# getter = None
# const = None
# payable = False
def setWinner(uint256 _Resultado): # not payable
  if unknownbbe7a75bAddress != caller:
      require caller == owner
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.gameId() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require _Resultado == ext_call.return_data[0]
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.state() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] <= 6
  require ext_call.return_data[0] == 3
  require not unknown1a9b0b7c
  unknown1a9b0b7c = 1
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.0xd811b100 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.0x662a3b81 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.0x31c359fa with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not totalBid:
      call addr(ext_call.return_data[0]) with:
         value 70 * eth.balance(this.address) / 100 wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      unknown75024ae5 = 0
  else:
      if eth.balance(this.address) == totalBid:
          unknown75024ae5 = 1
      else:
          totalBalance = eth.balance(this.address) - totalBid
          require ext_code.size(unknownbbe7a75bAddress)
          call unknownbbe7a75bAddress.0x4182fa46 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          call addr(ext_call.return_data[0]) with:
             value 70 * ext_call.return_data[0] * totalBalance / 10000 wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          call addr(ext_call.return_data[0]) with:
             value 30 * totalBalance * ext_call.return_data[0] / 10000 wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(unknownbbe7a75bAddress)
          call unknownbbe7a75bAddress.0x40c97617 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          referralAmount = totalBalance * ext_call.return_data[0] / 100
          call addr(ext_call.return_data[0]) with:
             value totalBalance * ext_call.return_data[0] / 100 wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          totalBalance = eth.balance(this.address)
          unknown75024ae5 = 2
  unknown2ce5c284 = 0
  remaining = betters.length


# hash = 0x11610c25
# getter = None
# const = None
# payable = True
def bet() payable: 
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.getPrice() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if call.value < ext_call.return_data[0]:
      revert with 0, 'Too small bet'
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.canBet() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if not stor2[caller]:
      betters.length++
      betters[betters.length].field_0 = caller
      stor2[caller] = 1
  betAmount[caller] += call.value
  totalBid += call.value
  log StateChanged(
        bool success=1,
        string message=Array(len=13, data='Bet submitted'))


# hash = 0x136f1016
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 2]]]]
# const = None
# payable = False
def hasBet(address _better): # not payable
  return bool(stor2[_better])


# hash = 0x1a9b0b7c
# getter = ['bool', ['storage', 8, 8, 8]]
# const = None
# payable = False
def unknown1a9b0b7c(): # not payable
  return bool(unknown1a9b0b7c)


# hash = 0x262007c0
# getter = None
# const = None
# payable = False
def unknown262007c0(): # not payable
  if not betters.length:
      mem[(32 * betters.length) + 128] = 32
      mem[(32 * betters.length) + 160] = betters.length
      mem[(32 * betters.length) + 192 len floor32(betters.length)] = mem[128 len floor32(betters.length)]
      return memory
        from (32 * betters.length) + 128
         [93mlen (96 * betters.length) + 64
  mem[128] = addr(betters.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * betters.length) + 96 > [94midx:
      mem[[94midx + 32] = betters[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * betters.length) + 192 len floor32(betters.length)] = mem[128 len floor32(betters.length)]
  return Array(len=betters.length, data=mem[128 len floor32(betters.length)], mem[(32 * betters.length) + floor32(betters.length) + 192 len (32 * betters.length) - floor32(betters.length)]), 


# hash = 0x2ce5c284
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown2ce5c284(): # not payable
  return unknown2ce5c284


# hash = 0x2d180328
# getter = ['storage', 256, 0, ['add', ['sha3', 5], ['cd', 4]]]
# const = None
# payable = False
def unknown2d180328(uint256 _param1): # not payable
  require _param1 < unknown2d180328.length
  return unknown2d180328[_param1].field_0


# hash = 0x2faebb20
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown2faebb20(): # not payable
  return betters.length


# hash = 0x34aa7e00
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def betAmount(address _param1): # not payable
  return betAmount[_param1]


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if stor0 != caller:
      stop
  [93mselfdestruct([91mstor0[93m)


# hash = 0x5005537e
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def unknown5005537e(): # not payable
  return bool(unknown5005537e)


# hash = 0x55234ec0
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def remaining(): # not payable
  return remaining


# hash = 0x5926cf13
# getter = None
# const = None
# payable = False
def unknown5926cf13(uint256 _param1): # not payable
  require caller == unknownbbe7a75bAddress
  require not gameId
  gameId = _param1


# hash = 0x6bd68a8f
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def referralAmount(): # not payable
  return referralAmount


# hash = 0x6dad2a91
# getter = None
# const = None
# payable = False
def unknown6dad2a91(): # not payable
  if not unknown735ea6e2.length:
      mem[(32 * unknown735ea6e2.length) + 128] = 32
      mem[(32 * unknown735ea6e2.length) + 160] = unknown735ea6e2.length
      mem[(32 * unknown735ea6e2.length) + 192 len floor32(unknown735ea6e2.length)] = mem[128 len floor32(unknown735ea6e2.length)]
      return memory
        from (32 * unknown735ea6e2.length) + 128
         [93mlen (96 * unknown735ea6e2.length) + 64
  mem[128] = uint256(unknown735ea6e2.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknown735ea6e2.length) + 96 > [94midx:
      mem[[94midx + 32] = unknown735ea6e2[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown735ea6e2.length) + 192 len floor32(unknown735ea6e2.length)] = mem[128 len floor32(unknown735ea6e2.length)]
  return Array(len=unknown735ea6e2.length, data=mem[128 len floor32(unknown735ea6e2.length)], mem[(32 * unknown735ea6e2.length) + floor32(unknown735ea6e2.length) + 192 len (32 * unknown735ea6e2.length) - floor32(unknown735ea6e2.length)]), 


# hash = 0x735ea6e2
# getter = ['storage', 256, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = False
def unknown735ea6e2(uint256 _param1): # not payable
  require _param1 < unknown735ea6e2.length
  return unknown735ea6e2[_param1].field_0


# hash = 0x75024ae5
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknown75024ae5(): # not payable
  return unknown75024ae5


# hash = 0x883cf630
# getter = None
# const = None
# payable = False
def unknown883cf630(): # not payable
  require caller == unknownbbe7a75bAddress
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.state() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] <= 6
  require ext_call.return_data[0] == 5
  [94midx = 0
  while [94midx < betters.length:
      betAmount[stor3[[94midx].field_0] = 0
      mem[0] = betters[[94midx].field_0
      mem[32] = 2
      stor2[stor3[[94midx].field_0] = 0
      [94midx = [94midx + 1
      continue 
  betters.length = 0
  [94midx = 0
  while betters.length > [94midx:
      betters[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 
  unknown735ea6e2.length = 0
  [94midx = 0
  while unknown735ea6e2.length > [94midx:
      unknown735ea6e2[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 
  unknown2d180328.length = 0
  [94midx = 0
  while unknown2d180328.length > [94midx:
      unknown2d180328[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 
  totalBid = 0
  stor8 = 0
  gameId = 0
  referralAmount = 0
  unknown75024ae5 = 0
  unknown2ce5c284 = 0
  remaining = 0
  totalBalance = 0


# hash = 0x8a9e8671
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def totalBid(): # not payable
  return totalBid


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9890220b
# getter = None
# const = None
# payable = False
def drain(): # not payable
  if unknownbbe7a75bAddress != caller:
      require caller == owner
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.state() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] <= 6
  require ext_code.size(unknownbbe7a75bAddress)
  if ext_call.return_data[0]:
      call unknownbbe7a75bAddress.state() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 6
      require ext_call.return_data[0] == 6
  call unknownbbe7a75bAddress.0xd811b100 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  call ext_call.return_data[12 len 20] with:
     value 7 * eth.balance(this.address) / 10 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknownbbe7a75bAddress)
  call unknownbbe7a75bAddress.0x662a3b81 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  call ext_call.return_data[12 len 20] with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log StateChanged(
        bool success=1,
        string message=Array(len=16, data='Drain Successful'))


# hash = 0x9fda5d62
# getter = ['storage', 160, 0, ['add', ['sha3', 3], ['cd', 4]]]
# const = None
# payable = False
def betters(uint256 _param1): # not payable
  require _param1 < betters.length
  return betters[_param1].field_0


# hash = 0xad7a672f
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def totalBalance(): # not payable
  return totalBalance


# hash = 0xbbe7a75b
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def unknownbbe7a75b(): # not payable
  return unknownbbe7a75bAddress


# hash = 0xd7c81b55
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def gameId(): # not payable
  return gameId


# hash = 0xd811b7ca
# getter = None
# const = None
# payable = False
def unknownd811b7ca(addr _param1): # not payable
  if unknownbbe7a75bAddress != caller:
      require caller == owner
  call _param1 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xeb01d83b
# getter = None
# const = None
# payable = False
def unknowneb01d83b(): # not payable
  if unknown2d180328.length:
      mem[128] = uint256(unknown2d180328.field_0)
      if (32 * unknown2d180328.length) + 32 > 64:
          mem[160] = uint256(unknown2d180328.field_256)
          [94midx = 160
          [94ms = 1
          while (32 * unknown2d180328.length) + 96 > [94midx:
              mem[[94midx + 32] = unknown2d180328[[94ms].field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  mem[(32 * unknown2d180328.length) + 128] = 32
  mem[(32 * unknown2d180328.length) + 160] = unknown2d180328.length
  mem[(32 * unknown2d180328.length) + 192 len floor32(unknown2d180328.length)] = mem[128 len floor32(unknown2d180328.length)]
  return memory
    from (32 * unknown2d180328.length) + 128
     [93mlen (96 * unknown2d180328.length) + 64


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  log StateChanged(
        bool success=1,
        string message=Array(len=14, data='Ether Received'))


