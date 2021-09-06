# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x534004Ede1a26752e6373Dc55c73596A0B549312 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    MOTAddress # mask: a s
    # storage address 1
    feeMode # mask: a s
    # storage address 2
    feePercentage # mask: a s
    # storage address 3
    feeAmount # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 9
    name
    # storage address 10
    description
    # storage address 11
    category
    # storage address 12
    version
    # storage address 13
    contracts
# hash = 0x061d7db7
# getter = None
# const = None
# payable = False
def adjustFeeMode(uint8 m_newMode): # not payable
  require caller == mowner
  require m_newMode <= 1
  mfeeMode = m_newMode
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x280dd460
# getter = None
# const = None
# payable = False
def adjustFeePercentage(uint256 m_newPercentage): # not payable
  require caller == mowner
  require m_newPercentage <= 10000
  mfeePercentage = m_newPercentage
  return 1


# hash = 0x46479541
# getter = None
# const = None
# payable = False
def setWalletId(address m_newWallet): # not payable
  require caller == mowner
  require m_newWallet
  mstor4 = m_newWallet
  return 1


# hash = 0x4bb278f3
# getter = None
# const = None
# payable = False
def finalize(): # not payable
  mcontractsm[callerm]m.field_2048 = 0
  mcontractsm[callerm]m.field_0 = 0
  mcontractsm[callerm]m.field_768 = 0
  [94midx = 0
  mwhile mcontractsm[callerm]m.field_768 > [94midxm:
      mcontractsm[callerm]m[[94midx + 3m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x51cff8d9
# getter = None
# const = None
# payable = False
def withdraw(address m_payee): # not payable
  require mfeeMode <= 1
  require mfeeMode <= 1
  if mfeeMode:
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount > 0:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
          require ext_code.size(mMOTAddress)
          call mMOTAddress.allowance(address owner, address spender) with:
               gas gas_remaining wei
              args caller, this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, mstor4, mfeeAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  require mcontractsm[callerm]m.field_2048
  if not mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0:
      return 0
  require ext_code.size(caller)
  call caller.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0:
      require 10^ext_call.return_data[0]
      require ext_code.size(caller)
      call caller.balanceOf(address owner) with:
           gas gas_remaining wei
          args m_payee
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 > ext_call.return_data[0]:
          log 0x4cdcd27a: addr(_payee), 0, 0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1792 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1280
          mcontractsm[callerm]m.field_1280 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          mcontractsm[callerm]m[2m]m[addr(m_payee)m]m.field_0 = 0
          mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 = 0
          require 0 / 10^ext_call.return_data[0] <= mcontractsm[callerm]m.field_1536
          mcontractsm[callerm]m.field_1536 -= 0 / 10^ext_call.return_data[0]
          return 0
      if mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 != mcontractsm[callerm]m.field_1280:
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1792 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1280
          mcontractsm[callerm]m.field_1280 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          mcontractsm[callerm]m[2m]m[addr(m_payee)m]m.field_0 = 0
          mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 = 0
          require 0 / 10^ext_call.return_data[0] <= mcontractsm[callerm]m.field_1536
          mcontractsm[callerm]m.field_1536 -= 0 / 10^ext_call.return_data[0]
          log 0x4cdcd27a: addr(_payee), contracts[caller][4][addr(_payee)].field_0, 0 / 10^ext_call.return_data[0]
          return 0 / 10^ext_call.return_data[0], mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
  else:
      require mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 == mcontractsm[callerm]m.field_0
      require 10^ext_call.return_data[0]
      require ext_code.size(caller)
      call caller.balanceOf(address owner) with:
           gas gas_remaining wei
          args m_payee
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 > ext_call.return_data[0]:
          log 0x4cdcd27a: addr(_payee), 0, 0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1792 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1280
          mcontractsm[callerm]m.field_1280 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          mcontractsm[callerm]m[2m]m[addr(m_payee)m]m.field_0 = 0
          mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 = 0
          require mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / 10^ext_call.return_data[0] <= mcontractsm[callerm]m.field_1536
          mcontractsm[callerm]m.field_1536 -= mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / 10^ext_call.return_data[0]
          return 0
      if mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 != mcontractsm[callerm]m.field_1280:
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1792 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1280
          mcontractsm[callerm]m.field_1280 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
          mcontractsm[callerm]m[2m]m[addr(m_payee)m]m.field_0 = 0
          mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 = 0
          require mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / 10^ext_call.return_data[0] <= mcontractsm[callerm]m.field_1536
          mcontractsm[callerm]m.field_1536 -= mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / 10^ext_call.return_data[0]
          log 0x4cdcd27a: addr(_payee), contracts[caller][4][addr(_payee)].field_0, contracts[caller].field_0 * contracts[caller][4][addr(_payee)].field_0 / 10^ext_call.return_data[0]
          return mcontractsm[callerm]m.field_0 * mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 / 10^ext_call.return_data[0], 
                 mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
  ('eq', ('field', 0, ('stor', ('map', ('mask_shl', 160, 0, 0, ('param', '_payee')), ('array', 4, ('map', 'caller', ('name', 'contracts', 13)))))), ('field', 1280, ('stor', ('map', 'caller', ('name', 'contracts', 13)))))
  require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1792
  mcontractsm[callerm]m.field_1792 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
  require mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 <= mcontractsm[callerm]m.field_1280
  mcontractsm[callerm]m.field_1280 -= mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0
  mcontractsm[callerm]m[2m]m[addr(m_payee)m]m.field_0 = 0
  mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0 = 0
  require mcontractsm[callerm]m.field_1536 <= mcontractsm[callerm]m.field_1536
  mcontractsm[callerm]m.field_1536 -= mcontractsm[callerm]m.field_1536
  log 0x4cdcd27a: addr(_payee), contracts[caller][4][addr(_payee)].field_0, contracts[caller].field_1536
  return mcontractsm[callerm]m.field_1536, mcontractsm[callerm]m[4m]m[addr(m_payee)m]m.field_0


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5ad7c05c
# getter = None
# const = None
# payable = False
def unknown5ad7c05c(): # not payable
  if 0 >= mcontractsm[callerm]m.field_1280:
      if not mcontractsm[callerm]m.field_256:
          mem[(32 * mcontractsm[callerm]m.field_256) + 128] = 32
          mem[(32 * mcontractsm[callerm]m.field_256) + 160] = mcontractsm[callerm]m.field_256
          mem[(32 * mcontractsm[callerm]m.field_256) + 192 len floor32(mcontractsm[callerm]m.field_256)] = mem[128 len floor32(mcontractsm[callerm]m.field_256)]
          return memory
            from (32 * mcontractsm[callerm]m.field_256) + 128
             [93mlen (96 * mcontractsm[callerm]m.field_256) + 64
      mem[128] = mcontractsm[callerm]m[1m]m.field_0
      [94midx = 128
      [94ms = 0
      mwhile (32 * mcontractsm[callerm]m.field_256) + 96 > [94midxm:
          mem[[94midx + 32] = mcontractsm[callerm]m[[94ms + 1m]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      mem[(32 * mcontractsm[callerm]m.field_256) + 192 len floor32(mcontractsm[callerm]m.field_256)] = mem[128 len floor32(mcontractsm[callerm]m.field_256)]
      return Array(len=mcontractsm[callerm]m.field_256, data=mem[128 len floor32(mcontractsm[callerm]m.field_256)], mem[(32 * mcontractsm[callerm]m.field_256) + floor32(mcontractsm[callerm]m.field_256) + 192 len (32 * mcontractsm[callerm]m.field_256) - floor32(mcontractsm[callerm]m.field_256)]), 
  if not mcontractsm[callerm]m.field_768:
      mem[(32 * mcontractsm[callerm]m.field_768) + 128] = 32
      mem[(32 * mcontractsm[callerm]m.field_768) + 160] = mcontractsm[callerm]m.field_768
      mem[(32 * mcontractsm[callerm]m.field_768) + 192 len floor32(mcontractsm[callerm]m.field_768)] = mem[128 len floor32(mcontractsm[callerm]m.field_768)]
      return memory
        from (32 * mcontractsm[callerm]m.field_768) + 128
         [93mlen (96 * mcontractsm[callerm]m.field_768) + 64
  mem[128] = mcontractsm[callerm]m[3m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * mcontractsm[callerm]m.field_768) + 96 > [94midxm:
      mem[[94midx + 32] = mcontractsm[callerm]m[[94ms + 3m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mcontractsm[callerm]m.field_768) + 192 len floor32(mcontractsm[callerm]m.field_768)] = mem[128 len floor32(mcontractsm[callerm]m.field_768)]
  return Array(len=mcontractsm[callerm]m.field_768, data=mem[128 len floor32(mcontractsm[callerm]m.field_768)], mem[(32 * mcontractsm[callerm]m.field_768) + floor32(mcontractsm[callerm]m.field_768) + 192 len (32 * mcontractsm[callerm]m.field_768) - floor32(mcontractsm[callerm]m.field_768)]), 


# hash = 0x62a5af3b
# getter = None
# const = None
# payable = False
def freeze(): # not payable
  require not mcontractsm[callerm]m.field_2048
  require ext_code.size(caller)
  call caller.getPrice() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(caller)
  call caller.getETHBalance() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(caller)
  call caller.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not mcontractsm[callerm]m.field_1792:
      require 10^ext_call.return_data[0]
      if 0 / 10^ext_call.return_data[0] <= ext_call.return_data[0]:
          mcontractsm[callerm]m.field_0 = ext_call.return_data[0]
          mcontractsm[callerm]m.field_1536 = 0 / 10^ext_call.return_data[0]
      else:
          require ext_code.size(caller)
          call caller.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require mcontractsm[callerm]m.field_1792
              mcontractsm[callerm]m.field_0 = 0 / mcontractsm[callerm]m.field_1792
          else:
              require 10^ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == 10^ext_call.return_data[0]
              require mcontractsm[callerm]m.field_1792
              mcontractsm[callerm]m.field_0 = 10^ext_call.return_data[0] * ext_call.return_data[0] / mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1536 = ext_call.return_data[0]
  else:
      require ext_call.return_data[0] * mcontractsm[callerm]m.field_1792 / mcontractsm[callerm]m.field_1792 == ext_call.return_data[0]
      require 10^ext_call.return_data[0]
      if ext_call.return_data[0] * mcontractsm[callerm]m.field_1792 / 10^ext_call.return_data[0] <= ext_call.return_data[0]:
          mcontractsm[callerm]m.field_0 = ext_call.return_data[0]
          mcontractsm[callerm]m.field_1536 = ext_call.return_data[0] * mcontractsm[callerm]m.field_1792 / 10^ext_call.return_data[0]
      else:
          require ext_code.size(caller)
          call caller.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require mcontractsm[callerm]m.field_1792
              mcontractsm[callerm]m.field_0 = 0 / mcontractsm[callerm]m.field_1792
          else:
              require 10^ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == 10^ext_call.return_data[0]
              require mcontractsm[callerm]m.field_1792
              mcontractsm[callerm]m.field_0 = 10^ext_call.return_data[0] * ext_call.return_data[0] / mcontractsm[callerm]m.field_1792
          mcontractsm[callerm]m.field_1536 = ext_call.return_data[0]
  mcontractsm[callerm]m.field_2048 = 1
  [94midx = 0
  mwhile [94midx < mcontractsm[callerm]m.field_256m:
      require [94midx < mcontractsm[callerm]m.field_256
      mcontractsm[callerm]m.field_768++
      mstor[('array', 3, ('map', 'caller', ('name', 'contracts', 13))) + mcontractsm[callerm]m.field_768m]m.field_0 = mcontractsm[callerm]m[[94midx + 1m]m.field_0
      require [94midx < mcontractsm[callerm]m.field_256
      require [94midx < mcontractsm[callerm]m.field_256
      mcontractsm[callerm]m[4m]m[mcontractsm[callerm]m[[94midx + 1m]m.field_0m]m.field_0 = mcontractsm[callerm]m[2m]m[mcontractsm[callerm]m[[94midx + 1m]m.field_0m]m.field_0
      require [94midx < mcontractsm[callerm]m.field_256
      require mcontractsm[callerm]m[2m]m[mcontractsm[callerm]m[[94midx + 1m]m.field_0m]m.field_0 + mcontractsm[callerm]m.field_1280 >= mcontractsm[callerm]m.field_1280
      mcontractsm[callerm]m.field_1280 += mcontractsm[callerm]m[2m]m[mcontractsm[callerm]m[[94midx + 1m]m.field_0m]m.field_0
      mem[0] = caller
      mem[32] = 13
      [94midx = [94midx + 1
      mcontinue 
  mcontractsm[callerm]m.field_256 = 0
  [94midx = 0
  mwhile mcontractsm[callerm]m.field_256 > [94midxm:
      mcontractsm[callerm]m[[94midx + 1m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x69dc9ff3
# getter = ['struct', ['loc', 13]]
# const = None
# payable = False
def contracts(address m_param1): # not payable
  return mcontractsm[m_param1m]m.field_0, 
         mcontractsm[m_param1m]m.field_1280,
         mcontractsm[m_param1m]m.field_1536,
         mcontractsm[m_param1m]m.field_1792,
         bool(mcontractsm[m_param1m]m.field_2048)


# hash = 0x69e15404
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def feeAmount(): # not payable
  return mfeeAmount


# hash = 0x6dfc2fa8
# getter = None
# const = None
# payable = False
def isInProgress(): # not payable
  if not mcontractsm[callerm]m.field_2048:
      return bool(mcontractsm[callerm]m.field_2048)
  return (mcontractsm[callerm]m.field_1792 > 0)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x74e8ff0e
# getter = ['storage', 256, 0, ['add', 7, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 13]]]]
# const = None
# payable = False
def unknown74e8ff0e(addr m_param1): # not payable
  return mcontractsm[addr(m_param1)m]m.field_1792


# hash = 0x75e5af3b
# getter = ['storage', 256, 0, ['sha3', ['data', 'caller', ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 13]]]]]]
# const = None
# payable = False
def unknown75e5af3b(addr m_param1): # not payable
  return mcontractsm[addr(m_param1)m]m[2m]m[callerm]m.field_0


# hash = 0x8a00ad9c
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['add', 2, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 13]]]]]]
# const = None
# payable = False
def unknown8a00ad9c(addr m_param1, addr m_param2): # not payable
  return mcontractsm[addr(m_param1)m]m[2m]m[addr(m_param2)m]m.field_0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x977919bf
# getter = None
# const = None
# payable = False
def adjustFeeAmount(uint256 m_newAmount): # not payable
  require caller == mowner
  mfeeAmount = m_newAmount
  return 1


# hash = 0x99a5d747
# getter = None
# const = None
# payable = False
def calculateFee(uint256 m_value): # not payable
  require mfeeMode <= 1
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      return mfeeAmount
  if not m_value:
      return 0
  require mfeePercentage * m_value / m_value == mfeePercentage
  return (mfeePercentage * m_value / 10000)


# hash = 0x9d634fda
# getter = ['storage', 256, 0, ['add', 6, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 13]]]]
# const = None
# payable = False
def unknown9d634fda(addr m_param1): # not payable
  return mcontractsm[addr(m_param1)m]m.field_1536


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def feePercentage(): # not payable
  return mfeePercentage


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 1]
# const = None
# payable = False
def feeMode(): # not payable
  require mfeeMode <= 1
  return mfeeMode


# hash = 0xc55c4115
# getter = None
# const = ['return', 10000]
# payable = False
const FEE_CHARGER_DENOMINATOR = 10000


# hash = 0xc642f094
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def MOT(): # not payable
  return mMOTAddress


# hash = 0xc77e7614
# getter = None
# const = None
# payable = False
def unknownc77e7614(): # not payable
  if 0 >= mcontractsm[callerm]m.field_1280:
      return mcontractsm[callerm]m.field_1792
  return mcontractsm[callerm]m.field_1280


# hash = 0xc892693b
# getter = None
# const = None
# payable = False
def setMotAddress(address m_motAddress): # not payable
  require caller == mowner
  require m_motAddress
  require mMOTAddress != m_motAddress
  mMOTAddress = m_motAddress
  mem[128] = 'MOT'
  mem[96] = 3
  mem[131 len 0] = None
  mem[131] = Mask(208, 0, 'MOT'), mem[160 len 3]
  [94m_31 = sha3(mem[131 len 3])
  mem[131] = 0x95d89b4100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mMOTAddress)
  call mMOTAddress.symbol() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[131 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 131
  require return_data.size >= 32
  require mem[131] <= 4294967296
  require mem[131] + 32 <= return_data.size
  require return_data.size >= mem[mem[131] + 131] + mem[131] + 32 and mem[mem[131] + 131] <= 4294967296
  [94m_38 = mem[mem[131] + 131]
  mem[ceil32(return_data.size) + 163 len floor32(mem[mem[131] + 131])] = mem[mem[131] + 163 len floor32(mem[mem[131] + 131])]
  mem[ceil32(return_data.size) + floor32(mem[mem[131] + 131]) + -(mem[mem[131] + 131] % 32) + 195 len mem[mem[131] + 131] % 32] = mem[mem[131] + floor32(mem[mem[131] + 131]) + -(mem[mem[131] + 131] % 32) + 195 len mem[mem[131] + 131] % 32]
  mem[[94m_38 + ceil32(return_data.size) + 163 len floor32([94m_38)] = mem[ceil32(return_data.size) + 163 len floor32([94m_38)]
  mem[(2 * floor32([94m_38)) + ceil32(return_data.size) + 195 len [94m_38 % 32] = mem[ceil32(return_data.size) + floor32([94m_38) + -([94m_38 % 32) + 195 len [94m_38 % 32]
  require sha3(mem[[94m_38 + ceil32(return_data.size) + 163 len [94m_38]) == [94m_31
  return 1


# hash = 0xc8c01a55
# getter = None
# const = None
# payable = False
def unknownc8c01a55(addr m_param1, uint256 m_param2): # not payable
  require m_param2 + mcontractsm[callerm]m.field_1792 >= mcontractsm[callerm]m.field_1792
  require ext_code.size(caller)
  call caller.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] >= m_param2 + mcontractsm[callerm]m.field_1792
  require mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0 + m_param2 >= m_param2
  require mcontractsm[callerm]m[4m]m[addr(m_param1)m]m.field_0 >= 0
  require ext_code.size(caller)
  call caller.balanceOf(address owner) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] >= mcontractsm[callerm]m[4m]m[addr(m_param1)m]m.field_0 + mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0 + m_param2
  if not mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0:
      mcontractsm[callerm]m.field_256++
      mstor[('array', 1, ('map', 'caller', ('name', 'contracts', 13))) + mcontractsm[callerm]m.field_256m]m.field_0 = m_param1
  require m_param2 + mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0 >= mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0
  mcontractsm[callerm]m[2m]m[addr(m_param1)m]m.field_0 += m_param2
  require m_param2 + mcontractsm[callerm]m.field_1792 >= mcontractsm[callerm]m.field_1792
  mcontractsm[callerm]m.field_1792 += m_param2
  log WithdrawRequest(
        address participant=addr(_param1),
        uint256 amountTokens=contracts[caller][2][addr(_param1)].field_0)
  return 1


# hash = 0xcd481e51
# getter = None
# const = None
# payable = False
def unknowncd481e51(addr m_param1): # not payable
  if mcontractsm[addr(m_param1)m]m.field_256:
      mem[128] = mcontractsm[addr(m_param1)m]m[1m]m.field_0
      [94midx = 128
      [94ms = 0
      mwhile (32 * mcontractsm[addr(m_param1)m]m.field_256) + 96 > [94midxm:
          mem[[94midx + 32] = mcontractsm[addr(m_param1)m]m[[94ms + 1m]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  mem[(32 * mcontractsm[addr(m_param1)m]m.field_256) + 320 len floor32(mcontractsm[addr(m_param1)m]m.field_256)] = mem[128 len floor32(mcontractsm[addr(m_param1)m]m.field_256)]
  return mcontractsm[addr(m_param1)m]m.field_0, 
         Array(len=mcontractsm[addr(m_param1)m]m.field_256, data=mem[128 len floor32(mcontractsm[addr(m_param1)m]m.field_256)], mem[(32 * mcontractsm[addr(m_param1)m]m.field_256) + floor32(mcontractsm[addr(m_param1)m]m.field_256) + 320 len (32 * mcontractsm[addr(m_param1)m]m.field_256) - floor32(mcontractsm[addr(m_param1)m]m.field_256)]),
         mcontractsm[addr(m_param1)m]m.field_1792,
         bool(mcontractsm[addr(m_param1)m]m.field_2048),
         mcontractsm[addr(m_param1)m]m.field_1536


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def category(): # not payable
  return mcategorym[0 len mcategorym.lengthm]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


