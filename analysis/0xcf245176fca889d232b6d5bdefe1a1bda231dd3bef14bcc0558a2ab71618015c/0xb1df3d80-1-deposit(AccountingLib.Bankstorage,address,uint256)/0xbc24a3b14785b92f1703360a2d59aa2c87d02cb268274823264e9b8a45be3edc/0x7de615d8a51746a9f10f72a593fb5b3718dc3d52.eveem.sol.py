# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7De615D8a51746a9F10F72a593Fb5b3718dC3d52 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 99
    stor99
# hash = 0x5548c837
# getter = None
# const = None
# payable = True
def Deposit(address m_token, address m_owner, uint256 m_tokens) payable: 
  log _Deposit(
        address from=_tokens,
        address accountAddress=_token,
        uint256 value=_owner)


# hash = 0x5c54305e
# getter = None
# const = None
# payable = True
def InsufficientFunds(address m_accountAddress, uint256 m_value, uint256 m_balance) payable: 
  log _InsufficientFunds(
        address accountAddress=_value,
        uint256 value=_balance,
        uint256 balance=_accountAddress)


# hash = 0x6b103966
# getter = None
# const = None
# payable = True
def addFunds(AccountingLib.Bank storage m_self, address m_accountAddress, uint256 m_value) payable: 
  require m_value + mstor[m_selfm]m[addr(m_accountAddress)m] >= mstor[m_selfm]m[addr(m_accountAddress)m]
  mstor[m_selfm]m[addr(m_accountAddress)m] += m_value


# hash = 0x7fcf532c
# getter = None
# const = None
# payable = True
def Withdrawal(address m_src, uint256 m_amt) payable: 
  log _Withdrawal(
        address accountAddress=_amt,
        uint256 value=_src)


# hash = 0xb1df3d80
# getter = None
# const = None
# payable = True
def deposit(AccountingLib.Bank storage m_self, address m_accountAddress, uint256 m_value) payable: 
  require m_value + mstor[m_selfm]m[addr(m_accountAddress)m] >= mstor[m_selfm]m[addr(m_accountAddress)m]
  mstor[m_selfm]m[addr(m_accountAddress)m] += m_value
  return 1


# hash = 0xb5bc6dbb
# getter = None
# const = None
# payable = True
def withdraw(AccountingLib.Bank storage m_self, address m_accountAddress, uint256 m_value) payable: 
  if mstor[m_selfm]m[addr(m_accountAddress)m] < m_value:
      return 0
  require m_value <= mstor[m_selfm]m[addr(m_accountAddress)m]
  mstor[m_selfm]m[addr(m_accountAddress)m] -= m_value
  call m_accountAddress with:
     value m_value wei
       gas 0 wei
  if ext_call.success:
      return 1
  call m_accountAddress with:
     value m_value wei
       gas gas_remaining - 34050 wei
  revert 


# hash = 0xe62af6c1
# getter = None
# const = None
# payable = True
def deductFunds(AccountingLib.Bank storage m_self, address m_accountAddress, uint256 m_value) payable: 
  require m_value <= mstor[m_selfm]m[addr(m_accountAddress)m]
  mstor[m_selfm]m[addr(m_accountAddress)m] -= m_value


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


