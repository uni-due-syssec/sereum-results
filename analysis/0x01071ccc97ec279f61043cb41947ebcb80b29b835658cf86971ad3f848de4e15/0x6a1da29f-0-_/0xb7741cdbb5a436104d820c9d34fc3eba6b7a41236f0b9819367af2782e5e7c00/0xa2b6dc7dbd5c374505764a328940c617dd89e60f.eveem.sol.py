# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa2b6dC7DBD5C374505764a328940c617dD89e60F 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stopped # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    unknown2511b4f9 # mask: a s
    # storage address 3
    brokerAddress # mask: a s
    # storage address 4
    expireDate # mask: a s
    # storage address 5
    unknown8f0be74a # mask: a s
# hash = 0x1974884f
# getter = None
# const = None
# payable = False
def unknown1974884f(addr m_param1, bool m_param2, array m_param3, array m_param4): # not payable
  require mbrokerAddress == caller
  mem[(32 * m_param3.length) + (32 * m_param4.length) + 320 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[(64 * m_param3.length) + (32 * m_param4.length) + 320] = m_param4.length
  mem[(64 * m_param3.length) + (32 * m_param4.length) + 352 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  log 0xef251895: addr(_param1), _param2, Array(len=_param3.length, data=call.data[_param3 + 36 len floor32(_param3.length)], mem[(32 * _param3.length) + (32 * _param4.length) + floor32(_param3.length) + 320 len (32 * _param3.length) + (32 * _param4.length) + -floor32(_param3.length) + 32]), (32 * _param3.length) + 160


# hash = 0x1cd61dae
# getter = None
# const = None
# payable = False
def unknown1cd61dae(uint32 m_param1, addr m_param2): # not payable
  require mstor2m[callerm]
  log 0x7bb6fb50: _param1 << 224, _param2


# hash = 0x2511b4f9
# getter = ['storage', 32, 0, 3]
# const = None
# payable = False
def unknown2511b4f9(): # not payable
  return munknown2511b4f9


# hash = 0x3b7416ad
# getter = None
# const = None
# payable = False
def unknown3b7416ad(addr m_param1, addr m_param2): # not payable
  require not mstopped
  require block.timestamp < mexpireDate
  require ext_code.size(m_param2)
  call m_param2.cancel(address tag) with:
       gas gas_remaining - 710 wei
      args m_param1
  require ext_call.success
  mstor2m[addr(m_param2)m] = 0


# hash = 0x3eac7818
# getter = None
# const = None
# payable = False
def unknown3eac7818(addr m_param1): # not payable
  require not mstopped
  require ext_code.size(m_param1)
  call m_param1.0x79599f96 with:
       gas gas_remaining - 710 wei
  require ext_call.success
  mstor2m[addr(m_param1)m] = 0


# hash = 0x4fdf8d80
# getter = None
# const = None
# payable = False
def unknown4fdf8d80(): # not payable
  require addr(mstor0m.field_0) == caller
  Mask(96, 0, mstor0m.field_160) = Mask(96, 0, not mstopped)


# hash = 0x528fd71d
# getter = None
# const = None
# payable = False
def unknown528fd71d(uint32 m_param1): # not payable
  require addr(mstor0m.field_0) == caller
  munknown8f0be74a = m_param1
  log 0x969d6e22: _param1


# hash = 0x619ec1b3
# getter = None
# const = None
# payable = False
def unknown619ec1b3(uint32 m_param1, uint32 m_param2): # not payable
  require mstor2m[callerm]
  log 0xe3da4bba: _param1 << 224, _param2


# hash = 0x6a1da29f
# getter = None
# const = None
# payable = False
def unknown6a1da29f(addr m_param1): # not payable
  require not mstopped
  require block.timestamp < mexpireDate
  require ext_code.size(m_param1)
  call m_param1.cancel(address tag) with:
       gas gas_remaining - 710 wei
      args caller
  require ext_call.success
  mstor2m[addr(m_param1)m] = 0


# hash = 0x75f12b21
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def stopped(): # not payable
  return bool(mstopped)


# hash = 0x76f77017
# getter = None
# const = None
# payable = False
def unknown76f77017(uint32 m_param1): # not payable
  require mstor2m[callerm]
  log 0xcf113b65: _param1


# hash = 0x7d95d6b4
# getter = None
# const = None
# payable = False
def unknown7d95d6b4(uint256 m_param1): # not payable
  require addr(mstor0m.field_0) == caller
  require mstopped
  mexpireDate = m_param1


# hash = 0x839e703a
# getter = None
# const = None
# payable = False
def unknown839e703a(uint256 m_param1): # not payable
  return mstor1m[m_param1m], bool(mstor2m[mstor1m[m_param1m]m])


# hash = 0x8f0be74a
# getter = ['storage', 32, 0, 5]
# const = None
# payable = False
def unknown8f0be74a(): # not payable
  return munknown8f0be74a


# hash = 0xa41f3e3d
# getter = None
# const = None
# payable = False
def unknowna41f3e3d(uint32 m_param1, addr m_param2, bool m_param3): # not payable
  require mstor2m[callerm]
  log 0xdbb72ec5: _param1 << 224, addr(_param2), _param3


# hash = 0xabff0110
# getter = ['storage', 160, 32, 3]
# const = None
# payable = False
def broker(): # not payable
  return mbrokerAddress


# hash = 0xb2f450ca
# getter = None
# const = None
# payable = False
def unknownb2f450ca(uint32 m_param1, uint32 m_param2): # not payable
  require mstor2m[callerm]
  log 0x590cf103: _param1 << 224, _param2


# hash = 0xb8a67c3c
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def expireDate(): # not payable
  return mexpireDate


# hash = 0xbf0d0213
# getter = None
# const = None
# payable = False
def unknownbf0d0213(addr m_param1): # not payable
  require addr(mstor0m.field_0) == caller
  mbrokerAddress = m_param1
  log 0x722e4657: _param1


# hash = 0xc157f13d
# getter = None
# const = None
# payable = False
def unknownc157f13d(uint32 m_param1, uint32 m_param2): # not payable
  require mstor2m[callerm]
  log 0x48457ea0: _param1 << 224, _param2


# hash = 0xdb2e21bc
# getter = None
# const = None
# payable = False
def emergencyWithdraw(): # not payable
  require mstopped
  require addr(mstor0m.field_0) == caller
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0xe37d86d6
# getter = None
# const = None
# payable = False
def unknowne37d86d6(uint32 m_param1, uint256 m_param2, bool m_param3): # not payable
  require mstor2m[callerm]
  log 0xc4f0eba6: _param1 << 224, _param2, _param3


# hash = 0xf401e49a
# getter = None
# const = None
# payable = True
def unknownf401e49a(addr m_param1, uint32 m_param2, uint8 m_param3, bool m_param4) payable: 
  require not mstopped
  require block.timestamp < mexpireDate
  create contract with callvalue wei
                  code: 0x606060405260405160a0806106ed83398101604052808051919060200180519190602001805191906020018051919060200180519150505b73bb63ffb582a73d600df789631912c4031ed779a4633a7fdfe66000878787878760405163ffffffff8881167c01000000000000000000000000000000000000000000000000000000000282526004820197909752600160a060020a03959095166024860152928516604485015260ff9190911660648401521515608483015290911660a482015260c40160006040518083038186803b15156100d957600080fd5b6102c65a03f415156100ea57600080fd5b5050505b50505050505b6105ea806101036000396000f300606060405236156100725763ffffffff60e060020a6000350416634c33fe94811461008a5780635a0cf9f3146100ab57806379599f96146100d35780637e102b2a146100e8578063b82a097814610102578063d9214ed514610126578063d9a968521461014e578063df9b8fff14610178575b341561007d57600080fd5b6100885b600080fd5b565b005b341561009557600080fd5b610088600160a060020a036004351661019c565b005b6100bf600160a060020a0360043516610213565b604051901515815260200160405180910390f35b34156100de57600080fd5b6100886102a9565b005b34156100f357600080fd5b6100886004351515610310565b005b341561010d57600080fd5b610088600160a060020a0360043516602435610380565b005b6100bf600160a060020a0360043516610409565b604051901515815260200160405180910390f35b341561015957600080fd5b610088600160a060020a036004351663ffffffff602435166104a0565b005b341561018357600080fd5b610088600160a060020a0360043516602435610535565b005b73bb63ffb582a73d600df789631912c4031ed779a463e0c703dc60008360405160e060020a63ffffffff85160281526004810192909252600160a060020a0316602482015260440160006040518083038186803b15156101fb57600080fd5b6102c65a03f4151561020c57600080fd5b5050505b50565b600073bb63ffb582a73d600df789631912c4031ed779a46329f2e9076000846000806040516020015260405160e060020a63ffffffff86160281526004810193909352600160a060020a0390911660248301521515604482015260640160206040518083038186803b151561028757600080fd5b6102c65a03f4151561029857600080fd5b50505060405180519150505b919050565b73bb63ffb582a73d600df789631912c4031ed779a463d30d447d600060405160e060020a63ffffffff8416028152600481019190915260240160006040518083038186803b15156102f957600080fd5b6102c65a03f4151561030a57600080fd5b5050505b565b73bb63ffb582a73d600df789631912c4031ed779a463f547130760008360405160e060020a63ffffffff851602815260048101929092521515602482015260440160006040518083038186803b15156101fb57600080fd5b6102c65a03f4151561020c57600080fd5b5050505b50565b73bb63ffb582a73d600df789631912c4031ed779a463fe7a0fb960008484600060405160e060020a63ffffffff87160281526004810194909452600160a060020a03909216602484015260448301521515606482015260840160006040518083038186803b15156103f057600080fd5b6102c65a03f4151561040157600080fd5b5050505b5050565b600073bb63ffb582a73d600df789631912c4031ed779a46329f2e907600084600160006040516020015260405160e060020a63ffffffff86160281526004810193909352600160a060020a0390911660248301521515604482015260640160206040518083038186803b151561028757600080fd5b6102c65a03f4151561029857600080fd5b50505060405180519150505b919050565b73bb63ffb582a73d600df789631912c4031ed779a4630a8b79836000848460006040516020015260405163ffffffff85811660e060020a0282526004820194909452600160a060020a03929092166024830152909116604482015260640160206040518083038186803b151561051557600080fd5b6102c65a03f4151561052657600080fd5b505050604051805150505b5050565b73bb63ffb582a73d600df789631912c4031ed779a463fe7a0fb960008484600160405160e060020a63ffffffff87160281526004810194909452600160a060020a03909216602484015260448301521515606482015260840160006040518083038186803b15156103f057600080fd5b6102c65a03f4151561040157600080fd5b5050505b50505600a165627a7a72305820a8ab760947f53fdacdffc1af433ee27e6ccab351a8a886fa83270ff8773501f10000, addr(_param1), _param2 << 224, _param3 << 248, _param4, unknown2511b4f9 + 1 << 224
  require create.new_address
  require addr(create.new_address)
  munknown2511b4f9 = uint32(munknown2511b4f9 + 1)
  mstor1m[mstor3 + 1 << 224m] = addr(create.new_address)
  mstor2m[addr(create.new_address)m] = 1
  log 0xc05014c3: unknown2511b4f9, addr(_param1), addr(create.new_address), _param4, _param3, _param2 << 224


# hash = 0xffa1ad74
# getter = None
# const = ['return', 1]
# payable = False
const VERSION = 1


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  revert


