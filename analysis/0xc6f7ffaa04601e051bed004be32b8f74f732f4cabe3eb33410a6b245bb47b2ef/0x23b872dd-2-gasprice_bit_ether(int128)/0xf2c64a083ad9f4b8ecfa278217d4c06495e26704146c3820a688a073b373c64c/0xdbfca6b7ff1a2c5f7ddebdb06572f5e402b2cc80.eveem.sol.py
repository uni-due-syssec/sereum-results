# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xDBfCa6b7fF1a2c5F7ddEbDb06572F5E402B2CC80 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0
# hash = 0x5781aa86
# getter = None
# const = None
# payable = False
def unknown5781aa86(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if caller != 0x44dba507b909a6f92f3a708a844d4c4f23622bee:
      if caller != 0xed7ce3de532213314bb07622d8bf606a4ba03cf1:
          if caller != 0xe185e2ab092e8a046cbb815174d9d6aae1c91d9a:
              if not mstor0m[callerm]:
                  if caller != 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade:
                      revert with 0, 'e0'
  call 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade with:
     value m_param1 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x6bbc0545
# getter = None
# const = None
# payable = False
def unknown6bbc0545(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  if caller != 0x44dba507b909a6f92f3a708a844d4c4f23622bee:
      if caller != 0xed7ce3de532213314bb07622d8bf606a4ba03cf1:
          if caller != 0xe185e2ab092e8a046cbb815174d9d6aae1c91d9a:
              if not mstor0m[callerm]:
                  if caller != 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade:
                      revert with 0, 'e0'
  require ext_code.size(m_param1)
  call m_param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args this.address, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x8b9d7cd3
# getter = None
# const = None
# payable = False
def unknown8b9d7cd3(): # not payable
  if caller != 0x44dba507b909a6f92f3a708a844d4c4f23622bee:
      if caller != 0xed7ce3de532213314bb07622d8bf606a4ba03cf1:
          if caller != 0xe185e2ab092e8a046cbb815174d9d6aae1c91d9a:
              if not mstor0m[callerm]:
                  if caller != 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade:
                      revert with 0, 'e0'
  [93mdelegate call.data[4] with:
       gas -1 wei
      args call.data[36 len calldata.size - 36]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x92379af7
# getter = None
# const = None
# payable = False
def unknown92379af7(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  if caller != 0x44dba507b909a6f92f3a708a844d4c4f23622bee:
      if caller != 0xed7ce3de532213314bb07622d8bf606a4ba03cf1:
          if caller != 0xe185e2ab092e8a046cbb815174d9d6aae1c91d9a:
              if not mstor0m[callerm]:
                  if caller != 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade:
                      revert with 0, 'e0'
  require ext_code.size(m_param1)
  call m_param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xcfcaa498
# getter = None
# const = None
# payable = False
def unknowncfcaa498(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if caller != 0xb3e20b057cbf2c0d9d099bac6772af0c948c6ade:
      revert with 0, 'e0'
  mstor0m[addr(m_param1)m] = 1


# hash = 0xee6804f0
# getter = None
# const = None
# payable = True
def unknownee6804f0() payable: 
  stop


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


